<div class="servers form">
    <div style="position:absolute;right:40px;width:300px;top:90px;">
        <label for="TemplateSelect" style="display: inline-block">Templates</label>
        <span id="showQB" class="btn btn-primary useCursorPointer" style="margin: 5px;"><span class="fa fa-wrench"> Query Builder</span></span>
        <?php
            $options = '<option value="">None</option>';
              foreach($allValidApisFormated as $scope => $actions) {
                  $options .= sprintf('<optgroup label="%s">', $scope);
                  foreach($actions as $action) {
                      $options .= sprintf('<option value="%s">%s</option>', $action['url'], $action['action']);
                  }
              }
            echo sprintf('<select id="TemplateSelect">%s</select>', $options);
        ?>
        <div id="apiInfo" style="margin-top: 15px;"></div>
    </div>

    <?php echo $this->Form->create('Server');?>
    <fieldset>
        <legend><?php echo __('REST client');?></legend>
        <?php
            echo $this->Form->input('method', array(
                'label' => __('Relative path to query'),
                'options' => array(
                    'GET' => 'GET',
                    'POST' => 'POST'
                )
            ));
        ?>
        <div class="input clear" style="width:100%;">
        <?php
            echo $this->Form->input('url', array(
                'label' => __('Relative path to query'),
                'class' => 'input-xxlarge'
            ));
        ?>
        <div class="input clear" style="width:100%;">
        <?php
            echo $this->Form->input('use_full_path', array(
              'label' => 'Use full path - disclose my apikey',
                    'type' => 'checkbox'
                ));
        ?>
        <div class="input clear" style="width:100%;">
        <?php
            echo $this->Form->input('show_result', array(
                'type' => 'checkbox'
            ));
            echo $this->Form->input('skip_ssl_validation', array(
              'type' => 'checkbox',
              'label' => 'Skip SSL validation'
            ));
        ?>
        <div class="input clear" style="width:100%;">
        <?php
            echo $this->Form->input('header', array(
                    'type' => 'textarea',
                    'div' => 'input clear',
                    'class' => 'input-xxlarge',
                    'default' => !empty($this->request->data['Server']['header']) ? $this->request->data['Server']['header'] : $header
            ));
        ?>

        <div class="clear">
            <div id="qb-div" class="dashboard_element hidden" style="max-width: calc(100% - 400px); max-width: calc(100% - 400px); padding: 10px; border: 1px solid #DCC896; margin: 10px; background-color: #fffcf6;">
                <div class="selected-path-container">
                    <h3 id="selected-path" >---</h3>
                </div>
                <div id="querybuilder"></div>
                    <button id="btn-inject" type="button" class="btn btn-success"><i class="fa fa-mail-forward" style="transform: scaleX(-1);"></i> Inject </button>
                    <button id="btn-apply" type="button" class="btn btn-default"><i class="fa fa-list-alt"></i> Show rules </button>
            </div>
        </div>


        <div class="input clear" style="width:100%;">
        <?php
            echo $this->Form->input('body', array(
                    'type' => 'textarea',
                    'div' => 'input clear',
                    'class' => 'input-xxlarge'
            ));
        ?>
        <div class="input clear" style="width:100%;">
            <div id="template_description" style="display:none;width:700px;" class="alert alert-error">Fill out the JSON template above, make sure to replace all placeholder values. Fields with the value "optional" can be removed.</div>
                <?php
                    echo $this->Form->submit('Run query', array('class' => 'btn btn-primary'));
                    echo $this->Form->end();
                ?>
                <hr />
        </div>
    </fieldset>
    
    <?php
        $formats = array('Raw', 'JSON', 'HTML');
        if (!empty($data['code']) && $data['code'] < 300) {
            $query_formats = array('curl' => 'cURL', 'python' => 'PyMISP');
            echo '<ul class="nav nav-tabs" style="margin-bottom:5px;">';
            foreach ($query_formats as $format => $formatName) {
                if (!empty(${$format})) {
                    echo sprintf('<li><a href="#%s" data-toggle="tab">%s</a></li>', 'tab' . $format, $formatName);
                }
            }
            echo '</ul>';
            echo '<div class="tab-content">';
            foreach ($query_formats as $format => $formatName) {
                if (!empty(${$format})) {
                    echo sprintf('<div class="tab-pane" id="%s"><pre>%s</pre></div>', 'tab' . $format, ${$format});
                }
            }
            echo '</div>';
        }
    
        if (!empty($data['data'])):
            echo sprintf('<h3>%s</h3>', __('Response'));
            echo sprintf('<div><span class="bold">%s</span>: %d</div>', __('Response code'), h($data['code']));
            echo sprintf('<div><span class="bold">%s</span>: %s</div>', __('Request duration'), h($data['duration']));
            echo sprintf('<div class="bold">%s</div>', __('Headers'));
            foreach ($data['headers'] as $header => $value) {
                if (is_array($value)) {
                  $value = implode(',', $value);
                }
                echo sprintf('&nbsp;&nbsp;<span class="bold">%s</span>: %s<br />', h($header), h($value));
            }
            $format_toggles = '';
            foreach ($formats as $k => $format) {
                $position = '';
                if ($k == 0) {
                    $position = '-left';
                }
                if ($k == (count($formats) -1)) {
                    $position = '-right';
                }
                $format_toggles .= sprintf('<span class="btn btn-inverse qet toggle%s format-toggle-button" data-toggle-type="%s">%s</span>', $position, $format, $format);
            }
            echo sprintf('<div style="padding-bottom:24px;">%s</div>', $format_toggles);
            echo sprintf('<div class="hidden" id="rest-response-hidden-container">%s</div>', h($data['data']));
            echo '<div id="rest-response-container"></div>';
        endif;
    ?>
</div>

<?php
    echo $this->element('side_menu', array('menuList' => 'event-collection', 'menuItem' => 'rest'));

    echo $this->Html->script('doT');
    echo $this->Html->script('extendext');
    echo $this->Html->script('moment-with-locales');
    echo $this->Html->css('query-builder.default');
    echo $this->Html->script('query-builder');
    echo $this->Html->css('chosen.min');
    echo $this->Html->script('chosen.jquery.min');
    echo $this->Html->script('restClient');
?>

<script>
    allValidApis = <?php echo json_encode($allValidApis); ?>;
    fieldsConstraint = <?php echo json_encode($allValidApisFieldsContraint); ?>;
</script>

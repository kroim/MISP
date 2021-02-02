<div class="shadow_attributes <?php if (!isset($ajax) || !$ajax) echo 'form';?>">
<?php echo $this->Form->create('ShadowAttribute', array('url' => '/shadow_attributes/add/' . $event_id));?>
    <fieldset>
    <legend><?php echo __('Add Proposal'); ?></legend>
    <div id="formWarning" class="message ajaxMessage"></div>
    <div class="add_attribute_fields">
        <?php
            echo $this->Form->hidden('event_id');
            echo $this->Form->input('category', array(
                'empty' => __('(choose one)'),
                'div' => 'input',
                'label' => __('Category ') . $this->element('formInfo', array('type' => 'category')),
            ));
            echo $this->Form->input('type', array(
                'empty' => __('(first choose category)'),
                'label' => __('Type ') . $this->element('formInfo', array('type' => 'type')),
            ));
        ?>
        <div class="input clear"></div>
        <?php
            echo $this->Form->input('value', array(
                    'type' => 'textarea',
                    'error' => array('escape' => false),
                    'class' => 'input-xxlarge clear'
            ));
            echo $this->Form->input('comment', array(
                    'type' => 'text',
                    'label' => __('Contextual Comment'),
                    'error' => array('escape' => false),
                    'div' => 'input clear',
                    'class' => 'input-xxlarge'
            ));
        ?>
        <div class="input clear"></div>
        <?php
            echo $this->Form->input('to_ids', array(
                    'checked' => true,
                    'label' => __('for Intrusion Detection System'),
            ));
            echo $this->Form->input('batch_import', array(
                    'type' => 'checkbox',
            ));
        ?>
    </div>
    </fieldset>
    <p style="color:red;font-weight:bold;display:none;<?php if ($ajax) echo 'text-align:center;'; ?>" id="warning-message"><?php echo __('Warning: You are about to share data that is of a classified nature (Attribution / targeting data). Make sure that you are authorised to share this.');?></p>
    <?php if (isset($ajax) && $ajax): ?>
        <div class="overlay_spacing">
            <table>
                <tr>
                <td style="vertical-align:top">
                    <span tite="<?php echo __('Propose');?>" role="button" tabindex="0" aria-label="<?php echo __('Propose');?>" id="submitButton" class="btn btn-primary" onClick="submitPopoverForm('<?php echo $event_id;?>', 'propose')"><?php echo __('Propose');?></span>
                </td>
                <td style="width:540px;">
                    <p style="color:red;font-weight:bold;display:none;<?php if (isset($ajax) && $ajax) echo "text-align:center;"?>" id="warning-message"><?php echo __('Warning: You are about to share data that is of a sensitive nature (Attribution / targeting data). Make sure that you are authorised to share this.');?></p>
                </td>
                <td style="vertical-align:top;">
                    <span class="btn btn-inverse" id="cancel_attribute_add"><?php echo __('Cancel');?></span>
                </td>
                </tr>
            </table>
        </div>
    <?php
        else:
            echo $this->Form->button(__('Propose'), array('class' => 'btn btn-primary'));
        endif;
        echo $this->Form->end();
    ?>
</div>
<?php
    $event['Event']['id'] = $this->request->data['ShadowAttribute']['event_id'];
    if (!$ajax) {
        echo $this->element('side_menu', array('menuList' => 'event', 'menuItem' => 'proposeAttribute', 'event' => $event));
    }
?>
<script type="text/javascript">
<?php
    $formInfoTypes = array('category' => 'Category', 'type' => 'Type');
    echo 'var formInfoFields = ' . json_encode($formInfoTypes) . PHP_EOL;
    foreach ($formInfoTypes as $formInfoType => $humanisedName) {
        echo 'var ' . $formInfoType . 'FormInfoValues = {' . PHP_EOL;
        foreach ($info[$formInfoType] as $key => $formInfoData) {
            echo '"' . $key . '": "<span class=\"blue bold\">' . h($formInfoData['key']) . '</span>: ' . h($formInfoData['desc']) . '<br />",' . PHP_EOL;
        }
        echo '}' . PHP_EOL;
    }
?>
//
//Generate Category / Type filtering array
//
var category_type_mapping = new Array();
<?php
    foreach ($categoryDefinitions as $category => $def) {
        echo "category_type_mapping['" . addslashes($category) . "'] = {";
        $first = true;
        foreach ($def['types'] as $type) {
            if ($first) $first = false;
            else echo ', ';
            echo "'" . addslashes($type) . "' : '" . addslashes($type) . "'";
        }
        echo "}; \n";
    }
?>

$(document).ready(function() {
    initPopoverContent('ShadowAttribute');
    $("#ShadowAttributeCategory").on('change', function(e) {
        formCategoryChanged('ShadowAttribute');
        if ($(this).val() === 'Attribution' || $(this).val() === 'Targeting data') {
            $("#warning-message").show();
        } else {
            $("#warning-message").hide();
        }
    });

    $("#ShadowAttributeCategory, #ShadowAttributeType").change(function() {
        initPopoverContent('ShadowAttribute');
    });

    <?php if ($ajax): ?>
        $('#cancel_attribute_add').click(function() {
            cancelPopoverForm();
        });

    <?php endif; ?>
});
</script>
<?php echo $this->Js->writeBuffer(); // Write cached scripts

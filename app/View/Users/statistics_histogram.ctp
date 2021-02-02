<?php
    echo $this->Html->script('d3');
    echo $this->Html->script('cal-heatmap');
    echo $this->Html->css('cal-heatmap');
?>
<div class = "index">
<h2>Statistics</h2>
<?php echo $this->element('Users/statisticsMenu'); ?>
<div id = "histogram"></div>
</div>
<?php
    echo $this->element('side_menu', array('menuList' => 'globalActions', 'menuItem' => 'statistics'));
?>
<script type="text/javascript">
$(document).ready(function () {
    updateHistogram('');
});
</script>
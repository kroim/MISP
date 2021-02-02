<?php
  $tr_class = '';
  $linkClass = 'white';
  $currentType = 'denyForm';
  $tr_class = 'tableHighlightBorderTop borderBlue';
  if ($event['Event']['id'] != $object['event_id']) {
    if (!$isSiteAdmin && $event['extensionEvents'][$object['event_id']]['Orgc']['id'] != $me['org_id']) {
      $mayModify = false;
    }
  }
  if ($object['deleted']) $tr_class .= ' lightBlueRow';
  else $tr_class .= ' blueRow';
  if (!empty($k)) {
    $tr_class .= ' row_' . h($k);
  }
?>
<tr id = "Object_<?php echo $object['id']; ?>_tr" class="<?php echo $tr_class; ?>" tabindex="0">
  <?php
    if ($mayModify || $extended):
  ?>
    <td style="width:10px;" data-position="<?php echo h($object['objectType']) . '_' . h($object['id']); ?>">
      <?php
        if ($mayModify):
      ?>
        <input id = "select_object_<?php echo $object['id']; ?>" class="select_object row_checkbox" type="checkbox" data-id="<?php echo $object['id'];?>" />
      <?php
        endif;
      ?>
    </td>
  <?php
    endif;
  ?>
  <td class="short context hidden">
    <?php echo h($object['id']); ?>
  </td>
  <td class="short context hidden">
    <?php echo h($object['uuid']); ?>
  </td>
  <td class="short">
    <?php echo date('Y-m-d', $object['timestamp']); ?>
  </td>
  <?php
    if ($extended):
  ?>
    <td class="short">
      <?php echo '<a href="' . $baseurl . '/events/view/' . h($object['event_id']) . '" class="white">' . h($object['event_id']) . '</a>'; ?>
    </td>
  <?php
    endif;
  ?>
  <td class="short">
    <?php
      if ($extended):
        if ($object['event_id'] != $event['Event']['id']):
          $extensionOrg = $event['extensionEvents'][$object['event_id']]['Orgc'];
          echo $this->OrgImg->getOrgImg(array('name' => $extensionOrg['name'], 'id' => $extensionOrg['id'], 'size' => 24));
        else:
          echo $this->OrgImg->getOrgImg(array('name' => $event['Orgc']['name'], 'id' => $event['Orgc']['id'], 'size' => 24));
        endif;
      endif;
    ?>
    &nbsp;
  </td>
  <td colspan="5">
    <span class="bold"><?php echo __('Name: ');?></span><?php echo h($object['name']);?>
    <span class="fa fa-expand useCursorPointer" title="<?php echo __('Expand or Collapse');?>" role="button" tabindex="0" aria-label="<?php echo __('Expand or Collapse');?>" data-toggle="collapse" data-target="#Object_<?php echo h($object['id']); ?>_collapsible"></span>
    <br />
    <div id="Object_<?php echo $object['id']; ?>_collapsible" class="collapse">
      <span class="bold"><?php echo __('Meta-category: ');?></span><?php echo h($object['meta-category']);?><br />
      <span class="bold"><?php echo __('Description: ');?></span><?php echo h($object['description']);?><br />
      <span class="bold"><?php echo __('Template: ');?></span><?php echo h($object['name']) . ' v' . h($object['template_version']) . ' (' . h($object['template_uuid']) . ')'; ?>
    </div>
    <?php
      echo $this->element('/Events/View/row_object_reference', array(
        'deleted' => $deleted,
        'object' => $object,
        'mayModify' => $mayModify
      ));
      if (!empty($object['referenced_by'])) {
        echo $this->element('/Events/View/row_object_referenced_by', array(
          'deleted' => $deleted,
          'object' => $object
        ));
      }
    ?>
  </td>
  <td class="shortish">
    <?php echo h($object['comment']); ?>
  </td>
  <td colspan="4">&nbsp;
  </td>
  <td class="shortish">
    <?php
      $turnRed = '';
      if ($object['objectType'] == 0 && $object['distribution'] == 0) $turnRed = 'style="color:red"';
    ?>
    <div id = "<?php echo $currentType . '_' . $object['id'] . '_distribution_placeholder'; ?>" class = "inline-field-placeholder"></div>
    <div id = "<?php echo $currentType . '_' . $object['id'] . '_distribution_solid'; ?>" <?php echo $turnRed; ?> class="inline-field-solid" ondblclick="activateField('<?php echo $currentType; ?>', '<?php echo $object['id']; ?>', 'distribution', <?php echo $event['Event']['id'];?>);">
      <?php
        if ($object['objectType'] == 0) {
          if ($object['distribution'] == 4):
      ?>
          <a href="/sharing_groups/view/<?php echo h($object['sharing_group_id']); ?>"><?php echo h($object['SharingGroup']['name']);?></a>
      <?php
          else:
            echo h($shortDist[$object['distribution']]);
          endif;
        }
      ?>&nbsp;
    </div>
  </td>
  <td>&nbsp;</td>
  <td>&nbsp;</td>
  <td class="short action-links">
    <?php
      if ($mayModify && empty($object['deleted'])) {
        echo sprintf(
          '<a href="%s/objects/edit/%s" title="Edit" class="icon-edit icon-white useCursorPointer"></a>',
          $baseurl,
          h($object['id'])
        );
        echo sprintf(
          '<span class="icon-trash icon-white useCursorPointer" title="%1$s" role="button" tabindex="0" aria-label="%1$s" onClick="%2$s"></span>',
          (empty($event['Event']['publish_timestamp']) ? __('Permanently delete object') : __('Soft delete object')),
          sprintf(
            'deleteObject(\'objects\', \'delete\', \'%s\', \'%s\');',
            empty($event['Event']['publish_timestamp']) ? h($object['id']) . '/true' : h($object['id']),
            h($event['Event']['id'])
          )
        );
      }
    ?>
  </td>
</tr>
<?php
  if (!empty($object['Attribute'])) {
    end($object['Attribute']);
    $lastElement = key($object['Attribute']);
    foreach ($object['Attribute'] as $attrKey => $attribute) {
      echo $this->element('/Events/View/row_' . $attribute['objectType'], array(
        'object' => $attribute,
        'mayModify' => $mayModify,
        'mayChangeCorrelation' => $mayChangeCorrelation,
        'page' => $page,
        'fieldCount' => $fieldCount,
        'child' => $attrKey == $lastElement ? 'last' : true
      ));
    }
  }
?>

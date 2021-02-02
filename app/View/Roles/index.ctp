<div class="roles index">
    <h2><?php echo __('Roles');?></h2>
    <div class="pagination">
        <ul>
        <?php
        $this->Paginator->options(array(
            'update' => '.span12',
            'evalScripts' => true,
            'before' => '$(".progress").show()',
            'complete' => '$(".progress").hide()',
        ));

            echo $this->Paginator->prev('&laquo; ' . __('previous'), array('tag' => 'li', 'escape' => false), null, array('tag' => 'li', 'class' => 'prev disabled', 'escape' => false, 'disabledTag' => 'span'));
            echo $this->Paginator->numbers(array('modulus' => 20, 'separator' => '', 'tag' => 'li', 'currentClass' => 'active', 'currentTag' => 'span'));
            echo $this->Paginator->next(__('next') . ' &raquo;', array('tag' => 'li', 'escape' => false), null, array('tag' => 'li', 'class' => 'next disabled', 'escape' => false, 'disabledTag' => 'span'));
        ?>
        </ul>
    </div>
    <table class="table table-striped table-hover table-condensed">
    <tr>
            <th><?php echo $this->Paginator->sort('id');?></th>
            <th><?php echo __('Default');?></th>
            <th><?php echo $this->Paginator->sort('name');?></th>
            <th><?php echo $this->Paginator->sort('permission', 'Permission');?></th>
            <?php
                foreach ($permFlags as $k => $flags):
            ?>
                <th title="<?php echo h($flags['title']); ?>"><?php echo $this->Paginator->sort($k, $flags['text']);?></th>
            <?php
                endforeach;
            ?>
    </tr><?php
foreach ($list as $item): ?>
    <tr>
        <td class="short"><?php echo h($item['Role']['id']); ?>&nbsp;</td>
        <td class="short" style="text-align:center;width:20px;"><div class="icon-<?php echo $default_role_id == $item['Role']['id'] ? __('ok') : __('remove') ?>"></div></td>
        <td><?php echo h($item['Role']['name']); ?>&nbsp;</td>
        <td class="short"><?php echo h($options[$item['Role']['permission']]); ?>&nbsp;</td>
        <?php foreach ($permFlags as $k => $flags): ?>
            <td class="short"><span class="<?php if ($item['Role'][$k]) echo 'icon-ok'; ?>"></span>&nbsp;</td>
        <?php endforeach; ?>
    </tr><?php
endforeach; ?>
    </table>
    <p>
    <?php
    echo $this->Paginator->counter(array(
    'format' => __('Page {:page} of {:pages}, showing {:current} records out of {:count} total, starting on record {:start}, ending on {:end}')
    ));
    ?>
    </p>
    <div class="pagination">
        <ul>
        <?php
            echo $this->Paginator->prev('&laquo; ' . __('previous'), array('tag' => 'li', 'escape' => false), null, array('tag' => 'li', 'class' => 'prev disabled', 'escape' => false, 'disabledTag' => 'span'));
            echo $this->Paginator->numbers(array('modulus' => 20, 'separator' => '', 'tag' => 'li', 'currentClass' => 'active', 'currentTag' => 'span'));
            echo $this->Paginator->next(__('next') . ' &raquo;', array('tag' => 'li', 'escape' => false), null, array('tag' => 'li', 'class' => 'next disabled', 'escape' => false, 'disabledTag' => 'span'));
        ?>
        </ul>
    </div>
</div>
<?php
    echo $this->element('side_menu', array('menuList' => 'globalActions', 'menuItem' => 'roles'));

<div id="server_push_rule_popover" class="ajax_popover_form server_rule_popover">
    <div class="confirmation">
        <legend><?php echo __('Set push rules');?></legend>
        <div style="padding-left:5px;padding-right:5px;padding-bottom:5px;">
        <div style="padding:10px;">
            <table>
                <tr>
                    <td style="width:120px;">
                        <p style="color:green;font-weight:bold;"><?php echo __('Allowed Tags (OR)');?></p>
                        <select id="tagspushLeftValues" size="5" multiple style="width:185px;">
                        </select>
                    </td>
                    <td style="width:50px;text-align:center;">
                        <span title="<?php echo __('Move tag to the list of tags to allow');?>" role="button" tabindex="0" aria-label="<?php echo __('Move tag to the list of tags to allow');?>" class="btn btn-inverse" id="tagspushLeftLeft" onClick="serverRuleMoveFilter('push', 'tags', 'Middle', 'Left');" style="padding:2px;">&lt;&lt;</span>
                        <span title="<?php echo __('Remove tag from the list of tags to allow');?>" role="button" tabindex="0" aria-label="<?php echo __('Remove tag from the list of tags to allow');?>"class="btn btn-inverse" id="tagspushLeftRight" onClick="serverRuleMoveFilter('push', 'tags', 'Left', 'Middle');" style="padding:2px;">&gt;&gt;</span>
                    </td>
                    <td style="width:120px;">
                        <p style="font-weight:bold;"><?php echo __('Available Tags');?></p>
                        <select id="tagspushMiddleValues" size="5" multiple style="width:185px;">
                        </select>
                    </td>
                    <td style="width:50px;text-align:center;">
                        <span title="<?php echo __('Remove tag from the list of tags to block');?>" role="button" tabindex="0" aria-label="<?php echo __('Remove tag from the list of tags to block');?>" class="btn btn-inverse" id="tagspushRightLeft" style="padding:2px;" onClick="serverRuleMoveFilter('push', 'tags', 'Right', 'Middle');">&lt;&lt;</span>
                        <span title="<?php echo __('Move tag to the list of tags to block');?>" role="button" tabindex="0" aria-label="<?php echo __('Move tag to the list of tags to block');?>" class="btn btn-inverse" id="tagspushRightRight" style="padding:2px;" onClick="serverRuleMoveFilter('push', 'tags', 'Middle', 'Right');">&gt;&gt;</span>
                    </td>
                    <td style="width:120px;">
                        <p style="color:red;font-weight:bold;"><?php echo __('Blocked Tags (AND NOT)');?></p>
                        <select id="tagspushRightValues" size="5" multiple style="width:185px;"></select>
                    </td>
                </tr>
                <tr>
                    <td class="bold green center" style="padding-bottom:15px;padding-top:15px;"><?php echo __('AND');?></td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td class="bold red center" style="padding-bottom:15px;padding-top:15px;"><?php echo __('AND NOT');?></td>
                </tr>
                <tr>
                    <td style="width:120px;">
                        <p style="color:green;font-weight:bold;"><?php echo __('Allowed Orgs (OR)');?></p>
                        <select id="orgspushLeftValues" size="5" multiple style="width:185px;">
                        </select>
                    </td>
                    <td style="width:50px;text-align:center;">
                        <span title="<?php echo __('Move organisation to the list of organisations to allow');?>" role="button" tabindex="0" aria-label="<?php echo __('Move organisation to the list of organisations to allow');?>" class="btn btn-inverse" id="orgspushLeftLeft" onClick="serverRuleMoveFilter('push', 'orgs', 'Middle', 'Left');" style="padding:2px;">&lt;&lt;</span>
                        <span title="<?php echo __('Remove organisation from the list of organisations to allow');?>" role="button" tabindex="0" aria-label="<?php echo __('Remove organisation from the list of organisations to allow');?>" class="btn btn-inverse" id="orgspushLeftRight" onClick="serverRuleMoveFilter('push', 'orgs', 'Left', 'Middle');" style="padding:2px;">&gt;&gt;</span>
                    </td>
                    <td style="width:120px;">
                        <p style="font-weight:bold;"><?php echo __('Available  Organisations');?></p>
                        <select id="orgspushMiddleValues" size="5" multiple style="width:185px;">
                        </select>
                    </td>
                    <td style="width:50px;text-align:center;">
                        <span title="<?php echo __('Remove organisation from the list of organisations to block');?>" role="button" tabindex="0" aria-label="<?php echo __('Remove organisation from the list of organisations to block');?>" class="btn btn-inverse" id="orgspushRightLeft" onClick="serverRuleMoveFilter('push', 'orgs', 'Right', 'Middle');" style="padding:2px;">&lt;&lt;</span>
                        <span title="<?php echo __('Move organisation to the list of organisations to block');?>" role="button" tabindex="0" aria-label="<?php echo __('Move organisation to the list of organisations to block');?>"class="btn btn-inverse" id="orgspushRightRight" onClick="serverRuleMoveFilter('push', 'orgs', 'Middle', 'Right');" style="padding:2px;">&gt;&gt;</span>
                    </td>
                    <td style="width:120px;">
                        <p style="color:red;font-weight:bold;"><?php echo __('Blocked Orgs (AND NOT)');?></p>
                        <select id="orgspushRightValues" size="5" multiple style="width:185px;"></select>
                    </td>
                </tr>
            </table>
        </div>
            <table>
                <tr>
                    <td style="vertical-align:top">
                        <span id="PromptYesButton" class="btn btn-primary" onClick="submitServerRulePopulateTagPicklistValues('push');"><?php echo __('Update');?></span>
                    </td>
                    <td style="width:540px;">
                    </td>
                    <td style="vertical-align:top;">
                        <span class="btn btn-inverse" id="PromptNoButton" onClick="serverRuleCancel();"><?php echo __('Cancel');?></span>
                    </td>
                </tr>
            </table>
        </div>
    </div>
</div>

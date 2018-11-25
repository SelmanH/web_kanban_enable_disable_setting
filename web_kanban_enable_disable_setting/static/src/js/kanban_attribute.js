odoo.define('enable_disable_kanbanview_group_setting', function (require) {
    "use strict";

    var config = require('web.config');
    var core = require('web.core');
    var Dialog = require('web.Dialog');
    var form_common = require('web.form_common');
    var Widget = require('web.Widget');
    var quick_create = require('web_kanban.quick_create');
    var KanbanRecord = require('web_kanban.Record');
    var KanbanColumn = require('web_kanban.Column');
    var KanbanView = require('web_kanban.KanbanView');

    KanbanColumn.include({
        init: function(parent, group_data, options, record_options) {
            this._super.apply(this, arguments);
            this.enable_setting = true ;
            if (options.enable_setting != 'undefined'){
                this.enable_setting = options.enable_setting;
            }
        },
    });

    KanbanView.include({
        get_column_options: function () {
            return {
                editable: this.is_action_enabled('group_edit'),
                deletable: this.is_action_enabled('group_delete'),
                enable_setting: this.is_action_enabled('enable_setting'),
                has_active_field: this.has_active_field(),
                grouped_by_m2o: this.grouped_by_m2o,
                relation: this.relation,
                qweb: this.qweb,
                fields: this.fields_view.fields,
                quick_create: this._is_quick_create_enabled(),
            };
        },
    })
});
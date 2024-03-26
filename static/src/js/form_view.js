odoo.define('digizilla.form_view', function (require) {
    "use strict";

    var core = require('web.core');
    var FormController = require('web.FormController');

    FormController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            if (this.mode === 'readonly') {
                this.$buttons.find('.o_form_button_create').hide();
            }
        },
    });
});


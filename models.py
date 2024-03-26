from odoo import models, fields

class Digizilla(models.Model):
    _name = 'digizilla.digizilla'
    _description = 'Digizilla Model'

    name = fields.Char(string="Name", required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    country = fields.Char(string="Country")
    joining_date = fields.Date(string="Joining Date")
    tags = fields.Many2many('digizilla.tags', string="Tags")
    customers = fields.Many2many('res.partner', string="Customers")
    company = fields.Many2one('res.company', string="Company", required=True)
    notes = fields.Text(string="Notes")
    comments = fields.Char(string="Comments")

    def write(self, vals):
        # Add your custom code here to log changes
        res = super(Digizilla, self).write(vals)
        # Log the changes
        # Example: self.env['logger.model'].create({'record_id': self.id, 'changes': vals})
        return res


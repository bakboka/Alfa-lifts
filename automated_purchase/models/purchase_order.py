from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    invoice_id = fields.Many2one('account.invoice', string="Invoice")

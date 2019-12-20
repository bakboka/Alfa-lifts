from odoo import api, fields, models, _


class Invoice(models.Model):
    _inherit = 'account.invoice'

    def create_purchase_order(self):
        default_vendor = self.env['res.partner'].search([('name', '=', 'الفا ليفتس - المصنع')], limit=1)
        if not default_vendor:
            default_vendor = self.env['res.partner'].search([('supplier', '=', True)], limit=1)
        self.env['purchase.order'].create({
            'partner_id': default_vendor.id,
            'invoice_id': self.id,
            'order_line': [(0, 0, {
                'product_id': line.product_id.id,
                'name': line.name,
                'date_planned': fields.Datetime.now(),
                'product_qty': line.quantity,
                'product_uom': line.product_id.uom_id.id,
                'price_unit': self.env['product.template'].search([('id', '=', line.product_id.id)], limit=1).seller_ids[0].price
            }) for line in self.invoice_line_ids],
        })
        self.write({
            'purchase_id': self.env['purchase.order'].search([], limit=1).id
        })

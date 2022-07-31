from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    report_description = fields.Text(string="Notas", required=False, copy=False)


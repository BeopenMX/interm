from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    report_description = fields.Text(string="Notas", required=False, copy=False)

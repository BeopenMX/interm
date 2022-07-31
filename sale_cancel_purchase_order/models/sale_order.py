# Copyright 2021 Munin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _activity_cancel_on_purchase(self):
        purchases = self.env['purchase.order'].search([('origin', 'ilike', self.name)])
        for purchase in purchases:
            orders = purchase.origin.split(',') if purchase.origin else []  # get the orders
            is_valid = self.name in orders and not len(orders) > 1  # just make sure that you there is no more orders
            if is_valid:
                purchase.button_cancel()
        return super(SaleOrder, self)._activity_cancel_on_purchase()

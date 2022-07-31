# -*- coding: utf-8 -*-
# © 2021 PRAGMATIC
from odoo import api, fields, models
import dateutil.parser
import datetime


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange("date_order")
    def onchange_date_order(self):
        self.x_studio_fecha = self.date_order

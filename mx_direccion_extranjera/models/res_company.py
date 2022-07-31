# -*- coding: utf-8 -*-
# © 2021 PRAGMATIC
from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    street_foreign = fields.Char(string="Dirección Extranjera")

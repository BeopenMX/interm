# Copyright 2017, Jarsa Sistemas, S.A. de C.V.
from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    l10n_mx_edi_fuel_code_sat_ids = fields.Many2many(
        'l10n_mx_edi.product.sat.code', string='SAT fuel codes',
        domain=[('applies_to', '=', 'product')])

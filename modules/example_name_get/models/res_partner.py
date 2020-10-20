# -*- coding: utf-8 -*-

from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    custom_model = fields.Many2one('custom.model', string='Custom Model')

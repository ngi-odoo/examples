# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CustomModel(models.Model):
    _name = 'custom.model'
    _description = 'Custom Model'
    _rec_name = 'custom_name'

    name = fields.Char('Name', default='Name', required=True)
    custom_int = fields.Integer('Custom Int', required=True)
    custom_name = fields.Char('Custom Name', compute='_compute_custom_name')

    @api.depends('name', 'custom_int')
    def _compute_custom_name(self):
        self.custom_name = self.name + ' - ' + str(self.custom_int)

# -*- coding: utf-8 -*-

from odoo import fields, models


class Partner(models.Model):
    # We inherit the res.partner model
    # In that case, we don't redefine _name so _name is 'res.partner'
    # Like _name is the same as res.partner, this model will "extend"
    #   res.partner model and not duplicate it
    # So, creating new variables will create new entries in res_partner table
    _inherit = ['res.partner']

    # Two simple fields that will be added in res_partner table
    name_before = fields.Char('Name before', default='before')
    name_after = fields.Char('Name after', default='after')
    name_inside = fields.Char('Name inside', default='inside')
    name_replace = fields.Char('Name replace', default='replace')
    name_move = fields.Char('Name move', default='move')
    incorrect_display = fields.Char('Incorrect display', default='Incorrect')
    incorrect_display2 = fields.Char('Incorrect display 2', default='Incorrect 2')
    incorrect_display3 = fields.Char('Incorrect display 3', default='Incorrect 3')
    incorrect_display4 = fields.Char('Incorrect display 4', default='Incorrect 4')

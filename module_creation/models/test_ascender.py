# -*- coding: utf-8 -*-

from odoo import models, fields


class TestAscender(models.Model):
    _name = 'test.ascender'
    _description = 'test_ascender'

    name = fields.Char(
        string='Name'
    )
    date = fields.Date(
        string='Date'
    )

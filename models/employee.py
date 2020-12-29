# -*- coding: utf-8 -*-
from odoo import fields, models


class Employee(models.Model):
    _inherit = 'hr.employee.skill'

    release_date = fields.Date(string="Release Date")
    expiration_date = fields.Date(string="Expiration Date")
    document_number = fields.Char(string="Document Number")
    issuing_authority = fields.Selection([
        ('k1', 'Kontrahent 1'),
        ('k2', 'Kontrahent 2'),
        ('k3', 'Kontrahent 3'),
        ('k4', 'Kontrahent 4'),
    ], string="Issuing Authority")

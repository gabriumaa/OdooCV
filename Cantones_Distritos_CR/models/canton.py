# -*- coding: utf-8 -*-

from odoo import models, fields, api

class canton(models.Model):
     _name = 'canton.state'
     _description = 'Cantón'

     id = fields.Integer( string="Código de cantón", required=True )
     name = fields.Char( string="Nombre cantón", required=True )
     state = fields.Many2one( comodel_name="res.country.state", string="Provincia", required=True )
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class distrito(models.Model):
     _name = 'distrito.canton'
     _description = 'Distrito'

     id = fields.Integer( string="Código de distrito", required=True )
     name = fields.Char( string="Nombre distrito", required=True )
     canton = fields.Many2one( comodel_name="canton.state", string="Cantón", required=True )
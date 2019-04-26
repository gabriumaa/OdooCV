# -*- coding: utf-8 -*-

from odoo import models, fields, api


class canton(models.Model):
    _name = "res.country.state.canton"
    _description = "Cantón"

    name = fields.Char( string="Nombre cantón", required=True )
    code = fields.Char( string="Código de cantón", size=4, required=True )
    state_id = fields.Many2one( comodel_name="res.country.state", string="Provincia", domain="[('country_id','=',country_id)]", required=True )
    country_id = fields.Many2one( comodel_name="res.country", string="País", required=True )
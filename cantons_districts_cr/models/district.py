# -*- coding: utf-8 -*-

from odoo import models, fields, api


class district(models.Model):
    _name = "res.country.state.canton.district"
    _description = "Distrito"

    code = fields.Char( string="Código de distrito", size=5, required=True )
    name = fields.Char( string="Nombre cantón", required=True )
    canton_id = fields.Many2one( comodel_name="res.country.state.canton", string="Cantón", domain="[('state_id','=',state_id)]", required=True )
    state_id = fields.Many2one( comodel_name="res.country.state", string="Provincia", domain="[('country_id','=',country_id)]", required=True )
    country_id = fields.Many2one( comodel_name="res.country", string="País", required=True )
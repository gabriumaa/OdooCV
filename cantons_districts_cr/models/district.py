# -*- coding: utf-8 -*-

from odoo import models, fields, api


class District(models.Model):
    _name = "res.country.state.canton.district"
    _description = "Distrito"

    name = fields.Char(string="Nombre distrito", required=True)
    code = fields.Char(string="Código de distrito", size=5, required=True)
    canton_id = fields.Many2one(comodel_name="res.country.state.canton", string="Cantón", domain="[('state_id','=',state_id)]", required=True, ondelete="restrict")
    state_id = fields.Many2one(comodel_name="res.country.state", string="Provincia", domain="[('country_id','=',country_id)]", required=True, ondelete="restrict")
    country_id = fields.Many2one(comodel_name="res.country", string="País", required=True, ondelete="restrict")

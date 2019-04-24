# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inheritContact(models.Model):
    _inherit = "res.partner"

    district_id = fields.Many2one( comodel_name="res.country.state.canton.district", domain="[('canton_id','=',canton_id)]" )
    canton_id = fields.Many2one( comodel_name="res.country.state.canton", domain="[('state_id','=',state_id)]" )

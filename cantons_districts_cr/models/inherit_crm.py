# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inheritCrm(models.Model):
    _inherit = "crm.lead"

    district_id = fields.Many2one( comodel_name="res.country.state.canton.district", domain="[('canton_id','=',canton_id)]" )
    canton_id = fields.Many2one( comodel_name="res.country.state.canton", domain="[('state_id','=',state_id)]" )

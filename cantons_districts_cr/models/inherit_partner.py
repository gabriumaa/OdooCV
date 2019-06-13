# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritPartner(models.Model):
    _inherit = "res.partner"

    district_id = fields.Many2one(comodel_name="res.country.state.canton.district", string="Distrito", domain="[('canton_id','=',city)]", ondelete="restrict")
    city = fields.Many2one(comodel_name="res.country.state.canton", string="Cantón", domain="[('state_id','=',state_id)]", ondelete="restrict")

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            self.state_id = False
            self.city = False
            self.district_id = False
            self.zip = ""

    @api.onchange('state_id')
    def _onchange_state_id(self):
        if self.state_id:
            self.city = False
            self.district_id = False
            self.zip = ""

    @api.onchange('city')
    def _onchange_city(self):
        if self.city:
            self.district_id = False
            self.zip = ""

    @api.onchange('district_id')
    def _onchange_district_id(self):
        if self.district_id:
            self.zip = self.district_id.code
        else:
            self.zip = ""


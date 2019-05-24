# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritPartner(models.Model):
    _inherit = "res.partner"

    district_id = fields.Many2one(comodel_name="res.country.state.canton.district", string="Distrito", domain="[('canton_id','=',city)]", ondelete="restrict")
    city = fields.Many2one(comodel_name="res.country.state.canton", string="Cantón", domain="[('state_id','=',state_id)]", ondelete="restrict")

    @api.onchange('district_id')
    def _onchange_district(self):
        if self.district_id:
            self.zip = self.district_id.code
        else:
            self.zip = ""

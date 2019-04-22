# -*- coding: utf-8 -*-

from odoo import models, fields, api


class canton(models.Model):
    _name = 'res.country.state.canton'
    _description = 'Cantón'

    code = fields.Char( string="Código de cantón", size=3, required=True )
    name = fields.Char( string="Nombre cantón", required=True )
    state_id = fields.Many2one( comodel_name="res.country.state", string="Provincia", required=True )
    country_id = fields.Many2one( comodel_name="res.country", string="País", required=True )

    @api.multi
    @api.onchange('country_id')
    def _onchange_country(self):
        if self.country_id:
            return {'domain': {'state_id': [('res.country.state.country_id', '=', self.country_id.id)]}}
        else:
            return {'domain': {'state_id': []}}

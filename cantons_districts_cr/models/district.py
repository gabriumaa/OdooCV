# -*- coding: utf-8 -*-

from odoo import models, fields, api


class distrito(models.Model):
    _name = 'res.country.state.canton.district'
    _description = 'Distrito'

    code = fields.Char( string="Código de distrito", size=4, required=True )
    name = fields.Char( string="Nombre cantón", required=True )
    canton_id = fields.Many2one( comodel_name="res.country.state.canton", string="Cantón", required=True )
    state_id = fields.Many2one( comodel_name="res.country.state", string="Provincia", required=True )
    country_id = fields.Many2one( comodel_name="res.country", string="País", required=True )

    @api.multi
    @api.onchange('country_id')
    def _onchange_country(self):
        if self.country_id:
            return {'domain': {'state_id': [('res.country.state.country_id', '=', self.country_id.id)]}}
        else:
            return {'domain': {'state_id': []}}

    @api.multi
    @api.onchange('state_id')
    def _onchange_state(self):
        if self.state_id:
            return {'domain': {'canton_id': [('res.country.state.canton.state_id', '=', self.state_id.id)]}}
        else:
            return {'domain': {'canton_id': []}}

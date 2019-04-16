# -*- coding: utf-8 -*-

from odoo import models, fields, api

class canton(models.Model):
    _name = 'canton.state'
    _description = 'Cantón'

    id = fields.Char( string="Código de cantón", size=3, required=True )
    name = fields.Char( string="Nombre cantón", required=True )
    state_fk = fields.Many2one( comodel_name="res.country.state", string="Provincia", required=True )
    country_fk = fields.Many2one( comodel_name="res.country", string="País", required=True )


@api.onchange('country_fk')
def _onchange_country(self):
    if self.country_fk:
        return {'domain': {'state_fk': [('res.country.state.country_id', '=', self.country_fk.id)]}}
    else:
        return {'domain': {'state_fk': []}}

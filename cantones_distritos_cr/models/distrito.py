# -*- coding: utf-8 -*-

from odoo import models, fields, api

class distrito(models.Model):
     _name = 'distrito.canton'
     _description = 'Distrito'

     id = fields.Integer( string="Código de distrito", required=True )
     name = fields.Char( string="Nombre distrito", required=True )
     canton_fk = fields.Many2one( comodel_name="canton.state", string="Cantón", required=True )
     state_fk = fields.Many2one( comodel_name="res.country.state", string="Provincia", required=True )
     country_fk = fields.Many2one( comodel_name="res.country", string="País", required=True )

@api.onchange('country_fk')
def _onchange_country(self):
    if self.country_fk:
        return {'domain': {'state_fk': [('res.country.state.country_id', '=', self.country_fk.id)]}}
    else:
        return {'domain': {'state_fk': []}}

@api.onchange('state_fk')
def _onchange_state(self):
    if self.state_fk:
        return {'domain': {'canton_fk': [('canton.state.state_fk', '=', self.state_fk.id)]}}
    else:
        return {'domain': {'canton_fk': []}}

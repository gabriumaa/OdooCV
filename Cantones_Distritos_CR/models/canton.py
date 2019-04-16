# -*- coding: utf-8 -*-

from odoo import models, fields, api


class canton(models.Model):
    _name = 'canton.state'
    _description = 'Cantón'

    id = fields.Char( string="Código de cantón", size=2, required=True )
    name = fields.Char( string="Nombre cantón", required=True )
    state = fields.Many2one( comodel_name="res.country.state", string="Provincia", required=True )
    country = fields.Many2one( comodel_name="res.country", string="País", required=True )


@api.onchange('country')
def _onchange_country(self):
    if self.country_id:
        self.state = {'domain': {'state_id': [('country_id', '=', self.country.id)]}}
    else:
        self.state = {'domain': {'state_id': []}}

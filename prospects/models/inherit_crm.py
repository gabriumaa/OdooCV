# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inheritCrm(models.Model):
    _inherit = "crm.lead"

    company_type = fields.Selection( [("person", "Individual"), ("company", "Compañía")], string="Tipo de cliente", default="person" )
    vat = fields.Char( string="Cédula o identificación" )
    electric_company = fields.Selection( [("cnfl", "CNFL"), ("ice", "ICE"), ("esph", "ESPH"), ("jasec", "JASEC")], string="Compañía eléctrica" )
    nise = fields.Char( string="NISE" )
    node = fields.Char( string="Nodo" )
    plate = fields.Char( string="Placa" )
    other_phone = fields.Char( string="Otro teléfono" )
    function = fields.Many2one( comodel_name="res.partner.industry", string="Ocupación" )

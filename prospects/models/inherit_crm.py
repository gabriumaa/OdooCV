# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inheritCrm(models.Model):
    _inherit = "crm.lead"

    company_type = fields.Selection( [("person", "Residencial"), ("company", "Empresarial")], string="Tipo de cliente", default="person" )
    vat = fields.Char( string="Cédula o identificación" )
    function = fields.Many2one( comodel_name="res.partner.industry", string="Puesto de trabajo" )
    electric_company = fields.Selection( [("cnfl", "CNFL"), ("ice", "ICE"), ("esph", "ESPH"), ("jasec", "JASEC")], string="Compañía eléctrica" )
    nise = fields.Char( string="NISE" )
    node = fields.Char( string="Nodo" )
    plate = fields.Char( string="Placa" )
    other_phone = fields.Char( string="Otro teléfono" )
    product_ids = fields.Many2many( comodel_name="product.product", string="Servicios de interés" )


# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritPartner(models.Model):
    _inherit = "res.partner"

    client_number = fields.Char(index=True, string="Número de cliente")
    last_name = fields.Char(index=True, string="Apellidos")
    company_type = fields.Selection(selection=[("person", "Residencial"), ("company", "Empresarial")], string="Company Type", compute="_compute_company_type", inverse="_write_company_type")
    function = fields.Many2one(comodel_name="res.partner.industry", string="Puesto de trabajo")
    electric_company = fields.Selection(selection=[("cnfl", "CNFL"), ("ice", "ICE"), ("esph", "ESPH"), ("jasec", "JASEC")], string="Compañía eléctrica")
    nise = fields.Char(string="NISE")
    node = fields.Char(string="Nodo")
    plate = fields.Char(string="Placa")
    other_phone = fields.Char(string="Otro teléfono")
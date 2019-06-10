# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritPartner(models.Model):
    _inherit = "res.partner"


    company_type = fields.Selection(selection=[("person", "Residencial"), ("company", "Empresarial")], string="Company Type", compute="_compute_company_type", inverse="_write_company_type")
    function = fields.Many2one(comodel_name="res.partner.industry", string="Puesto de trabajo")

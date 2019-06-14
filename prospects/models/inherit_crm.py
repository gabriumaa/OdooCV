# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritCrm(models.Model):
    _inherit = "crm.lead"

    name = fields.Char(compute="_crm_name", index=True)
    first_name = fields.Char(string="Nombre")
    last_name = fields.Char(string="Apellidos")
    company_type = fields.Selection(selection=[("person", "Residencial"), ("company", "Empresarial")], string="Tipo de cliente", default="person")
    planned_revenue = fields.Monetary(currency_field="company_currency", string="Expected Revenue", compute="_products_total")
    vat = fields.Char(string="Cédula o identificación", help="The Tax Identification Number. Complete it if the contact is subjected to government taxes. Used in some legal statements.")
    function = fields.Many2one(comodel_name="res.partner.industry", string="Puesto de trabajo")
    electric_company = fields.Selection(selection=[("cnfl", "CNFL"), ("ice", "ICE"), ("esph", "ESPH"), ("jasec", "JASEC")], string="Compañía eléctrica")
    nise = fields.Char(string="NISE")
    node = fields.Char(string="Nodo")
    plate = fields.Char(string="Placa")
    other_phone = fields.Char(string="Otro teléfono")
    crm_products_ids = fields.One2many(comodel_name="crm.lead.products", inverse_name="crm_lead_id", copy=True)

    @api.onchange('company_type')
    def _onchange_company_type_values(self):
        if self.company_type == "company":
            self.last_name = ""
            self.function = ""

    @api.depends('first_name', 'last_name')
    def _crm_name(self):
        for record in self:
            last_name = record.last_name if record.last_name else ""
            first_name = record.first_name if record.first_name else ""

            record.name = last_name + " " + first_name

    @api.depends('crm_products_ids')
    def _products_total(self):
        for record in self:
            total = 0
            for product in record.crm_products_ids:
                total += product.product_price

            record.planned_revenue = str(total)

    @api.multi
    def action_apply_lead(self):
        """ Override de método action_apply de crm.lead2opportunity.partner
        """
        self.ensure_one()
        values = {
            "name": "convert",
            "team_id": self.team_id.id,
            "action": "nothing"
        }

        if self.partner_id:
            values["partner_id"] = self.partner_id.id

        values.update({"lead_ids": self.id, "user_ids": [self.user_id.id]})
        obj = self.env["crm.lead2opportunity.partner"].create(values)
        obj._convert_opportunity(values)

        return self.redirect_opportunity_view()

    def _onchange_partner_id_values(self, partner_id):
        """ Super de método _onchange_partner_id_values agregando nuevos field """
        result = super(InheritCrm, self)._onchange_partner_id_values(partner_id)

        if partner_id:
            partner = self.env['res.partner'].browse(partner_id)
            result.update({
                'company_type': partner.company_type,
                'first_name': partner.first_name,
                'last_name': partner.last_name,
                'vat': partner.vat,
                'district_id': partner.district_id,
                'electric_company': partner.electric_company,
                'nise': partner.nise,
                'node': partner.node,
                'plate': partner.plate,
                'other_phone': partner.other_phone
            })

        return result

    @api.multi
    def write(self, vals):
        super(InheritCrm, self).write(vals)

        for product in self.crm_products_ids:
            product.product_price = product.product_id.lst_price


class CrmLeadProducts(models.Model):
    _name = "crm.lead.products"
    _description = "Relación de Productos en CRM"

    crm_lead_id = fields.Many2one(comodel_name="crm.lead", ondelete="cascade")
    product_id = fields.Many2one(comodel_name="product.product", string="Código y nombre", required=True, index=True)
    product_price = fields.Integer(string="Precio")

    @api.onchange('product_id')
    def _onchange_product(self):
        if self.product_id:
            self.product_price = self.product_id.lst_price

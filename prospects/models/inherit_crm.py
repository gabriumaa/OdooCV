# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritCrm(models.Model):
    _inherit = "crm.lead"

    last_name = fields.Char(index=True, string="Apellidos")
    company_type = fields.Selection(selection=[("person", "Residencial"), ("company", "Empresarial")], string="Tipo de cliente", default="person")
    planned_revenue = fields.Monetary(currency_field="company_currency", string="Expected Revenue", compute="_products_total")
    vat = fields.Char(string="Cédula o identificación")
    function = fields.Many2one(comodel_name="res.partner.industry", string="Puesto de trabajo")
    electric_company = fields.Selection(selection=[("cnfl", "CNFL"), ("ice", "ICE"), ("esph", "ESPH"), ("jasec", "JASEC")], string="Compañía eléctrica")
    nise = fields.Char(string="NISE")
    node = fields.Char(string="Nodo")
    plate = fields.Char(string="Placa")
    other_phone = fields.Char(string="Otro teléfono")
    crm_products_ids = fields.One2many(comodel_name="crm.lead.products", inverse_name="crm_lead_id", copy=True)

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

    @api.multi
    def write(self, vals):
        super(InheritCrm, self).write(vals)
        for product in self.crm_products_ids:
            product.product_price = product.product_id.lst_price

    @api.depends('crm_products_ids')
    def _products_total(self):
        for record in self:
            total = 0
            for product in record.crm_products_ids:
                total += product.product_price

            record.planned_revenue = str(total)


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

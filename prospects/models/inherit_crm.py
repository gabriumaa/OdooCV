# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inheritCrm(models.Model):
    _inherit = "crm.lead"

    company_type = fields.Selection( [("person", "Residencial"), ("company", "Empresarial")], string="Tipo de cliente", default="person" )
    planned_revenue = fields.Monetary( currency_field='company_currency', string='Expected Revenue', compute='_products_total' )
    vat = fields.Char( string="Cédula o identificación" )
    function = fields.Many2one( comodel_name="res.partner.industry", string="Puesto de trabajo" )
    electric_company = fields.Selection( [("cnfl", "CNFL"), ("ice", "ICE"), ("esph", "ESPH"), ("jasec", "JASEC")], string="Compañía eléctrica" )
    nise = fields.Char( string="NISE" )
    node = fields.Char( string="Nodo" )
    plate = fields.Char( string="Placa" )
    other_phone = fields.Char( string="Otro teléfono" )
    product_ids = fields.Many2many( comodel_name="product.product", string="Servicios de interés" )

    @api.multi
    def action_apply_lead(self):
        """ Override de método action_apply de crm.lead2opportunity.partner
        """
        self.ensure_one()
        values = {
            'name': 'convert',
            'team_id': self.team_id.id,
            'action': 'nothing'
        }

        if self.partner_id:
            values['partner_id'] = self.partner_id.id

        values.update({'lead_ids': self.id, 'user_ids': [self.user_id.id]})
        obj = self.env["crm.lead2opportunity.partner"].create(values)
        obj._convert_opportunity(values)

        return self.redirect_opportunity_view()

    @api.depends('product_ids')
    def _products_total(self):
        total = 0
        for product in self.product_ids:
            total += product.lst_price

        self.planned_revenue = str(total)

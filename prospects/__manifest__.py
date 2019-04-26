# -*- coding: utf-8 -*-
{
    "name": "Prospectos",

    "summary": """
        Proceso de preventa""",

    "description": """
        Mantenga el flujo de preventa hasta la instalación para un futuro cliente.""",

    "author": "Cable Visión de Costa Rica",
    "website": "https://www.cablevision.cr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Sales",
    "version": "1.0",

    # any module necessary for this one to work correctly
    "depends": ["base", "crm", "contacts"],

    # always loaded
    "data": [
        #"security/ir.model.access.csv",
        "views/inherit_crm.xml",
    ],
}
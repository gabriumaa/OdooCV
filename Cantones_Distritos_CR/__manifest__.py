# -*- coding: utf-8 -*-
{
    'name': "Cantones y distritos de Costa Rica",

    'summary': """
        Contiene la información de la división geografíca de Costa Rica""",

    'description': """
        Completa la información de contacto y módulos asociados sobre los datos de dirección de Costa Rica.
    """,

    'author': "Cable Visión de Costa Rica",
    'website': "https://www.cablevision.cr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/tecnicos_view.xml',
        'data/canton.xml',
        'data/distrito.xml'
    ],
}
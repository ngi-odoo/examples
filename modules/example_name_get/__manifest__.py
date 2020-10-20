# -*- coding: utf-8 -*-

{
    'name': 'example_name_get',
    'summary': """
            Show the power of `name_get` and `_rec_name`
    """,
    'description': """
            Show the power of `name_get` method and `_rec_name` field
    """,
    'author': 'ngi-odoo',
    'website': 'https://github.com/ngi-odoo/examples/tree/master/modules/example_name_get',
    'category': 'Example Module',
    'version': '1.0',
    'depends': ['contacts'],
    'data': [
        'views/custom_model.xml',
        'views/res_partner.xml',
        'security/ir.model.access.csv',
    ],
}

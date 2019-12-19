# -*- coding: utf-8 -*-
{
    'name': "automated_purchase",

    'summary': """
        Automated purchase orders based on phases.""",

    'description': """
        
    """,

    'author': "Odoo sa",
    'website': "http://www.odoo.com",

    'category': 'user',
    'version': '0.1',

    'depends': [
        'base',
        'account',
        'sale',
        'purchase',
    ],

    'data': [
        'views/account_invoice.xml'
    ],
    'qweb': [

        ],
}

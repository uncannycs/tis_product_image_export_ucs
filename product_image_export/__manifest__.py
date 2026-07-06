# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO Open Source Management Solution
#
#    ODOO Addon module by Uncanny Consulting Services LLP
#    Copyright (C) 2025 Uncanny Consulting Services LLP (<https://uncannycs.com>).
#
##############################################################################
{
    "name": 'Product Image Export UCS',
    "version": '18.0.1.0.0',
    "sequence": 1,
    "category": 'Inventory',
    "summary": 'Product Image Export',
    "website": "https://uncannycs.com",
    "author": "Uncanny Consulting Services LLP",
    "maintainers": "Uncanny Consulting Services LLP",
    'description': """Product Image Export
        """,
    'depends': ['stock',
                ],

    'data': [
        'report/product_report.xml',
        'wizard/product_details_view.xml',
        'security/ir.model.access.csv',
    ],
    'images': ["static/description/banner.gif"],
    'installable': True,
    'application': True,
    'auto_install': False,
    "price":25.00,
    "currency":'USD',
}

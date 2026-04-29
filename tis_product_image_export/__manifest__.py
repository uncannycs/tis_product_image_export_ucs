# -- coding: utf-8 --
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2019. All rights reserved.

{
    'name': 'Product Image Export UCS',
    'version': '17.0.1.0.0',
    'sequence': 1,
    'category': 'Inventory',
    'summary': 'Product Image Export',
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'website': 'http://www.technaureus.com/',
    'price': 25,
    'currency': 'USD',
    'license': 'Other proprietary',
    'description': """Product Image Export
        """,
    'depends': ['stock',
                ],

    'data': [
        'report/product_report.xml',
        'wizard/product_details_view.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

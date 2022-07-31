# Copyright 2021 Munin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Cancel Purchase Order',
    'description': """
        Module to cancel Make to Order Purchase Orders  when canceling a Sale Order""",
    'version': '13.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Munin',
    'depends': ['sale','sale_purchase'
    ],
    'data': [
        # 'views/sale_order.xml',
    ],
    'demo': [
    ],
}

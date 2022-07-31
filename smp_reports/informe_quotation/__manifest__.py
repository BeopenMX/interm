{
    'name': 'Xmarts Reporte cotizacion interm',
    'version': '13',
    'category': "",
    'description': """ Sales quotation Report 
    Reporte Cotizacion 
    """,
    'author':'Xmarts',
    'depends': ['base','sale'],
    'data': [
        "report/sale_quotation.xml",
        "views/sale_order.xml",
    ],
    'qweb': [
        ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    "images": ['static/src/img/Ubicacion.jpg' , 'static/src/img/telefono.jpg' , 'static/src/img/Correo.jpg'],
}

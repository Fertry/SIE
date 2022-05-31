# -*- coding: utf-8 -*-

{

   'name': 'Gestion de Eventos Salutemedia',
   'summary': 'Gestionar los eventos de Salutemedia',
   'version': '1.0',
   'description': "Modulo personalizado para el ERP de Salutemedia", 
   'depends': ['base'],
   'data': [
       'security/ir.model.access.csv',
       'views/evento.xml',
   ],
   'demo': [],
   'company': 'Salutemedia',
   'website': 'https://salutemedia.es',
   'category': 'Extra tools',
   'installable': True,
   'auto_install': False,

}
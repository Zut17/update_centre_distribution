{
    'name': 'Partenaires - Centres de distribution multiples',
    'version': '15.0.1.0.0',
    'category': 'Sales',
    'summary': 'Permet de sélectionner plusieurs centres de distribution',
    'depends': ['zy_extended_partner_zone'],
    'data': [
        'security/security.xml',
        'views/res_partner_views.xml',
    ],
    'post_init_hook': 'migrate_operating_unit_data',
    'installable': True,
    'application': False,
}
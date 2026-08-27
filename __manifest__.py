{
    'name': "Intégration d'un serveur LLM dans Odoo 18",
    'version': '18.0.1.1.0',
    'summary': 'Module générique pour intégrer un serveur LLM dans Odoo 18',
    'description': """
    """,
    "author"   : "Tony Galmiche / InfoSaône",
    "category" : "InfoSaône",
    'website': '',
    'license': 'AGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/is_vllm_groups.xml',
        'security/ir.model.access.csv',
        'security/is_search_general_rules.xml',
        'views/is_search_general_views.xml',
        'views/res_company_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

{
    'name': 'Odoo Color Theme',
    'version': '15.1',
    'summary': 'Odoo Color Theme',
    'author': 'Nirmal',
    'license': 'AGPL-3',
    'maintainer': 'Nirmal',
    'depends': ['web'],
    'description': """
           Odoo Color Theme
    """,
    'assets': {
        'web._assets_primary_variables': [
            '/odoo_color_theme/static/src/scss/primary_variables_custom.scss',
        ],
        'web.assets_backend': [
            'odoo_color_theme/static/src/js/app_window_title.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}

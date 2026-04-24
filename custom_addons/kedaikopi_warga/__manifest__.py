# -*- coding: utf-8 -*-
{
    'name': "Kedai Kopi Warga - Terpusat",
    'summary': 'Sistem Integrasi POS Terpusat',
    'description': 'Modul middleware untuk integrasi PoS cabang, master menu, dan laporan keuangan konsolidasi.',
    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            'kedaikopi_warga/static/src/scss/kedaikopi_backend.scss',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'data/dummy_data.xml',
        'views/menu_utama.xml',
        'views/monitoring_views.xml',
        'views/master_menu_views.xml',
        'views/transaksi_views.xml',
        'views/laporan_views.xml',
    ],
    'installable': True,
    'application': True,
}
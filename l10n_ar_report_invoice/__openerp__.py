# -*- coding: utf-8 -*-
{
    'name': 'Argentinian Like Invoice Report',
    'version': '1.0',
    'category': 'Localization/Argentina',
    'sequence': 14,
    'summary': '',
    'description': """
Argentinian Like Invoice Report
===============================
    """,
    'author':  'Ingenieria ADHOC',
    'website': 'www.ingadhoc.com',
    'images': [
    ],
    'depends': [
        'report_extended_account',
        'l10n_ar_invoice',
        'l10n_ar_report_base',
    ],
    'data': [
        'invoice_report.xml',
        'views/report_invoice.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
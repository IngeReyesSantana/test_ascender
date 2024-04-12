# -*- coding: utf-8 -*-
{
    'name': "Test Ascender",

    'summary': """
        test_ascender
    """,

    'description': """
        Test Ascender module
    """,

    'author': "Reyes Hernando Santana Perez - inghernandosan@gmail.com",
    'website': "https://shf.com.co",

    'category': 'Operations',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml'
    ],

    'application': True,
    'license': 'LGPL-3',
}

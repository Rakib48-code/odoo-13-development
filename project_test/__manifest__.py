{
    'name': 'Test Module',
    'category': 'Test',
    'summary': 'Create A Demo Module',
    'sequence': '-100',
    'version': '13.1.4.5',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient.xml',
        'wizard/create_appointment_wizard.xml',
        'views/hospital_menu.xml',
        'views/view_patient_menu.xml',
        'views/view_female_patient.xml',
        'views/view_doctor_menu.xml',
        'views/view_appointment_menu.xml',

    ],
    'demo': [
        'demo/patient_demo.xml',
        'demo/doctor_demo.xml',
    ],
    'installable': True,
    'application': True
}

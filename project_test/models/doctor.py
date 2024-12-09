from odoo import api,models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor Information'

    name = fields.Char(string='Name', required=True)
    specialist = fields.Char(string='Specialist')
    doctor_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', required=True)
    image = fields.Binary(string='Image')
    degree = fields.Selection([
        ('mbbs', 'MBBS'),
        ('md', 'MD'),
        ('ms', 'MS'),
        ('bds', 'BDS'),
        ('mch', 'MCh'),
        ('dnb', 'DNB'),
        ('other', 'Other'),
    ], string='Degree', required=True)
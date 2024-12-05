from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient Information'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ], string='Gender', required=True)
    dob = fields.Date(string='Date of Birth')
    blood_group = fields.Selection([
        ('A+', 'A Positive'),
        ('A-', 'A Negative'),
        ('B+', 'B Positive'),
        ('B-', 'B Negative'),
        ('O+', 'O Positive'),
        ('O-', 'O Negative'),
        ('AB+', 'AB Positive'),
        ('AB-', 'AB Negative'),
    ], string='Blood Group')
    ref = fields.Char(string='Reference')
    check_up_date = fields.Date(string='Check Up Date', default=fields.Date.context_today)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')


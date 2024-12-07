from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment Information'
    _rec_name = 'patient_id'

    appointment_date = fields.Date(string='Appointment Date')
    booking_date = fields.Date(string='Booking Date')
    # doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    # sl_no = fields.Integer(string='SL NO')
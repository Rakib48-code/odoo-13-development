from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment Information'

    appointment_date = fields.Date(string='Appointment Date', default=fields.Date.context_today)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
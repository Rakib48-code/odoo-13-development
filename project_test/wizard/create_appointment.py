from odoo import api, models, fields

class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    name = fields.Char(string='Name', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    appointment_date = fields.Date(string='Appointment Date')

    def action_create_appointment(self):
        vals = {
            'patient_id':self.patient_id.id,
            'appointment_date': self.appointment_date
        }

        self.env['hospital.appointment'].create(vals)
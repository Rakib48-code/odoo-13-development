from odoo import api, models, fields,_


class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    name = fields.Char(string='Name', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    date_appointment = fields.Date(string='Appointment Date')
    booking_date = fields.Date(string='Booking Date')

    def action_create(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.date_appointment,
            'booking_date': self.booking_date
        }

        self.env['hospital.appointment'].create(vals)

        # return {
        #     'name': _('Appointment'),
        #     'view_mode': 'form',
        #     'res_model': 'hospital.appointment',
        #     'res_id': appointment_rec.id,
        #     'type': 'ir.actions.act_window',
        #     'target': 'new',
        # }

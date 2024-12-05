from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient Information'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
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
    ref = fields.Char(string='Reference', default='Patients')
    check_up_date = fields.Date(string='Check Up Date', default=fields.Date.context_today)
    doctor_id = fields.Many2many('hospital.doctor', string='Doctor Name', required=True)
    specialist = fields.Char(string='Specialist', related='doctor_id.specialist')
    doctor_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', required=True)
    appointment_id = fields.Many2many('hospital.appointment', string='Appointment')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('approve', 'Approved'),
        ('cancel', 'Cancel')
    ], string='Status', default='draft')
    note = fields.Char(string='Note')
    pt_sl = fields.Char(string='Number of Serial')

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('pt_sl', _('New')) == _('New'):
            vals['pt_sl'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient,self).create(vals) #super(class name, self)
        return res

    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'confirm'

    def action_approve(self):
        self.state = 'approve'

    def action_cancel(self):
        self.state = 'cancel'

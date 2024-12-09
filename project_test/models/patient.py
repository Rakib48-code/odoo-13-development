from odoo import api, fields, models, _
from datetime import date


# from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient Information'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _order = 'id desc'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', required=True)
    dob = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', readonly=False)
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
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor Name', required=False)
    specialist = fields.Char(string='Specialist', related='doctor_id.specialist')
    doctor_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', required=False)
    # appointment_id = fields.Many2many('hospital.appointment', string='Appointment')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('approve', 'Approved'),
        ('cancel', 'Cancel')
    ], string='Status', default='draft')
    note = fields.Text(string='Note')
    image = fields.Binary(string='Image', attachment=True)
    pt_sl = fields.Char(string='Number of Serial', required=True, copy=False, readonly=True,
                        default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('pt_sl', _('New')) == _('New'):
            vals['pt_sl'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient, self).create(vals)  # super(class name, self)
        return res

    @api.depends('dob')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 0

    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'confirm'

    def action_approve(self):
        self.state = 'approve'

    def action_cancel(self):
        self.state = 'cancel'

    # @api.constrains('name','doctor_id')
    # def _check_doctor(self):
    #     for rec in self:
    #         if rec.name == rec.doctor_id:
    #             raise ValidationError("Fields name and doctor must be different")

    def action_url(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': 'https://github.com/Rakib48-code',
        }

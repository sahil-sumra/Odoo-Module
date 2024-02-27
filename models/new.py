from odoo import fields,models,api


class New(models.Model):
	_name = "new.new"
	_description = "this model use to manage additional details"
	_rec_name = "name_id"

	name_id = fields.Many2one(
		'student.student',
		string='Name',required = True
		)
	images = fields.Binary(string="Image",related='name_id.image')
	age = fields.Integer(string="Age",related='name_id.age')
	tutor_id = fields.Many2one(string="tutor",related='name_id.tutor_id')
	id = fields.Char(string="ID",related='name_id.student_id')
	contact = fields.Char(string="Contact",related='name_id.mobile')
	star = fields.Selection(string="star",related='name_id.star')
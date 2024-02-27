from odoo import fields,models,api


class Exam(models.Model):
	_name = "exam.exam"
	_description = "exam modules"
	_rec_name = "name_id"

	name_id = fields.Many2one(
		'student.student',
		string='Name',required = True
		)
	std = fields.Selection(String="Standard",related="name_id.std")
	test = fields.Selection([("0","Monthly Test"),("1","Weekly Test")],default="1") 
	maths = fields.Integer(string="Maths")
	ss = fields.Integer(string="Social Science")
	snskrit = fields.Integer(string="Sanskrit")
	science = fields.Integer(string="Science")
	eng = fields.Integer(string="English")
	hin = fields.Integer(string="Hindi")
	guj = fields.Integer(string="Gujrati")
	cmp = fields.Integer(string="Computer")


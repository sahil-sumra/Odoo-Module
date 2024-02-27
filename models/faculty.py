from odoo import fields,models,api


class Faculty(models.Model):
	_name = "faculty.faculty"
	_description = "this model use to manage faculty details"
	_rec_name = "faculty_name"

	faculty_name = fields.Char()
	faculty_id = fields.Char(string="Faculty ID")
	gender = fields.Selection([("male","Male"),("female","Female"),("other","Other")])
	mobile = fields.Char(string="Mobile",default="+91 ")
	mail = fields.Char(default="@gmail.com")
	description = fields.Html(string="Description")
	info = fields.Html(string="Info")
	image = fields.Binary(string="Picture")
	rate = fields.Selection([("0","0"),("1","1"),("2","2"),("3","3")])
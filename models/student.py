from odoo import fields,models,api
from datetime import date


class Student(models.Model):
	_name = "student.student"
	_description = "Brilliant Tution Classes"
	_inherit = ['mail.thread','mail.activity.mixin']
	_order = "student_name"
	_rec_name = "student_name"

	student_name = fields.Char(string="Name", tracking=True)
	age = fields.Integer(string="Age",compute="_compute_age")
	student_id = fields.Char(string="Student ID")
	gender = fields.Selection([("male","Male"),("female","Female"),("other","Other")],default="male")
	dob = fields.Date(string="Date of Birth",default=fields.Datetime.now)
	height = fields.Float(string="Height")
	ref = fields.Char(string="Reference" ,help="check scholar to write")
	active = fields.Boolean(string="Active",default=True)
	city = fields.Char(string="City")
	admission = fields.Date(string="Admission Date")
	fee = fields.Selection([("paid","Paid"),("unpaid","Unpaid")],default="unpaid")
	scholar = fields.Boolean(string="Scholar")
	weight = fields.Integer(string="Weight")
	mobile = fields.Char(string="Mobile",default="+91 ")
	mail = fields.Char(default="@gmail.com")
	std = fields.Selection([("6","6th"),("7","7th"),("8","8th"),("9","9th"),('10', '10th'),("11","11th"),("12","12th"),],string="Standard")
	address = fields.Text(string="Address")
	marks = fields.Integer(string="Marks(Previous Year)")
	description = fields.Html(string="Description")
	education = fields.Html(string="Educational Details")
	info = fields.Html(string="Info")
	star = fields.Selection([("0","0"),("1","1"),("2","2"),("3","3"),("4","4"),("5","5")],string="Excellence")
	data = fields.Binary(string="Additional Document")
	image = fields.Binary(string="Picture",help="upload in size 225x225",required=True) 
	contact = fields.Char(string="Emergency Contact",default="+91 ")
	blood_grp = fields.Char(string="Blood Group")
	allergy = fields.Char(string="Allergy",default="None")
	new_ids = fields.One2many('new.new', 'age')
	new_id = fields.One2many('exam.exam', 'test')
	tutor_id = fields.Many2one('faculty.faculty',string='Tutor')
	rating= fields.Selection(related='tutor_id.rate',string="Rating")
	mob = fields.Char(related='tutor_id.mobile',string="Mobile")
	faculty_ids = fields.Many2many('faculty.faculty','faculty_id',string="Faculty Data")
	state = fields.Selection([
		("inquiry","Enrolled"),
		("admission","Unenrolled")
		],string="Status")
	
	@api.depends('dob')
	def _compute_age(self):
			for i in self:
				today = date.today()
				if i.dob:
					i.age = today.year - i.dob.year 
				else:
					i.age=0	

	@api.model
	def create(self, values):
		print("<<<<<<<<<<<<<<<<<<create method triggerd>>>>>>>>>>>>>>>>>>>>",values)
		result = super(Student, self).create(values)
		print('result contains record set : ', result)
		return result

	# write method

	def write(self, vals):
		print("<<<<<<<<<<<<<<<<write method triggered>>>>>>>>>>>>>>>>>>>>>>>", vals)
		return super(Student,self).write(vals)

	def unlink(self):
		print("<<<<<<<<<<<<<<<<<<  unlink method")
		res = super(Student, self).unlink()
		print('deleted by unlink : ', res)
		return res
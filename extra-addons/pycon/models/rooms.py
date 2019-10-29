from odoo import models, fields, api

class PyconRoom(models.Model):
	_name = "pycon.room"

	name = fields.Char(string="Name", required=True)
	capacity = fields.Integer()
	presentations = fields.One2many('pycon.presentation', 'room', 'Presentations')
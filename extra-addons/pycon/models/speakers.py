from odoo import models, fields

class PyconSpeaker(models.Model):
	_name = "pycon.speaker"
	_description="Pycon speakers"

	name = fields.Char(string="Speaker Name")

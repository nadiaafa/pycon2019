from odoo import models, fields, api

class PyconRoom(models.Model):
	_name = "pycon.room"

	name = fields.Char(string="Name", required=True)
	capacity = fields.Integer()
	presentations = fields.One2many('pycon.presentation', 'room', 'Presentations')
	nbr_presentations = fields.Integer(compute="_compute_nbr_presentations")

	@api.depends('presentations')
	def _compute_nbr_presentations(self):
	    for record in self:
	        record.nbr_presentations = len(record.presentations)
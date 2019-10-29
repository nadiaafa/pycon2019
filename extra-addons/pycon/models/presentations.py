# -*- coding: utf-8 -*-

from odoo import models, fields

class PyconPresentation(models.Model):
	_name = "pycon.presentation"
	_description="Pycon Presentations"

	name = fields.Char(string='Name', required=True)
	date = fields.Datetime()
	room = fields.Many2one('pycon.room') 


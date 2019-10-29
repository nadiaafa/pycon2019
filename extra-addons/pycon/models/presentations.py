# -*- coding: utf-8 -*-

from odoo import models, fields

class PyconPresentation(models.Model):
	_name = "pycon.presentation"
	_description="Pycon Presentations"

	name = fields.Char(string='Name', required=True)
	date = fields.Datetime()
	room = fields.Many2one('pycon.room') 
	speakers = fields.Many2many("pycon.speaker", string='Speakers')
	max_attendees = fields.Integer(related='room.capacity')

	_sql_constraints = [
        ('unique_name', 'unique (name)', 'This value already exists !')
    ]
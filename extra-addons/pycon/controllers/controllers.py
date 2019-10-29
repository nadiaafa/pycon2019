# -*- coding: utf-8 -*-
from odoo import http

# class /mnt/extra-addons/pycon(http.Controller):
#     @http.route('//mnt/extra-addons/pycon//mnt/extra-addons/pycon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/pycon//mnt/extra-addons/pycon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/pycon.listing', {
#             'root': '//mnt/extra-addons/pycon//mnt/extra-addons/pycon',
#             'objects': http.request.env['/mnt/extra-addons/pycon./mnt/extra-addons/pycon'].search([]),
#         })

#     @http.route('//mnt/extra-addons/pycon//mnt/extra-addons/pycon/objects/<model("/mnt/extra-addons/pycon./mnt/extra-addons/pycon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/pycon.object', {
#             'object': obj
#         })
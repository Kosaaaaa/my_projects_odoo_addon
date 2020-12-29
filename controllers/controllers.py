# -*- coding: utf-8 -*-
# from odoo import http


# class MyProjects(http.Controller):
#     @http.route('/my_projects/my_projects/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_projects/my_projects/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_projects.listing', {
#             'root': '/my_projects/my_projects',
#             'objects': http.request.env['my_projects.my_projects'].search([]),
#         })

#     @http.route('/my_projects/my_projects/objects/<model("my_projects.my_projects"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_projects.object', {
#             'object': obj
#         })

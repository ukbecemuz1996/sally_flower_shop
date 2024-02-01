# -*- coding: utf-8 -*-
# from odoo import http


# class Sally(http.Controller):
#     @http.route('/sally/sally', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sally/sally/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sally.listing', {
#             'root': '/sally/sally',
#             'objects': http.request.env['sally.sally'].search([]),
#         })

#     @http.route('/sally/sally/objects/<model("sally.sally"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sally.object', {
#             'object': obj
#         })


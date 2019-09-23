from odoo import models,fields,api


class Customer(models.Model):
    _name = 'library.customer'
    _description = 'This is a customer of the library'

    name = fields.Char()

    address = fields.Char()

    birth_date = fields.Date()

    email = fields.Char()

    rental_ids = fields.One2many('library.rental', 'customer_id', readonly=True)
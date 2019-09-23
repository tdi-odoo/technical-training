from odoo import models,fields,api


class Customer(models.Model):
    _name = 'library.book'
    _description = 'This is a book of the library'

    name = fields.Char()

    authors = fields.Char()

    year = fields.Integer()

    ISBN = fields.Char()

    rental_ids = fields.One2many('library.rental', 'book_id', readonly=True)
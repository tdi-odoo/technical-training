from odoo import models,fields,api


class Customer(models.Model):
    _name = 'library.rental'
    _description = 'This is a rental of the library'

    name = fields.Char()

    start_date = fields.Date()

    end_date = fields.Date()

    customer_id = fields.Many2one('library.customer')

    book_id = fields.Many2one('library.book')
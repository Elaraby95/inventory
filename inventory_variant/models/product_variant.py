from odoo import models, fields


class ProductVariant(models.Model):
    _inherit = "product.product"

    unique_code = fields.Char()

# Copyright 2020 MathBenTech <info@mathben.tech>
# License AGPLv3.0 or later (https://www.gnu.org/licenses/agpl-3.0.en.html).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_enable_show_task_id = fields.Boolean(string="Show task_id",
                                            help="Enable to show task_id of each sale.order.line in form and tree view.")

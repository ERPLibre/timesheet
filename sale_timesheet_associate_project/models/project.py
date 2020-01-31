# Copyright 2020 MathBenTech <info@mathben.tech>
# License AGPLv3.0 or later (https://www.gnu.org/licenses/agpl-3.0.en.html).

from odoo import api, models, _


class Project(models.Model):
    _inherit = 'project.project'

    @api.multi
    def action_make_billable_associate(self):
        return {
            "name": _("Associate Sales Order"),
            "type": 'ir.actions.act_window',
            "res_model": 'project.associate.sale.order',
            "views": [[False, "form"]],
            "target": 'new',
            "context": {
                'active_id': self.id,
                'active_model': 'project.project',
            },
        }

# Copyright 2020 MathBenTech <info@mathben.tech>
# License AGPLv3.0 or later (https://www.gnu.org/licenses/agpl-3.0.en.html).

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    stories_ids = fields.Many2many('project.task', compute='_compute_stories_ids',
                                   string='Stories associated to this sale')
    stories_count = fields.Integer(string='Stories', compute='_compute_stories_ids',
                                   groups="project.group_project_user")

    @api.multi
    @api.depends('order_line.story_id')
    def _compute_stories_ids(self):
        for order in self:
            order.stories_ids = [line.story_id.id for line in order.order_line if line.story_id]
            order.stories_count = len(order.stories_ids)

    @api.multi
    def action_view_story(self):
        self.ensure_one()

        list_view_id = self.env.ref('project.view_task_tree2').id
        form_view_id = self.env.ref('project.view_task_form2').id

        action = {'type': 'ir.actions.act_window_close'}

        # TODO upgrade this part when fix timesheet with story
        # Check module sale_timesheet, method action_view_task
        action = self.env.ref('project.action_view_task').read()[0]
        action['context'] = {}  # erase default context to avoid default filter
        if self.stories_count > 1:  # cross project kanban task
            action['views'] = [[False, 'kanban'], [list_view_id, 'tree'], [form_view_id, 'form'], [False, 'graph'],
                               [False, 'calendar'], [False, 'pivot']]
            action['domain'] = [('id', 'in', self.stories_ids.ids)]
        elif self.stories_count == 1:  # single task -> form view
            action['views'] = [(form_view_id, 'form')]
            action['res_id'] = self.stories_ids.id
        # filter on the task of the current SO
        action.setdefault('context', {})
        return action


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # TODO use env.ref("project_agile.project_task_type_story") instead of hardcoded type_id of story/epic
    story_id = fields.Many2one('project.task', 'Story Task', index=True, copy=False,
                               domain=[("type_id", 'in', (7, 9))],
                               help="Associate a story with sales order item.")

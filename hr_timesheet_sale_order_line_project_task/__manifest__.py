# Copyright 2020 MathBenTech <info@mathben.tech>
# License AGPLv3.0 or later (https://www.gnu.org/licenses/agpl-3.0.en.html).

{
    'name': 'Task_id in Sales Orders Line',
    'version': '1.0',
    'category': 'Sales',
    'description': """
This module adds task_id of project in each sale order line
============================================================

    """,
    'depends': ['sale', 'sale_timesheet'],
    'data': ['views/sale_order_line_view.xml'],
}

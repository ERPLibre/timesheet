# Copyright 2020 MathBenTech <info@mathben.tech>
# License AGPLv3.0 or later (https://www.gnu.org/licenses/agpl-3.0.en.html).

{
    "name": "Sale Timesheet associate project",
    "summary": "Associate an existing SO with an existing project.",
    "category": "Sale",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "author": "MathBenTech",
    "website": "https://www.mathben.tech",
    'description': """
Sale Timesheet associate project
================================
Can associate an existing project with an existing Sale Order.
This is used when not following normal workflow.

""",
    "depends": [
        'sale_management',
        'sale_timesheet'
    ],
    "data": [
        "views/project_task_views.xml",
        "wizard/project_associate_sale_order_views.xml",
    ],
    "demo": [],
    "qweb": [],
    "application": False,
}

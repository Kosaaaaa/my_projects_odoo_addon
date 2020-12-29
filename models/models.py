# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Project(models.Model):
    _name = 'my_projects.project'
    _description = 'My Projects Project Model'

    name = fields.Char(string='Project Name', required=True)
    description = fields.Text()
    created_date = fields.Date(default=lambda self: fields.Date.today(), readonly=True)


class Task(models.Model):
    _name = 'my_projects.task'
    _description = 'My Projects Task Model'

    name = fields.Char(string='Task name', required=True)
    description = fields.Text()
    created_date = fields.Date(default=lambda self: fields.Date.today(), readonly=True)
    due_date = fields.Date()
    is_completed = fields.Boolean(default=False, string='Completed')
    project_id = fields.Many2one('my_projects.project', ondelete='cascade', string='Project', required=True)

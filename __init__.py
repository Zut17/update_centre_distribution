from . import models

def migrate_operating_unit_data(cr, registry):
    from odoo import api, SUPERUSER_ID
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['res.partner']._migrate_operating_unit_to_many2many()
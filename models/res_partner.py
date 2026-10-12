from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    operating_unit_ids = fields.Many2many(
        'operating.unit',
        'res_partner_operating_unit_rel',
        'partner_id',
        'operating_unit_id',
        string="Centres de distribution"
    )

    @api.model
    def _migrate_operating_unit_to_many2many(self):
        """Copie les valeurs existantes de operating_unit_id vers operating_unit_ids
        pour ne perdre aucune donnée lors de l'installation du module."""
        partners = self.search([
            ('operating_unit_id', '!=', False),
        ])
        for partner in partners:
            if partner.operating_unit_id.id not in partner.operating_unit_ids.ids:
                partner.operating_unit_ids = [(4, partner.operating_unit_id.id)]
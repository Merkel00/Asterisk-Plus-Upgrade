# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerContact(models.Model):
    _inherit = "asterisk_plus.call"

    partner = fields.Many2one("res.partner", string="Partner", compute="_compute_partner_id")

    @api.depends("calling_user")
    def _compute_partner_id(self):
        for rec in self:
            rec.partner = False
            if rec.calling_user:
                rec.partner = rec.calling_user.parent_id


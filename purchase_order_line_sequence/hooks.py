# Copyright 2017-23 ForgeFlow S.L
# Copyright 2017 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, pool):
    """
    Fetches all the PO and resets the sequence of the purchase order lines.
    """
    env = Environment(cr, SUPERUSER_ID, {})
    purchase = env["purchase.order"].search([])
    purchase._reset_sequence()

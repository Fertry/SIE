from odoo import models, fields, api

class Evento(models.Model):
    _name = "Gestion de eventos"

    name = fields.Char(String="Name")
    destination = fields.Char(String="Destination")
    start_date = fields.Date(String="Start date")
    end_date = fields.Date(String="End date")
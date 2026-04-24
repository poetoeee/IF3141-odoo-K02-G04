from odoo import models, fields

class POSSystem(models.Model):
    _name = 'kedaikopi.pos_system'
    _description = 'Data POS System'
    
    name = fields.Char(string="Nama POS", required=True)
    lokasi_lantai = fields.Selection([('atas', 'Lantai Atas'), ('bawah', 'Lantai Bawah')], string="Lokasi Lantai")
    tipe_sistem = fields.Char(string="Tipe Sistem")
    status_aktif = fields.Boolean(string="Status Aktif", default=True)
    ip_address = fields.Char(string="IP Address")
from odoo import models, fields

class MenuCategory(models.Model):
    _name = 'kedaikopi.menu_category'
    _description = 'Menu Category'
    name = fields.Char(string="Nama Kategori", required=True)
    deskripsi = fields.Text(string="Deskripsi")
    urutan_tampil = fields.Integer(string="Urutan Tampil")

class MenuItem(models.Model):
    _name = 'kedaikopi.menu_item'
    _description = 'Menu Item'
    name = fields.Char(string="Nama Menu", required=True)
    id_kategori = fields.Many2one('kedaikopi.menu_category', string="Kategori")
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    harga = fields.Monetary(string="Harga (Rp)", currency_field='currency_id')
    status_tersedia = fields.Boolean(string="Status Tersedia", default=True)
    varian = fields.Char(string="Varian")
    deskripsi = fields.Text(string="Deskripsi")

    def updateMenu(self):
        return True
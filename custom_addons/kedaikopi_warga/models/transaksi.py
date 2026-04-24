from odoo import models, fields

class Transaction(models.Model):
    _name = 'kedaikopi.transaction'
    _description = 'Transaction'
    name = fields.Char(string="ID Transaksi", required=True)
    id_pos = fields.Many2one('kedaikopi.pos_system', string="POS Cabang")
    waktu_transaksi = fields.Datetime(string="Waktu Transaksi")
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    total_harga = fields.Monetary(string="Total Harga", currency_field='currency_id')
    metode_pembayaran = fields.Selection([('tunai', 'Tunai'), ('qris', 'QRIS'), ('debit', 'Debit')], string="Metode Pembayaran")
    status_transaksi = fields.Char(string="Status Transaksi")
    diskon_loyalitas = fields.Float(string="Diskon Loyalitas")
    item_ids = fields.One2many('kedaikopi.transaction_item', 'id_transaksi', string="Detail Item")

class TransactionItem(models.Model):
    _name = 'kedaikopi.transaction_item'
    _description = 'Transaction Item'
    id_transaksi = fields.Many2one('kedaikopi.transaction', string="Transaksi")
    id_menu = fields.Many2one('kedaikopi.menu_item', string="Menu Item")
    jumlah = fields.Integer(string="Jumlah")
    harga_satuan = fields.Float(string="Harga Satuan")
    subtotal = fields.Float(string="Subtotal")
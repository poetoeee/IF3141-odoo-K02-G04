from odoo import models, fields, api

class SyncLog(models.Model):
    _name = 'kedaikopi.sync_log'
    _description = 'Sync Log'
    name = fields.Char(string="ID Log", required=True, default='New')
    id_pos = fields.Many2one('kedaikopi.pos_system', string="POS Cabang")
    waktu_sinkron = fields.Datetime(string="Waktu Sinkron")
    status_sinkron = fields.Selection([('sukses', 'Sukses'), ('gagal', 'Gagal')], string="Status Sinkron")
    latency_ms = fields.Float(string="Latency API (ms)")
    jumlah_record = fields.Integer(string="Jumlah Record")
    pesan_error = fields.Text(string="Pesan Error")

    def retrySync(self):
        return True
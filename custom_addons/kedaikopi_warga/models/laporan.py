from odoo import models, fields

class FinancialReport(models.Model):
    _name = 'kedaikopi.financial_report'
    _description = 'Financial Report'
    name = fields.Char(string="ID Laporan", required=True)
    periode = fields.Char(string="Periode Laporan")
    tanggal_periode = fields.Date(string="Tanggal Laporan", required=True, default=fields.Date.context_today)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    total_pendapatan = fields.Monetary(string="Total Pendapatan", currency_field='currency_id')
    total_transaksi = fields.Integer(string="Total Transaksi")
    total_pajak_pb1 = fields.Monetary(string="Total Pajak PB1", currency_field='currency_id')
    estimasi_laba_rugi = fields.Monetary(string="Estimasi Laba Rugi", currency_field='currency_id')
    tanggal_dibuat = fields.Datetime(string="Tanggal Dibuat", default=fields.Datetime.now)

    def eksporLaporan(self):
        return True

    def action_dummy(self):
        return True
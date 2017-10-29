

from odoo import fields, models, api
from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx




class brt_customer(models.Model):
    _inherit = 'res.partner'

    codice_cliente = fields.Char()
    tipo_notifica = fields.Selection([(0, 'Nessuna'), (1, 'Email'), (2, 'SMS'), (3, 'Entrambe')])



class brt_sale_order(models.Model):
    _inherit = 'sale.order'

    tipo_servizio_bolle = fields.Selection([('E', 'Espresso'), ('C', 'Corriere'), ('D', 'Distribuzione')])
    codice_bolla = fields.Char()
    numero_bolla_fattura = fields.Integer()
    numero_colli = fields.Integer()
    peso_lordo_spedizione = fields.Float()
    importo_contrassegno = fields.Float()
    note_per_corriere = fields.Text()
    note_per_corriere_due = fields.Text()
    riferimento_mittente = fields.Char()


class Bartolini_xlsx(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, picking_ids):


        sheet = workbook.add_worksheet("brt_export")
        bold = workbook.add_format({'bold': True})

        sheet.write(0, 0, 'vabccm', bold)
        sheet.write(0, 1, 'vabtsp', bold)
        sheet.write(0, 2, 'vablnp', bold)
        sheet.write(0, 3, 'vabctr', bold)
        sheet.write(0, 4, 'vabcbo', bold)
        sheet.write(0, 5, 'vabrmn', bold)
        sheet.write(0, 6, 'vabrsd', bold)
        sheet.write(0, 7, 'vabind', bold)
        sheet.write(0, 8, 'vablod', bold)
        sheet.write(0, 9, 'vabcad', bold)
        sheet.write(0, 10, 'vabprd', bold)
        sheet.write(0, 11, 'vabnzd', bold)
        sheet.write(0, 12, 'vabncl', bold)
        sheet.write(0, 13, 'vabpkb', bold)
        sheet.write(0, 14, 'vabcas', bold)
        sheet.write(0, 15, 'vabvca', bold)
        sheet.write(0, 16, 'vabnot', bold)
        sheet.write(0, 17, 'vabnt2', bold)
        sheet.write(0, 18, 'vabnrc', bold)
        sheet.write(0, 19, 'vabtrc', bold)
        sheet.write(0, 20, 'vabtic', bold)
        sheet.write(0, 21, 'vabemd', bold)
        sheet.write(0, 22, 'vabcel', bold)
        sheet.write(0, 23, 'vabtno', bold)
        sheet.write(0, 24, 'vabrma', bold)

        c = 0
        r = 1
        for o in picking_ids:
            if o.origin:
                order_id = self.env['sale.order'].search([('name','=', o.origin)], limit=1)
                if order_id:
                    sheet.write(r, c, str(o.partner_id.codice_cliente) if o.partner_id.codice_cliente else '')
                    sheet.write(r, c + 1, str(order_id.tipo_servizio_bolle) if order_id.tipo_servizio_bolle  else '')
                    sheet.write(r, c + 2, '53' if '53' else '') #Codice Punto Operativo
                    sheet.write(r, c + 3, '0' if '0' else '') #Codice Tariffa
                    sheet.write(r, c + 4, str(order_id.codice_bolla) if order_id.codice_bolla  else '')
                    sheet.write(r, c + 5, str(order_id.numero_bolla_fattura) if order_id.numero_bolla_fattura  else '')
                    sheet.write(r, c + 6, str(o.partner_id.name) if o.partner_id.name  else '')
                    sheet.write(r, c + 7, str(o.partner_id.street) if o.partner_id.street  else '')
                    sheet.write(r, c + 8, str(o.partner_id.city) if o.partner_id.city  else '')
                    sheet.write(r, c + 9, str(o.partner_id.zip) if o.partner_id.zip  else '')
                    sheet.write(r, c + 10, str(o.partner_id.state_id.code) if o.partner_id.state_id.code  else '')
                    sheet.write(r, c + 11, str(o.partner_id.country_id.name) if o.partner_id.country_id.name else '')
                    sheet.write(r, c + 12, str(order_id.numero_colli) if order_id.numero_colli  else '')
                    sheet.write(r, c + 13, str(order_id.peso_lordo_spedizione) if order_id.peso_lordo_spedizione else '')
                    sheet.write(r, c + 14, str(order_id.importo_contrassegno) if order_id.importo_contrassegno  else '')
                    sheet.write(r, c + 15, str('EUR') if 'EUR'  else '')
                    sheet.write(r, c + 16, str(order_id.note_per_corriere) if order_id.note_per_corriere  else '')
                    sheet.write(r, c + 17, str(order_id.note_per_corriere_due) if order_id.note_per_corriere_due  else '')
                    sheet.write(r, c + 18, str(o.partner_id.name) if o.partner_id.name  else '')
                    sheet.write(r, c + 19, str(o.partner_id.phone) if o.partner_id.phone  else '')
                    sheet.write(r, c + 20, '' if '' else '') #Tipo incasso contrassegno
                    sheet.write(r, c + 21, str(o.partner_id.email) if o.partner_id.email  else '')
                    sheet.write(r, c + 22, str(o.partner_id.mobile) if o.partner_id.mobile  else '')
                    sheet.write(r, c + 23, str(o.partner_id.tipo_notifica) if o.partner_id.tipo_notifica  else '')
                    sheet.write(r, c + 24, str(order_id.riferimento_mittente) if order_id.riferimento_mittente  else '')

                    r += 1



Bartolini_xlsx('report.brt.xlsx', 'stock.picking')









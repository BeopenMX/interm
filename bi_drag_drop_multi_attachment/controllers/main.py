# -*- coding: utf-8 -*-
import json
import base64
import logging


from odoo import http
from odoo.http import request


class UploadAttachment(http.Controller):

    @http.route('/drop_attachment', type='http', auth="user", csrf=False)
    def drop_attachment(self, **post):
        attchment_obj = request.env['ir.attachment']
        try:
            filename = post.get("attachment").filename
            print(post,'============================post \n\n')
            vals = {
                'name' : filename,
                'datas': base64.encodestring(post.get("attachment").read()),
                'res_model': post.get("model", ''),
                'res_id': int(post.get("id", '0')),
                'type': 'binary',
            }
            # print(vals,'============================vals \n\n')
            attach_id = attchment_obj.sudo().create(vals)
            print(attach_id,'===================attach_id \n\n')
            return json.dumps({'success': True})
        except Exception as e:
            return json.dumps({'success': False,'error': "Something wrong happened."})

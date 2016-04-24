# -*- coding: utf-8 -*-

from flask import render_template, request

from bookhouse.core import app


@app.route('/test/', methods=['GET'])
def test():
    if request.method == 'GET':
        return u'test'

# -*- coding: utf-8 -*-

from flask import render_template, request

from bookhouse.core import app
from bookhouse.main.misc.auth import auth_required


@app.route('/my/books/', methods=['GET'])
def books_page():
    return render_template('books.html')


@app.route('/api/books/', methods=['GET', 'POST'])
@auth_required
def books_api():
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        pass


@app.route('/api/books/<int:book_id>/', methods=['GET', 'PUT', 'DELETE'])
@auth_required
def book_api(book_id):
    if request.method == 'GET':
        pass

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass

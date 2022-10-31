"""Application routes."""
from datetime import datetime as dt
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask import current_app as app
from flask import make_response, redirect, render_template, request, url_for
import logging
from .models import students, db, ohlc_test1
logger = logging.getLogger()
@app.route('/')
def ohlc_all():
    return render_template('ohlc_all.html', ohlc_all=ohlc_test1.query.all())

# @app.route('/index')
# def index():
#     return render_template('index.html')

# @app.route('/vote')
# def vote():
#     return render_template('vote.html')

# @app.route('/new', methods=['GET', 'POST'])
# def new():
#     if request.method == 'POST':
#         if not request.form['name'] or not request.form['city'] or not request.form['addr']:
#             flash('Please enter all the fields', 'error')
#         else:
#             student = students(request.form['name'], request.form['city'],
#                                request.form['addr'], request.form['pin'])
#
#             db.session.add(student)
#             db.session.commit()
#             flash('Record was successfully added')
#             return redirect(url_for('show_all'))
#     return render_template('new.html')

@app.route("/ohlc", methods=['GET', 'POST'])
def ohlc():
    if request.method == 'GET':
        return render_template("ohlc_new.html")
    else:
        if request.is_json is True:
            content = request.get_json()
            logger.warning(f"Content of REQUEST: '{content}'")  # {'symbol':'ES1', 'dt':'2022-10-31T14:13:00Z', 'open':3878.5, 'high':3878.5, 'low':3877.5, 'close':3878, 'volume':215}
            temp_dt = dt.fromisoformat(content['dt'][:-1])
            ohlc = ohlc_test1(content['symbol'], temp_dt, content['open'], content['high'],
                               content['low'], content['close'], content['volume'])
            db.session.add(ohlc)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('ohlc_all'))
        else:
            return jsonify({"msg": "Missing JSON in request"}), 400
            # logger.warning(f"Content type of REQUEST: '{request.content_type}'")
            # if not request.form['open'] or not request.form['high'] or not request.form['low'] or not request.form['close']:
            #     flash('Please enter all the fields', 'error')
            # else:
            #     ohlc = ohlc_test(request.form['open'], request.form['high'],
            #                        request.form['low'], request.form['close'])
            #     db.session.add(ohlc)
            #     db.session.commit()
            #     flash('Record was successfully added')
            #     return redirect(url_for('ohlc_all'))


import os
import sqlite3
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for
from ..forms.forms import AppointmentForm

bp = Blueprint('main', __name__, url_prefix='/books')

DB_FILE = os.environ.get('DB_FILE') or 'not found'


@bp.route('/', methods=['GET', 'POST'])
def main():
    form = AppointmentForm()
    if form.validate_on_submit():
        params = {
            'name': form.name.data,
            'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
            'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
            'description': form.description.data,
            'private': form.private.data
        }
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO appointments (name, start_datetime, end_datetime, description, private) VALUES (:name, :start_datetime, :end_datetime, :description, :private);", params)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('main.main'))

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, start_datetime, end_datetime, description, private FROM appointments ORDER BY start_datetime;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    for i, row in enumerate(rows):
        start_datetime_str = row[2]
        end_datetime_str = row[3]
        start_datetime = datetime.strptime(
            start_datetime_str, '%Y-%m-%d %H:%M:%S')
        end_datetime = datetime.strptime(end_datetime_str, '%Y-%m-%d %H:%M:%S')
        rows[i] = row[:2] + (start_datetime, end_datetime,) + row[4:]

    return render_template('main.html', rows=rows, form=form)

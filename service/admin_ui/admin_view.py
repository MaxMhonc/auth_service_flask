from flask import Blueprint, render_template

admin_ui = Blueprint('admin', __name__, template_folder='/templates')


@admin_ui.route('/admin', methods=['GET'])
def admin():
    data = {'name': 'Max'}
    return render_template('menu.html', data=data)

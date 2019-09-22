from init import *
from dbmodels import *


@app.route('/')
@app.route('/index')
def index():
    kwargs = {'title': 'СТП им. Арташеса - Главная'}
    return render_template('index.html', **kwargs)


@app.route('/download/stencil')
def download_stencil():
    return send_file('static/downloadable_content/ГОСТ 19.701-90v5.vssx',
                     attachment_filename='ГОСТ 19.701-90v5.vssx',
                     as_attachment=True)


@app.route('/thanks')
def thank():
    kwargs = {'title': 'СТП им. Арташеса - Главная'}
    return render_template('thank.html', **kwargs)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

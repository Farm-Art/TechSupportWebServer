from init import *
from dbmodels import *


@app.route('/')
@app.route('/index')
def index():
    kwargs = {'title': 'СТП им. Арташеса - Главная',
              'project_name': 'Служба Тех.Поддержки'}
    return render_template('index.html', **kwargs)


@app.route('/download/stencil')
def download_stencil():
    return send_file('static/downloadable_content/ГОСТ 19.701-90v5.vssx',
                     attachment_filename='ГОСТ 19.701-90v5.vssx',
                     as_attachment=True)


@app.route('/download/fontandstencil')
def download_font_and_stencil():
    return send_file('static/downloadable_content/Visio.zip',
                     attachment_filename='ГОСТ-пакет v6.zip',
                     as_attachment=True)


@app.route('/thanks')
def thank():
    kwargs = {'title': 'СТП им. Арташеса - Главная',
              'project_name': 'Служба Тех.Поддержки'}
    return render_template('thank.html', **kwargs)


@app.route('/blog/info')
def bloginfo():
    kwargs = {'title': 'Блог им. Арташеса - Главная',
              'project_name': 'Блог о Программировании'}
    return render_template('bloginfo.html', **kwargs)


@app.route('/lectures')
def lectures():
    kwargs = {'title': 'Лекции им. Арташеса - Главная',
              'project_name': 'Лекции'}
    return render_template('lectures.html', **kwargs)


@app.route('/download/lectures/<string:subject>')
def download_lecture(subject):
    address = filename = None
    if subject == 'informatics':
        filename = "Лекции Информатика.docx"
        address = 'static/downloadable_content/Lectures/' + filename
    if address and filename:
        return send_file(address, attachment_filename=filename,
                         as_attachment=True)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

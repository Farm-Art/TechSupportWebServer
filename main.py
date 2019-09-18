from init import *
from dbmodels import *


@app.route('/')
@app.route('/index')
def index():
    kwargs = {'title': 'СТП им. Арташеса - Главная'}
    return render_template('base.html', **kwargs)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

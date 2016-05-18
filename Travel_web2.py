from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index.html')
def index_():
    return render_template('index.html')

@app.route('/hotel_lichuan.html')
def hotel_lichuan():
    return render_template('hotel_lichuan.html')

@app.route('/ticket.html')
def ticket():
    return render_template('ticket.html')

@app.route('/car.html')
def car():
    return render_template('car.html')

@app.route('/village.html')
def village():
    return render_template('village.html')


@app.route('/eat.html')
def eat():
    return render_template('eat.html')

if __name__ == '__main__':
    app.run()

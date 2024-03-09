from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/gardening')
def gardening_info():
    return render_template('gardening.html')

@app.route('/cooking')
def cooking_details():
    return render_template('cooking.html')

@app.route('/sci-fi')
def sci_fi_world():
    return render_template('sci-fi.html')

if __name__ == '__main__':
       app.run(debug=True)


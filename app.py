from flask import Flask, render_template

app = Flask(__name__)


#Landing Page Route
@app.route('/')
def landing_page():
    return render_template('LandingPage.html')

@app.route('/products')
def products_spread():
    return render_template('ProductSpread.html')

if __name__ == '__main__':
    app.run(debug=True)


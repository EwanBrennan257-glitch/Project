from flask import Flask, render_template, request, redirect, url_for
from Service.UserService import UserService
from Validation.UserValidation import UserValidation

app = Flask(__name__)


#Landing Page Route
@app.route('/')
def landing_page():
    return render_template('LandingPage.html')

@app.route('/products')
def products_spread():
    return render_template('ProductSpread.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        # Process the form data (e.g., save to a database)
        validation=UserValidation()
        UserService(validation).create_user(firstname, lastname, email, password)
        return redirect(url_for('success'))  # Redirect to a success page
    return render_template('SignUp.html')

@app.route('/success')
def success():
    return "Sign-up successful!"

if __name__ == '__main__':
    app.run(debug=True)

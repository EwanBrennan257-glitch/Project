
from flask import (Flask, render_template, request, redirect, url_for,
flash, session,g)

from Service.ProductService import ProductService
from Service.UserService import UserService
from Validation.UserValidation import UserValidation


app = Flask(__name__)

app.secret_key = "mysecretkey"

"""before every request this function will check the session object has email or not
 if email exists we will get user, if user exists we assign global user
 otherwise we clear the session
"""

@app.before_request
def before_request():
    email=session.get("email")
    if email is None:
        g.user = None
    else:
        validation = UserValidation()
        user=UserService(validation).get_user_by_email(email)
        if user:
            g.user=user
            #we want to allow logged in users to have the cart object
            if 'cart' not in session:
                session['cart'] = {"user": user.email, "items": [],}
            else:
                g.cart = session['cart']
        else:
            session.clear()
#Landing Page Route
@app.route('/')
def landing_page():
    return render_template('LandingPage.html')

@app.route('/products')
def products_spread():
    products=ProductService().get_products()
    return render_template('ProductSpread.html',products=products)

@app.route('/products/<name>')
def get_product(name):
    product=ProductService().get_product(name)
    return render_template('ProductDetail.html', product=product)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        # Process the form data (e.g., save to a database)
        validation=UserValidation()
        user,message=UserService(validation).create_user(firstname, lastname, email, password)
        if user:
            return redirect(url_for('signin_page'))
        else:
            flash(message,'danger')
            return redirect(url_for('signup_page'))
    return render_template('SignUp.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin_page():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        validation = UserValidation()
        user=UserService(validation).signin(email, password)
        if user:
            session.clear()
            session['email'] = email
            if user.is_admin:
                return redirect(url_for('dashboard'))
            return redirect(url_for('products_spread'))
        else:
            flash('Invalid credentials','danger')
            return redirect(url_for('signin_page'))
    return render_template('Signin.html')

@app.route('/signout', methods=['GET'])
def signout_page():
    session.clear()
    flash('You have been signed out',"warning")
    return redirect(url_for('signin_page'))

@app.route('/success')
def success():
    return "Sign-up successful!"

@app.route('/create-product', methods=['GET', 'POST'])
def create_product():
    if g.user and g.user.is_admin:
        created_by = g.user
        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            imageurl = request.form['imageurl']
            stock = int(request.form['stock'])
            price = float(request.form['price'])
            producttype_name = request.form['producttype_name']
            producttype_material = request.form['producttype_material']
            producttype_size = request.form['producttype_size']
            service=ProductService()
            service.create_product(name, description, imageurl, stock, price, created_by,
                                   producttype_name, producttype_material, producttype_size)
            return "Product created successfully!"  # Example response
        return render_template('ProductCreate.html')  # Load form template for GET requests
    flash("You are unauthorised","danger")
    return redirect(url_for('signin_page'))

@app.route('/Cart', methods=['POST'])
def add_to_cart():
    if g.user:
        productname=request.form['productname']
        service=ProductService()
        cart=service.add_product_to_cart(g.user, productname, session['cart'])
        session['cart'] = cart  # Save updated cart back to session
        session.modified = True  # Mark the session as modified
        flash("Product added to cart succesfully", "success")
        return redirect(url_for('get_product',name=productname))
    return redirect(url_for('signin_page'))

@app.route('/MyCart', methods=['POST', 'GET'])
def my_cart():
    if not g.user:
        return redirect(url_for('signin_page'))
    else:
        if request.method == "POST":
            pass
        totalprice = 0
        for item in g.cart['items']:
            totalprice=totalprice+(item['price'])*(item['quantity'])
        return render_template('mycart.html' ,totalprice=totalprice, productitems=g.cart['items'])

@app.route('/update_cart', methods=['POST'])
def update_cart():
    item_name = request.form.get('item_name')
    action = request.form.get('action')
    for item in g.cart['items']:
        if item['name'] == item_name:
            if action == 'increase' and item['quantity'] < item['stock']:
                item['quantity'] += 1
            elif action == 'decrease' and item['quantity'] > 1:
                item['quantity'] -= 1
            break
    # Update the total number of items
    g.cart['numberofitems'] = sum(item['quantity'] for item in g.cart['items'])
    session['cart']=g.cart #Assigning modified cart object into session cart because we just modified it so it stays persistent
    return redirect(url_for('my_cart'))

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    item_name = request.form.get('item_name')
    g.cart['items'] = [item for item in g.cart['items'] if item['name'] != item_name]
    # Update the total number of items
    g.cart['numberofitems'] = sum(item['quantity'] for item in g.cart['items'])
    session['cart']=g.cart
    return redirect(url_for('my_cart'))

@app.route('/checkout')
def checkout():
    pass

@app.route('/dashboard')
def dashboard():
    if g.user and g.user.is_admin:
        return render_template('dashboard.html')
    flash("You are unauthorised","danger")
    return redirect(url_for('signin_page'))

if __name__ == '__main__':
    app.run(debug=True)
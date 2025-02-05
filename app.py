from db import initdb
from flask import (Flask, render_template, request, redirect, url_for,
flash, session,g)
import datetime


from Service.ProductService import ProductService
from Service.UserService import UserService
from Validation.UserValidation import UserValidation
from db import select_products, select_product_by_name, update_product, delete_product_by_name, select_products_types,filter_products

app = Flask(__name__)
app.cli.add_command(initdb)
app.secret_key = "mysecretkey"



"""before every request this function will check the session object has email or not
 if email exists we will get user, if user exists we assign global user
 otherwise we clear the session
"""

@app.before_request
def before_request():
    '''
    This function will be called before every request for example here we are loading
    the logged in user from session
    '''
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
                g.cart = session['cart']#assign cart to g.cart to access in the template easily
        else:
            session.clear()

@app.route('/',methods=['GET','POST'])
def products_spread():
    '''
    This endpoint is the main homepage for users it retrieves products to display them from productserivce
    '''
    product_types=select_products_types()
    producttypename=request.args.get('producttypename')
    producttypematerial = request.args.get('producttypematerial')
    producttypesize = request.args.get('producttypesize')
    if producttypename:
        products=filter_products(name=producttypename, material=producttypematerial, size=producttypesize)
    else:
        products=select_products()
    return render_template('ProductSpread.html',products=products,product_types=product_types,
                           selected_producttypename=producttypename, selected_producttypematerial=producttypematerial,
                           selected_producttypesize=producttypesize)

@app.route('/products/<name>')
def get_product(name):
    '''
    to display a single product it retreives a product by name from product service
    if product does not exist and display an error message to user and redirect to product spread
    Exception used so that it can handle all errors and display message to users
    '''
    try:
        product=select_product_by_name(name)
        return render_template('ProductDetail.html', product=product)
    except Exception as e:
        print(e)
        flash('The Product does not exist','danger')
        return redirect(url_for('products_spread'))

@app.route('/products/<name>/edit', methods=['GET', 'POST'])
def product_edit(name):
    #only admin users can access this page
    if g.user and g.user.is_admin:
        try:
            product=select_product_by_name(name)
            if request.method == 'POST':
                name=request.form['name']
                description=request.form['description']
                stock=request.form['stock']
                price=request.form['price']
                imageurl=request.form['imageurl']
                producttypename=request.form['producttypename']
                producttypematerial=request.form['producttypematerial']
                producttypesize=request.form['producttypesize']
                product_typeid=product['product_type']['id']
                isupdated=update_product(product['id'], name,description,stock,price,imageurl, product_typeid, producttypename, producttypematerial, producttypesize)
                if isupdated:
                    flash('Product Updated','success')
                    return redirect(url_for('get_product', name=name))
                flash('Product Not Updated','warning')
            return render_template('ProductEdit.html', product=product)
        except Exception as e:
            print(e)
            flash('Error while updating','danger')
            return redirect(url_for('products_spread'))
    flash('Unauthorised users cannot edit product','danger')
    return redirect(url_for('products_spread'))

@app.route('/products/<name>/delete', methods=['POST'])
def product_delete(name):
    if g.user and g.user.is_admin:
        try:
            is_deleted=delete_product_by_name(name)
            if is_deleted:
                flash('Deleted Sucessfully','success')
                return redirect(url_for('products_spread'))
            flash ('Error while deleting','danger')
            return redirect(url_for('products_spread'))
        except Exception as e:
            flash('Product does not exist','danger')
            return redirect(url_for('products_spread'))


@app.route('/about')#Takes the user to the about page that does not service any real purpose
def about_page():
    return render_template('about.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    '''
    this route function handles get and post requests.
    request.form contains the data sent by the user after filling in the form on the frontend
    if user service creates a user succesfully they are redirected to signin page otherwise display an error message and
    redirect to sign up again
    '''
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        #Validates the users inputs
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
    '''
    User sends email and password its passed to user service and if the credentials match with stored any user it returns
    the user object. otherwise None is returned display error message and redirect to signin again
    If user is admin they are redirected to the dashboard otherwise redirect to product spread
    '''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        validation = UserValidation()
        user=UserService(validation).get_user(email, password)

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
def signout_page():#Clears the session of the user and displays a pop telling them they have been signed out
    session.clear()
    flash('You have been signed out',"warning")
    return redirect(url_for('signin_page'))

@app.route('/create-product', methods=['GET', 'POST'])
def create_product():
    if g.user and g.user.is_admin:
        if request.method == 'POST':
            service=ProductService()
            name = request.form['name']
            description = request.form['description']
            stock = request.form['stock']
            price = request.form['price']
            imageurl = request.form['imageurl']
            producttypename = request.form['producttypename']
            producttypematerial = request.form['producttypematerial']
            producttypesize = request.form['producttypesize']
            createdby = g.user.id
            createdat = datetime.datetime.now(datetime.timezone.utc)
            service.create_product(name, description, stock, price, imageurl,createdby, createdat, producttypename, producttypematerial, producttypesize)
            flash('Product added sucessfully', "success")
            return redirect(url_for('products_spread'))
        return render_template('createproduct.html')
    return redirect(url_for('signin_page'))

@app.route('/Cart', methods=['POST'])
def add_to_cart():
    '''
    The logged(g.user) in user sends product name to add to their cart,
    '''
    if g.user:
        productname=request.form['productname']
        service=ProductService()
        cart=service.add_product_to_cart(g.user, productname, session['cart'])
        session['cart'] = cart  # Save the updated version of the cart
        session.modified = True  # Marks the session as have been modified
        flash("Product added to cart succesfully", "success")
        return redirect(url_for('get_product',name=productname))
    return redirect(url_for('signin_page'))

@app.route('/MyCart', methods=['POST', 'GET'])
def my_cart():
    '''
    If the user is not logged in they are returned to signin page,
    '''
    if not g.user:
        return redirect(url_for('signin_page'))
    else:#This is for logged in users
        totalprice = 0
        #calculates the total price of the cart items
        for item in g.cart['items']:
            totalprice=totalprice+(item['price'])*(item['quantity'])
        return render_template('mycart.html' ,totalprice=totalprice, productitems=g.cart['items'])

@app.route('/update_cart', methods=['POST'])
def update_cart():
    '''
    It checks the cart items and loops over them, if given product name matches then action is applied eg increaing or
    decrease the quantity
    '''
    item_name = request.form.get('item_name')
    action = request.form.get('action')
    for item in g.cart['items']:
        if item['name'] == item_name:
            if action == 'increase':
                if item['stock']==1:
                    flash("Not enough stock to increase quantity" ,"warning")
                elif item['quantity'] < item['stock']:
                    item['quantity'] += 1
            elif action == 'decrease':
                if item['stock']==1:
                    flash("Not enough stock to decrease quantity","warning")
                elif item['quantity'] > 1:
                    item['quantity'] -= 1
            break
    # Update the total number of items
    g.cart['numberofitems'] = sum(item['quantity'] for item in g.cart['items'])
    session['cart']=g.cart #Assigning modified cart object into session cart because we just modified it so it stays persistent
    return redirect(url_for('my_cart'))

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    '''
    loop over cart items and populate them in new list except given item name(product_name)
    '''
    item_name = request.form.get('item_name')
    g.cart['items'] = [item for item in g.cart['items'] if item['name'] != item_name]
    # Update the total number of items
    g.cart['numberofitems'] = sum(item['quantity'] for item in g.cart['items'])
    session['cart']=g.cart
    return redirect(url_for('my_cart'))

@app.route('/checkout')
def checkout():
    session['cart'] = {"user": g.user.email, "items": [],}
    #clearing cart items when confirming order so they do not stay for next order
    flash("Your order has been Confirmed", "success")
    return redirect(url_for('products_spread'))

@app.route('/dashboard')#This only allows the admin user to acess the page and if they are not authorised they will receive
#a message and be redirected
def dashboard():
    if g.user and g.user.is_admin:
        return render_template('dashboard.html')
    flash("You are unauthorised","danger")
    return redirect(url_for('signin_page'))

if __name__ == '__main__':
    app.run(debug=True)
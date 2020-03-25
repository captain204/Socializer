from flask import (
    Blueprint,
    redirect,
    request,
    flash,
    url_for,
    render_template,session)
from flask_login import (
    login_required,
    login_user,
    current_user,
    logout_user)

from werkzeug.security import (generate_password_hash, 
                               check_password_hash)
from application.extensions import db,login_manager

from application.blueprints.users.models import(
     User) 

from application.blueprints.users.forms import (
     SignupForm,
     LoginForm)


from application.blueprints.posts.models import(
     Post) 


user = Blueprint('user', __name__, template_folder='templates')


@user.route('/signup', methods=['GET','POST'])
def signup():
    """User sign-up page."""
    form = SignupForm(request.form)
    # POST: Sign user in
    if request.method == 'POST':
        if form.validate():
            # Get Form Fields
            username = request.form.get('username')
            email = request.form.get('email')
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            password = request.form.get('password')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(username=username,email=email,firstname=firstname,lastname=lastname,password=generate_password_hash(password, method='sha256'))   
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('mypost.allpost'))
            flash('A user already exists with that email address.')
            return redirect(url_for('user.login'))
    # GET: Serve Sign-up page
    return render_template('signup.html', form=form)



@user.route('/login', methods=['GET','POST'])
def login():
    """User login page."""
    # Bypass Login screen if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('user.feeds'))
    form = LoginForm(request.form)
    # POST: Create user and redirect them to the app
    if request.method == 'POST':
        if form.validate():
            #Get Form Fields
            email = request.form.get('email')
            password = request.form.get('password')
            # Validate Login Attempt
            user = User.query.filter_by(email=email).first()
            if user:
                if user.check_password(password=password):
                    login_user(user)
                    next = request.args.get('next')
                    session['user_id'] = user.id
                    return redirect(next or url_for('mypost.allpost'))
        flash('Invalid username/password combination')
        return redirect(url_for('user.login'))
    #GET: Serve Log-in page
    return render_template('login.html', form=form) 



@user.route('/feeds', methods=['GET','POST'])
@login_required
def feeds():
    user_id = current_user.id
    post =  Post.query.filter_by(user_id=user_id).all()
    return render_template('feeds.html', mypost = post)


@user.route('/myprofile', methods=['GET', 'POST'])
@login_required
def myprofile():
    id = current_user.id
    user = User.query.filter_by(id = id).first()
    return render_template('profile.html',user = user)

@user.route('/people', methods=['GET','POST'])
@login_required
def people():
    #id = current_user.id
    #people = User.query.filter_by(id = id).all()
    people = User.query.all()
    return render_template('people.html',group=people)


@user.route("/logout")
@login_required
def logout_page():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('user.login'))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """ Redirect unauthorized users to Login page ."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('user.login'))


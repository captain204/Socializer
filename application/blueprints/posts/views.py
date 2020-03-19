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

from application.extensions import db,login_manager

from application.blueprints.users.models import(
     User) 

from application.blueprints.posts.models import(
     Post)


from application.blueprints.posts.forms import (
     PostForm)

 
mypost = Blueprint('mypost', __name__, template_folder='templates')



@mypost.route('/post', methods=['GET','POST'])
#@login_required
def post():
    """Add new Post"""
    form = PostForm(request.form)
    if request.method == 'POST':
        if form.validate():
            body = request.form.get('body')
            user_id = current_user.id
            new_post = Post(body=body,user_id = user_id)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('mypost.post'))
        else:
            flash("Something went wrong while posting your listing")
            return redirect(url_for('mypost.post'))

    return render_template('add_post.html', form=form)


#Update Post
@mypost.route('/post/update/<id>',methods=['GET','POST'])
#@login_required
def update(id):
    post =  Post.query.filter_by(id=id).first()
    form = PostForm(request.form)
    form.body.data = post.body
    if request.method == 'POST':
        if form.validate():
            body = request.form.get('body')
            #user_id = current_user.id
            post.body = body
            post.id = id
            db.session.query(Post).filter_by(id=id).update({"body":body})
            db.session.commit()
            #db.session.add(post)
            #db.session.commit()
            return redirect(url_for('mypost.post'))
            flash("Post updated successfully")
        else:
            flash("Something went wrong while sending your post")
            return redirect(url_for('mypost.post'))
    return render_template('add_post.html', form=form)
    




#Delete Post
@mypost.route('/delete/<id>', methods=['POST'])
@login_required
def delete(id):
    Post.query.filter_by(id=id).delete()
    delete.session.commit()
    return redirect(url_for('user.feeds'))

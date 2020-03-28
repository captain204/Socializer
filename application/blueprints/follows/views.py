"""from flask import (
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


 
follow = Blueprint('follow', __name__, template_folder='templates')



@follow.route('/follows/<username>', methods=['GET','POST'])
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('user.people'))
    if current_user.is_following(user):
        flash('You are already following {username}'.format(username=user.username))
        return redirect(url_for('user.people'))
    current_user.follow(user)
    db.session.commit()
    flash('You are now following %s.' % user.username)
    return redirect(url_for('user.people', username=username))


@follow.route('/unfollow/<username>', methods=['GET','POST'])
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('user.people'))
    if not current_user.is_following(user):
        flash('You are not following {username}'.format(username = user.username))
        return redirect(url_for('user.people'))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are no longer following {username}'.format(username = user.username))
    return redirect(url_for('user.people'))
"""
"""
@user.route('/follows/<username>', methods=['GET','POST'])
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


@user.route('/unfollow/<username>', methods=['GET','POST'])
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

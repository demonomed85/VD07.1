from flask import render_template, redirect, url_for, flash
from . import db
from my_flask_app.models import User
from forms import CreateUserForm, EditProfileForm
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = CreateUserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Пользователь успешно создан!', 'success')
        return redirect(url_for('main.create_user'))
    return render_template('create_user.html', form=form)

@main.route('/edit_profile/<int:user_id>', methods=['GET', 'POST'])
def edit_profile(user_id):
    user = User.query.get_or_404(user_id)
    form = EditProfileForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.commit()
        flash('Профиль успешно обновлен!', 'success')
        return redirect(url_for('main.edit_profile', user_id=user.id))
    return render_template('edit_profile.html', form=form, user=user)
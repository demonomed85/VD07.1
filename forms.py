from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class CreateUserForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Электронная почта', validators=[DataRequired()])  # Удален валидатор Email
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Создать пользователя')

class EditProfileForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Электронная почта', validators=[DataRequired()])  # Удален валидатор Email
    password = PasswordField('Пароль', validators=[DataRequired(), EqualTo('confirm_password', message='Пароли должны совпадать.')])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired()])
    submit = SubmitField('Сохранить изменения')
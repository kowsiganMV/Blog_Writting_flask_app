from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,FileField
from wtforms.validators import DataRequired,Length,Email,EqualTo
from flask_wtf.file import FileAllowed

class Registerform(FlaskForm):
  username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
  email=StringField('Email',validators=[DataRequired(),Email()])
  password=PasswordField('Password',validators=[DataRequired()])
  confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
  profile=FileField(render_kw={"class": "custom-file-input"}, validators=[FileAllowed(['jpg', 'png'], 
  'Images only!')])
  submit=SubmitField('Sin Up')

class Loginform(FlaskForm):
  email=StringField('Email',validators=[DataRequired(),Email()])
  password=PasswordField('Password',validators=[DataRequired()])
  remember=BooleanField('Remember Me')
  submit=SubmitField('Login')

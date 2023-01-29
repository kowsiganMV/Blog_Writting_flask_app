from datetime import *
from flask import Flask, render_template,flash,redirect, url_for,request
from forms import Registerform,Loginform
from connectmongo import adding,getdatas,get_posts,addpost,myblogs
import datetime


app=Flask(__name__)

app.config['SECRET_KEY']='1068d00e3aaf112b3c097f72b6756887'

user=""
userdatas=[]
@app.route("/",methods=['POST','GET'])
def home():
  global user,userdatas
  posts=get_posts()
  if user!='':
    if request.form.get('action')=='logout':
      user=""
      userdatas=[]
      return redirect(url_for('home'))
    return render_template('home.html',posts=posts,title='Home',user=user,userdatas=userdatas)
  else:
    return render_template('home.html',posts=posts,title='Home')

@app.route("/about",methods=['POST','GET'])
def about():
  global user,userdatas
  if user!='':
    if request.form.get('action')=='logout':
      user=""
      userdatas=[]
      return redirect(url_for('home'))
    return render_template('about.html',title='About',user=user,userdatas=userdatas)
  else:
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
  global user,userdatas
  form=Registerform()
  if form.validate_on_submit():
    user+=form.username.data
    n=form.username.data
    e=form.email.data
    p=form.password.data
    id=adding(n,e,p)
    userdatas.extend([id,n,e,p])
    flash(f'Account Created for {form.username.data}!','success')
    return redirect(url_for('home'))
  return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
  global user,userdatas
  form=Loginform()
  if form.validate_on_submit():
    datas=getdatas()
    for data in datas:
      if form.email.data==data[2] and form.password.data==data[3]:
        flash(f'You have been Logged in!','success')
        user+=str(data[1])
        userdatas.extend(data)
        return redirect(url_for('home'))
    else :
      flash('Login Unsuccessful. Please check username and password','danger')
  return render_template('login.html',title='Login',form=form)

@app.route("/newpost",methods=['POST','GET'])
def newpost():
  global user,userdatas
  if user!='':
    if request.form.get('action')=='posts':
      tittle=request.form['tittle']
      content=request.form['content']
      aurthor=request.form['aurthor']
      date=""
      tempdate=str(datetime.datetime.now())
      for i in range(len(tempdate)):
        if tempdate[i]==" ":
          date=tempdate[:i]
          break
      addpost(userdatas[0],tittle,content,aurthor,date)
      flash('Your post is posted','success')
      return redirect(url_for('home'))
    if request.form.get('action')=='logout':
      user=""
      userdatas=[]
      return redirect(url_for('home'))
    return render_template('newpost.html',title='Write Blog',user=user,userdatas=userdatas)
  return redirect(url_for('register'))
  
@app.route("/profile",methods=['POST','GET'])
def profile():
  global user,userdatas
  if user!='':
    posts=myblogs(userdatas[0])
    num=len(posts)
    if request.form.get('action')=='logout':
      user=""
      userdatas=[]
      return redirect(url_for('home'))
    if request.form.get('action')=='myblogs':
      use=user+"'s Blogs"
      return render_template('home.html',posts=posts,title=use,user=user,userdatas=userdatas)
    else:
      return render_template('profile.html',title='Profile',blogs=num,user=user,userdatas=userdatas)
  else:
    return redirect(url_for('home'))

if __name__ =='__main__':  
    app.run(debug = True) 
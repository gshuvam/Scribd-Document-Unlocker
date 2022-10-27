from package import app
from flask import redirect, render_template, request, flash
from flask_login import current_user, login_user, login_required
from package.models import User

@app.route('/', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect('/unlock')
    elif request.method == "POST":
        email = request.form['mail']
        password = request.form['pass']
        user = User.query.filter_by(email = email).first()
        
        if user and user.password == password:
            if "remember" in list(request.form.keys()):
                login_user(user,request.form["remember"])
            else:
                login_user(user)
            next_page = request.args.get('next')
            flash(f"Welcome Back, {user.name.split(' ')[0]}", "success")
            return redirect(next_page) if next_page else redirect("/unlock")
        else:
            flash(f"Invalid Email or Password", "danger")
    return render_template("login.html")

@app.route('/unlock', methods=["GET","POST"])
@login_required
def home():
    return render_template("index.html")

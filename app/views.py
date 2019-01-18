from app import app

from flask import render_template, flash, redirect
from flask_login import login_required, logout_user


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out successfully.", category="success")
    return redirect("index")

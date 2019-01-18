from app import app, db
from app.models import Category, Item

from flask import render_template, flash, redirect
from flask_login import login_required, logout_user


@app.route("/")
@app.route("/index")
def index():
    categories = Category.query.all()
    # Limit the items query limit to contain no more
    # latest items then there are categories
    items_query_limit = 10 if len(categories) < 10 else len(categories)
    items = Item.query.order_by(Item.date.desc()).limit(10).all()
    return render_template(
        "index.html",
        title="Catalog App",
        categories=categories,
        items=items
    )


@app.route("/catalog/<string:category>/items")
def catalog_items(category):
    categories = Category.query.all()
    category_items = Item.query. \
        filter_by(
            category=next(cat for cat in categories if cat.name == category)
        ).all()
    return render_template(
        "catalog_items.html",
        title="Catalog App",
        categories=categories,
        category=category,
        category_items=category_items,
        category_items_count=len(category_items)
    )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out successfully.", category="success")
    return redirect("index")

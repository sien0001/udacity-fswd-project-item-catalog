from app import app, db
from app.models import Category, Item
from app.forms import AddItemForm, AddCategoryForm

from flask import render_template, flash, redirect, url_for
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


@app.route("/catalog/<string:category>/<string:item>")
def item(category, item):
    cat = Category.query.filter(Category.name == category).one()
    i = Item.query.filter_by(category=cat).filter(Item.title == item).one()
    return render_template(
        "item.html",
        title="Catalog App",
        item=i
    )


@app.route("/catalog/add_item", methods=["GET", "POST"])
@login_required
def add_item():
    form = AddItemForm()
    categories = Category.query.all()
    form.categories.choices = [(c.name, c.name.capitalize()) for c in categories]
    if form.validate_on_submit():
        item = Item(
            title=form.title.data,
            description=form.description.data,
            category=Category.query.filter(Category.name == form.categories.data).one()
        )
        db.session.add(item)
        db.session.commit()
        flash("Item was added successfully.", category="primary")
        return redirect(url_for("index"))
    return render_template(
        "add_item.html",
        title="Catalog App",
        form=form
    )


@app.route("/catalog/add_category", methods=["GET", "POST"])
@login_required
def add_category():
    form = AddCategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        flash("Category was added successfully.", category="primary")
        return redirect(url_for("index"))
    return render_template(
        "add_category.html",
        title="Catalog App",
        form=form
    )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out successfully.", category="success")
    return redirect("index")

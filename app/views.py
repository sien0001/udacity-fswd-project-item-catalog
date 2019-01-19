from app import app, db
from app.models import Category, Item
from app.forms import ItemForm, AddCategoryForm

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, logout_user


@app.route("/api")
def api():
    return render_template("api.html", title="Catalog App")


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
    form = ItemForm()
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
        flash("Item was added successfully.", category="success")
        return redirect(url_for("index"))
    return render_template(
        "item_form.html",
        title="Catalog App",
        form=form
    )


@app.route("/catalog/<string:item>/edit", methods=["GET", "POST"])
@login_required
def edit_item(item):
    item = Item.query.filter(Item.title == item).one()
    form = ItemForm()
    categories = Category.query.all()
    form.categories.choices = [(c.name, c.name.capitalize()) for c in categories]
    if form.validate_on_submit():
        item.title = form.title.data
        item.description = form.description.data
        item.category = Category.query.filter(Category.name == form.categories.data).one()
        db.session.commit()
        flash("Item has been updated successfully.", category="success")
        return redirect(url_for("index"))
    elif request.method == "GET":
        form.title.data = item.title
        form.description.data = item.description
        form.categories.data = sorted(
            form.categories.choices, key=lambda c: item.category.name > c[0]
        )
    return render_template(
        "item_form.html",
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
        flash("Category was added successfully.", category="success")
        return redirect(url_for("index"))
    return render_template(
        "add_category.html",
        title="Catalog App",
        form=form
    )


@app.route("/catalog/<string:item>/delete", methods=["GET", "POST"])
@login_required
def delete_item(item):
    item = Item.query.filter(Item.title == item).one()
    db.session.delete(item)
    db.session.commit()
    flash("Item has been deleted successfully.", category="success")
    return redirect(url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out successfully.", category="success")
    return redirect("index")

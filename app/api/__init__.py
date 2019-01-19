from app.models import Category, Item

from flask_restful import Resource


class Catalog(Resource):
    def get(self):
        catalog = list()
        for c in Category.query.all():
            items = list()
            for i in Item.query.filter(Item.category_id==c.id).all():
                items.append(
                    {
                        'id': i.id,
                        'title': i.title,
                        'description': i.description
                    }
                )
            catalog.append(
                {
                    'id': c.id,
                    'name': c.name,
                    'items': items
                }
            )   
        return {"Categories": catalog}

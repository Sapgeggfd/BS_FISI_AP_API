from fastapi import FastAPI
import custom_sql

app = FastAPI()


class InvItem:
    def __init__(self, id, name, price, in_stock: 0):
        self.id = id
        self.name = name
        self.price = price
        self.stock = in_stock

    def in_stock(self) -> bool:
        if self.stock > 0:
            return True
        return False


items = [
    InvItem(0, "Spezi", 2.39, 200),
    InvItem(1, "Club Marte", 1.33, 404),
    InvItem(2, "Coffee", 1.00, 500),
    InvItem(3, "shit?", 99.99, 0),
]


db = custom_sql.db_requests()


@app.get("/api/products/list")
async def list_items():
    ret = {"items": {}}
    for item in db.list_items():
        ret["items"][item[0]] = {
            "item_name": item[1],
            "item_price": item[2],
            "stock_amount": item[3],
        }
    return ret


@app.get("/api/products/item")
async def show_item(item_id: int):
    item = db.list_one_item(item_id)[0]
    return {
        "item": {
            "item_id": item[0],
            "item_name": item[1],
            "item_price": item[2],
            "stock_amount": item[3],
        }
    }


@app.get("/api/products/reorder")
async def show_item_stock():
    ret = {"items": {}}
    for item in db.list_items():
        ret["items"][item[0]] = {
            "item_name": item[1],
            "item_price": item[2],
            "stock_amount": item[3],
        }
    return ret

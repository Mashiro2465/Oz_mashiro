from fastapi import FastAPI

app = FastAPI()

@app.get("/orders/{order_id}")
def get_order(order_id: int = 100, show_items: bool = False):
    items = ["item1", "item2", "item3"]

    if show_items:
        return {"order_id": order_id, "items" : items}
    return {"order_id": order_id}

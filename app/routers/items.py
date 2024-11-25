from fastapi import APIRouter, HTTPException
from app.models.item_model import Item

router = APIRouter()

items_db = {}

@router.get("/items/{item_id}", summary = "obtener un item por id")
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return items_db[item_id]

@router.post("/items", summary = "crear un nuevo item")
def create_item(item_id: int, item: Item):
    if item_id in items_db:
        raise HTTPException(status_code=400, detail="ID ya existe")
    items_db[item_id] = item.dict()
    return {"message": "Item creado", "item": item}

@router.put("/items/{item_id}", summary = "actualizar item existente")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    items_db[item_id] = item.dict()
    return {"message": "Item actualizado", "item": item}

@router.delete("/items/{item_id}", summary="eliminar item")
def delete_item(item_id:int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    del items_db[item_id]
    return {"message": "Item eliminado"}
from pydantic import BaseModel


class ProductOut(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    costo: float
    cantidad: int

class ProductAddCantIn(BaseModel):
    product_id: str
    cantidad: int

class ProductAddCantOut(BaseModel):
    nombre: str
    cantidad: int


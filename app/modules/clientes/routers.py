from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.modules.clientes.schemas import Cliente
from app.modules.clientes.services import get_cliente_by_id, get_clientes, create_cliente

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/{cliente_id}", response_model=Cliente)
def obtener_cliente(cliente_id: int):
    cliente = get_cliente_by_id(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.get("/", response_model=List[Cliente])
def listar_clientes(
    nombre: str = None,
    email: str = None
):
    return get_clientes(nombre, email)


@router.post("/", response_model=Cliente)
def crear_cliente(cliente: Cliente):
    try:
        return create_cliente(cliente)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    


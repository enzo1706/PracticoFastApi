from typing import List, Optional
from app.modules.clientes.schemas import Cliente

clientes_db: List[Cliente] = []

def get_clientes(nombre: Optional[str] = None, email: Optional[str] = None) -> List[Cliente]:
    resultados = clientes_db

    if nombre:
        resultados = [c for c in resultados if c.nombre == nombre]

    if email:
        resultados = [c for c in resultados if c.email == email]

    return resultados


def create_cliente(cliente: Cliente):
    if any(c.email == cliente.email for c in clientes_db):
        raise ValueError("El email ya está registrado")

    if len(cliente.nombre) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres")

    clientes_db.append(cliente)
    return cliente


def get_cliente_by_id(cliente_id: int):
    for c in clientes_db:
        if c.id == cliente_id:
            return c
    return None
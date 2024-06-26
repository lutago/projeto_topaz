from pydantic import BaseModel, ConfigDict
from typing import List
from app.classe.tarefas import ItemResponse, ItemRequest

class UsuarioRequest(BaseModel):
    nome: str
    itens: List[ItemRequest]
    
    model_config = ConfigDict(from_attributes=True)
        
class UsuarioResponse(BaseModel):
    id: int
    nome: str
    itens: List[ItemResponse]
    
    model_config = ConfigDict(from_attributes=True)
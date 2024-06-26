from typing import List
from pydantic import BaseModel, ConfigDict

class ItemRequest(BaseModel):
    descricao: str
    
    model_config = ConfigDict(from_attributes=True)


class ItemRequestCadastro(BaseModel):
    itens: List[ItemRequest]
    
    model_config = ConfigDict(from_attributes=True)

        
class ItemResponse(BaseModel):
    id: int
    descricao: str
    data_criacao: str
    
    model_config = ConfigDict(from_attributes=True)
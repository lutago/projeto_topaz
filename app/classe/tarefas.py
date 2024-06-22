from datetime import datetime
from typing import List
from pydantic import BaseModel

class Tarefa(BaseModel):
    descricao: str
    dt_criacao: datetime

class TarefasUsuario(BaseModel):
    usuario: str
    tarefa: List[Tarefa] = []

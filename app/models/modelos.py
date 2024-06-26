from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.banco_dados.database import Base

class UsuarioBD(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    itens = relationship("ItemBD", back_populates="relacao_usuario_item")
    
class ItemBD(Base):
    __tablename__ = 'itens'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String, index=True)
    data_criacao = Column(DateTime, default=func.now())
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    relacao_usuario_item = relationship("UsuarioBD", back_populates="itens")
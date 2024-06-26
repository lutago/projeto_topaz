from fastapi import APIRouter, Depends, HTTPException
from app.models.modelos import UsuarioBD, ItemBD
from app.classe.usuario import UsuarioResponse
from app.classe.tarefas import ItemResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import List
from app.banco_dados.dependencias import get_bd


rota = APIRouter(prefix="/busca")

@rota.get("/usuarios", response_model=List[UsuarioResponse])
async def busca_usuario(db: AsyncSession = Depends(get_bd)):
    async with db.begin():
        query = select(UsuarioBD).options(selectinload(UsuarioBD.itens))
        result = await db.execute(query)
        usuarios = result.scalars().all()
        
        if not usuarios:
            raise HTTPException(status_code=404, detail="Nenhum usuário encontrado")

        usuarios_response = [
            UsuarioResponse(
                id=usuario.id,
                nome=usuario.nome,
                itens=[
                    ItemResponse(
                        id=item.id,
                        descricao=item.descricao,
                        data_criacao=item.data_criacao.isoformat()
                    ) for item in usuario.itens
                ]
            ) for usuario in usuarios
        ]
        return usuarios_response

@rota.get("/usuarios/{user_id}", response_model=UsuarioResponse)
async def busca_usuario_por_id(user_id: int, db: AsyncSession = Depends(get_bd)):
    async with db.begin():
        query = select(UsuarioBD).where(UsuarioBD.id == user_id).options(selectinload(UsuarioBD.itens))
        result = await db.execute(query)
        usuario = result.scalar_one_or_none()
        
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        usuario_response = UsuarioResponse(
            id=usuario.id,
            nome=usuario.nome,
            itens=[
                ItemResponse(
                    id=item.id,
                    descricao=item.descricao,
                    data_criacao=item.data_criacao.isoformat()
                ) for item in usuario.itens
            ]
        )
        return usuario_response
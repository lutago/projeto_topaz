from fastapi import APIRouter, Depends, HTTPException
from app.models.modelos import UsuarioBD, ItemBD
from app.banco_dados.dependencias import get_bd
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete


rota = APIRouter(prefix="/exluir")

@rota.delete("/usuario/{usuario_id}", status_code=204)
async def deletar_usuario(usuario_id: int, db: AsyncSession = Depends(get_bd)):
    async with db.begin():
        try:
            query = select(UsuarioBD).where(UsuarioBD.id == usuario_id)
            result = await db.execute(query)
            usuario = result.scalar_one_or_none()
            
            if usuario is None:
                raise HTTPException(status_code=404, detail="Usuário não encontrado")
            
            await db.execute(delete(ItemBD).where(ItemBD.usuario_id == usuario_id))
            
            await db.execute(delete(UsuarioBD).where(UsuarioBD.id == usuario_id))
            
            await db.commit()
        except Exception as e:
            raise HTTPException(status_code=500, detail="Erro interno do servidor")

@rota.delete("/itens/{item_id}/usuario/{usuario_id}", status_code=204)
async def deletar_item(usuario_id: int, item_id: int, db: AsyncSession = Depends(get_bd)):
    async with db.begin():
        try:
            query = select(ItemBD).where(ItemBD.id == item_id, ItemBD.usuario_id == usuario_id)
            result = await db.execute(query)
            item = result.scalar_one_or_none()
            
            if item is None:
                raise HTTPException(status_code=404, detail="Item não encontrado ou não pertence ao usuário")
            
            await db.execute(delete(ItemBD).where(ItemBD.id == item_id))
            await db.commit()
        except Exception as e:
            raise HTTPException(status_code=500, detail="Erro interno do servidor")
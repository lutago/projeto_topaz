from fastapi import APIRouter, Depends, HTTPException
from app.classe.usuario import UsuarioRequest, UsuarioResponse
from app.classe.tarefas import ItemResponse, ItemRequestCadastro
from app.models.modelos import UsuarioBD, ItemBD
from sqlalchemy.ext.asyncio import AsyncSession
from app.banco_dados.dependencias import get_bd
from sqlalchemy.future import select


rota = APIRouter(prefix="/cadastro")

@rota.post("/usuario", status_code=201)
async def cadastro_usuario(usuario: UsuarioRequest, db: AsyncSession  = Depends(get_bd)):
    if not usuario.nome:
        raise HTTPException(status_code=400, detail="Nome do usuário é obrigatório.")
    
    async with db.begin():
        try:
            usuario_request = UsuarioBD(nome=usuario.nome)
            db.add(usuario_request)
            await db.flush()
            
            if len(usuario.itens) > 0:
                item_bd = [ItemBD(descricao=item.descricao, usuario_id=usuario_request.id) for item in usuario.itens]
                db.add_all(item_bd)
                await db.flush()
                
            await db.refresh(usuario_request)
            await db.commit()
            
            
            usuario_response = UsuarioResponse(
                id=usuario_request.id,
                nome=usuario_request.nome,
                itens=[
                    ItemResponse(
                        id=item.id, 
                        descricao=item.descricao, 
                        data_criacao=item.data_criacao.isoformat()
                        ) 
                    for item in item_bd
                ] if len(usuario.itens) > 0 else []
            )
            
            return usuario_response
        except Exception as e:
            raise HTTPException(status_code=500, detail="Erro interno do servidor")
        
    
@rota.post("/usuario/{usuario_id}/itens", status_code=201)
async def cadastro_itens(usuario_id: int, itens_request: ItemRequestCadastro, db: AsyncSession = Depends(get_bd)):
    async with db.begin():
        try:
            query = select(UsuarioBD).where(UsuarioBD.id == usuario_id)
            result = await db.execute(query)
            usuario = result.scalar_one_or_none()
            
            if usuario is None:
                raise HTTPException(status_code=404, detail="Usuário não encontrado")
            
            item_bd = [ItemBD(descricao=item.descricao, usuario_id=usuario.id) for item in itens_request.itens]
            db.add_all(item_bd)
            await db.flush()
            await db.commit()
            
            itens_response = [
                ItemResponse(
                    id=item.id,
                    descricao=item.descricao,
                    data_criacao=item.data_criacao.isoformat()
                ) for item in item_bd
            ]
            
            return {"usuario_id": usuario.id, "itens": itens_response}
        except Exception as e:
            raise HTTPException(status_code=500, detail="Erro interno do servidor")
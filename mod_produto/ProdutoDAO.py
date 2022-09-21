# import da persistência
import db
from mod_produto.ProdutoModel import ProdutoDB
from fastapi import APIRouter
from pydantic import BaseModel

# import da segurança
from fastapi import Depends
import security

# dependências de forma global
router = APIRouter( dependencies=[Depends(security.verify_token), Depends(security.verify_key)] )



class Produto(BaseModel):
    codigo: int = None
    nome: str
    grupo: int

# Criar os endpoints de Produto: GET, POST, PUT, DELETE

@router.get("/produto/", tags=["produto"])
def get_produto():
    try:
        session = db.Session()
        # busca todos
        dados = session.query(ProdutoDB).all()
        return dados, 200
    
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()

@router.get("/produto/{id}", tags=["produto"])
def get_produto(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).all()
        return dados, 200

    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()


@router.post("/produto/{id}", tags=["produto"])
def post_produto(corpo: Produto):
    try:
        session = db.Session()
        
        dados = ProdutoDB(None, corpo.nome, corpo.matricula, corpo.grupo)

        session.add(dados)
        
        session.commit()
        
        return {"msg": "Cadastrado com sucesso!", "id": dados.id_produto}, 200
    
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao cadastrar", "erro": str(e)}, 406
    finally:
        session.close()

@router.put("/produto/{id}", tags=["produto"])
def put_produto(id: int, corpo: Produto):
    try:
        session = db.Session()
        
        dados = session.query(ProdutoDB).filter(
            ProdutoDB.id_produto == id).one()

        dados.nome = corpo.nome
        dados.matricula = corpo.matricula
        dados.grupo = corpo.grupo
        
        session.add(dados)
        session.commit()
        return {"msg": "Editado com sucesso!", "id": dados.id_produto}, 201

    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao editar", "erro": str(e)}, 406
    finally:
        session.close()

@router.delete("/produto/{id}", tags=["produto"])
def delete_produto(id: int):
    try:
        session = db.Session()
        
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(dados)
        session.commit()
        
        return {"msg": "Excluido com sucesso!", "id": dados.id_produto}, 201
    
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao excluir", "erro": str(e)}, 406
    finally:
        session.close()
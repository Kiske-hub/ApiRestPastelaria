import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer

# ORM

class ProdutoDB(db.Base):
    __tablename__= 'tb_produto'

    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    matricula = Column(CHAR(10), nullable=False)
    grupo = Column(Integer, nullable=False)

    def __init__(self, id_produto, nome, matricula, grupo):
        self.id_cliente = id_produto
        self.nome = nome
        self.matricula = matricula
        self.grupo = grupo
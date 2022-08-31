from flask import Flask
from flask_restful import Api

# import das classes com os endpoints

from ClienteDAO import cliente

from FuncionarioDAO import funcionario

app = Flask(__name__)
api = Api(app)

# mapeamento dos endpoints

api.add_resource(funcionario, "/funcionario/<int:id>", endpoint = 'funcionario')

api.add_resource(cliente, "/cliente/<int:id>", endpoint = 'cliente')

if __name__ == "__main__":
    """ Inicia a API Flask RESTful """
    app.run(host='0.0.0.0', port=5000, debug=True)
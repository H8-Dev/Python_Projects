from flask import jsonify, request #type: ignore
from services.usuario_service import UsuarioServices
from services.chamado_service import ChamadoServices

class UsuarioController():

    @staticmethod
    def listar():
        usuarios = UsuarioServices.lista_usuarios()
        return jsonify(usuarios)

    @staticmethod
    def lista_id(id):
        usuario = UsuarioServices.lista_user(id)
        if not usuario:
            return jsonify({"erro": "Usuário não encontrado"}), 404
        return jsonify(usuario)
    
    @staticmethod
    def cadastrar():
        data = request.get_json()
        usuario = UsuarioServices.cadastro_usuario(**data)
        return jsonify({"mensagem": "Usuário cadastrado com sucesso"}), 201

    @staticmethod
    def atualizar(id):
        data = request.get_json()
        usuario = UsuarioServices.atualiza_usuario(id, **data)
        if not usuario:
            return jsonify({"erro": "Usuário não encontrado"}), 404
        return jsonify({"mensagem": "Usuário atualizado com sucesso"})

    @staticmethod
    def deletar(id):
        usuario = UsuarioServices.deleta_usuario(id)
        if not usuario:
            return jsonify({"erro": "Usuário não encontrado"}), 404
        return jsonify({"mensagem": "Usuário deletado com sucesso"})

    @staticmethod
    def listar_chamados(id):
        chamados = ChamadoServices.lista_chamados_usuario(id)
        if not chamados:
            return jsonify({"erro": "Chamados não encontrados para o usuário"}), 404
        
        return jsonify(chamados)
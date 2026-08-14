from flask import jsonify, request #type: ignore
from datetime import date
from services.chamado_service import ChamadoServices
from services.usuario_service import UsuarioServices

class ChamadoController():

    @staticmethod
    def validar_dados(dados):
        if not dados:
            return jsonify({"erro": "JSON inválido"}), 400

        if len(dados.get("titulo", "")) < 5:
            return jsonify({"erro": "Título inválido"}), 400

        if len(dados.get("descricao", "")) < 10:
            return jsonify({"erro": "Descrição inválida"}), 400

        titulo = dados.get("titulo")
        if not titulo:
            return jsonify({"erro": "Título é obrigatório"}), 400

        user = dados.get("usuario_id")
        check_user = UsuarioServices.validacao(user)
        if check_user == None:
            return jsonify({"erro": "Usuário não existe"}), 400

        check_count = ChamadoServices.validacao_count(user)
        if check_count == False:
            return jsonify({"erro": "Usuário não pode ter mais de 5 chamados"}), 400

        prioridade = dados.get("prioridade")
        if not prioridade.lower() == "baixa" and not prioridade.lower() == "media" and not prioridade.lower() == "alta" and not prioridade.lower() == "média":
            return jsonify({"erro": "Prioridade inválida"}), 400

        status = dados.get("status")
        if not status.lower() == "aberto":
            return jsonify({"erro": "Novos chamados só podem ter como seu status aberto"}), 400
        return True


    @staticmethod
    def listar():
        chamados = ChamadoServices.lista_chamados()
        return jsonify(chamados)

    @staticmethod
    def lista_id(id):
        chamado = ChamadoServices.lista_chamado_id(id)
        if not chamado:
            return jsonify({"erro": "Chamado não encontrado"}), 404
        return jsonify(chamado)

    @staticmethod
    def cadastrar():
        dados = request.json
        validados = ChamadoController.validar_dados(dados)
        if validados != True:
            return validados

        chamado = ChamadoServices.cadastro_chamado(
            titulo=dados['titulo'],
            descricao=dados['descricao'],
            prioridade=dados['prioridade'],
            status=dados['status'],
            tecnico=dados['tecnico'],
            data_abertura=date.today().strftime("%d/%m/%Y"),
            usuario_id=dados['usuario_id']
        )
        
        return jsonify({"mensagem": f"Chamado {chamado.titulo} cadastrado com sucesso"}), 201

    @staticmethod
    def atualizar(id):
        dados = request.json
        validados = ChamadoController.validar_dados(dados)
        if validados != True:
            return validados

        chamado = ChamadoServices.atualiza_chamado(
            id=id,
            titulo=dados['titulo'],
            descricao=dados['descricao'],
            prioridade=dados['prioridade'],
            status=dados['status'],
            tecnico=dados['tecnico'],
            data_abertura=dados['data_abertura'],
            usuario_id=dados['usuario_id']
        )
        if not chamado:
            return jsonify({"erro": "Chamado não encontrado"}), 404
        
        return jsonify({"mensagem": f"Chamado {chamado.titulo} atualizado com sucesso"}), 200

    @staticmethod
    def deletar(id):
        chamado = ChamadoServices.deleta_chamado(id)
        if not chamado:
            return jsonify({"erro": "Chamado não encontrado"}), 404

        return jsonify({"mensagem": f"Chamado {chamado.titulo} deletado com sucesso"}), 200

    @staticmethod
    def iniciar(id):
        chamado = ChamadoServices.inicia_chamado(id)
        if not chamado:
            return jsonify({"erro": "Chamado não encontrado"}), 404
        
        return jsonify({"mensagem": f"Chamado {chamado.titulo} iniciado com sucesso"}), 200
    
    @staticmethod
    def encerrar(id):
        chamado = ChamadoServices.encerra_chamado(id)
        if not chamado:
            return jsonify({"erro": "Chamado não encontrado"}), 404
        
        return jsonify({"mensagem": f"Chamado {chamado.titulo} encerrado com sucesso"}), 200

    @staticmethod
    def calls_abertas():
        chamados = ChamadoServices.lista_chamados_abertos()
        return jsonify(chamados)
    
    @staticmethod
    def prioridade():
        chamados = ChamadoServices.lista_prioridade_alta()
        return jsonify(chamados)

from flask import jsonify, request #type: ignore
from dispositivo.disp_services import DispositivoService

class DispositivoController:
    
    @staticmethod
    def cadastrar():
        dados = request.get_json()
        disp = DispositivoService.cadastrar_dispositivo(dados)
        return jsonify(disp), 201

    @staticmethod
    def listar():
        dispositivos = DispositivoService.listar_dispositivos()
        if not dispositivos:
            return jsonify({'message': 'Nenhum dispositivo encontrado.'}), 404
        return jsonify(dispositivos), 200

    @staticmethod
    def listar_id(id):
        disp = DispositivoService.listar_dispositivo_por_id(id)
        if not disp:
            return jsonify({'message': 'Dispositivo não encontrado.'}), 404
        return jsonify(disp), 200

    @staticmethod
    def atualizar(id):
        dados = request.get_json()
        disp = DispositivoService.atualizar_dispositivo(id, dados)
        if not disp:
            return jsonify({'message': 'Dispositivo não encontrado.'}), 404
        return jsonify(disp), 200

    @staticmethod
    def deletar(id):
        disp = DispositivoService.deletar_dispositivo(id)
        if not disp:
            return jsonify({'message': 'Dispositivo não encontrado.'}), 404
        return jsonify({'message': 'Dispositivo deletado com sucesso.'}), 200

    @staticmethod
    def alterar_status(id):
        disp = DispositivoService.alterar_status(id)
        if not disp:
            return jsonify({'message': 'Dispositivo não encontrado.'}), 404
        return jsonify(disp), 200
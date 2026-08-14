from flask import Blueprint #type: ignore
from controllers.chamado_controller import ChamadoController
from controllers.usuario_controller import UsuarioController

chamado_bp = Blueprint("chamado_bp", __name__)
user_bp = Blueprint("user_bp", __name__)

#Usuario
user_bp.add_url_rule('/usuarios', view_func=UsuarioController.listar, methods=['GET'])
user_bp.add_url_rule('/usuarios/<id>', view_func=UsuarioController.lista_id, methods=['GET'])
user_bp.add_url_rule('/usuarios', view_func=UsuarioController.cadastrar, methods=['POST'])
user_bp.add_url_rule('/usuarios/<id>', view_func=UsuarioController.atualizar, methods=['PUT'])
user_bp.add_url_rule('/usuarios/<id>', view_func=UsuarioController.deletar, methods=['DELETE'])
user_bp.add_url_rule('/usuarios/<id>/chamados', view_func=UsuarioController.listar_chamados, methods=['GET'])


#Chamado
chamado_bp.add_url_rule('/chamados', view_func=ChamadoController.listar, methods=['GET'])
chamado_bp.add_url_rule('/chamados/<id>', view_func=ChamadoController.lista_id, methods=['GET'])
chamado_bp.add_url_rule('/chamados', view_func=ChamadoController.cadastrar, methods=['POST'])
chamado_bp.add_url_rule('/chamados/<id>', view_func=ChamadoController.atualizar, methods=['PUT'])
chamado_bp.add_url_rule('/chamados/<id>', view_func=ChamadoController.deletar, methods=['DELETE'])
chamado_bp.add_url_rule('/chamados/<id>/iniciar', view_func=ChamadoController.iniciar, methods=['PATCH'])
chamado_bp.add_url_rule('/chamados/<id>/encerrar', view_func=ChamadoController.encerrar, methods=['PATCH'])
chamado_bp.add_url_rule('/chamados/abertos', view_func=ChamadoController.calls_abertas, methods=['GET'])
chamado_bp.add_url_rule('/chamados/prioridade/alta', view_func=ChamadoController.prioridade, methods=['GET'])

from flask import Blueprint #type: ignore
from dispositivo.disp_controller import DispositivoController

disp_bp = Blueprint('disp_bp', __name__)

disp_bp.route('/dispositivos', methods=['POST'])(DispositivoController.cadastrar)
disp_bp.route('/dispositivos', methods=['GET'])(DispositivoController.listar)
disp_bp.route('/dispositivos/<int:id>', methods=['GET'])(DispositivoController.listar_id)
disp_bp.route('/dispositivos/<int:id>', methods=['PUT'])(DispositivoController.atualizar)
disp_bp.route('/dispositivos/<int:id>', methods=['DELETE'])(DispositivoController.deletar)
disp_bp.route('/dispositivos/<int:id>/status', methods=['PATCH'])(DispositivoController.alterar_status)
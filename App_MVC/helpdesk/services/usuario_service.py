from database import db
from ..repositories.usuario_repository import UsuarioRepository

class UsuarioServices():
    @staticmethod
    def validacao(id):
        user = UsuarioRepository.lista_user_id
        if not user:
            return None
        return user
    
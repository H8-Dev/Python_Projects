from database import db
from repositories.usuario_repository import UsuarioRepository

class UsuarioServices():
    @staticmethod
    def validacao(id):
        user = UsuarioRepository.lista_user_id(id)
        if not user:
            return None
        return user

    @staticmethod
    def lista_usuarios():
        users = UsuarioRepository.listar_user()
        usuarios = []

        for user in users:
            usuarios.append({
                "id": user.id,
                "nome": user.nome,
                "email": user.email,
                "setor": user.setor
            })
        return usuarios

    @staticmethod
    def lista_user(id):
        user = UsuarioRepository.lista_user_id(id)
        return user

    @staticmethod
    def cadastro_usuario(**kwargs):
        user = UsuarioRepository.cadastrar_user(kwargs)
        return user

    @staticmethod
    def atualiza_usuario(id, **kwargs):
        user = UsuarioRepository.atualizar_user(id, kwargs)
        return user

    @staticmethod
    def deleta_usuario(id):
        user = UsuarioRepository.deletar_user(id)
        return user
    
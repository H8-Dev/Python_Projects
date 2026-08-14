from database import db
from models.usuario import Usuario

class UsuarioRepository():

    @staticmethod
    def lista_user_id(id):
        return Usuario.query.filter(Usuario.id == id).first()
    
    @staticmethod
    def listar_user():
        return Usuario.query.all()

    @staticmethod
    def cadastrar_user(dados):
        user = Usuario(
            nome = dados['nome'],
            email = dados['email'],
            setor = dados['setor'],
        )
        db.session.add(user)
        db.session.commit()
        return user
        
    @staticmethod
    def atualizar_user(id, dados):
        user = UsuarioRepository.lista_user_id(id)
        if not user:
            return None
        
        user.nome = dados['nome']
        user.email = dados['email']
        user.setor = dados['setor']

        db.session.commit()
        return user
    
    @staticmethod
    def deletar_user(id):
        user = UsuarioRepository.lista_user_id(id)
        if not user:
            return None
        
        db.session.delete(user)
        db.session.commit()
        return user
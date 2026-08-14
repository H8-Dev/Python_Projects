from database import db
from models.chamado import Chamado

class ChamadoRepository():

    @staticmethod
    def lista_call_id(id):
        return Chamado.query.filter(Chamado.id == id).first()

    @staticmethod
    def lista_count_call(id):
        return Chamado.query.filter(Chamado.usuario_id == id).count()

    @staticmethod
    def listar_call():
        return Chamado.query.order_by(Chamado.titulo).all()

    @staticmethod
    def cadastrar_chamado(dados):
        call = Chamado(
            titulo = dados['titulo'],
            descricao = dados['descricao'],
            prioridade = dados['prioridade'],
            status = dados['status'],
            tecnico = dados['tecnico'],
            data_abertura = dados['data_abertura'],
            usuario_id = dados['usuario_id'],
        )
        db.session.add(call)
        db.session.commit()
        return call
    
    @staticmethod
    def atualizar_chamado(id, dados):
        call = ChamadoRepository.lista_call_id(id)
        if not call:
            return None
        
        call.titulo = dados['titulo']
        call.descricao = dados['descricao']
        call.prioridade = dados['prioridade']
        call.status = dados['status']
        call.tecnico = dados['tecnico']
        call.data_abertura = dados['data_abertura']
        call.usuario_id = dados['usuario_id']

        db.session.commit()
        return call
    
    @staticmethod
    def deletar_chamado(id):
        call = ChamadoRepository.lista_call_id(id)
        if not call:
            return None
        
        db.session.delete(call)
        db.session.commit()
        return call
    
    @staticmethod
    def chamados_abertas():
        return Chamado.query.filter_by(status="Aberto").all()
    
    @staticmethod
    def iniciar_chamado(id):
        call = ChamadoRepository.lista_call_id(id)
        if not call:
            return None
        if call.status == "Encerrado":
            return None
        if call.status == "Em atendimento":
            return None
        
        call.status = "Em atendimento"

        db.session.commit()
        return call
    
    @staticmethod
    def encerrar_chamado(id):
        call = ChamadoRepository.lista_call_id(id)
        if not call:
            return None
        if call.status == "Aberto":
            return None
        if call.status == "Encerrado":
            return None
        
        call.status = "Encerrado"

        db.session.commit()
        return call
    
    @staticmethod
    def lista_priod_alta():
        return Chamado.query.filter(Chamado.prioridade == "Alta").all()
    
    @staticmethod
    def lista_user(id):
        return Chamado.query.filter(Chamado.usuario_id == id).first()
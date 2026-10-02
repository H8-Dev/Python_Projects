from database import db
from dispositivo.disp_model import Dispositivo

class DispositivoRepository:

    @staticmethod
    def cadastrar_dispositivo(dados):
        disp = Dispositivo(
            hostname=dados['hostname'],
            ip_address=dados['ip_address'],
            tipo=dados['tipo'],
            status=dados['status']
        )
        db.session.add(disp)
        db.session.commit()
        return disp

    @staticmethod
    def listar_dispositivos():
        return Dispositivo.query.all()

    @staticmethod
    def listar_dispositivo_por_id(id):
        return Dispositivo.query.filter(Dispositivo.id == id).first()

    @staticmethod
    def atualizar_dispositivo(id, dados):
        disp = Dispositivo.query.filter(Dispositivo.id == id).first()
        if not disp:
            return None
        
        disp.hostname = dados['hostname']
        disp.ip_address = dados['ip_address']
        disp.tipo = dados['tipo']
        disp.status = dados['status']
        db.session.commit()
        return disp

    @staticmethod
    def deletar_dispositivo(id):
        disp = Dispositivo.query.filter(Dispositivo.id == id).first()
        if not disp:
            return None
        
        db.session.delete(disp)
        db.session.commit()
        return disp

    @staticmethod
    def alterar_status(id):
        disp = Dispositivo.query.filter(Dispositivo.id == id).first()
        if not disp:
            return None
        
        if disp.status == 'ativo':
            disp.status = 'inativo'
        else:
            disp.status = 'ativo'
        db.session.commit()
        return disp
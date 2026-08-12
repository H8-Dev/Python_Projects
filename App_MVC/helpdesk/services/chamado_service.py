from database import db
from ..repositories.chamado_repository import ChamadoRepository

class ChamadoServices():
    @staticmethod
    def validacao(id):
        call = ChamadoRepository.lista_call_id
        if not call:
            return None
        return call
    

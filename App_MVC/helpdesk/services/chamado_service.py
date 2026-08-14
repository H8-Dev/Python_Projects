from repositories.chamado_repository import ChamadoRepository

class ChamadoServices():
    @staticmethod
    def validacao(id):
        call = ChamadoRepository.lista_call_id
        if not call:
            return None
        return call

    @staticmethod
    def validacao_count(id):
        call = ChamadoRepository.lista_count_call(id)
        if call >= 5:
            return False
        return True

    @staticmethod
    def lista_chamados():
        chamados = ChamadoRepository.listar_call()
        call = []

        for chamado in chamados:
            call.append({
                "id": chamado.id,
                "titulo": chamado.titulo,
                "descricao": chamado.descricao,
                "prioridade": chamado.prioridade,
                "status": chamado.status,
                "tecnico": chamado.tecnico,
                "data_abertura": chamado.data_abertura.strftime("%d/%m/%Y %H:%M"),
                "usuario_id": chamado.usuario_id,
            })
        return call

    @staticmethod
    def cadastro_chamado(**kwargs): #pode usr kwargs.id para pegar o id

        call = ChamadoRepository.cadastrar_chamado(kwargs)
        return call

    @staticmethod
    def atualiza_chamado(id, **kwargs):
        call = ChamadoRepository.atualizar_chamado(id, kwargs)
        return call

    @staticmethod
    def deleta_chamado(id):
        call = ChamadoRepository.deletar_chamado(id)
        return call
    
    @staticmethod
    def lista_chamado_id(id):
        call = ChamadoRepository.lista_call_id(id)
        return call

    @staticmethod
    def lista_chamados_abertos():
        call = ChamadoRepository.chamados_abertas()
        return call

    @staticmethod
    def inicia_chamado(id):
        call = ChamadoRepository.iniciar_chamado(id)
        return call

    @staticmethod
    def encerra_chamado(id):
        call = ChamadoRepository.encerrar_chamado(id)
        return call

    @staticmethod
    def lista_prioridade_alta():
        call = ChamadoRepository.lista_priod_alta()
        return call

    @staticmethod
    def lista_usuario(id):
        call = ChamadoRepository.lista_user(id)
        return call
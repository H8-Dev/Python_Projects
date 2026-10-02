from dispositivo.disp_repository import DispositivoRepository

class DispositivoService:

    @staticmethod
    def cadastrar_dispositivo(dados):
        disp = DispositivoRepository.cadastrar_dispositivo(dados)
        return disp.to_dict()

    @staticmethod
    def listar_dispositivos():
        dispositivos = DispositivoRepository.listar_dispositivos()
        return [disp.to_dict() for disp in dispositivos]

    @staticmethod
    def listar_dispositivo_por_id(id):
        disp = DispositivoRepository.listar_dispositivo_por_id(id)
        return disp.to_dict()

    @staticmethod
    def atualizar_dispositivo(id, dados):
        disp = DispositivoRepository.atualizar_dispositivo(id, dados)
        return disp.to_dict()

    @staticmethod
    def deletar_dispositivo(id):
        disp = DispositivoRepository.deletar_dispositivo(id)
        return disp.to_dict()

    @staticmethod
    def alterar_status(id):
        disp = DispositivoRepository.alterar_status(id)
        return disp.to_dict()
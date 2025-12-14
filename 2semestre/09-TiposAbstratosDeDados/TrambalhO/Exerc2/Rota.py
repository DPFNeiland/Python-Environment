
def somar_valores(valores: list[dict], str) -> float:
    soma = 0

    for valor in valores:
        soma += valor[str]

    return soma


class Rota:
    # Codifique um TAD (Tipo Abstrato de Dados) em python chamado Rota. A classe Rota deverá ter os 
    # seguintes atributos: 
    # nome (str): identificador da rota (ex.: "Rota Centro"). 
    # trecho: list[dict] — cada trecho é um dicionário com as chaves: 
    # o {"dist_km": float, "vel_kmh": float, "semáforos": int} 
    # delay_sinal: float — atraso médio por semáforo em segundos (padrão: 45s).

    def __init__(self, nome: str, trecho: list[dict], delay_sinal: float = 0.75):
        self.nome = nome
        self.trecho = trecho
        self.delay_sinal = delay_sinal

    # a) tempo_total_min() -> float: calcula o tempo total da rota em minutos: 
    def tempo_total_min(self) -> float:
        tempo_h = somar_valores(self.trecho, "dist_km")/somar_valores(self.trecho, "vel_kmh")
        paradas_min = self.delay_sinal*somar_valores(self.trecho, "semaforos")
        tempo_total_min = 60 * tempo_h + paradas_min
        return int(tempo_total_min*100)/100

    # b) velocidade_media_kmh() -> float: velocidade média global da rota: 
    def calcular_velocidade_media(self) -> float:
        distancia_total = somar_valores(self.trecho, "dist_km")
        horas = self.tempo_total_min()/60
        velocidade_media = distancia_total/horas
        return int(velocidade_media*100)/100

    # atende_janela(inicio_min: float, fim_min: float) -> bool: retorna True se tempo_total_min() estiver 
    # no intervalo [início, fim] (em minutos). 
    def verificar_atende_janela(self, inicio_min: float, fim_min: float) -> float:
        tempo = self.tempo_total_min() 
        return True if tempo >= inicio_min and tempo <= fim_min else False
    
    # c) custo_emissao(kg_co2_km: float) -> float: estima emissões: 
    def calcular_custo_emissao(self, kg_co2_km: float) -> float:
        emissao = somar_valores(self.trecho, "dist_km") * kg_co2_km
        return emissao
    

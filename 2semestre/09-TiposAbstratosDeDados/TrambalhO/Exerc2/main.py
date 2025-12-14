
from Rota import Rota
import modules

def main():

    Rotas = modules.cadastrar_rotas()

    modules.imprimir_rotas(Rotas)

    modules.verificar_rotas_janela(Rotas)

    modules.calcular_co2_rotas(Rotas)

if __name__ == "__main__":
    main()
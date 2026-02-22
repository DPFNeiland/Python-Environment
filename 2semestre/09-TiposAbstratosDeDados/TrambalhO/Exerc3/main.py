import modules




def main():
    
    professores = modules.cadastrar_professores()

    modules.imprimir_professores(professores)

if __name__ == "__main__":
    main()
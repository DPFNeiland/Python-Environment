

# Talvez eu tenha subestimado essa questão em específico...

### Criação das Classes!
class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

    def __str__(self):
        return (f"Título: {self.titulo}\nAutor: {self.autor}\n\n")

class Usuario:
    def __init__(self, ra: str, nome: str):
        self.ra = ra
        self.nome = nome
        self.listaLivrosEmprestado = []

    def emprestar_livro(self, livro: Livro):
        self.listaLivrosEmprestado.append(livro)

    def devolver_livro(self, livro: Livro):
        self.listaLivrosEmprestado.remove(livro)

    def listar_livros(self):
        if self.listaLivrosEmprestado:
            for livro in self.listaLivrosEmprestado:
                print(livro)

        else:
            print("Nenhum livro emprestado\n\n")

class Biblioteca():
    def __init__(self, 
                 listaDeLivros: dict[str] = {}, 
                 listaDeUsuarios: dict[str] = {}):
        self.listaDeLivros = listaDeLivros
        self.listaDeUsuarios = listaDeUsuarios

    def cadastrar_livro(self, livro: Livro):
        if livro.titulo in self.listaDeLivros:
            print("Livro com mesmo título já cadastrado!\n\n")

        else:
            self.listaDeLivros[livro.titulo] = livro
            print("Livro cadastrado com sucesso!\n\n")

    def cadastrar_usuario(self, usuario: Usuario):
        if usuario.ra in self.listaDeUsuarios:
            print("Usuário com mesmo RA já cadastrado\n\n")
        
        else:
            self.listaDeUsuarios[usuario.ra] = usuario
            print("Usuário cadastrado com sucesso!\n\n")

    def realizar_emprestimo(self, ra: str, titulo_livro: str):
        
        if ra in self.listaDeUsuarios:
            if titulo_livro in self.listaDeLivros:

                livro = self.listaDeLivros[titulo_livro]
                usuario = self.listaDeUsuarios[ra]

                if livro.disponivel:
                    if livro in usuario.listaLivrosEmprestado:
                        print("Usuário já possui este livro")
                    
                    else:
                        livro.emprestar()
                        usuario.emprestar_livro(livro)
                        print("Empréstimo realizado com sucesso!\n")

                else:
                    print("Livro indisponível para empréstimo\n\n")
            else:
                print("Livro não encontrado\n\n")
        else:
            print("Usuário não encontrado\n\n")
            
    def realizar_devolucao(self, ra: str, titulo_livro: str):
        if ra in self.listaDeUsuarios:
            if titulo_livro in self.listaDeLivros:

                livro = self.listaDeLivros[titulo_livro]
                usuario = self.listaDeUsuarios[ra]

                if livro in usuario.listaLivrosEmprestado:
                    usuario.devolver_livro(livro)
                    livro.devolver()
                    print("Devolução realizado com sucesso!\n")

                else:
                    print("Este usuário não possui este livro.\n\n")
            else:
                print("Livro não encontrado\n\n")
        else:
            print("Usuário não encontrado\n\n")


    def listar_livros_disponiveis(self):
        encontrados = False
        for livro in self.listaDeLivros.values():
            if livro.disponivel:
                print(livro)
                encontrados = True
        if not encontrados:
            print("Nenhum livro disponível no momento.\n\n")

    def listar_livros_emprestados_usuario(self, ra: str):
        if ra in self.listaDeUsuarios:
            self.listaDeUsuarios[ra].listar_livros()
        else:
            print("Usuário não encontrado.\n")
### Criação do Menu
def main():
    bibi = Biblioteca()
    
    Acoes = ["Cadastrar livro",
             "Cadastrar usuário",
             "Realizar empréstimo",
             "Realizar devolução",
             "Listar livros disponíveis",
             "Listar livros emprestados ao usuário",
             "Finalizar"
             ]
    
    while True:
        nAcoes = len(Acoes)
        for i in range(1, nAcoes+1):
            print(f"{i}. {Acoes[i-1]}")
        
        n = int(input(""))

        match n:
            case 1:
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                bibi.cadastrar_livro(Livro(titulo, autor))
                
            case 2:
                ra = input("Digite o RA do usuário: ")
                nome = input("Digite o nome do usuário: ")
                bibi.cadastrar_usuario(Usuario(ra, nome))
            
            case 3:
                ra = input("Digite o RA do usuário: ")
                titulo = input("Digite o título do livro: ")
                bibi.realizar_emprestimo(ra, titulo)
            
            case 4:
                ra = input("Digite o RA do usuário: ")
                titulo = input("Digite o título do livro: ")
                bibi.realizar_devolucao(ra, titulo)
            
            case 5:
                bibi.listar_livros_disponiveis()
            
            case 6:
                ra = input("Digite o RA do usuário: ")
                bibi.listar_livros_emprestados_usuario(ra)

            case 7:
                print("Finalizando sistema...")
                break
            case _:
                print("Digite um valor válido!\n\n")

        
if __name__ == "__main__":
    main()
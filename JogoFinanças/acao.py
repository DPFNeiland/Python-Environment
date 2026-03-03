import random
import os
import time


# =========================
# LIMPAR TELA
# =========================

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# =========================
# INPUT SEGURO
# =========================

def input_int(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = input(mensagem).strip()

            if valor == "":
                raise ValueError

            valor = int(valor)

            if minimo is not None and valor < minimo:
                print(f"Digite um número maior ou igual a {minimo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"Digite um número menor ou igual a {maximo}.")
                continue

            return valor

        except ValueError:
            print("Digite um número inteiro válido.")


def input_float(mensagem, minimo=None):
    while True:
        try:
            valor = input(mensagem).strip()

            if valor == "":
                raise ValueError

            valor = float(valor)

            if minimo is not None and valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue

            return valor

        except ValueError:
            print("Digite um número válido.")


def input_string(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor == "":
            print("Entrada não pode ser vazia.")
        else:
            return valor


# =========================
# CLASSE ACAO
# =========================

class Acao:
    _id_counter = 1

    def __init__(self):
        self.ID = Acao._id_counter
        Acao._id_counter += 1

        self.nome = f"Acao_{self.ID}"
        self.juros = round(random.uniform(0.02, 0.12), 2)
        self.tipo_juros = random.choice(["Simples", "Compostos"])
        self.chanc_suc = round(random.uniform(0.4, 0.7), 2)

    def recal_chance_acao(self):
        variacao = random.uniform(-0.05, 0.05)
        self.chanc_suc = max(0.1, min(0.9, self.chanc_suc + variacao))


# =========================
# CLASSE INVESTIMENTO
# =========================

class Investimento:

    def __init__(self, acao, dinheiro, meses):
        self.acao = acao
        self.dinheiro_inicial = dinheiro
        self.saldo_atual = dinheiro
        self.meses_restantes = meses

    def atualizar_mes(self):
        if self.meses_restantes <= 0:
            return False

        self.acao.recal_chance_acao()
        sucesso = random.random() <= self.acao.chanc_suc

        if self.acao.tipo_juros == "Simples":
            if sucesso:
                self.saldo_atual += self.dinheiro_inicial * self.acao.juros
            else:
                self.saldo_atual -= self.dinheiro_inicial * self.acao.juros
        else:
            if sucesso:
                self.saldo_atual *= (1 + self.acao.juros)
            else:
                self.saldo_atual *= (1 - self.acao.juros)

        self.meses_restantes -= 1
        return self.meses_restantes > 0

    def lucro(self):
        return self.saldo_atual - self.dinheiro_inicial


# =========================
# CLASSE PESSOA
# =========================

class Pessoa:

    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
        self.dinheiro = 1000
        self.investimentos = []

    def investir_acao(self, dinheiro, acao, meses, meses_restantes_run):

        if dinheiro > self.dinheiro:
            print("Dinheiro insuficiente!")
            time.sleep(1)
            return False

        if meses > meses_restantes_run:
            print("Você não pode investir por mais meses do que restam na RUN!")
            time.sleep(1)
            return False

        self.dinheiro -= dinheiro
        self.investimentos.append(Investimento(acao, dinheiro, meses))
        print("Investimento realizado!")
        time.sleep(1)
        return True

    def atualizar_investimentos(self):
        finalizados = []

        for inv in self.investimentos:
            ativo = inv.atualizar_mes()
            if not ativo:
                finalizados.append(inv)

        for inv in finalizados:
            lucro = inv.lucro()
            print(f"\nInvestimento em {inv.acao.nome} finalizado.")
            print(f"Lucro obtido: R$ {round(lucro,2)}")
            self.dinheiro += inv.saldo_atual
            self.pontuacao += lucro
            self.investimentos.remove(inv)
            time.sleep(2)

    def finalizar_todos(self):
        print("\nFinalizando investimentos restantes...")
        for inv in self.investimentos:
            lucro = inv.lucro()
            self.dinheiro += inv.saldo_atual
            self.pontuacao += lucro
        self.investimentos.clear()

    def status(self, mes):
        print(f"===== MÊS {mes}/12 =====")
        print(f"Jogador: {self.nome}")
        print(f"Dinheiro disponível: R$ {round(self.dinheiro,2)}")
        print(f"Pontuação atual: {round(self.pontuacao,2)}")

        if not self.investimentos:
            print("\nNenhum investimento ativo.")
        else:
            print("\n--- INVESTIMENTOS ATIVOS ---")
            for i, inv in enumerate(self.investimentos, start=1):
                saldo = round(inv.saldo_atual, 2)
                lucro_atual = round(inv.lucro(), 2)

                print(f"\n{i}) {inv.acao.nome}")
                print(f"   Saldo atual: R$ {saldo}")
                print(f"   Meses restantes: {inv.meses_restantes}")
                print(f"   Se retirasse agora: R$ {saldo}")
                print(f"   Lucro até agora: R$ {lucro_atual}")


# =========================
# CLASSE JOGO
# =========================

class Jogo:

    def __init__(self):
        self.ranking = []

    def menu(self):
        while True:
            limpar_tela()
            print("===== MENU PRINCIPAL =====")
            print("1 - Jogar")
            print("2 - Rank")
            print("3 - Créditos")
            print("4 - Sair")

            escolha = input_int("Escolha: ", 1, 4)

            if escolha == 1:
                self.iniciar_run()
            elif escolha == 2:
                self.mostrar_rank()
            elif escolha == 3:
                self.creditos()
            elif escolha == 4:
                limpar_tela()
                print("Saindo...")
                break

    def iniciar_run(self):
        limpar_tela()
        nickname = input_string("Digite seu nickname: ")
        jogador = Pessoa(nickname)

        mes = 1
        acao_atual = None

        while mes <= 12:

            limpar_tela()

            if acao_atual is None:
                acao_atual = Acao()

            meses_restantes_run = 13 - mes

            jogador.status(mes)

            print("\nAção disponível:")
            print(f"Nome: {acao_atual.nome}")
            print(f"Juros: {acao_atual.juros*100}% ao mês")
            print(f"Tipo: {acao_atual.tipo_juros}")
            print(f"Chance sucesso: {acao_atual.chanc_suc*100}%")

            print("\n1 - Investir")
            print("2 - Avançar mês")

            escolha = input_int("Escolha: ", 1, 2)

            if escolha == 1:
                dinheiro = input_float("Quanto investir? ", 0.01)
                print(f"Máximo de meses: {meses_restantes_run}")
                meses = input_int("Por quantos meses? ", 1, meses_restantes_run)
                jogador.investir_acao(dinheiro, acao_atual, meses, meses_restantes_run)

            elif escolha == 2:
                jogador.atualizar_investimentos()
                mes += 1
                acao_atual = None

        limpar_tela()
        print("===== FIM DA RUN =====")

        jogador.finalizar_todos()

        lucro_total = jogador.pontuacao
        dinheiro_final = jogador.dinheiro

        print(f"\nJogador: {jogador.nome}")
        print(f"Dinheiro final acumulado: R$ {round(dinheiro_final,2)}")
        print(f"Pontuação final: {round(lucro_total,2)}")

        if lucro_total >= 0:
            print(f"Lucro total da RUN: R$ {round(lucro_total,2)}")
        else:
            print(f"Prejuízo total da RUN: R$ {round(lucro_total,2)}")

        input("\nPressione ENTER para voltar ao menu...")

        self.ranking.append((jogador.nome, jogador.pontuacao))
        self.ranking.sort(key=lambda x: x[1], reverse=True)

    def mostrar_rank(self):
        limpar_tela()
        print("===== RANKING =====")

        if not self.ranking:
            print("Nenhuma run realizada ainda.")
        else:
            for i, (nome, pontos) in enumerate(self.ranking, start=1):
                print(f"{i}º - {nome}: {round(pontos,2)} pontos")

        input("\nPressione ENTER para voltar...")

    def creditos(self):
        limpar_tela()
        print("===== CRÉDITOS =====")
        print("Jogo desenvolvido por Rodrigo Neiland")
        print("Projeto de estudo de POO e Game Design")
        input("\nPressione ENTER para voltar...")


# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":
    jogo = Jogo()
    jogo.menu()
from datetime import datetime, timedelta

# Entrada: número de semanas passadas
N = int(input("Digite o número de semanas passadas: "))

# Data atual
hoje = datetime.today()

# Calcula a data de N semanas atrás
data_passada = hoje - timedelta(weeks=N)

# Exibe o resultado formatado
print(f"Hoje é: {hoje.strftime('%d/%m/%Y')} (Semana atual: {hoje.isocalendar().week})")
print(f"Há {N} semanas atrás foi: {data_passada.strftime('%d/%m/%Y')} (Semana: {data_passada.isocalendar().week})")

from datetime import datetime

# Momento atual
agora = datetime.now()

# Data do Natal (24/12/2025 às 18h00)
prazo = datetime(2025, 12, 24, 18, 0, 0)

# Diferença
delta = prazo - agora

# Total em segundos
total_segundos = int(delta.total_seconds())

# Conversões
total_minutos = total_segundos // 60
total_horas   = total_segundos // 3600
total_dias    = delta.days
total_semanas = total_dias // 7

print(f"Faltam {total_semanas} semanas para o Natal 🎄 \n"
      f"Faltam {total_dias} dias para o Natal 🎄 \n"
      f"Faltam {total_horas} horas para o Natal 🎄 \n"
      f"Faltam {total_minutos} minutos para o Natal 🎄 \n"
      f"Faltam {total_segundos} segundos para o Natal 🎄\n")

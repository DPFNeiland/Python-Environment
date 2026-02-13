from datetime import datetime

# Momento atual
agora = datetime.now()


# Diferença
delta = prazo - agora

dias = delta.days
horas, resto = divmod(delta.seconds, 3600)
minutos, segundos = divmod(resto, 60)


print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos")
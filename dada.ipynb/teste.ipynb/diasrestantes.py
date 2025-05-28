

from datetime import datetime

agora = datetime.now()

prazo = datetime(2025, 6, 10, 0, 0, 0)

temporestante = prazo - agora

print(temporestante)

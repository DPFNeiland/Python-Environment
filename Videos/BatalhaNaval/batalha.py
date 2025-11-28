import numpy as np
import random

# parâmetros do Q-Learning
TAMANHO_TABULEIRO = 10
TAXA_APRENDIZADO = 0.1 # alfa (alpha)
FATOR_DESCONTO = 0.9 # gamma
TAXA_EXPLORACAO = 1.0
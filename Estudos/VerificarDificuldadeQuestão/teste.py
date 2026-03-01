import pdfplumber
import re
import pandas as pd
import os
import sys
import traceback

"""
Script Corrigido: Analisador de Maratona (BOCA)
Garante o processamento de múltiplas páginas mantendo a referência das colunas.
"""

def localizar_pdf_absoluto():
    diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
    arquivos = [f for f in os.listdir(diretorio_do_script) if f.lower().endswith('.pdf')]
    for f in arquivos:
        if f.startswith('202505') or 'paulista' in f.lower():
            return os.path.join(diretorio_do_script, f)
    if arquivos:
        return os.path.join(diretorio_do_script, arquivos[0])
    return None

def analisar_resultados_maratona(caminho_pdf):
    colunas_problemas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    stats = {p: {'resolvidos': 0, 'tempos': []} for p in colunas_problemas}
    
    # Variáveis para manter o mapeamento entre páginas
    mapa_colunas_global = {}
    total_equipes_processadas = 0

    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            print(f"-> Analisando arquivo: {os.path.basename(caminho_pdf)}")
            print(f"-> Total de páginas: {len(pdf.pages)}")
            
            for i, page in enumerate(pdf.pages):
                table = page.extract_table()
                if not table:
                    continue
                
                header_row_idx = -1
                mapa_colunas_pagina = {}
                
                # Tenta localizar o cabeçalho nesta página
                for row_idx, row in enumerate(table[:10]): # Aumentei a busca para as primeiras 10 linhas
                    row_str = [str(c) if c else "" for c in row]
                    encontrados = [p for p in colunas_problemas if p in row_str]
                    if len(encontrados) >= 5:
                        header_row_idx = row_idx
                        for p in colunas_problemas:
                            if p in row_str:
                                mapa_colunas_pagina[p] = row_str.index(p)
                        break
                
                # Se achou um novo mapa, atualiza o global. Se não, usa o global anterior.
                if mapa_colunas_pagina:
                    mapa_colunas_global = mapa_colunas_pagina
                    print(f"-> Página {i+1}: Novo cabeçalho detectado.")
                elif mapa_colunas_global:
                    print(f"-> Página {i+1}: Usando cabeçalho da página anterior.")
                else:
                    print(f"-> Página {i+1}: Cabeçalho não encontrado, pulando...")
                    continue

                # Processa as linhas
                for row_idx, row in enumerate(table):
                    # Pula o cabeçalho apenas se foi encontrado nesta página
                    if row_idx <= header_row_idx:
                        continue
                    
                    # Uma linha de equipe válida costuma ter o padrão "tentativas/tempo" ou "tentativas/-"
                    linha_texto = " ".join([str(c) for c in row if c])
                    if not re.search(r'\d+/(\d+|-)', linha_texto):
                        continue
                    
                    equipe_teve_acerto = False
                    for p, col_idx in mapa_colunas_global.items():
                        if col_idx < len(row):
                            celula = str(row[col_idx]) if row[col_idx] else ""
                            match = re.search(r'(\d+)/(\d+)', celula)
                            if match:
                                tempo = int(match.group(2))
                                stats[p]['resolvidos'] += 1
                                stats[p]['tempos'].append(tempo)
                                equipe_teve_acerto = True
                    
                    # Mesmo que não tenha acertado nada, se a linha é de equipe, contamos para log
                    total_equipes_processadas += 1

        print(f"-> Total de registros de equipes analisados: {total_equipes_processadas}")

        lista_final = []
        for p, dados in stats.items():
            total = dados['resolvidos']
            tempo_medio = sum(dados['tempos']) / total if total > 0 else 0
            lista_final.append({
                'Problema': p,
                'Total Resolvido': total,
                'Tempo Médio (min)': round(tempo_medio, 2)
            })
        
        df = pd.DataFrame(lista_final)
        return df.sort_values(by=['Total Resolvido', 'Tempo Médio (min)'], ascending=[False, True])

    except Exception as e:
        print(f"\n[ERRO] {e}")
        traceback.print_exc()
        return None

if __name__ == "__main__":
    print("=== ANALISADOR DE MARATONA (FIX MULTI-PÁGINA) ===")
    caminho_pdf = localizar_pdf_absoluto()
    
    if caminho_pdf:
        resultado = analisar_resultados_maratona(caminho_pdf)
        if resultado is not None:
            print("\n=== RANKING FINAL (TODAS AS PÁGINAS) ===")
            ranking_ativo = resultado[resultado['Total Resolvido'] > 0]
            print(ranking_ativo.to_string(index=False))
            
            print("\n=== PROBLEMAS NÃO RESOLVIDOS ===")
            nao_resolvidos = resultado[resultado['Total Resolvido'] == 0]['Problema'].tolist()
            print(", ".join(nao_resolvidos) if nao_resolvidos else "Todos resolvidos!")
    else:
        print("\n[ERRO] PDF não encontrado na pasta.")

import re
import pandas as pd
import os

"""
Script Ultra-Rápido para HTML de Resultados (BOCA).
Processa o arquivo como texto puro usando Regex para máxima performance em arquivos grandes.
"""

def analisar_html_fast(caminho_html):
    print(f"-> Analisando arquivo grande ({os.path.getsize(caminho_html)/1024/1024:.2f} MB)...")
    
    letras_problemas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    stats = {p: {'resolvidos': 0, 'tempos': []} for p in letras_problemas}
    
    # Regex para capturar linhas de tabela <tr>...</tr>
    # E dentro delas, capturar as células <td>...</td>
    re_linha = re.compile(r'<tr.*?>.*?</tr>', re.DOTALL | re.IGNORECASE)
    re_celula = re.compile(r'<td.*?>.*?</td>', re.DOTALL | re.IGNORECASE)
    re_acerto = re.compile(r'(\d+)/(\d+)')

    with open(caminho_html, 'r', encoding='utf-8', errors='ignore') as f:
        conteudo = f.read()

    print("-> Extraindo linhas...")
    linhas = re_linha.findall(conteudo)
    total_equipes = 0

    for linha in linhas:
        # Só nos interessam linhas que tenham muitos TDs (equipes)
        celulas = re_celula.findall(linha)
        if len(celulas) < 10:
            continue
            
        # Limpar tags HTML das células
        textos = [re.sub(r'<.*?>', '', c).strip() for c in celulas]
        # Remover entidades HTML comuns
        textos = [t.replace('&nbsp;', '').strip() for t in textos]
        
        # Localizar onde começam os problemas
        inicio_probs = -1
        for i, txt in enumerate(textos):
            if re.search(r'\d+/(\d+|-)', txt):
                inicio_probs = i
                break
        
        if inicio_probs != -1:
            total_equipes += 1
            for idx, letra in enumerate(letras_problemas):
                col_idx = inicio_probs + idx
                if col_idx < len(textos):
                    match = re_acerto.search(textos[col_idx])
                    if match:
                        tempo = int(match.group(2))
                        stats[letra]['resolvidos'] += 1
                        stats[letra]['tempos'].append(tempo)

    print(f"-> Sucesso! {total_equipes} registros processados.")
    
    lista_final = []
    for p in letras_problemas:
        total = stats[p]['resolvidos']
        medio = sum(stats[p]['tempos']) / total if total > 0 else 0
        lista_final.append({'Problema': p, 'Total Resolvido': total, 'Tempo Médio (min)': round(medio, 2)})
    
    df = pd.DataFrame(lista_final)
    return df.sort_values(by=['Total Resolvido', 'Tempo Médio (min)'], ascending=[False, True])

if __name__ == "__main__":
    arquivo = "ReportPage25.html"
    if os.path.exists(arquivo):
        res = analisar_html_fast(arquivo)
        print("\n=== RANKING EXTRAÍDO DO HTML (MODO FAST) ===")
        print(res[res['Total Resolvido'] > 0].to_string(index=False))
        
        nao_res = res[res['Total Resolvido'] == 0]['Problema'].tolist()
        print(f"\nProblemas não resolvidos: {', '.join(nao_res)}")
    else:
        print("Arquivo não encontrado.")

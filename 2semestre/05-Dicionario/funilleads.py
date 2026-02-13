def FiltrarLeadsQualificados(leads: list) -> list:
    
    leadsQualificados = []
    
    for lead in leads:
        
        if lead.get("score") >= 70:
            leadsQualificados.append(lead)
            
    return leadsQualificados

def ImprimirLeads(leads: list) -> None:
    
    for lead in leads:
        print(f"nome: {lead.get("nome")}", end="  ")
        print(f"origem: {lead.get("origem")}", end="  ")
        print(f"score: {lead.get("score")}", end="  ")
        print(f"status: {lead.get("status")}")

def CalcularTaxaDeConversaoOrigem(leads: list) -> list:
    OrigemConTotal = []
    origens = []

    for lead in leads:
        
        origem = lead.get("origem")
       
       
        if origem in origens:
            print(OrigemConTotal[origens.index(origem)].get("total"))
            
            OrigemConTotal[origens.index(origem)]["total"] += 1

        else:
            OrigemConTotal.append({"origem": origem, "total": 1, "convertido": 0})
            origens.append(origem)
        
        if lead.get("status") == "ganho":
            OrigemConTotal[origens.index(origem)]["convertido"] += 1

        
    return OrigemConTotal

def ImprimirConversao(conversao: list) -> None:
    
    for umaconversao in conversao:
        print(f"origem: {umaconversao.get("origem")}", end="  ")
        print(f"convertido: {umaconversao.get("convertido")}", end="  ")
        print(f"total: {umaconversao.get("total")}", end="  ")
        print(f"Taxa de Conversão Relativo: {(umaconversao.get("convertido")/umaconversao.get("total")*100):.2f}%")

def main():

    leads = [
        {"nome": "Ana" , "origem": "Instagram" , "score": 82, "status": "ganho"  },
        {"nome": "Beto", "origem": "Google Ads", "score": 65, "status": "perdido"},
        {"nome": "Cris", "origem": "Indicação" , "score": 90, "status": "ganho"  },
        {"nome": "Duda", "origem": "Instagram" , "score": 74, "status": "perdido"},
        {"nome": "Enzo", "origem": "Google Ads", "score": 71, "status": "ganho"  },
    ]

    # ImprimirLeads(leads)
    
    # ImprimirLeads(FiltrarLeadsQualificados(leads))
    
    ImprimirConversao(CalcularTaxaDeConversaoOrigem(leads))
    
if __name__ == "__main__":
    main()
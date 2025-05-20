
from math import inf

vencedor = ""
nomesEmpatados = ""
votosVencedor = -inf

votosWindows = 0
votosUnix = 0
votosLinux = 0
votosNetWare = 0
votosMacOS = 0
votosOutros = 0
votostotal = 0 



while True: 
    print("Qual o melhor Sistema Operacional para uso em servidores?", end="\n\n")

    print("As possíveis respostas são:", end="\n\n")

    print("1. Windows Server")
    print("2. Unix")
    print("3. Linux")
    print("4. Netware")
    print("5. MacOS")
    print("6. Outro")

    resp = int(input("Resp: "))

    match resp:
        case 0:
            break
        
        case 1:
            votosWindows += 1
            votostotal += 1
            
        case 2:
            votosUnix += 1
            votostotal += 1
            
        case 3:
            votosLinux += 1
            votostotal += 1
            
        case 4:
            votosNetWare += 1
            votostotal += 1
            
        case 5:
            votosMacOS += 1
            votostotal += 1
            
        case 6:
            votosOutros += 1
            votostotal += 1
            
        case _:
            print("Digite um valor válido!!!")
            
print("Sistema Operacional      Votos     %", end="\n\n") 
print("-------------------      -----    ------")
print(f"Windows Server            {votosWindows}      {votosWindows/votostotal*100:.2f}%") 
print(f"Unix                      {votosUnix}      {votosUnix/votostotal*100:.2f}%")
print(f"Linux                     {votosLinux}      {votosLinux/votostotal*100:.2f}%") 
print(f"Netware                   {votosNetWare}       {votosNetWare/votostotal*100:.2f}%") 
print(f"Mac OS                    {votosMacOS}       {votosMacOS/votostotal*100:.2f}%") 
print(f"Outro                     {votosOutros}       {votosOutros/votostotal*100:.2f}%") 
print("-------------------      -----")
print(f"Total                     {votostotal}")

if votosVencedor < votosWindows:
    votosVencedor = votosWindows
    vencedor = "Windows Server"



if votosVencedor == votosUnix:
    vencedor = "Empate"
    nomesEmpatados += "Unix\n"
    votosVencedor = votosUnix

    
    
if votosVencedor < votosUnix:
    votosVencedor = votosUnix
    vencedor = "Unix"
    
    
    
if votosVencedor == votosLinux:
    vencedor = "Empate"
    nomesEmpatados += "Linux\n"
    votosVencedor = votosLinux
    
    
if votosVencedor < votosLinux:
    votosVencedor = votosLinux
    vencedor = "Linux"


    
if votosVencedor == votosNetWare:
    vencedor = "Empate"   
    nomesEmpatados += "Netware\n"
    votosVencedor = votosNetWare
    
if votosVencedor < votosNetWare:
    votosVencedor = votosNetWare
    vencedor = "Netware"



if votosVencedor == votosMacOS:
    vencedor = "Empate"
    nomesEmpatados += "MacOS\n"
    votosVencedor = votosMacOS

if votosVencedor < votosMacOS:
    votosVencedor = votosMacOS
    vencedor = "Mac OS"

    
    
if votosVencedor == votosOutros:
    vencedor = "Empate"
    nomesEmpatados += "Outros\n"
    votosVencedor = votosOutros    

if votosVencedor < votosOutros:
    votosVencedor = votosOutros
    vencedor = "Outros"



if votosVencedor == votosWindows:
    vencedor = "Empate"
    nomesEmpatados += "Windows\n"
    votosVencedor = votosWindows

  
if vencedor == "Empate":
    print(f"A votação da enquete terminou empatada, com (votos) de {votosVencedor/votostotal*100:.2f}% cada\n")
    print(f"Entre os empatados, estão: \n{nomesEmpatados}")
    
else:
    print(f"O sistema Operacional mais votado foi o Unix, com {votosVencedor} votos,")
    print(f"correspondendo a {votosVencedor/votostotal*100:.2f}% dos votos.")
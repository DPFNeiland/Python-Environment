
tabela ={
    "A": 14.64,
    "B": 1.04,
    "C": 3.88,
    "D": 4.10,
    "E": 12.57,
    "F": 1.02,
    "G": 1.30,
    "H": 1.28,
    "I": 6.18,
    "J": 0.40,
    "L": 2.78,
    "M": 4.75,
    "N": 5.05,
    "O": 10.73,
    "P": 2.52,
    "Q": 1.20,
    "R": 6.53,
    "S": 7.81,
    "T": 4.34,
    "U": 4.64,
    "V": 1.70,
    "X": 0.21,
    "Z": 0.47
    
}

criptografia = "SUMZFI GCSGC SVZFC LZLSJ EZQSL HIFUI JDZQS LTSRF SGCSJ UOZSZ OJTZL ZOEEO LHMSE ESDSL IECLU ILHCD ZTIFE SZMOJ QCZSU IJPSU OTZZL ZOIFH ZFDST IHFIU SEEIH ITSES FZCDI LZDOA ZTIIG CSDIF JZOJB OZBSO EDITI EIEUI TOQIE GCSSJ BIMBS LECVE DODCO UZITS MSDFZ EUILI IGCSS EDZLIE CDOMO AZJTI HZFZU ITORO UZFSE DZLSJ EZQSL JZBSF TZTSZ MQCJE TIEHF OLSOF IEUIL HCDZT IFSER IFZLU FOZTIE HFSUO EZLSJ DSHZF ZZNCT ZFZGC SVFZFI EUITO QIEES UFSDI ECEZTI EHSMIE ZMSLZ SETCF ZJDS ZESQC JTZQC SFFZL CJTOZ MSJDF SSEDS ESEDZB ZIUIM IEEICL UILHC DZTIF UIEJD FCOTI JZOJQ MZDSF FZHIF CLZSG COHSM OTSFZ TZHIF ZMZJD CFOJQ CLTIE RCJTZ TIFSE TZUILH CDZUZI UOSJDO ROUZ"


valores = {}
total = 0
jatirado = []

resp = {}

for v in criptografia:
    
    if v in jatirado:
        total +=1
        valores[v] += 1
    elif v != " ":
        valores[v] = 1
        jatirado.append(v)
        total +=1
        

minimo = 101

for letra, qtd in valores.items():
    minimo = 101
    
    for tabelaLetra, tabelaPor in tabela.items():
        aux = abs(qtd/total*100- tabelaPor)
        
        if aux < minimo and aux <= 0.42:
            resp[letra] = tabelaLetra
            minimo = aux

resp[" "] = " "

for letra, qtd in resp.items():
    print(f"{letra} -> {qtd}")


for letra in criptografia: 
    print(f"{"?" if resp.get(letra) == None else resp.get(letra)}", end="")
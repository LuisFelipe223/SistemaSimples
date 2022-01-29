import csv
import pandas as pd

# Lista de informações
listaNome = []
listaQtde = []
listaPreco = []

# Lista de resultado das infomrações
listaGastoFinal = []

# 1- Ler arquivo CSV 
arquivoCSV = csv.reader(open("./CSV/arquivoJaneiro.csv"), delimiter = ",")

# 2- Percorrendo todos os itens do arquivo CSV
for [nome, qtde, preco] in arquivoCSV:
    gasto = float(qtde) * float(preco)
    
    listaNome.append(nome)
    listaQtde.append(qtde)
    listaPreco.append(preco)
    
    # Adicionando todos os preços*qtde com duas casas após a virgula
    listaGastoFinal.append((f"{gasto:.2f}"))

# 34- Gerando dicionário de dados para o DataFrame
dados = {
    "Nome": listaNome,
    "Quantidade": listaQtde,
    "Preço": listaPreco,
    "Gasto Final": listaGastoFinal
}

# 4- Gerando DataFrame(planilha)
df = pd.DataFrame(data = dados)
print(df)

# 5- Salvando a planilha
df.to_excel("./EXCEL/ArquivoJaneiro.xlsx", index = False)
print("-----FINALIZADO------")

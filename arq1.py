#Abrir o arquivo de inscritos .csv e popular a lista_inscritos
nome_arquivo = "dados.dat"

with open(nome_arquivo, "r", encoding='utf8') as procurador:
    for linha in procurador:
        vetor_linhas = linha.split("\n")
        print (linha, end="")

        # Perguntar para o chat GPT lista, discionario e dupla
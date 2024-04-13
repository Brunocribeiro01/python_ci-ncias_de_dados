import statistics

class Glicemia:
    def __init__(self, data, hora, glicemia, kcal, carb):
        self.data = data
        self.hora = hora
        self.glicemia = float(glicemia)
        self.kcal = float(kcal)
        self.carb = float(carb)

def ler_arquivo(nome_arquivo):
    glicemias = []
    with open(nome_arquivo, 'r') as arquivo:
        next(arquivo)  # Pula o cabeçalho se existir
        for linha in arquivo:
            partes = linha.strip().split(';')
            if len(partes) >= 5:
                obj_glicemia = Glicemia(*partes[:5])
                glicemias.append(obj_glicemia)
    return glicemias

def calcular_media(lista, atributo):
    valores = [getattr(x, atributo) for x in lista]
    return sum(valores) / len(valores)

def calcular_mediana(lista, atributo):
    valores = sorted(getattr(x, atributo) for x in lista)
    return statistics.median(valores)

def calcular_moda(lista, atributo):
    valores = [getattr(x, atributo) for x in lista]
    return statistics.mode(valores)

# Uso das funções
nome_arquivo = 'dados_glicemia.csv'
lista_glicemias = ler_arquivo(nome_arquivo)

print("Médias:")
print("Glicemia:", calcular_media(lista_glicemias, 'glicemia'))
print("Kcal:", calcular_media(lista_glicemias, 'kcal'))
print("Carb:", calcular_media(lista_glicemias, 'carb'))

print("\nMedianas:")
print("Glicemia:", calcular_mediana(lista_glicemias, 'glicemia'))
print("Kcal:", calcular_mediana(lista_glicemias, 'kcal'))
print("Carb:", calcular_mediana(lista_glicemias, 'carb'))

print("\nModas:")
print("Glicemia:", calcular_moda(lista_glicemias, 'glicemia'))
print("Kcal:", calcular_moda(lista_glicemias, 'kcal'))
print("Carb:", calcular_moda(lista_glicemias, 'carb'))

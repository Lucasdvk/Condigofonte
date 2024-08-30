# 1) Cálculo do valor variável soma

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(SOMA)

# Saída = 91.


## 2) Verificação se um número pertence à sequência de Fibonacci


def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

# Número informado
numero = int(input("Informe um número: "))

# Verificar se pertence à sequência de Fibonacci
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")


## 3) Cálculos de faturamento diário (menor, maior e dias acima da média)

import json

# Dados do faturamento diário em formato JSON (exemplo)
faturamento_json = '''
{
    "faturamento": [0, 1500, 2500, 0, 2200, 1700, 0, 800, 1900, 2500, 0, 0, 3000, 1200]
}
'''

# Parse dos dados JSON
dados = json.loads(faturamento_json)
faturamento = dados['faturamento']

# Remover dias sem faturamento (faturamento = 0)
faturamento_validos = [valor for valor in faturamento if valor > 0]

# Cálculos
menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)
media_mensal = sum(faturamento_validos) / len(faturamento_validos)

# Dias com faturamento acima da média
dias_acima_media = len([valor for valor in faturamento_validos if valor > media_mensal])

# Resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")



## 4) Cálculo de percentual de faturamento por estado

# Valores de faturamento por estado
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Faturamento total
faturamento_total = sum(faturamento_estados.values())

# Cálculo dos percentuais
for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")



# 5)  Inversão de string sem usar funções prontas

def inverte_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# String informada
string = input("Informe uma string: ")

# Resultado
print(f"String invertida: {inverte_string(string)}")


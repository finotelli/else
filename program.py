# Solicita ao usuário que insira um valor numérico
x = int(input('Entre com o valor numérico: '))

# Verifica se o valor é ímpar
if ((x % 2) != 0):
    x += 10  # Adiciona 10 ao valor se for ímpar

# Se não for ímpar, verifica se não é divisível por 3
elif ((x % 3) != 0):
    x += 20  # Adiciona 20 ao valor se não for divisível por 3

# Se não for ímpar e não for divisível por 3
else:
    x += 30  # Adiciona 30 ao valor

# Exibe o valor final de x após as operações
print(x)
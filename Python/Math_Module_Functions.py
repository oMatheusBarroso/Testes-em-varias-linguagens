import math

# ALGUMAS FUNÇÕES DO MÓDULO MATH

#-------------------------------------------------------------
# Função pow() - exponenciação

print(" > Função pow() - exponenciação:\n")
operacao = math.pow(2,3) # base, expoente
print(operacao)
print()

#-------------------------------------------------------------
# Função floor() - arredondamento p/ baixo
print(" > Função floor() - arredondamento p/ baixo:\n")
operacao = math.floor(3.9)
print(operacao)
operacao = math.floor(10.5)
print(operacao)
print()

#-------------------------------------------------------------
# Função ceil() - arredondamento p/ cima

print(" > Função ceil() - arredondamento p/ cima:\n")
operacao = math.ceil(3.9)
print(operacao)
operacao = math.ceil(10.5)
print(operacao)
print()

#-------------------------------------------------------------
# Função fabs() - módulo (valor absoluto, sem sinal)

print(" > Função fabs() - módulo (valor absoluto, sem sinal):\n")
operacao = math.fabs(10)
print(operacao)
operacao = math.fabs(-10)
print(operacao)
print()

#-------------------------------------------------------------
# Função log() - logaritmo
# Por padrão, sem informar a base será 10

print(" > Função log() - logaritmo:\n")
operacao = math.log(10) # Sem informar base: base = 10
print(operacao)
operacao = math.log(10,2) # logaritmando, base
print(operacao)
print()

#-------------------------------------------------------------
# Função sqrt() - raíz quadrada

print(" > Função sqrt() - raíz quadrada:\n")
operacao = math.sqrt(9)
print(operacao)
print()
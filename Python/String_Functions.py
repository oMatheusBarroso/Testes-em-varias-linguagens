pais = "brasil"
bandeira = "ordem e progresso"

# ----------------------------------------------------------------
# Capitalize()
# Primeira letra transformada em maiúsculo

print("Função capitalize():")

print(pais.capitalize())
print(bandeira.capitalize(), "\n")

# ----------------------------------------------------------------
# Count()
# Retorna o número de ocorrências do parâmetro fornecido

print("Função count():")

print(bandeira.count("o"), "\n")

# ----------------------------------------------------------------
# Find()
# Retorna o index/posição da primeira ocorrência do parâmetro fornecido

print("Função find():")

print(pais.find("b"))
print(pais.find("a"))
print(bandeira.find("e"))
print(pais.find("o"), "\n") # retorna -1 pois não é encontrado

# ----------------------------------------------------------------
# Join()
# Concatena uma sequência de strings fornecida como parâmetro

print("Função join():")

str = " " # contém o separador que será usado na concatenação
iter = ("I","am","awesome") # lista de strings
a = str.join(iter)
print(a)
print("")
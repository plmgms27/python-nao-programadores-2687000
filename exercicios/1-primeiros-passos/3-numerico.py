data_nascimento = '05-10-1976'
idade_numerica = 46
altura = 1.74

# Descubra o tipo de dado de cada variável acima
print(type(data_nascimento))
print(type(idade_numerica))
print(type(altura))

# Realize uma operação entre dados do tipo string e inteiro
frase = "Paloma nasceu em "
print(frase + data_nascimento)
# Realize uma operação entre dados do tipo inteiro e float
soma = idade_numerica + altura
print(soma)
round(soma,1)
a = int(input('Entre com o primeiro valor:'))
b = int(input('Entre com o segundo valor:' ))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {soma}. '
      '\nSubtração: {subtracao}. '
      '\nMultiplicação: {multiplicacao}'
      '\nDivisão: {divisao}'
      '\nresto: {resto}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto))
print(resultado)

# x = '1'
# soma2 = int(x) +1
# print(soma2)
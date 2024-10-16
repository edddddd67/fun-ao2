# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.
def verificar_paridade(numero):
    if numero % 2 == 0:
        return( f"o numero {numero} será PAR ")
    else:
        return (f"o numero {numero} será IMPAR ")
    
a = int(input("digite o numero para ver a paridade "))
par = verificar_paridade(a)

print(par)

from time import sleep
def classificar_imc(imc):
    if imc <= 17:
        print('Seu IMC é bem baixo. Você é muito magro!')
    elif 17 < imc <= 24:
        print('Seu IMC pode ser considerado normal. Você está em uma faixa de peso aparentemente\nsaudável.')
    elif 24 < imc <= 30:
        print('Seu IMC está acima do normal. Você aparentemente está com sobrepeso.')
    elif 30 < imc <= 35:
        print('Seu IMC está alto. Você está obeso(a).')
    else:
        print('Seu IMC está altíssimo. Infelizmente parece que você tem obesidade mórbida. Procure um médico urgentemente e cuide de sua saúde.')
def calcular_imc(peso, altura):
    altura_quadrada = altura ** 2
    imc = peso / altura_quadrada
    print(f'O seu IMC é {imc:.2f}.')
    classificar_imc(imc)
    return imc
print('-=' * 15,'CALCULADORA DE IMC', '-=' * 15)
peso = float(input('Digite seu peso (kg): '))
altura = float (input('Digite sua altura (m): '))
print('Calculando IMC, Aguarde.')
sleep(1)
print('.')
sleep(1)
print('..')
sleep(1)
print('...')
sleep(1)
print('*-' * 40)
imc = calcular_imc(peso, altura)
print('*-' * 40)
print('-=' * 40)

    

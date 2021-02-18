from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - nasc
print('-' * 40)
if idade > 18:
    saldo = idade - 18
    print('Você têm {} anos.\nParabéns seu alistamento foi há {} anos.'.format(idade,saldo))
elif idade == 18:
    print('ATENÇÃO você têm {} anos.\nFaça seu alistamento imediatamente!!!'.format(idade))
elif idade < 18:
    saldo = 18 - idade
    print('Você têm {} anos.\nSeu alistamento será daqui a {} anos.'.format(idade,saldo))
print('-' * 40)    

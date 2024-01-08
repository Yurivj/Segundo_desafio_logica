def resultado_calculadora(Vitoria, Derrota):
    resultado = Vitoria - Derrota
    return resultado

print('=====Ranking=====')

Vitorias = int(input('Digite a quantidade de Vitórias:'))
Derrotas = int(input('Digite a quantidade de Derrotas:'))
resultado = resultado_calculadora(Vitorias, Derrotas)

print(resultado)

if resultado < 10:
    nivel = 'Ferro'
    print(f'O Héroi tem de saldo de {resultado} e está no nível {nivel}.')
if 11 <= resultado <= 20:
    nivel = 'Bronze'
    print(f'O Herói tem de saldo de {resultado} e está no nível {nivel}')
if 21 <= resultado <= 50:
    nivel = 'Prata'
    print(f'O Herói tem de saldo de {resultado} e está no nível {nivel}')
if 51 <= resultado <= 80:
    nivel = 'Ouro'
    print(f'O Herói tem de saldo de {resultado} e está no nível {nivel}')
if 81 <= resultado <= 90:
    nivel = 'Diamante'
    print(f'O Herói tem de saldo de {resultado} e está no nível {nivel}')
if 91 <= resultado <= 100:
    nivel = 'Lendário'
    print(f'O Herói tem de saldo de {resultado} e está no nível {nivel}')
if resultado >= 101:
    nivel = 'Imortal'
    print(f'O Herói tem de saldo de {resultado} e está no nível {nivel}')
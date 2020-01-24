# arquivo que vai rodar no terminal
from caixa import CaixaEletronico

caixa_eletronico = CaixaEletronico()

resposta = ''
while resposta != 's':
    resposta = input('Voce deseja acessar o caixa eletronico (Digite e) ou sair (Digite s)?')
    
    if resposta == 'e':
        caixa_eletronico.exibir_menu()

    elif resposta != 's' and resposta != '':
        print('Resposta inválida.')
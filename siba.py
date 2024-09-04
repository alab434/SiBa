import os


MENU_LARGURA = 40
MENU_VOLTAR_MENSAGEM = '\n>> TECLE [0] PARA VOLTAR AO MENU: '
CONTA_EXTRATO_HISTORICO = []
SAQUES_VALOR_LIMITE_POR_TRANSACAO = 500.00
SAQUES_QUANTIDADE_POR_DIA = 3
saques_efetuados_dia = 0
saques_valor_total_dia = 0.00
opcao_escolhida = -99


def menu_titulo():
	os.system('clear')
	print('\n' + ' BANCO PRAÇA '.center(MENU_LARGURA, '$') + '\n')


def menu_subtitulo(texto):
	print(f' {texto.upper()} '.center(MENU_LARGURA, '_') + '\n')


def menu_fim():
	print(MENU_LARGURA*'_')


def menu_opcoes():
	MENU_OPCOES = f'''________________ MENU __________________
   
   [1] VISUALIZAR EXTRATO
   [2] DEPOSITAR
   [3] SACAR

   [0] SAIR
________________________________________

>> ESCOLHA UMA OPÇÃO: '''
	return int(input(MENU_OPCOES))


def calcular_saldo(valores):
	valor_saldo = 0.00
	for item in CONTA_EXTRATO_HISTORICO:
		valor_saldo += -item[1] if item[0] == 'SAQUE' else item[1]
	return valor_saldo


def extrato(opcao):
	voltar = -99
	saldo_disponivel = calcular_saldo(CONTA_EXTRATO_HISTORICO)

	while voltar != 0:
		menu_titulo()
		menu_subtitulo('EXTRATO')

		if opcao == 'exibir':
			for item in CONTA_EXTRATO_HISTORICO:
				simbolo = '-' if item[0] == 'SAQUE' else '+'
				print(f'   {item[0]:20} {simbolo} R$ {item[1]:9.2f}')
			
			print(20*' -')
			print(f'   SALDO DISPONÍVEL     = R$ {saldo_disponivel:9.2f}')

		else:
			print('\n>> OPÇÃO INDISPONÍVEL!')

		print(MENU_LARGURA*'_')
		voltar = int(input(MENU_VOLTAR_MENSAGEM))
	

def depositar(opcao=''):
	voltar = -99

	while voltar != 0:
		menu_titulo()
		menu_subtitulo('DEPÓSITO')

		if opcao == '':
			valor_deposito = float(input('>> QUAL O VALOR DE DEPÓSITO? '))
			if valor_deposito <= 0:
				print(20*' -', '\n')
				print(f'>> OPERAÇÃO NÃO REALIZADA!')
				print(f'   VALOR INVÁLIDO.')
			else:
				CONTA_EXTRATO_HISTORICO.append(('DEPOSITO', valor_deposito))
				print(20*' -', '\n')
				print(f'>> OPERAÇÃO REALIZADA COM SUCESSO!')
				print(f'   DEPÓSITO EFETUADO      R$ {valor_deposito:9.2f}')

		else:
			print('\n>> OPÇÃO INDISPONÍVEL!')

		print(MENU_LARGURA*'_')
		voltar = int(input(MENU_VOLTAR_MENSAGEM))


def sacar(opcao=''):
	voltar = -99
	saldo_disponivel = calcular_saldo(CONTA_EXTRATO_HISTORICO)
	global saques_efetuados_dia
	global saques_valor_total_dia

	while voltar != 0:
		menu_titulo()
		menu_subtitulo('SAQUE')

		if saldo_disponivel <= 0.00:
			print(20*' -','\n')
			print(f'>> OPERAÇÃO NÃO REALIZADA!')
			print(f'   A CONTA NÃO POSSUE SALDO.')
		elif saques_efetuados_dia >= SAQUES_QUANTIDADE_POR_DIA:
			print(20*' -','\n')
			print(f'>> OPERAÇÃO NÃO REALIZADA!')
			print(f'   LIMITE DE SAQUES DIÁRIO ATINGIDO.')
		else:
			print(f'   SALDO DISPONÍVEL     = R$ {saldo_disponivel:9.2f}')
			print(MENU_LARGURA*'_')
			valor_saque = float(input('\n>> QUAL O VALOR DO SAQUE? '))

			if valor_saque <= 0:
				print(20*' -','\n')
				print(f'>> OPERAÇÃO NÃO REALIZADA!')
				print(f'   VALOR INVÁLIDO.')
			else:
				if valor_saque > saldo_disponivel:
					print(20*' -','\n')
					print(f'>> OPERAÇÃO NÃO REALIZADA!')
					print(f'   SALDO INSUFICIENTE.')
				elif valor_saque > SAQUES_VALOR_LIMITE_POR_TRANSACAO:
					print(20*' -','\n')
					print(f'>> OPERAÇÃO NÃO REALIZADA!')
					print(f'   O VALOR MÁXIMO PARA SAQUES É R$ {SAQUES_VALOR_LIMITE_POR_TRANSACAO}')
				else:
					CONTA_EXTRATO_HISTORICO.append(('SAQUE', valor_saque))
					saques_valor_total_dia += valor_saque
					saques_efetuados_dia += 1
					print(20*' -', '\n')
					print(f'>> OPERAÇÃO REALIZADA COM SUCESSO!')
					print(f'   SAQUE EFETUADO         R$ {valor_saque:9.2f}')
				
		print(MENU_LARGURA*'_')
		voltar = int(input(MENU_VOLTAR_MENSAGEM))


"""
	Sistema Bancário Simples:
	- EXTRATO
	- DEPOSITO
	- SAQUE
"""
while opcao_escolhida != 0:
	menu_titulo()
	opcao_escolhida = menu_opcoes()

	if opcao_escolhida == 1:
		extrato('exibir')
	elif opcao_escolhida == 2:
		depositar()
	elif opcao_escolhida == 3:
		sacar()

else:
	menu_fim()
	print()
	menu_titulo()
	print(f' FIM DO ATENDIMENTO '.center(MENU_LARGURA, '_'))
	print(3*'\n')

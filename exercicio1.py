import sys
import json
import requests
from datetime import datetime

# Todas as moedas disponibilizadas pelo BC
moedas_disponiveis = ['AUD','CAD','CHF','DKK','EUR','GBP','JPY','NOK','SEK','USD']

#Pegando a data de hoje
hoje = datetime.now()

#Método de conversão de moedas (Exercício 1)
def conversao_moedas(data_cotacao, moeda_origem, moeda_final, valor_desejado):

	#Separando a string de data do BC para convertê-la no padrão do Python
	ano_python = data_cotacao.split('-')[2]
	dia_python = data_cotacao.split('-')[1]
	mes_python = data_cotacao.split('-')[0]
	
	#Convertendo a string de data do BC para o padrão de data do python
	data_BC_python_str = ano_python + '-' + mes_python + '-' + dia_python

	#Conversão de string de data em data de fato
	data_BC_python = datetime.strptime(data_BC_python_str, '%Y-%m-%d')

	#Tratando o erro caso a data digitada seja posterior ao dia de hoje
	if data_BC_python > hoje:
		print("Não é possível acessar a cotação de uma data posterior a hoje!")
		sys.exit(0)

	#Tratando o erro caso a moeda de origem ou a moeda final não estejam na base de dados disponibilizada pelo BC	
	moeda_origem_n_contem = moeda_origem not in moedas_disponiveis
	moeda_final_n_contem = moeda_final not in moedas_disponiveis
	if moeda_origem_n_contem == True or moeda_final_n_contem == True:
		print('Moedas não disponíveis para consulta!')
		sys.exit(0)
		
	
	#String HTTP que pega o valor da cotação da moeda de origem e da moeda final na data desejada (data_cotacao)
	url_moeda_origem = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda=%27' + moeda_origem + '%27&@dataInicial=%27'+ data_cotacao + '%27&@dataFinalCotacao=%27' + data_cotacao + '%27&$top=4&$format=json&$select=cotacaoCompra,dataHoraCotacao'
	url_moeda_final = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda=%27' + moeda_final + '%27&@dataInicial=%27'+ data_cotacao + '%27&@dataFinalCotacao=%27' + data_cotacao + '%27&$top=4&$format=json&$select=cotacaoCompra,dataHoraCotacao'

	#API REST que pega o valor da cotação da moeda de origem e da moeda final na data desejada (data_cotacao)
	request_moeda_origem = requests.get(url_moeda_origem)
	request_moeda_final = requests.get(url_moeda_final)

	#Transforma para o modo json a API REST da moeda de origem e da moeda final
	json_moeda_origem = request_moeda_origem.json()
	json_moeda_final = request_moeda_final.json()

	try: 

		#Converte a moeda de origem para o valor do Real Brasileiro (R$)
		valor_moeda_origem = 150 * json_moeda_origem['value'][3]['cotacaoCompra']

		#Converte o valor do Real Brasileiro (R$) para a moeda final
		valor_moeda_final = round(valor_moeda_origem / json_moeda_final['value'][3]['cotacaoCompra'] , 2)

		print('Convertendo', moeda_origem, 'para', moeda_final, '...')
		print('Resultado:', valor_moeda_final)

	except IndexError:
		print("Verifique se a data que colocou não é um fim de semana ou feriado. Se for, não será possível acessar a cotação deste dia!")	


#conversao_moedas('01-03-2020', 'AUD', 'USD', 150)



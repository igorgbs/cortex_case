# **Case Cortex**

Case proposto para a vaga de Engenheiro de Software Pleno na Cortex-Intelligence.

Para resolver este problemas, deve-se instalar o seguinte:

1. Python: disponível para download [aqui](https://www.python.org/downloads/)
2. MySQL Workbench: disponível para download [aqui](https://www.mysql.com/downloads/)

## **Exercício 1**

No primeiro exercício, foi solicitado um serviço (API) que pudesse ser capaz de obter os dados de cotação de moedas do site do Banco Central e o resultado deveria ser o valor convertido para a moeda final, com os seguintes parâmetros:

1. data de cotação
2. moeda de origem
3. moeda final
4. valor desejado

Para isso, alguns procedimentos foram adotados:

- Para a obtenção dos dados das cotações de moedas do Banco Central, foi utilizado o método de API REST disponibilizado pelo BC. Podendo ser acessado [aqui](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/recursos/CotacaoMoedaPeriodo#eyJmb3JtdWxhcmlvIjp7IiRmb3JtYXQiOiJqc29uIiwiJHRvcCI6MTAwfX0=). A documentação deste método pode ser acessada [aqui](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/documentacao). 
- Com isso, foi desenvolvido um script em python, chamado [exercicio1.py](https://github.com/igorgbs/cortex_case/blob/master/exercicio1.py), que realiza esta conversão a partir dos dados do Banco Central.
- O método contido na API foi denominado de: *conversao_moedas()*. Onde seus parâmetros são:
    - data_cotacao 
    - moeda_origem
    - moeda_final
    - valor desejado
- Para utilizar o método, basta criar um *arquivo.py*, importar o arquivo que contém o método e chamá-lo. Exemplo:

```python
from exercicio1 import *
conversao_moedas('01-03-2020', 'AUD', 'USD', 150)
```

- Para fazer a importação do método, é bom que os dois arquivos (exercicio1.py e o arquivo.py, que contém a chamada do método, estejam no mesmo diretório).

- Existe um padrão para sintaxe do método. Ex.:
    - data_cotacao: 'MM-DD-AAAA' (*formato*: string)
    - moeda_orgiem: 'AUD' (*formato*: string)
    - moeda_final: 'USD' (*formato*: string)
    - valor_desejado: 150 (*formato*: float)

- Alguns casos foram tratados, tais como:

1. Se você inserir uma data de cotação posterior a data corrente, o código irá gerar um aviso: **Não é possível acessar a cotação de uma data posterior a hoje!**
2. Se você inserir alguma sigla de moeda (tanto para a moeda de origem quanto para moeda final) não disponibilizada pelo Banco Central, o código irá gerar um aviso: **Moedas não disponíveis para consulta!**
3. Se você inserir alguma data de cotação que seja fim de semana ou feriado, o código irá gerar um aviso: **Verifique se a data que colocou não é um fim de semana ou feriado. Se for, não será possível acessar a cotação deste dia!**

- As moedas disponibilizadas pelo Banco Central são:

Sigla | Moeda
----- | -----
AUD   | Dólar Australiano
CAD   | Dólar Canadense
CHF   | Franco Suíço
DKK   | Coroa Dinamarquesa
EUR   | Euro
GBP   | Libra Esterlina
JPY   | Iene Japonês
NOK   | Coroa Norueguesa
SEK   | Coroa Sueca
USD   | Dólar Americano


## **Exercício 2**

No segundo exercício foi apresentada uma [base de dados](https://docs.google.com/spreadsheets/d/1CELbpon5O66OkW3fXIl36gJ8P7thUBKrRag_QP0Uwfg/edit#gid=1297471854) e foi pedido um script a fim de criar agregações dos resultados.

Para resolver o problema proposto, a base de dados foi transformada para SQL, a fim de armazenar estas informações em banco. Além disso, facilitaria o desenvolvimento do script, já que o mesmo foi desenvolvido em SQL.

O script de resolução do exercício 2 está todo contido num só arquivo, chamado [exercicio2.sql](/exercicio2.sql). Nele estão contidos todos os scripts para resolver os 3 itens do exercício 2. Basta executar o script no MySQL Workbench (ou em algum outro ambiente SQL).


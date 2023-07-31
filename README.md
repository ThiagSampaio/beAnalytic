# beAnalytic Challenge - Thiago Sampaio

## Questão:

Realize a extração das informações que conseguir da base de dados listada no website:

https://steamdb.info/sales/

Armazene estes dados no Google BigQuery
Em seguida exporte ou conecte esses dados em um Google Sheets e nos envie o link.
Atenção:

Você deve criar um repositório público e não listado em um GIT para compartilhar conosco;
Compartilhar o Sheets final (o link precisa ser público);
Lembrar de pôr no repositório os arquivos da automação;

## Solução:
Abaixo os passos feitos para solução do problema.

1- Primeiro passo foi analisar a possibilidade de extração de dados diretamente do link passado. Este passo é importante, pois ocorrem regras de proteção relacionado ao webScrapping.

1.1 -  Se formos no faq(https://steamdb.info/faq/) do site, encontramos a <b>proibição de scrape</b> do site:
```
Can I use auto-refreshing plugins or automatically scrape/crawl SteamDB?
No, there's a chance you'll get automatically banned for doing so.

We also do not allow scraping/crawling on SteamDB. Please get the information from Steam itself, take a look at "How are we getting this information?" question above for more information.
```

2- Sabendo desta limitação , pesquisei sobre a API da steam. A steam possui uma API 'aberta', podendo ser feita 100.000 requesições/dia. O Número de requisições por minuto está na casa de 50 requisições em pacotes de 500 jogos(tecnica explicada adiante), com números superiores, a API bloqueou o uso.

3- O Script é simples: Primeiro pegamos a lista de todos os jogos presentes na steam no endpoint: 'http://api.steampowered.com/ISteamApps/GetAppList/v0001/'. Este endpoint nos da os nomes de todos os jogos e seus respectivos ids(appid)
3.1 - Depois agregei os ids em batches de 500 jogos e fiz a chamada para o endpoint: http://store.steampowered.com/api/appdetails?appids={app_ids}&cc={country_code}&filters=price_overview'
3.2 - Temos mais de 120.000 jogos listados, seria invíavel a chamada da api para cada ID, por isso a escolha por batches. Além disso , fiz também de modo assíncrono, com a utilização de threads paralelas, acelerando ainda mais o processo.

4.1- Ao final o script gera json local, no qual o usuário pode escolher a melhor forma de fazer o update para o BQ

## Rodando o script localmente:
1- Toda solução está no arquivo `main.py`. Para rodar localmente e ver a chamada no seu pc, faça um ambiente virtual para este projeto, instale as dependências e rode o arquivo.


## Pontos de melhora:
1- Podemos colocar o script na cloud run para automatizar o processo de coleta. Podemos também automatizar o processo de load dos dados no BQ. Fica a escolha do leitor dar os próximos passos.


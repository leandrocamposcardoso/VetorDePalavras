# Vetor de Palavras
Projeto para gerar vetor de palavras em Django + Django Rest Framework para processamento de linguagem natural.  A maior parte do NLP([Natural Language Processing) foi feita utilizando a biblioteca **nltk** do python.

## Rodando o projeto
Após instalar as dependência para rodar o projeto execute os comandos dentro da pasta API
*Instalar todas as dependências nessesárias do python*
> pip install -r requirements.txt

Gerar o banco de dados
> python manage.py migrate

Rodar o servidor
> python manage.py runserver

Rodar testes
> python manage.py test

## Natural language processing

### Endpoints
***{host}/words_vector/***
| URL |METHOD|PARAMS|
|--|--|--|
| /file-vocabulary|POST|Multipart Form(files)|
| /file-two-grams-vocabulary|POST|Multipart Form(files)|
| /file-two-grams-vector|POST|Multipart Form(files)|
| /file-vectors|POST|Multipart Form(files)|


### Exemplos de chamadas
#### {host}/words_vector/file-vocabulary
Retorna o vocabulário gerado com as palavras únicas de todos os arquivos
Data:
Method: POST
Type: Multipart Form

    file1     file1.txt
    file2     file2.txt

Response:

    {"vocabulary": [
    "fácil",
    "escrever",
    "código",
    "difícil",
    "funcione",
    "falar",
    "mostre"],
    "words": 7
    }



#### {host}/words_vector/file-two-grams-vocabulary
Retorna o vocabulário gerado com as palavras únicas de todos os arquivos
Data:
Method: POST
Type: Multipart Form

    file1     file1.txt
    file2     file2.txt

Response:

    {
        "falar é",
        "é fácil",
        "fácil mostreme",
        "mostreme o",
        "o código",
        "código é",
        "fácil escrever",
        "escrever código",
        "código difícil",
        "difícil é",
        "é escrever",
        "código que",
        "que funcione"
    ],
	    "words": 13
    }


#### {host}/words_vector/file-two-grams-vector
Retorna o vocabulário gerado com as palavras únicas de todos os arquivos
Data:
Method: POST
Type: Multipart Form

    file1     file1.txt
    file2     file2.txt

Response:

    [
	    {
	    "name": "teste.txt",
	    "vector": [1,1,1,1,1,1,0,0,0,0,0,0,0,0]
	  },
	  {
	    "name": "teste2.txt",
	    "vector": [0,1,0,0,0,0,0,1,2,1,1,1,1,1]
	  }
	]

#### {host/words_vector/file-vectors
Retorna o vocabulário gerado com as palavras únicas de todos os arquivos
Data:
Method: POST
Type: Multipart Form

    file1     file1.txt
    file2     file2.txt

Response:

    [
	  {
	    "name": "teste.txt",
	    "vector": [1,1,1,1,0,0,0]
	  },
	  {
	    "name": "teste2.txt",
	    "vector": [0,1,0,2,2,1,1]
	  }
	]


# Django Admin Painel
### Logs dos dados processados
#### {host}/admin/words_vector/logs/
![enter image description here](https://i.ibb.co/8gHmf0x/image.png)

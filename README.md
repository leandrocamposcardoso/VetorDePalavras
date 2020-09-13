# Vetor de Palavras
Projeto para gerar vetor de palavras em Django + Django Rest Framework para processamento de linguagem natural.  A maior parte do NLP([Natural Language Processing) foi feita utilizando a biblioteca **nltk** do python.

#### Dependências do projeto
Projeto utiliza o banco Microsoft Sql Server, conectado utilizando [msodbc](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver15) e a dependencia do python [django-pyodbc-azure](https://pypi.org/project/django-pyodbc-azure/).

#### Variáveis de ambiente
    export SECRET_KEY="teste"
    export DEBUG=True
    export API_HOST="*"
    export DATABASE_NAME="NOME_BANCO"
    export DATABASE_DSN="localhost"
    export DATABASE_PORT="1433"
    export DATABASE_USER="sa"
    export DATABASE_PASSWORD="SENHA_BANCO"

## Rodando o projeto
Após instalar as dependências para rodar o projeto execute os comandos dentro da pasta API
*Instalar todas as dependências nessesárias do python*
> pip install -r requirements.txt

Gerar o banco de dados
> python manage.py migrate

Rodar o servidor
> python manage.py runserver

## Natural language processing)

### Endpoints
Exemplo chamada Imnsonia:
![](https://i.ibb.co/1Jz7RWG/image.png)
#### /words_vector/file-vocabulary
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



#### /words_vector/file-two-grams-vocabulary
Retorna o vocabulário gerado com as palavras únicas de todos os arquivos
Data:
Method: POST
Type: Multipart Form

    file1     file1.txt
    file2     file2.txt

Response:

    {
	    "vocabulary": [
	    "falar é",
	    "é fácil",
	    "fácil mostre",
	    "mostre me",
	    "me o",
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
	    "words": 14
    }


#### /words_vector/file-two-grams-vector
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
	    "vector": [
	      1,
	      1,
	      1,
	      1,
	      1,
	      1,
	      0,
	      0,
	      0,
	      0,
	      0,
	      0,
	      0,
	      0
	    ]
	  },
	  {
	    "name": "teste2.txt",
	    "vector": [
	      0,
	      1,
	      0,
	      0,
	      0,
	      0,
	      0,
	      1,
	      2,
	      1,
	      1,
	      1,
	      1,
	      1
	    ]
	  }
	]

#### /words_vector/file-vectors
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
	    "vector": [
	      1,
	      1,
	      1,
	      1,
	      0,
	      0,
	      0
	    ]
	  },
	  {
	    "name": "teste2.txt",
	    "vector": [
	      0,
	      1,
	      0,
	      2,
	      2,
	      1,
	      1
	    ]
	  }
	]


# Django Admin Painel
### Logs dos dados processados
#### /admin/words_vector/logs/
![enter image description here](https://i.ibb.co/8gHmf0x/image.png)

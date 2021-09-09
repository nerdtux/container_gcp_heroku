# desafio_kyros

Para executar em ambiente virtual recomenda-se instalar o Pipenv

# 1. Instalar Pipenv
`pip install --user pipx`
`pipx install pipenv`

Para instalar os requerimentos digite
`pipenv install`

Entre no ambiente virtual
`pipenv shell`

# 2. Teste o aplicativo

Declare a variável de ambiente "SERVICE".
`export SERVICE="Serviço ABC"`

Execute o aplicativo
`flask run`

Abra o browser de internet e digite http://localhost:5000.
Deverá aparecer o valor da variável "SERVICE"




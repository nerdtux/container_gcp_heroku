# desafio_kyros

Requerimentos
- Ubuntu 20.04
- Python 3.8.10
- Docker 20.10.8

Baixe os arquivos necessários
`git clone https://github.com/nerdtux/container_gcp_heroku_nginx`

Para executar em ambiente virtual recomenda-se instalar o Pipenv

### 1. Instalar Pipenv
`pip install --user pipx`
`pipx install pipenv`

Para instalar os requerimentos digite
`pipenv install`

Entre no ambiente virtual
`pipenv shell`

### 2. Teste o aplicativo

Declare a variável de ambiente "SERVICE".
`export SERVICE="Serviço ABC"`

Execute o aplicativo
`flask run`

Abra o browser de internet e digite http://localhost:5000.
Deverá aparecer o valor da variável "SERVICE"

### 3. Instalar o Heroku CLI

Instale o Heroku CLI para Ubuntu através do comando
`sudo snap install --classic heroku`

Verifique sua instalação
`heroku --version`

### Colar imagem do resultado do código acima

Entrar com usuário e senha após o comando
`heroku login -i`

Crie um app Heroku
`heroku create`

Confira o nome do app criado
imagem app

Configure a stack do app para container
`herouku stack:set container`

Entre no seu portal Heroku e clique no app criado anteriormente
imagem 1

Clique em Settings para conferir se a stack foi alterada corretamente
imagem 2
imagem 3

Clique em Deploy e conecte a conta do GitHub
Imagem 4

Na mesma página configure uma pipeline
Imagem 5

Na tela que abrir, já teremos o link para acesso ao app
imagem 6

Para finalizar a configuração da pipeline vamos conectar novamente ao GitHub
imagem 7
imagem 8

Link para validar o resultado da aplicação no Heroku
<https://sleepy-crag-40442.herokuapp.com/>

### Realizar o deploy usando Clou Run da Google Cloud

Requisitos:
- Conta Google Cloud
- Gcloud instalado - veja como instalar [aqui](https://cloud.google.com/sdk/docs/install#deb)

### Autenticação no gcloud
`gcloud auth login`

### Criando um projeto novo
`gcloud projects create nomedoprojeto`

### Para verificar seu PROJECT_ID
`gcloud projects list`

### Defina seu projeto como padrão
`gcloud config set project PROJECT_ID`

### Execute o comando abaixo para obter o BILLING ACCOUNT ID
`gcloud alpha billing accounts list`

### Defina uma conta de pagamentos ao projeto criado
`glcloud alpha billing projects link PROJECT_ID --billing-account 0X0X0X-0X0X0X-0X0X0X`

### Crie uma Conta de serviços
`gcloud iam service-accounts create nomedacontadeservicos

### Dê permissão para que a conta de serviços criada gerencie os recursos do projeto
``gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:nomedacontadeservicos@PROJECT_ID.iam.gserviceaccount.com" --roles="roles/editor"`

### Compile a imagem de conteiner usando o Cloud Build.
`gcloud builds submit --tag gcr.io/PROJECT_ID/nomedoconteiner`

### Realize o deploy
`gcloud run deploy --image gcr.io/PROJECT_ID/nomedoconteiner --platform managed`

Se for solicitada a ativação da API, responda y.
O nome do serviço será solicitado: pressione Enter para aceitar o padrão.
Você deverá selecionar a região quando solicitado.
Responda y quando receber solicitação para Allow unauthenticated invocations.

Faça o teste abrindo o link que retornar como resultado.

No meu caso o link é [esse](https://servico-4mzy6cfcfa-ue.a.run.app).


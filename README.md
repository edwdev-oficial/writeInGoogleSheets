# Carregar, Ler e Editar Planilhas Google Sheets em WebApp Streamlit.io

##### Criar uma planilha Google Sheets em seu driver
1 - Criar uma planilha em https://docs.google.com/spreadsheets/u/0/


###### Criar um projeto no Google Clound Console
01 - Acessar Google Clound Console em https://console.cloud.google.com
02 - Selecionar o projeto criado
03 - Buscar por Google Sheets API
04 - Ativar o Google Sheets API
05 - No menu da esquerda clicar em Credenciais
06 - Clicar em CRIAR CREDENCIAIS
07 - Selecionar o tipo de credencial: ID do cliente OAuth 2.0
08 - Clicar em CONFIGURAR TELA DE CONSENTIMENTO
09 - User Type, selecionar External
10 - Clicar em CRIAR
11 - Informar nome do APP
12 - Informar e-mail de suporte
13 - Informar e-mail em Dados de contato do desenvolvedor
14 - Clicar em SALVAR E CONTINUAR
15 - Em Escopos não precisa configurar nada clique em SALVAR E CONTINUAR
16 - Em Usuários de Teste também não é necessário configurar nada, apenas clique em SALVAR E CONTINUAR
17 - Em Summary clique em VOLTAR AO PAINEL (BACK TO DASHBOAR)
18 - No painel clicar em PUBLICAR O APLICATIVO (PUBLISH APP) e confirme
19 - Clicar novamente em CRIAR CREDENCIAIS e selecione Conta de Serviço
20 - Em Detalhes da Conta de Serviço no campo ID da conta de serviço informar um nome que pode ser o mesmo nome da aplicação. O ID da conta de serviço precisa começar com uma letra minúscula, seguida por um ou mais caracteres alfanuméricos minúsculos que podem ser separados por hifens. Exemplo: streamlittest-1
21 - Clicar em CRIAR E CONTINUAR
22 - Clicar em CONCLUIR
23 - Clicar na contade serviço que foi criada
24 - Selecionar a aba CHAVES
25 - Clicar em ADICIONAR CHAVE e selecionar Criar nova chave
26 - Tipo de chave selecionar JSON
27 - Clicar em CRIAR para gerar e fazer o download do arquivo JSON
28 - Acesse a pasta para onde foi baixado o arquivo e para manter o contexto pode alterar o nome dele para credentials.json
29 - Em seguida mova-o para a pasta raiz do projeto.

###### Compartilhar a planilha no Google Sheets
01 - Acessar a planilha do Google Sheets pelo Google Drive, clicar em compartilhar e informar o e-mail da conta de serviço que é obtida na aba DETALHES da página principal do projeto no Google Clound
02 - Cole o e-mail em "Adicionar participantes, grupos e eventos de agenda" na planilha do Google Sheets clique em enviar

###### Configurar o arquivo secrets.toml
01 - Na raiz do projeto crie um diretório chamado .streamlit
02 - Dentro do diretório .streamlit crie um arquivo chamado secrets.toml
03 - Edite o arquivo secrets.toml conforme abaixo completando as informações com os seguintes dados:
    . Em spreadsheet, inserir a url da planilha Google Sheets
    . Em From your JSON key file preencha os campos com os dados do arquivo JSON que foi baixado do Google Clound e movido para a pasta raiz do projeto
~~~~
#.streamlit/secrets.toml

[connections.gsheets]
spreadsheet = ""

#From your JSON key file
type = ""
project_id = ""
private_key_id = ""
private_key = ""
client_email = ""
client_id = ""
auth_uri = ""
token_uri = ""
auth_provider_x509_cert_url = ""
client_x509_cert_url = ""
universe_domain = ""
~~~~

## Deploy para o streamlit.io

#### Enviar a aplicação para o repositório do github

01 - Criar o repositório no github 
02 - Acessar o repositório no github e copiar o link do repositório (no meu caso: foi criado em: https://github.com/edwdev-oficial/writeInGoogleSheets.git)
03 - Criar o arquivo .gitignore com os seguintes arquivos e diretórios
~~~~

~~~~
03 - Rodar o git init no terminal




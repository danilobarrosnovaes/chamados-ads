# chamados-ads
# API de Chamados de Suporte (`chamados-ads`)

**Estudante:** Danilo Barros de Novaes — 
**Disciplina:** Projeto Programação Web

## Objetivo
Criar a estrutura inicial da API de chamados de suporte, reproduzindo o desenvolvimento apresentado na videoaula “Criando a primeira API com Flask”.

## Como instalar as dependências
Certifique-se de ter o `uv` instalado e execute o comando abaixo na raiz do projeto:

```bash
uv sync --locked
```

## Como executar a aplicação
Para iniciar o servidor Flask no GitHub Codespaces, execute:

```bash
uv run flask --app app run --host=0.0.0.0 --port=5000
```

## Como acessar a rota inicial e resposta esperada
Com a aplicação em execução, faça uma requisição `GET` para a rota `/` (pelo navegador na porta `5000` ou via terminal com `curl -i http://localhost:5000/`).

**Resposta esperada (HTTP 200 OK — `application/json`):**
```json
{
  "mensagem": "API de chamados em funcionamento"
}
```
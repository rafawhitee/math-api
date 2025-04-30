# DPESP IA LLM

## Principais Tecnologias
- Python 3.12.x
- FastAPI para api rest robusta e com swagger já integrado
- Pydantic para validação de models, dtos, etc.
- Langchain para fazer a separação de textos para os LLM
- Titkoken para cálculo de tokens
- Alembic para fazer versionamento do banco de dados (migrations)
- SQLAlchemy para conexão com o banco de dados
- OpenAI sdk para chamada do openai (gpt, azure, etc.)

## Executando

### DEV
- Precisa ter um banco postgres rodando, com o banco basta colocar as configurações do banco no .env no root do projeto
```bash
sh start-fastapi.sh
```

### PROD (simulando)
- Precisa buildar o Dockerfile
```bash
sh docker-build.sh
```

- Subir a imagem docker
- OBS: o docker-compsoe abaixo contém um db, caso não queira, só retirá-lo
```bash
sh docker-compose.sh
```

## Alembic Migrations
Cria uma nova revisão (versão de scripts)
```bash
alembic revision --autogenerate -m "NOME_DA_VERSAO_DA_MIGRATION"
```

Executa a última revision
```bash
alembic upgrade head
```
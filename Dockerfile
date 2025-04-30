### 
### Etapa 1
###
FROM python:3.12.10-alpine AS builder

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev python3-dev cargo

WORKDIR /build

COPY requirements.txt .

RUN python3.12 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt && \
    ls -lah /venv/bin && \
    /venv/bin/gunicorn --version

### 
### Etapa 2
###
FROM python:3.12.10-alpine AS runner

RUN apk add --no-cache libffi openssl dos2unix

COPY --from=builder /venv /venv

ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV PYTHONPATH="/ia-llm:/ia-llm/app:/ia-llm/app/config:/ia-llm/app/middlewares:/ia-llm/app/routers:/ia-llm/app/entities:/ia-llm/app/repositories:/ia-llm/app/logger:/ia-llm/app/decorators:/ia-llm/app/exceptions:/ia-llm/app/models:/ia-llm/app/models/requests:/ia-llm/app/models/responses:/ia-llm/app/models/exception:/ia-llm/app/services:/ia-llm/app/utils"

WORKDIR /ia-llm

COPY app app
COPY start-gunicorn.sh .

RUN chmod +x ./start-gunicorn.sh

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN chown -R appuser:appgroup /ia-llm
USER appuser

EXPOSE 8000

RUN dos2unix start-gunicorn.sh && \
    find app -type f -name "*.py" -exec dos2unix {} \;

ENTRYPOINT ["sh", "start-gunicorn.sh"]
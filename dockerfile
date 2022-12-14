ARG PYTHON_VERSION=3.9
ARG POETRY_VERSION=1.0.0

FROM python:$PYTHON_VERSION-slim-bullseye

ARG POETRY_VERSION

WORKDIR /app

RUN apt-get update \
  && apt-get clean \
  && apt-get -y install

RUN pip install poetry==$POETRY_VERSION

COPY app ./app
COPY poetry.lock pyproject.toml ./

RUN poetry export --dev --without-hashes --format requirements.txt > requirements.txt \
    && pip install --no-cache-dir -r requirements.txt


CMD ["uvicorn", "app.main:app", "--workers", "3", "--host", "0.0.0.0", "--http" , "h11" , "--port", "8002"]

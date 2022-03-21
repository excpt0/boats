FROM python:3.8.8-slim as production

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=10 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update \
 && apt-get install --no-install-recommends -y curl build-essential \
 && rm -rf /var/lib/apt/lists/*

# install poetry
ENV POETRY_VERSION=1.1.10
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python

# install runtime dependencies
COPY poetry.lock pyproject.toml $PYSETUP_PATH/
RUN cd $PYSETUP_PATH \
 && poetry run pip install -U pip \
 && poetry install --no-dev

# copy app and migrations
COPY boats /app/boats

# copy configuration files
COPY Makefile uwsgi.ini /app/boats/

# Set the working directory to /app
WORKDIR /app/boats

RUN mkdir "/app/boats/static" && python manage.py collectstatic
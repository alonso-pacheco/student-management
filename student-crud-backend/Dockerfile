FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend

WORKDIR /backend

COPY pyproject.toml poetry.lock ./

RUN apt-get update && \
    apt-get install -y python3-dev build-essential libpq-dev curl \
    default-libmysqlclient-dev pkg-config libxml2-dev libxmlsec1-dev

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root


COPY . .

EXPOSE 5000

COPY wait-for-mysql.sh /wait-for-mysql.sh
RUN chmod +x /wait-for-mysql.sh

CMD ["/wait-for-mysql.sh", "&&", "python", "app.py"]
# CMD ["flask", "run"]
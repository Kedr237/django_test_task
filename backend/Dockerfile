FROM python:3.10

RUN apt-get update \
    && apt-get install -y netcat-traditional

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip --no-cache-dir \
    && pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh"]
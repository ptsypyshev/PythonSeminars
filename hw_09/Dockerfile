# базовый образ
FROM debian:bullseye-slim

# установка рабочей директории (по умолчанию) в образе и переменной для директории проекта
WORKDIR /app
ARG project_path=./gamebot

# установка необходимого ПО
RUN set -ex ;\
    apt-get update ;\
    apt-get install -y --no-install-recommends python3-pip;\
    apt-get clean && rm -rf /var/lib/apt/lists/* ;\
    touch TOKEN.env

# копирование файла зависимостей
COPY $project_path/* ./

# установка зависимостей через pip
RUN pip3 install -r requirements.txt

# запуск скрипта при запуске контейнера
ENTRYPOINT ["python3", "main.py"]
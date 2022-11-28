FROM python:latest

ENV PYTHONDONTWIREBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN python3 -m pip install -r requirments.txt

COPY . /code/

EXPOSE 8000

CMD ['./entrypoint.sh']
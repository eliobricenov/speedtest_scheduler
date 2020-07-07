FROM python:3.8-alpine

LABEL maintainer=eliobricenov

WORKDIR scheduler

COPY src ./src/

COPY ["main.py", ".env", "requirements.txt", "./"]

RUN mkdir db && mkdir logs && pip install -r requirements.txt

CMD python main.py && crond -f -l 8

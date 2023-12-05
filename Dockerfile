FROM python:3.11

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

ARG APP_ENV='0.0.0.0'
ENV APP $APP_ENV

ARG APP_ENV2=5000
ENV APP2 $APP_ENV2


COPY . /app

EXPOSE $APP2_ENV2

CMD cd src && flask run --host $APP --port $APP2


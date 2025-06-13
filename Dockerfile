FROM python:3.9

# AUTHOR huudanphan@gmail.com
LABEL type web

ENV FOO bar
ENV FOO_1=bar1
ENV APP_HOME /app
ARG MESSAGE

RUN mkdir -p $APP_HOME

COPY . /$APP_HOME

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["app.py"]

ENTRYPOINT [ "python" ]
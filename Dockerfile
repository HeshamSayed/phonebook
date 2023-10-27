FROM python:3.10.4
ENV $PHONE_BOOK=/phonebook
RUN mkdir -p $PHONE_BOOK
RUN mkdir -p $PHONE_BOOK/static
RUN mkdir -p $PHONE_BOOK/logs
WORKDIR $PHONE_BOOK
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements/base.txt $PHONE_BOOK/base.txt
COPY ./requirements/production.txt $PHONE_BOOK/requirements.txt
COPY ./start.sh $PHONE_BOOK/start.sh
RUN pip install -r requirements.txt
RUN apt update -y
RUN apt install -y nano dos2unix libaio1
RUN apt upgrade -y tzdata
RUN dos2unix $PHONE_BOOK/start.sh
ENV TZ=Africa/Cairo

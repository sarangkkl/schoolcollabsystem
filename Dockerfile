FROM python:3.10
ENV APP_HOME /schoolcollabsystem
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get -y install gcc make \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /schoolcollabsystem
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "schoolapp.py"]
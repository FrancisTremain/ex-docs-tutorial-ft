# base image
FROM python:3.7.2

# set environment variable
ENV PYTHONIOENCODING utf-8

# copy content into directory
COPY . /code/

# optionally run any command (shell/bash)
RUN pip install flake8

# Optionally set working directory
WORKDIR /code/

# what command will be executed on `docker run`
CMD ["python", "-u", "/code/main.py"]

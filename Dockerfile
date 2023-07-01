FROM python:3.10

WORKDIR /usr/src/test/test_docker_app/
RUN mkdir  -p /usr/src/test_docker_app
COPY . /usr/src/app
CMD ['python',"main.py"]
#ENTRYPOINT ["python","main.py"]
#//RUN mkdir usr/src/test_app_docker/

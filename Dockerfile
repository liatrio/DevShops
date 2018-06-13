FROM python:3
RUN yum update -y
RUN yum install git -y
RUN git clone https://github.com/liatrio/DevShops
RUN pip install /Devshops/requirements.txt
RUN cd /Devshops/devshops
RUN python manage.py runserver

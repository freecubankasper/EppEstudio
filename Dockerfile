FROM python:3.10-bullseye

# default python envs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore

# django envs
ENV PRODUCTION=1
ENV SECRET_KEY=1234
ENV DEBUG=0
ENV ALLOWED_HOSTS="localhost, 72.167.50.223.nip.io"

#RUN apt-get install nano -y
RUN python -m pip install --upgrade pip

# copy the requirements to the root and install
COPY eppEstudio50/requirements.txt /
RUN  python -m pip install -r /requirements.txt

# add the app folder
RUN mkdir /eppEstudio50
ADD --chown=root:root /eppEstudio50 /eppEstudio50
WORKDIR /eppEstudio50


#Copy sh to run the server
ADD runserver.sh /runserver.sh
RUN chmod +x /runserver.sh

#Run the server
ENTRYPOINT [ "/runserver.sh" ]
#RUN python manage.py collectstatic
#CMD [ "python","manage.py","runserver","0.0.0.0:8000"]



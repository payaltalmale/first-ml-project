FROM python:3.7
#operating system
COPY . /app   
#copy this all the  from current directory in this app folder
WORKDIR /app
#  working directory to app
RUN pip install -r requirements.txt
# copy everything hence requirements.txt also install
EXPOSE $PORT
# $PORT environment name so it will run on that port
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
# with the help of gunicorn we can launch our application ip address map with 0000 that will be localhost ip address
# whwnvwer i run docker image i willl send this port directly app:app filename and object name


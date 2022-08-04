# Use an official Python runtime as a parent image
FROM python:3

# To the terminal without buffering it first
ENV PYTHONUNBUFFER 1
ENV PYTHONDONTWRITEBYTECODE 1

#To create working directory
WORKDIR /home/app
ADD . /home/app

# Installation of dependency packages
COPY ./requirements.txt/ /home/app/requirements.txt
RUN apt-get update 
RUN pip install -r /home/app/requirements.txt 

# Copy the contents
COPY . /home/app

#RUN python manage.py run server
CMD ["python","manage.py","runserver"]



# Expose the container port at port 8000
EXPOSE 8000







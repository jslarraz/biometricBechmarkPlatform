# Seleccionamos la imagen base
FROM debian:buster

# Set some environment vars
ENV DEBIAN_FRONTEND noninteractive

# Update repos and upgrade packages
RUN apt-get -y update
RUN apt-get -y upgrade

# Copy project and change directory
ADD . /tmp
WORKDIR /tmp

# Install python and numpy
RUN apt-get -y install python
RUN apt-get -y install python-pip
RUN pip install -r requirements.txt

# Run bash
CMD ["/bin/bash"]

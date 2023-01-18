#zakladni docker image, ze ktereho vychazime
FROM php:8.0-apache

#instalace rozsireni pro XSL procesor
RUN apt-get update && \
    apt-get install -y libxslt1-dev && \
    docker-php-ext-install xsl && \
    apt-get remove -y libxslt1-dev icu-devtools libicu-dev libxml2-dev && \
    rm -rf /var/lib/apt/lists/*

#instalace rozsireni mysqli pro komunikace s mysql databazi
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli

#instalace novych verzi zavislosti
RUN apt-get update && apt-get upgrade -y
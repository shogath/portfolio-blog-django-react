FROM nginx:1.23.0-alpine

RUN apk update && apk add openssl
# Create self-signed certificate to use with nginx
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
            -subj "/C=US/ST=Test/L=Test/O=Test/CN=localhost" \
            -addext 'subjectAltName = DNS:127.0.0.1, DNS:localhost' \
            -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

WORKDIR /usr/src/app
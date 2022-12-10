FROM traefik:v2.9

COPY configs /configs
COPY /traefik.yml /etc/traefik/traefik.yml

RUN mkdir -p /logs/ \
  && touch /logs/traefik.log \
  && chmod 600 /logs/traefik.log

RUN mkdir -p /ssl-certs/

VOLUME /logs
VOLUME /ssl-certs
VOLUME /shared
VOLUME /config

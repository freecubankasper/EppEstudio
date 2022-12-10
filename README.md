# Epp Estudio
Web page


Cuando necesitas sevir statics rápido, usas las opciones de catching de nginx para confiurarlo en esos directorios

*No se genera certificado para nginx
time="2022-12-10T03:29:57Z" level=error msg="Unable to obtain ACME certificate for domains \"72.167.50.223.nip.io,*.72.167.50.223.nip.io\"" providerName=default-resolver.acme ACME CA="https://acme-v02.api.letsencrypt.org/directory" rule="Host(`page.72.167.50.223.nip.io`)" routerName=nginx@docker error="unable to generate a wildcard certificate in ACME provider for domain \"72.167.50.223.nip.io,*.72.167.50.223.nip.io\" : ACME needs a DNSChallenge"

# Escritorio Chromium real accesible desde un navegador remoto.
# Se usa bajo la licencia correspondiente de LinuxServer.io.
FROM lscr.io/linuxserver/chromium:latest
COPY preview.html /config/Desktop/PRUEBA_STRINGART_SERVIDOR.html
EXPOSE 3000

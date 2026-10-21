FROM lscr.io/linuxserver/chromium:latest
COPY preview.html /config/Desktop/PRUEBA_STRINGART_SERVIDOR.html
COPY bootstrap_stringart.py /usr/local/bin/bootstrap_stringart.py
ENTRYPOINT ["/bin/sh","-c","python3 /usr/local/bin/bootstrap_stringart.py && exec /init"]
EXPOSE 3000

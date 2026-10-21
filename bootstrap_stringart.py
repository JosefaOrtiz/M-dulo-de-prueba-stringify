#!/usr/bin/env python3
"""Reconstruye el HTML privado desde variables de entorno, sin publicarlo en Git."""
import hashlib
import os
from pathlib import Path

dest=Path("/config/Desktop/STRINGART.html")
amount=int(os.environ.get("STRINGART_HTML_CHUNKS","0"))
if amount:
    if amount < 1 or amount > 128:
        raise RuntimeError("Número de partes inválido")
    chunks=[]
    for index in range(amount):
        key=f"STRINGART_HTML_PART_{index:03d}"
        if key not in os.environ:
            raise RuntimeError(f"Falta parte {index}")
        chunks.append(os.environ[key])
    content="".join(chunks).encode("utf-8")
    expected=os.environ.get("STRINGART_HTML_SHA256","")
    digest=hashlib.sha256(content).hexdigest()
    if not expected or expected.lower()!=digest:
        raise RuntimeError("La suma SHA-256 del HTML no coincide")
    dest.parent.mkdir(parents=True,exist_ok=True)
    tmp=dest.with_suffix(".html.tmp")
    tmp.write_bytes(content)
    tmp.chmod(0o644)
    tmp.replace(dest)
    print(f"STRING ART privado preparado: {len(content)} bytes, SHA256={digest}")
else:
    print("STRING ART privado no configurado; usar prueba inicial")

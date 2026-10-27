"""Genera una versión compacta de un TXT de normativa para leerlo con menos contexto.

Quita líneas vacías, pies de firma y cabeceras repetidas por página, y conserva
'=== Página N ===' y el número de línea original como prefijo para poder citar.
Uso:  python -m herramientas.limpiar_texto <entrada.txt> <salida.txt>
"""
import re
import sys
from pathlib import Path

RUIDO = re.compile(
    r"^\s*$"
    r"|^\s*(I|SERVICIO ANDALUZ DE SALUD)\s*$"
    r"|^\s*\d+(\s+\d+)?\s*$"
    r"|^C.digo: \S+ Fecha"
    r"|^Firmado Por"
    r"|^Url De Verificaci"
)


def limpiar(entrada: Path, salida: Path) -> int:
    lineas = entrada.read_text(encoding="utf-8").splitlines()
    out = []
    for n, linea in enumerate(lineas, 1):
        if linea.startswith("=== P") or not RUIDO.match(linea):
            out.append(f"{n}|{re.sub(r'\\s+', ' ', linea).strip()}")
    salida.write_text("\n".join(out), encoding="utf-8")
    return len(out)


if __name__ == "__main__":
    total = limpiar(Path(sys.argv[1]), Path(sys.argv[2]))
    print(f"{total} líneas escritas en {sys.argv[2]}")

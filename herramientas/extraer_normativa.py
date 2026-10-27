"""Extrae el texto de los PDF de normativa a datos/normativa_txt/<nombre>.txt (uno por PDF).

Cada página se marca con '=== Página N ===' para poder citar. Solo lectura sobre los PDF.
Uso:  python -m herramientas.extraer_normativa
"""
from pathlib import Path

from PyPDF2 import PdfReader

from herramientas.acceso import NORMATIVA_DIR

SALIDA = Path(__file__).resolve().parent.parent / "datos" / "normativa_txt"


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    for pdf in sorted(Path(NORMATIVA_DIR).glob("*.pdf")):
        lector = PdfReader(str(pdf))
        paginas = []
        for i, p in enumerate(lector.pages, 1):
            try:
                texto = p.extract_text() or ""
            except Exception as e:  # PDF con página dañada
                texto = f"[error al extraer: {e}]"
            paginas.append(f"=== Página {i} ===\n{texto}")
        contenido = "\n".join(paginas)
        destino = SALIDA / (pdf.stem + ".txt")
        destino.write_text(contenido, encoding="utf-8")
        print(f"{pdf.name}: {len(lector.pages)} págs, {len(contenido):,} caracteres")


if __name__ == "__main__":
    main()

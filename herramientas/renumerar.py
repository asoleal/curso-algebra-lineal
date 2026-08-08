#!/usr/bin/env python3
"""Renumera encabezados H1/H2 de los .qmd segun el orden de _quarto.yml.

Esquema: unidad U (part, 1-based), seccion S (archivo en la part),
subseccion N (## dentro del archivo) -> H1 = "U.S Titulo", H2 = "U.S.N Titulo".
- Ignora cercas de codigo (``` de cualquier largo).
- Preserva atributos finales tipo {.unnumbered}.
- Los H2 marcados con {.nonum} quedan SIN numero (clase inerte, sin efecto
  visual; sirve para "Aplicacion...", "Ventana IA", "Idea clave", etc.).
- --marcar: agrega {.nonum} a los H2 que hoy no tienen numero (una sola vez).
Uso: python3 herramientas/renumerar.py [--check] [--marcar]
"""
import re
import sys
import yaml

H = re.compile(r"^(#{1,2})\s+(?:\d+(?:\.\d+)*\s+)?(.*?)(\s*\{[^}]*\})?\s*$")

def orden_capitulos():
    with open("_quarto.yml", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    partes = []
    for item in cfg["book"]["chapters"]:
        if isinstance(item, dict) and "chapters" in item:
            partes.append(item["chapters"])
    return partes

def procesar(texto, u, s, marcar=False):
    lineas, dentro_cerca, cerca = texto.split("\n"), False, ""
    n, cambios = 0, []
    for i, ln in enumerate(lineas):
        m = re.match(r"^(`{3,})", ln)
        if m:
            if not dentro_cerca:
                dentro_cerca, cerca = True, m.group(1)
            elif ln.startswith(cerca):
                dentro_cerca = False
            continue
        if dentro_cerca:
            continue
        h = H.match(ln)
        if not h:
            continue
        nivel, titulo, attr = h.group(1), h.group(2), h.group(3) or ""
        if not titulo.strip():
            continue
        sin_num_viejo = not re.match(r"^#{1,2}\s+\d", ln)
        if ".nonum" in attr:
            nuevo = f"{nivel} {titulo}{attr}"
        elif marcar and nivel == "##" and sin_num_viejo:
            nuevo = f"## {titulo} {{.nonum}}"
        elif nivel == "#":
            nuevo = f"# {u}.{s} {titulo}{attr}"
        else:
            n += 1
            nuevo = f"## {u}.{s}.{n} {titulo}{attr}"
        if nuevo != ln:
            cambios.append((i + 1, ln, nuevo))
            lineas[i] = nuevo
    return "\n".join(lineas), cambios

def main():
    check, marcar = "--check" in sys.argv, "--marcar" in sys.argv
    total = 0
    for u, archivos in enumerate(orden_capitulos(), start=1):
        for s, ruta in enumerate(archivos, start=1):
            with open(ruta, encoding="utf-8") as f:
                nuevo, cambios = procesar(f.read(), u, s, marcar)
            for fila, viejo, nue in cambios:
                total += 1
                print(f"{ruta}:{fila}\n  - {viejo}\n  + {nue}")
            if cambios and not check:
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(nuevo)
    print(f"\n{'Faltan' if check else 'Hechos'} {total} cambio(s)." if total
          else "Numeracion ya correcta, nada que hacer.")
    sys.exit(1 if check and total else 0)

if __name__ == "__main__":
    main()
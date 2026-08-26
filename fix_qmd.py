import re

with open('unidades/u2-determinantes/2.1-intuicion-geometrica.qmd', 'r') as f:
    lines = f.readlines()

out = []
in_code = False
for i, line in enumerate(lines):
    stripped = line.strip()
    
    # Detecta el inicio de un bloque de Python sin fences
    if not in_code and (stripped.startswith('#| label: fig-') or stripped.startswith('import numpy')):
        if not out or not out[-1].strip().startswith('```'):
            out.append('```{python}\n')
            in_code = True
            
    # Detecta el final del bloque (cuando vuelve a empezar una sección o un bloque :::)
    if in_code and (stripped.startswith('## ') or stripped.startswith(':::') or stripped.startswith('# ')):
        out.append('```\n\n')
        in_code = False
        
    out.append(line)

if in_code:
    out.append('```\n')

with open('unidades/u2-determinantes/2.1-intuicion-geometrica.qmd', 'w') as f:
    f.writelines(out)

print("✅ Archivo corregido. Los bloques de Python ahora tienen sus fences.")

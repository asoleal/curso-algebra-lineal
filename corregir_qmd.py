#!/usr/bin/env python3
import re

# Leer el archivo
with open('unidades/u2-determinantes/2.1-intuicion-geometrica.qmd', 'r', encoding='utf-8') as f:
    content = f.read()

# Dividir en líneas
lines = content.split('\n')
output = []
in_code = False
code_buffer = []

i = 0
while i < len(lines):
    line = lines[i]
    
    # Detectar inicio de chunk de Python (líneas que empiezan con import o np. o plt.)
    if (line.strip().startswith('import ') or 
        line.strip().startswith('from ') or
        line.strip().startswith('np.') or
        line.strip().startswith('plt.') or
        line.strip().startswith('A = np.array') or
        line.strip().startswith('u, v =') or
        line.strip().startswith('fig, ax =') or
        line.strip().startswith('#| label:')):
        
        # Si no estamos en un chunk, iniciarlo
        if not in_code:
            # Verificar si ya tiene el delimitador
            if not line.strip().startswith('```'):
                output.append('```{python}')
                in_code = True
        
        output.append(line)
        
    # Detectar fin de chunk (línea vacía seguida de texto no-Python o ## o :::)
    elif in_code and (line.strip().startswith('##') or 
                      line.strip().startswith(':::') or
                      (line.strip() == '' and i+1 < len(lines) and 
                       (lines[i+1].strip().startswith('##') or 
                        lines[i+1].strip().startswith(':::')))):
        output.append(line)
        output.append('```')
        in_code = False
        
    else:
        output.append(line)
    
    i += 1

# Cerrar último chunk si quedó abierto
if in_code:
    output.append('```')

# Escribir el archivo corregido
with open('unidades/u2-determinantes/2.1-intuicion-geometrica.qmd', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print("✅ Archivo corregido. Los chunks de Python ahora están correctamente delimitados.")

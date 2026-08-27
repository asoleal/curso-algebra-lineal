import os
import re

# Recorre todas las carpetas y archivos .qmd
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".qmd"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            with open(filepath, 'w', encoding='utf-8') as f:
                for line in lines:
                    # Si la línea empieza con #, ##, ###, etc.
                    if re.match(r'^#+\s+\d+\.\d+', line):
                        # Quita los números y puntos iniciales, deja el título
                        clean_line = re.sub(r'^(#+\s+)(\d+(\.\d+)*\s*)+', r'\1', line)
                        # Quita también el {.unnumbered} si lo tiene
                        clean_line = clean_line.replace(" {.unnumbered}", "")
                        f.write(clean_line)
                    else:
                        f.write(line)

print("✅ ¡Numeraciones manuales eliminadas! Quarto ahora las pondrá automáticamente.")

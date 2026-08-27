import os
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text[:50]

type_map = {
    "definición": "def", "definicion": "def",
    "teorema": "thm", "ejemplo": "exm",
    "proposición": "prp", "proposicion": "prp",
    "lema": "lem", "corolario": "cor"
}

# Patrón para encontrar: **Definición 1.1.1 (Título).** o **Ejemplo 1.2.3.**
pattern = re.compile(r'^\*\*(Definición|Definicion|Teorema|Ejemplo|Proposición|Proposicion|Lema|Corolario)\s+\d+[\.\d]*\s*(?:\((.*?)\))?[\.]?\*\*\s*(.*)$')

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".qmd"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            new_lines = []
            inside_div = False
            inside_code = False
            
            for line in lines:
                # Detectar si entramos o salimos de un bloque de código
                if line.strip().startswith("```"):
                    if inside_code:
                        inside_code = False
                    else:
                        # Si estamos dentro de un div y empieza un código, cerramos el div
                        if inside_div:
                            new_lines.append(":::\n\n")
                            inside_div = False
                        inside_code = True
                    new_lines.append(line)
                    continue
                
                # Si estamos dentro del código, copiamos tal cual sin tocar nada
                if inside_code:
                    new_lines.append(line)
                    continue
                
                match = pattern.match(line)
                
                # Si encontramos un título o nueva definición, cerramos el div anterior
                if inside_div:
                    if line.startswith('#') or line.startswith(':::') or match:
                        new_lines.append(":::\n\n")
                        inside_div = False
                
                if match:
                    elem_type = match.group(1).lower()
                    title = match.group(2) if match.group(2) else elem_type.capitalize()
                    rest_of_line = match.group(3).strip()
                    
                    prefix = type_map.get(elem_type, "def")
                    slug = slugify(title)
                    
                    new_lines.append(f"::: {{{prefix}-{slug}}}\n")
                    new_lines.append(f"### {title}\n")
                    if rest_of_line:
                        new_lines.append(f"\n{rest_of_line}\n")
                    inside_div = True
                else:
                    new_lines.append(line)
            
            if inside_div:
                new_lines.append(":::\n")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)

print("✅ Versión 2: Definiciones convertidas y código Python protegido.")

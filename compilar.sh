#!/bin/bash

echo "🚀 Compilando HTML..."
quarto render --to html

echo "📄 Compilando PDF..."
quarto render --to pdf

echo "✅ Compilación terminada. Abriendo el libro en el navegador..."
xdg-open _book/index.html

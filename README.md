# 📘 Álgebra Lineal con Aplicaciones e Inteligencia Artificial

Repositorio oficial del libro interactivo **Álgebra Lineal con Aplicaciones e Inteligencia Artificial**, diseñado para estudiantes de ingeniería, agronomía, agroindustria y ciencias ambientales, con un fuerte énfasis en la intuición geométrica y las aplicaciones modernas en Machine Learning e IA.

🌐 **Sitio web:** [asoleal.github.io/curso-algebra-lineal](https://asoleal.github.io/curso-algebra-lineal/)

---

## 🎯 Enfoque del Libro

Este material no es un texto de álgebra lineal tradicional. Su "ADN" pedagógico se basa en cuatro pilares:

1. **Intuición Geométrica antes que Álgebra Abstracta:** Cada concepto se visualiza primero en $\mathbb{R}^2$ y $\mathbb{R}^3$ (rectas, planos, transformaciones) antes de generalizar a $n$ dimensiones.
2. **La "Ventana IA":** Cada tema abstracto se conecta directamente con el Machine Learning (ej. neuronas, sobreajuste, regularización, capas densas). No es un apéndice, está integrado en el flujo natural del aprendizaje.
3. **Interactividad Nativa:** El libro se genera en dos formatos simultáneos:
   - **Web (HTML):** Incluye módulos interactivos en HTML/JS (steppers, laboratorios de matrices, quizzes adaptativos con `localStorage`) y gráficos 3D con Plotly.
   - **PDF (Libro impreso):** Incluye fallbacks estáticos con Matplotlib y enlaces a la versión web para los módulos interactivos.
4. **Contextualización por Carrera:** Las aplicaciones (`callout-note`) aterrizan siempre en problemas reales de Agronomía, Agroindustria, Mecatrónica y Ciencias Ambientales.

---

## 📂 Estructura del Repositorio

```text
.
├── _quarto.yml             # Configuración central de Quarto (Web + PDF)
├── index.qmd               # Página de inicio del libro
├── prefacio.qmd            # Prefacio y metodología
├── unidades/               # Contenido principal del libro (.qmd)
│   └── u1-sistemas/        # Unidad 1: Sistemas de ecuaciones y matrices
├── notebooks/              # Notebooks de Jupyter (.ipynb) para Google Colab
├── herramientas/           # Scripts de utilería (ej. renumerar.py)
├── assets/css/             # Estilos personalizados (custom.css)
└── _book/                  # Carpeta de salida generada (ignorada en git)
🛠️ Requisitos Previos
Para compilar el libro localmente necesitas tres componentes principales:

    Quarto: El motor de publicación científica.
    Python 3.10+ y librerías: Para ejecutar los chunks de Jupyter embebidos.
    Tectonic: El motor de LaTeX para generar el PDF de alta calidad.

Instalación en Arch Linux

bash
1
2
3
4
5
6
7
8
9
10

⚙️ Compilación y Visualización
Asegúrate de estar en la raíz del repositorio y de tener tu entorno virtual de Python activado (source venv/bin/activate).
1. Modo Preview (Recomendado para escribir)
Levanta un servidor local con recarga automática. Cada vez que guardes un .qmd, el navegador se actualizará.

bash
1

(Se abrirá automáticamente en http://localhost:4848 o similar).
2. Compilar solo la Web (HTML)
Genera el sitio estático en la carpeta _book/. Es rápido y ideal para verificar interactividad.

bash
1

Para ver el resultado: xdg-open _book/index.html
3. Compilar solo el PDF
Genera el libro completo en PDF usando Tectonic.

bash
1

Para ver el resultado: xdg-open "_book/Álgebra-Lineal-con-Aplicaciones-e-Inteligencia-Artificial.pdf"
4. Compilar Todo (Web + PDF)
Este es el comando que ejecuta el workflow de GitHub Actions al hacer push a main.

bash
1

🚀 Flujo de Trabajo para Nuevas Secciones
Si vas a desarrollar una nueva sección (ej. 2.1-definiciones.qmd), sigue esta anatomía para mantener la coherencia del libro:

    Encabezado: Título y subtítulo.
    Motivación / Intuición: Empieza en 2D/3D antes de la generalización.
    Formalización: Definiciones, teoremas e "Idea de la demostración".
    Ventana IA (::: {.callout-important}): Conecta el tema con ML/IA.
    Módulo Python: Código ejecutable con numpy/matplotlib.
    Módulo Interactivo: Bloque ::: {.content-visible when-format="html"} con HTML/JS, seguido de su fallback ::: {.content-visible when-format="pdf"}.
    Aplicaciones por carrera: Bloques ::: {.callout-note}.
    Ejercicios Adaptativos: Motor de JS con 3 niveles y localStorage.
    Resumen y Glosario: Tabla de términos y callout-tip.

Nota sobre los Gráficos
Para que los gráficos 3D interactivos (Plotly) funcionen en la web pero no rompan el PDF, usa la directiva de Quarto para condicionar el formato:

quarto
1
2
3
4
5
6

🤝 Contribución y Despliegue
El sitio se despliega automáticamente a GitHub Pages cada vez que hay un push a la rama main gracias al workflow ubicado en .github/workflows/publish.yml. 
Si encuentras un error tipográfico, una fórmula mal renderizada o tienes una idea para una nueva "Ventana IA", ¡abre un Issue o envía un Pull Request!
Desarrollado por John Jairo Leal Gómez.

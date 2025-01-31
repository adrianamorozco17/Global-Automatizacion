# 🚀 Proyecto en Python

Este es un proyecto en Python que utiliza un entorno virtual y `pytest` para pruebas automatizadas.

## 📌 Requisitos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior  
- `pip` (gestor de paquetes de Python)  
- `virtualenv` (para crear entornos virtuales)  

Verifica tu instalación ejecutando:

- python3 --version
- pip --version

## 📌 Instalación y configuración
1️⃣ Clonar el repositorio
- git clone https://github.com/tu-usuario/tu-repositorio.git
- cd tu-repositorio

2️⃣ Crear y activar el entorno virtual
- python3 -m venv venv
- source venv/bin/activate  # Para macOS/Linux
- venv\Scripts\activate      # Para Windows

3️⃣ Instalar dependencias
- pip install -r requirements.txt

## 🧪 Ejecución de pruebas
Para ejecutar los tests, usa:
- pytest

## 📂 Estructura del proyecto

📦 tu-repositorio
 ┣ 📂 config
 ┃ ┣ 📜 config.py
 ┣ 📂 tests
 ┃ ┣ 📜 test_consulta_usuario.py
 ┃ ┣ 📜 conftest.py
 ┣ 📜 README.md
 ┣ 📜 requirements.txt

## 🚀 Contribuir
- git pull origin main
- git status
- git add .
- git commit -m "Descripción de los cambios"
- git push origin main
- git pull origin main
# RadioFastAPI

Una aplicación de radios personalizada construida con **FastAPI** (backend) y **Vue.js** (frontend).  
Permite agregar tus emisoras favoritas y reproducirlas desde tu red local.

---

## 📂 Estructura del proyecto
radiofastapi/
├── backend/ # FastAPI (API REST)
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ └── database.py
├── frontend/ # Vue.js (UI)
│ ├── src/
│ └── public/
└── venv/ # Entorno virtual (no subir a Git)


## ⚡ Requisitos

- Python 3.10+  
- Node.js + npm (para frontend)  
- Git (para clonar)  
- Ubuntu / Windows / macOS  

---

## 🛠️ Instalación

### 1. Clonar el proyecto

git clone https://github.com/tuusuario/radiofastapi.git
cd radiofastapi

2. Crear y activar entorno virtual
# Windows (Git Bash / MINGW64)
python -m venv venv
source venv/Scripts/activate

# Windows (CMD)
venv\Scripts\activate

# Ubuntu / Linux / macOS
python3 -m venv venv
source venv/bin/activate

3. Instalar dependencias backend
pip install fastapi uvicorn[standard] sqlalchemy pydantic

🚀 Ejecutar la API FastAPI
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000


🎨 Frontend Vue.js


1. Instalar dependencias
cd frontend
npm install

2. Ejecutar frontend en modo desarrollo
npm run serve


Accede a la UI:
http://localhost:8080

3. Construir para producción
npm run build


Esto genera la carpeta dist/ que puedes servir con Nginx o cualquier servidor estático.

📌 Uso

Abre la UI (http://localhost:8080)

Agrega emisoras con nombre, URL y género

Reproduce la emisora con el botón ▶️

⚠️ Notas

Algunos streams pueden no reproducirse en navegador por CORS o formato de audio.

Para uso personal en la red local no hay problema, para acceso público considera proxy o Icecast.
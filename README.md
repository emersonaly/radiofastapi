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

### 3. Instalar dependencias backend
```bash
pip install -r backend/requirements.txt
```

### 4. Configurar variables de entorno
Crea un archivo `backend/.env` basado en la configuración de tu PostgreSQL:
```ini
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_db
```

### 🚀 Ejecutar la API FastAPI
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```


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

---

## 🗄️ Base de Datos y Migraciones (Alembic)

Este proyecto utiliza **Alembic** para gestionar los cambios en la base de datos PostgreSQL.

### 1. Sincronizar por primera vez (o en un nuevo servidor)
Si acabas de clonar el proyecto o creaste la base de datos:
```bash
cd backend
alembic upgrade head
```

### 2. Agregar o editar campos (Modelos)
Si realizas cambios en `backend/app/db/models.py`:
1. Genera el script de migración automáticamente:
   ```bash
   alembic revision --autogenerate -m "Descripción del cambio"
   ```
2. Revisa el archivo generado en `backend/alembic/versions/`.
3. Aplica los cambios a la base de datos:
   ```bash
   alembic upgrade head
   ```

### 3. Revertir cambios (Eliminar última migración)
Si cometiste un error y quieres volver atrás un paso:
```bash
alembic downgrade -1
```

### 4. Ver estado de las migraciones
Para ver qué versión tiene tu base de datos y cuál es la última disponible:
```bash
alembic history
alembic current
```

---

## ⚠️ Notas

Algunos streams pueden no reproducirse en navegador por CORS o formato de audio.

Para uso personal en la red local no hay problema, para acceso público considera proxy o Icecast.
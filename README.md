# Gestión de Facturas - CRM por Consola

Este proyecto es una aplicación de gestión de usuarios y facturas (tipo CRM) diseñada para ejecutarse desde consola, usando Python y **PostgreSQL** (con Docker).

## 🛠️ Tecnologías utilizadas

- Python 3.12
- PostgreSQL (usando Docker)
- Pytest (para testing)

## ▶️ Cómo ejecutar el sistema

1. Clona el repositorio:
```bash
git clone https://github.com/esscri97/gestion-facturas.git
cd gestion-facturas
```
2. Levanta la base de datos PostgreSQL con Docker:
```bash
docker-compose up -d
```
Esto creará la base de datos y las tablas automáticamente usando el archivo `init.sql`.

3. Crea y activa el entorno virtual:
```bash
python -m venv gestion-facturas
gestion-facturas\Scripts\Activate.ps1
```
4. Instala dependencias:
```bash
pip install -r requirements.txt
```

5. Ejecuta el menú principal:
```bash
python -m scripts.main 
```

## 🧪 Ejecutar tests
```bash
pytest test/
```

## 📋 Autor
Desarrollado por David Escrivá como práctica de gestión de datos y aplicaciones por consola.
# Gestión de Facturas - CRM por Consola

Este proyecto es una aplicación de gestión de usuarios y facturas (tipo CRM) diseñada para ejecutarse desde consola, usando Python y SQLite.

## 🎯 Objetivo

Permitir registrar usuarios, asociarles facturas y obtener reportes relevantes como:

- Búsqueda de usuarios por nombre o email
- Creación de facturas con estado
- Listado de facturas por usuario
- Resumen financiero general del sistema

## 🛠️ Tecnologías utilizadas

- Python 3.12
- SQLite (como base de datos embebida)
- Pytest (para testing)

## 🗃️ Estructura del proyecto
```css
gestion-facturas/
├── src/
│   └── crm/
│       ├── add_user.py
│       ├── add_invoice.py
│       ├── search_user.py
│       ├── show_invoices.py
│       ├── financial_summary.py
│       └── db.py
├── scripts/
│   └── main.py
├── test/
│   ├── test_add_user.py
│   ├── test_search_user.py
│   ├── test_invoice_logic.py
│   ├── test_user_flow.py
│   └── test_financial_summary.py
├── crm.db
├── README.md
├── requirements.txt
└── setup.py
```


## ▶️ Cómo ejecutar el sistema

1. Clona el repositorio:
```bash
git clone https://github.com/esscri97/gestion-facturas.git
cd gestion-facturas
```
2. Activa el entorno virtual.

3. Instala dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecuta el menú principal:
```bash
python -m scripts.main 
```
## 🧪 Ejecutar tests
```bash
pytest test/
```
## 📋 Autor
Desarrollado por David Escrivá como práctica de gestión de datos y aplicaciones por consola.
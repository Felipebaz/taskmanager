# Intelligent Task Manager

Aplicación CLI en Python para gestionar tareas personales. Permite crear, listar, completar y eliminar tareas, y además puede descomponer una tarea compleja en 3-4 subtareas concretas usando la API de OpenAI (modelo `gpt-4o-mini`). Las tareas se persisten localmente en un archivo JSON.

## Características

- Añadir, listar, completar y eliminar tareas.
- Descomponer tareas complejas en subtareas accionables usando IA (OpenAI `gpt-4o-mini`).
- Persistencia automática en `tasks.json` — las tareas se conservan entre sesiones.

## Instalación

**Requisitos:** Python 3.10+

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto con tu clave de OpenAI:

```
OPENAI_API_KEY=sk-...
```

> La clave no se sube al repositorio — `.env` ya está en `.gitignore`.

## Uso

```bash
python main.py
```

Menú interactivo:

```
 -- Intelligent Task Manager --
1. Add Task               → Añadir una tarea nueva
2. Implement Task with AI → Descomponer una tarea en subtareas con IA
3. List Tasks             → Ver todas las tareas
4. Complete Task          → Marcar una tarea como completada
5. Delete Task            → Eliminar una tarea por ID
6. Exit
```

## Estructura del proyecto

```
taskmanager/
├── main.py           # Punto de entrada y menú interactivo
├── task_manager.py   # Clases Task y TaskManager (lógica principal + persistencia)
├── ai_service.py     # Integración con OpenAI para generar subtareas
├── requirements.txt  # Dependencias
├── .env              # API key (no comitear)
└── tests/
    └── test_task_manager.py  # Pruebas unitarias
```

## Tests

```bash
python -m unittest tests.test_task_manager
```

Las pruebas usan un archivo temporal `test_tasks.json` para no interferir con los datos reales.

## Autor

**Felipe Baz**
- GitHub: [github.com/Felipebaz](https://github.com/Felipebaz)
- LinkedIn: [linkedin.com/in/felipe-baz](https://www.linkedin.com/in/felipe-baz/)

## Licencia

MIT

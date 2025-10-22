# Plantilla Python con DevContainers

Este repositorio ofrece una plantilla lista para usar que combina un proyecto basado en [FastAPI](https://fastapi.tiangolo.com/) con la configuración necesaria para ejecutarlo dentro de un [Dev Container](https://containers.dev/). Está pensado como punto de partida para crear APIs modernas en Python manteniendo un entorno de desarrollo reproducible.

## Características principales

- **Python 3.11** con FastAPI y Uvicorn.
- API REST sencilla con dos endpoints:
  - `GET /api/welcome`: devuelve el mensaje de bienvenida actual.
  - `POST /api/welcome`: actualiza el mensaje de bienvenida (requiere un cuerpo JSON con el campo `message`).
- Cobertura de pruebas automatizadas mediante `pytest` y el cliente de pruebas de FastAPI.
- Configuración de Dev Container para trabajar de forma consistente en VS Code o GitHub Codespaces.

## Requisitos previos

- [VS Code](https://code.visualstudio.com/) con la extensión **Dev Containers** o acceso a **GitHub Codespaces**.
- Docker instalado y ejecutándose si se usa VS Code en local.

## Uso del Dev Container

1. Abre el repositorio en VS Code.
2. Cuando se te solicite, selecciona **Reopen in Container** (o usa el comando `Dev Containers: Reopen in Container`).
3. La imagen incluye Python 3.11. Tras la construcción del contenedor se ejecuta `pip install -r requirements.txt` para instalar las dependencias del proyecto.

## Ejecución de la aplicación

Una vez dentro del Dev Container (o en tu entorno local con Python 3.11):

```bash
uvicorn app.main:app --reload --port 8000
```

La API estará disponible en `http://localhost:8000`.

### Ejemplo de peticiones

- Obtener el mensaje actual:

  ```bash
  curl http://localhost:8000/api/welcome
  ```

- Actualizar el mensaje:

  ```bash
  curl -X POST http://localhost:8000/api/welcome \
       -H "Content-Type: application/json" \
       -d '{"message": "Hola desde Dev Containers"}'
  ```

## Pruebas

Ejecuta la suite de pruebas con:

```bash
pytest
```

## Personalización

- Modifica el mensaje de bienvenida por defecto editando `src/app/main.py` (`_message_store`).
- Añade nuevas dependencias en `requirements.txt` según las necesidades de tu proyecto.
- Ajusta la configuración del contenedor en `.devcontainer/devcontainer.json` para incluir herramientas adicionales.

## Licencia

Este proyecto se distribuye bajo la licencia [MIT](LICENSE).

# Plantilla Spring Boot con DevContainers

Este repositorio ofrece una plantilla lista para usar que combina un proyecto Spring Boot con la configuración necesaria para ejecutarlo dentro de un [Dev Container](https://containers.dev/). Está pensado como punto de partida para crear APIs Java modernas manteniendo un entorno de desarrollo reproducible.

## Características principales

- **Spring Boot 3.2** con Java 21 y Maven.
- API REST sencilla con dos endpoints:
  - `GET /api/welcome`: devuelve el mensaje de bienvenida actual.
  - `POST /api/welcome`: actualiza el mensaje de bienvenida (requiere un cuerpo JSON con el campo `message`).
- Cobertura de pruebas automatizadas mediante `MockMvc`.
- Configuración de Dev Container para trabajar de forma consistente en VS Code o GitHub Codespaces.

## Requisitos previos

- [VS Code](https://code.visualstudio.com/) con la extensión **Dev Containers** o acceso a **GitHub Codespaces**.
- Docker instalado y ejecutándose si se usa VS Code en local.

## Uso del Dev Container

1. Abre el repositorio en VS Code.
2. Cuando se te solicite, selecciona **Reopen in Container** (o usa el comando `Dev Containers: Reopen in Container`).
3. La imagen incluye Java 21 y Maven. Tras la construcción del contenedor se ejecuta `mvn dependency:go-offline` para precargar dependencias.

## Ejecución de la aplicación

Una vez dentro del Dev Container (o en tu entorno local con Java 21 y Maven):

```bash
mvn spring-boot:run
```

La API estará disponible en `http://localhost:8080`.

### Ejemplo de peticiones

- Obtener el mensaje actual:

  ```bash
  curl http://localhost:8080/api/welcome
  ```

- Actualizar el mensaje:

  ```bash
  curl -X POST http://localhost:8080/api/welcome \
       -H "Content-Type: application/json" \
       -d '{"message": "Hola desde Dev Containers"}'
  ```

## Pruebas

Ejecuta la suite de pruebas con:

```bash
mvn test
```

## Personalización

- Modifica el mensaje de bienvenida por defecto editando `src/main/resources/application.properties` (`app.welcome-message`).
- Añade nuevas dependencias en `pom.xml` según las necesidades de tu proyecto.
- Ajusta la configuración del contenedor en `.devcontainer/devcontainer.json` para incluir herramientas adicionales.

## Licencia

Este proyecto se distribuye bajo la licencia [MIT](LICENSE).

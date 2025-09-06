# 🚀 Gestor de Tareas (Todo List Full-Stack)

Esta es una aplicación full-stack de lista de tareas (Todo List) construida con un backend en **FastAPI** y un frontend en **Astro**.

---

## 🛠️ Tecnologías Utilizadas

* **Backend**: Python, FastAPI, MongoDB
* **Frontend**: Astro, Tailwind CSS

---

## ⚙️ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

* [Python 3.11+](https://www.python.org/downloads/)
* [Node.js](https://nodejs.org/) (versión LTS recomendada)
* [MongoDB](https://www.mongodb.com/try/download/community) (puedes instalarlo localmente o usar una instancia en la nube como MongoDB Atlas).

---

## 📦 Instalación

Sigue estos pasos para configurar los entornos de backend y frontend.

### Backend (FastAPI)

1.  **Clona el repositorio del backend:**
    ```shell
    git clone <URL_DE_TU_REPOSITORIO_BACKEND>
    cd <nombre-de-la-carpeta-backend>
    ```

2.  **Crea y activa un entorno virtual:**
    * En macOS / Linux:
        ```shell
        python3 -m venv venv
        source venv/bin/activate
        ```
    * En Windows:
        ```shell
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Instala las dependencias de Python:**
    ```shell
    pip install -r requirements.txt
    ```

4.  **Configura las variables de entorno:**
    Crea un archivo llamado `.env` en la raíz de la carpeta del backend y añade las siguientes variables. Este archivo es ignorado por Git para proteger tus credenciales.

    ```env
    # .env
    MONGO_URI="mongodb://localhost:27017/"
    DB_NAME="todo_db"
    NAME_MONGO_COLLECTION="todos"
    ```

### Frontend (Astro)

1.  **Clona el repositorio del frontend:**
    ```shell
    git clone [https://github.com/Mario-Meza/todo_list_frontend](https://github.com/Mario-Meza/todo_list_frontend)
    cd todo_list_frontend
    ```

2.  **Instala las dependencias de Node.js:**
    ```shell
    npm install
    ```
3.  **Configura la URL de la API (si es necesario):**
    El frontend buscará un archivo `.env` para conectar con la API. Crea un archivo `.env` en la raíz del proyecto y añade la siguiente línea:
    ```env
    PUBLIC_API_URL=[http://127.0.0.1:8000](http://127.0.0.1:8000)
    ```

---

## ▶️ Ejecución

Para iniciar los servidores de desarrollo:

* **Para iniciar el Backend:**
    Asegúrate de estar en la carpeta del backend con el entorno virtual activado y ejecuta:
    ```shell
    uvicorn app.main:app --reload
    ```
    El servidor de la API estará disponible en `http://localhost:8000`.

* **Para iniciar el Frontend:**
    En una nueva terminal, navega a la carpeta del frontend y ejecuta:
    ```shell
    npm run dev
    ```
    La aplicación web estará disponible en `http://localhost:4321`.

---

## 📝 Endpoints de la API

La API del backend proporciona los siguientes endpoints para gestionar las tareas:

| Método | Ruta                      | Descripción                      |
| :----- | :------------------------ | :------------------------------- |
| `GET`  | `/api/v1/todo/`           | Obtiene todas las tareas.        |
| `GET`  | `/api/v1/todo/{id}`       | Obtiene una tarea por su ID.     |
| `POST` | `/api/v1/todo/`           | Crea una nueva tarea.            |
| `PUT`  | `/api/v1/todo/{id}`       | Reemplaza una tarea por su ID.   |
| `PATCH`| `/api/v1/todo/{id}`       | Actualiza una tarea parcialmente. |
| `DELETE`| `/api/v1/todo/{id}`      | Elimina una tarea por su ID.     |
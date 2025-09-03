def todo_schema(todo_document) -> dict:
    """
    Convierte un "document" de MongoDB de tipo diccionario a un squema standar de python
    (dict) para usar en la API y devolver al cliente.
    :param todo_document: documento de mongodb que representa una tarea.
    Debe contener las claves:
    "_id", "title","description", "status", "priority" y "due_date".
    :raise ValueError: Si el argumento recibido no es un diccionario.
    :return dict: Diccionario con los campos renombrados y el "_id" convertido en str
    """

    if not isinstance(todo_document, dict):
        raise ValueError(f"Se esperaba un diccionario, pero se recibió: {type(todo_document)}")

    return {
        "id": str(todo_document["_id"]),# convertir el ObjectId en str para JSON
        "title": todo_document["title"],
        "description": todo_document["description"],
        "status": todo_document["status"],
        "priority": todo_document["priority"],
        "due_date": todo_document["due_date"],
    }

def schema_validate(todo_documents) -> list:
    """
    Aplica la conversión de esquema a una lista de documentos de tareas.
    :param todo_documents: Lista de documentos proveniente de MongoDB
    :return: Lista de diccionarios con las tareas formateadas
    """
    return [todo_schema(todo) for todo in todo_documents]
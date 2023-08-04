from models.engine.file_storage import FileStorage

# Crea una única instancia de FileStorage para toda la aplicación
storage = FileStorage()

# Carga las instancias desde el archivo JSON
storage.reload()


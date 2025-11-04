# Examen: Monitoreo del Sistema con Django y Psutil

**Integrantes del grupo:**

- Cristhiam Enrique Colindres Zambrano (202310110255)
- Ricardo Antonio Pineda Méndez (201820110114)

# Descripción del Proyecto

Esta aplicación web desarrollada en Django permite monitorear en tiempo real el estado del sistema utilizando la librería psutil.  
Se muestran datos del CPU, memoria RAM, disco duro y sistema operativo mediante una interfaz.

# Instrucciones para Ejecutar el Proyecto

1. **Clonar o copiar el proyecto**
   git clone https://github.com/tuusuario/monitor.git
   cd monitor

2. **Crear un entorno virtual recomendado**
    python -m venv venv
    venv\Scripts\activate  

3. **Instalar Dependencias**
    pip install -r requirements.txt

4. **Ejecutar el servidor**
    python manage.py runserver

4. **Abrir en el navegador**
    http://127.0.0.1:8000/

# Explicación de los componentes principales

**utils.py  Recolección de datos del sistema**

Contiene las funciones que usan la librería psutil para obtener la información del sistema:

   - Uso del CPU (%): psutil.cpu_percent()
   - Uso de memoria: psutil.virtual_memory()
   - Uso del disco: psutil.disk_usage('/')
   - Información del sistema operativo: platform.system() y platform.release()
   - Número de núcleos: psutil.cpu_count()

**views.py Lógica**

    - index(request): Carga la plantilla principal index.html y pasa la información del sistema al contexto para mostrarla en la interfaz.

    - api_system(request): Devuelve los datos del sistema en formato JSON, permitiendo al frontend actualizar los valores sin recargar la página (usando fetch en JavaScript).

**index.html Interfaz Web**

Muestra los datos del sistema en tarjetas organizadas por categorías (CPU, RAM, Disco, Sistema).

Permite actualizar los datos de forma:

 - Manual: con el botón “Actualizar ahora”.

 - Automática: con intervalo configurable y contador visual.




# Examen-Arquitectura

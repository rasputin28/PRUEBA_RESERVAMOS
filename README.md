# Full Stack Data Engineer Challenge

Este proyecto es una aplicación de Streamlit que permite a los usuarios buscar hospedajes en diferentes ciudades, filtrar los resultados por precio y calificación, y seleccionar amenidades específicas.

## Descripción del Proyecto

La aplicación carga datos de hospedajes desde un archivo CSV, los procesa y los muestra en una interfaz interactiva. Los usuarios pueden buscar una ciudad, filtrar los resultados por precio y calificación, y seleccionar amenidades específicas. Los resultados se pueden ordenar por precio de manera ascendente o descendente.

## Estructura del Proyecto

- `app.py`: Archivo principal que contiene la lógica de la aplicación Streamlit.
- `utils/api.py`: Contiene la función para buscar ciudades utilizando la API de Reservamos.
- `utils/data_processing.py`: Contiene funciones para procesar y formatear los datos de hospedajes.
- `data/rooms_data.csv`: Archivo CSV que contiene los datos de hospedajes.
- `data/logo.svg`: Logo de la aplicación.

## Requisitos

- Python 3.7 o superior
- Streamlit
- Pandas
- Requests

## Instalación

Sigue estos pasos para descargar e instalar el repositorio:

1. Clona el repositorio desde GitHub:

    ```bash
    git clone https://github.com/rasputin28/PRUEBA_RESERVAMOS.git
    cd PRUEBA_RESERVAMOS
    ```

2. Crea un entorno virtual e instala las dependencias:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Ejecuta la aplicación:

    ```bash
    streamlit run app.py
    ```

## Uso

1. Abre la aplicación en tu navegador web. Debería abrirse automáticamente en `http://localhost:8501`.
2. Ingresa el nombre de una ciudad en el campo de texto "¿A dónde quieres ir?".
3. Filtra los resultados utilizando los deslizadores de "Precio por Noche" y "Calificación".
4. Selecciona las amenidades deseadas utilizando las casillas de verificación.
5. Ordena los resultados por precio utilizando el botón "Ordenar por Precio".

## Ejemplo de Uso

1. Ingresa "Monterrey" en el campo de texto.
2. Ajusta el rango de precios y calificaciones según tus preferencias.
3. Selecciona las amenidades que deseas.
4. Haz clic en "Ordenar por Precio" para alternar entre orden ascendente y descendente.

## Notas

- Si no se encuentran resultados para la ciudad especificada, se mostrará un mensaje indicando "No se encontraron resultados para la ciudad especificada".
- Si no se encuentran resultados después de aplicar los filtros, se mostrará un mensaje indicando "No se encontraron resultados".

## Opcional: Conversación con el Asistente

Para permitir que la aplicación converse con el usuario y considere los datos de la aplicación principal, sigue estos pasos:

1. **Preparar el Entorno**:
    - Asegúrate de tener las bibliotecas necesarias instaladas:
        ```bash
        pip install openai
        ```

2. **Configurar la API de OpenAI**:
    - Obtén una clave API de OpenAI y configúrala en tu entorno:
        ```python
        import openai

        openai.api_key = 'tu-clave-api'
        ```

3. **Crear una Función para Generar Respuestas**:
    - Utiliza la API de OpenAI para generar respuestas basadas en los datos filtrados:
        ```python
        def generate_response(prompt):
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        ```

4. **Integrar la Función en la Aplicación**:
    - Añade un campo de texto y un botón en la aplicación Streamlit para generar respuestas:
        ```python
        st.subheader("Conversación con el Asistente")
        conversation_input = st.text_input("¿En qué te puedo ayudar?")
        if conversation_input:
            prompt = f"Genera una respuesta basada en los siguientes datos de hospedajes:\n"
            for index, row in filtered_df.iterrows():
                prompt += f"Hospedaje: {row['Hospedaje']}, Precio por Noche: ${row['Precio por Noche']:.2f}, Calificación: {row['Calificación']}, Amenidades: {row['Amenidades']}\n"
            prompt += f"\nPregunta: {conversation_input}\nRespuesta:"

            response = generate_response(prompt)
            st.write(response)
        ```

5. **Ejecutar la Aplicación**:
    - Ejecuta la aplicación Streamlit y utiliza el campo de texto y el botón para obtener respuestas generadas automáticamente basadas en los datos filtrados.

    ## Uso de IA en el Desarrollo

    Durante el desarrollo de este proyecto, utilicé herramientas de inteligencia artificial para depurar algunos problemas menores y acelerar el proceso de codificación. En particular, empleé GitHub Copilot para obtener sugerencias de código y soluciones rápidas a problemas comunes. Esto me permitió enfocarme en la lógica principal de la aplicación y mejorar la eficiencia del desarrollo.

    Especialmente la utilicé para solucionar problemas triviales de sintáxis en app.py ya que no estoy completamente familairizado con streamlit. 

    El código de app.py considero que se podría refactorizar aún más especialmente en lo que corresponde al preprocesamiento de datos, solo que por tiempo no lo pude realizar.
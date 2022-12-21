# VALIDADOR_MODELO_SERIAL
Este código utiliza la librería Selenium para automatizar la interacción con un navegador web. Utiliza una opción de Chrome para excluir algunos interruptores, luego inicia una instancia de Chrome y navega a una página web específica. Luego, carga un libro de trabajo de Excel con la función load_workbook y obtiene una hoja de cálculo en particular llamada "Hoja1".

A continuación, se itera sobre un rango de valores y se obtienen los valores de ciertas celdas de la hoja de cálculo. Luego, se utiliza Selenium para encontrar un elemento en la página web por su nombre y escribir un valor en él. Después de eso, se utilizan dos expresiones xpath para encontrar otros elementos en la página y extraer su contenido.

Luego, se escribe una línea con los valores obtenidos en un archivo de texto llamado "EXPORTADO_INICIO_GARANTIA.TXT" y se imprime en la consola. Después de eso, se vuelve a cargar la página web inicial y se repite el proceso. Al final del bucle, se cierra el navegador y se escribe un archivo de texto llamado "EXPORTADO.TXT" con todas las líneas escritas durante el bucle.

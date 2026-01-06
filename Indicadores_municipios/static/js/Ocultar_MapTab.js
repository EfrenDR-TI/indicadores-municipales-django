function MostrarOcultarTablasMapas(accion) {
    // Almacena los elementos de la tabla, el mapa y la gráfica en variables
    const tabla = document.getElementById('OcultarMostrarTabla');
    const mapa = document.getElementById('OcultarMostrarMapa');
    const grafica = document.getElementById('OcultarMostrarGrafica');
    // Almacena los botones en una lista
    const botones = document.querySelectorAll("#tablaButton, #mapaButton, #graficaButton");
    // Almacena los elementos de selección en variables (nivel e indicador)
    const nivel = document.getElementById("nivel");
    const indicador = document.getElementById("indicador");
    // Verifica si los elementos existen antes de acceder a sus propiedades
    if (!tabla || !mapa || !grafica || !nivel || !indicador) {
        console.error("No se encuentran los elementos"); // Registra un error si alguno de los elementos no se encuentra
        return; // Sale de la función si algún elemento no está disponible
    }
    // Evalúa la acción recibida como parámetro
    switch (accion) {
        case 'OcultarMostrarTabla':
            // Muestra la tabla y oculta el mapa y la gráfica
            tabla.style.display = 'block';
            mapa.style.display = 'none';
            grafica.style.display = 'none';
            break;
        case 'OcultarMostrarMapa':
            // Muestra el mapa y oculta la tabla y la gráfica
            mapa.style.display = 'block';
            tabla.style.display = 'none';
            grafica.style.display = 'none';
            break;
        case 'OcultarMostrarGrafica':
            // Muestra la gráfica y oculta la tabla y el mapa
            grafica.style.display = 'block';
            tabla.style.display = 'none';
            mapa.style.display = 'none';
            break;
        case 'TipoBusquedaIndicador':
            // Verifica si el nivel y indicador, están seleccionados
            if (nivel.value && indicador.value) {
                // Habilita los botones si ambos están seleccionados
                botones.forEach(boton => {
                    boton.disabled = false;
                });
            } else {
                // Deshabilita los botones si no se han seleccionado ambos
                botones.forEach(boton => {
                    boton.disabled = true;
                });
            }
            break;
    }
}
// Espera a que el contenido del DOM se haya cargado completamente
document.addEventListener("DOMContentLoaded", () => {
    // Almacena los elementos de selección (nivel e indicador)
    const nivel = document.getElementById("nivel");
    const indicador = document.getElementById("indicador");
    // Almacena los botones en una lista
    const botones = document.querySelectorAll("#tablaButton, #mapaButton, #graficaButton");
    // Agrega eventos 'change' a los elementos de selección para verificar cuando se cambian
    [nivel, indicador].forEach(select => {
        select.addEventListener("change", () => {
            // Llama a la función MostrarOcultarTablasMapas para evaluar si habilitar los botones
            MostrarOcultarTablasMapas('TipoBusquedaIndicador');
        });
    });
    // Deshabilita los botones al cargar la página
    botones.forEach(boton => {
        boton.disabled = true;
    });
    // Llama a la función MostrarOcultarTablasMapas para establecer el estado correcto de los botones
    // al cargar la página
    MostrarOcultarTablasMapas('TipoBusquedaIndicador');
});

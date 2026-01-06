    // Elementos del DOM
    const rowsPerPageSelect = document.getElementById('rowsPerPage'); // Selector de filas por página
    const searchInput = document.getElementById('searchInput'); // Campo de búsqueda
    const tableBody = document.getElementById('tableBody'); // Cuerpo de la tabla donde se mostrarán las filas
    const paginationContainer = document.getElementById('pagination'); // Contenedor para la paginación
    const allRows = Array.from(tableBody.querySelectorAll('tr')); // Guardar todas las filas iniciales de la tabla

    let currentPage = 1; // Página actual

    // Función para renderizar la tabla con paginación
    function renderTable(rowsPerPage, page = 1) {
        const searchTerm = searchInput.value.toLowerCase(); // Obtener el término de búsqueda
        const filteredRows = allRows.filter(row => {
            const rowText = row.textContent.toLowerCase(); // Obtener el texto de la fila en minúsculas
            return searchTerm === '' || rowText.includes(searchTerm); // Filtrar las filas según el término de búsqueda
        });

        const totalRows = filteredRows.length; // Número total de filas después del filtro
        const totalPages = Math.ceil(totalRows / rowsPerPage); // Calcular el número total de páginas
        const start = (page - 1) * rowsPerPage; // Índice de la primera fila a mostrar en la página actual
        const end = start + rowsPerPage; // Índice de la última fila a mostrar en la página actual

        tableBody.innerHTML = ''; // Limpiar la tabla
        filteredRows.slice(start, end).forEach(row => {
            tableBody.appendChild(row.cloneNode(true)); // Añadir las filas filtradas a la tabla
        });

        renderPagination(totalPages, page); // Renderizar el paginador
    }

    // Función para renderizar el paginador
    function renderPagination(totalPages, currentPage) {
        paginationContainer.innerHTML = ''; // Limpiar el paginador

        // Función para crear un elemento de la paginación
        const createPageItem = (text, page, isDisabled = false, isActive = false) => {
            const li = document.createElement('li');
            li.className = `page-item${isDisabled ? ' disabled' : ''}${isActive ? ' active' : ''}`;

            const a = document.createElement('a');
            a.className = 'page-link';
            a.href = '#';
            a.textContent = text;

            // Añadir evento de click para cambiar de página
            if (!isDisabled) {
                a.addEventListener('click', (e) => {
                    e.preventDefault(); // Evitar el comportamiento por defecto del enlace
                    if (page !== currentPage) {
                        renderTable(parseInt(rowsPerPageSelect.value, 10), page); // Renderizar la tabla para la nueva página
                    }
                });
            }

            li.appendChild(a);
            return li;
        };

        // Añadir el botón "Anterior" al paginador
        paginationContainer.appendChild(createPageItem('Anterior', currentPage - 1, currentPage === 1));

        // Añadir los botones de número de página al paginador
        for (let i = 1; i <= totalPages; i++) {
            paginationContainer.appendChild(createPageItem(i, i, false, i === currentPage));
        }

        // Añadir el botón "Siguiente" al paginador
        paginationContainer.appendChild(createPageItem('Siguiente', currentPage + 1, currentPage === totalPages));
    }

    // Manejar cambios en el selector de filas por página
    rowsPerPageSelect.addEventListener('change', () => {
        currentPage = 1; // Reiniciar a la primera página
        renderTable(parseInt(rowsPerPageSelect.value, 10), currentPage); // Renderizar la tabla con las nuevas filas por página
    });

    // Manejar cambios en la barra de búsqueda
    searchInput.addEventListener('input', () => {
        currentPage = 1; // Reiniciar a la primera página
        renderTable(parseInt(rowsPerPageSelect.value, 10), currentPage); // Renderizar la tabla con el término de búsqueda
    });

    // Inicializar la tabla con el valor por defecto del selector de filas por página
    renderTable(parseInt(rowsPerPageSelect.value, 10), currentPage);


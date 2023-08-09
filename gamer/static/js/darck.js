    function toggleDarkMode() {
      document.body.classList.toggle('dark-mode');
    }


    const toggleButton = document.getElementById('toggleButton');
    const body = document.body;

    toggleButton.addEventListener('click', function() {
        body.classList.toggle('dark-mode');
        if (body.classList.contains('dark-mode')) {
            toggleButton.textContent = 'Cambiar a modo claro';
        } else {
            toggleButton.textContent = 'Cambiar a modo oscuro';
        }
    });

        // Comprueba si hay una preferencia guardada
    if (localStorage.getItem('dark-mode') === 'true') {
        body.classList.add('dark-mode');
        toggleButton.textContent = 'Cambiar a modo claro';
    }

    // Actualiza la preferencia cuando se hace clic en el botón
    toggleButton.addEventListener('click', function() {
        localStorage.setItem('dark-mode', body.classList.contains('dark-mode'));
    });
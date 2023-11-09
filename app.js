const express = require('express');
const app = express();
const path = require('path');  // Añade esta línea para trabajar con rutas de archivos

// Configurar la ubicación de tus archivos HTML
app.use(express.static(path.join(__dirname, 'templates')));

// Definir una ruta para "/ver_mapa"
app.get('/ver_mapa', (req, res) => {
    // En esta función, puedes renderizar la plantilla HTML que contiene el mapa
    // Reemplaza esta parte con la lógica adecuada para tu aplicación
    res.sendFile(path.join(__dirname, 'templates', 'map.html'));
});

// Configurar el puerto en el que escuchará el servidor (cambiado a 5500)
const port = process.env.PORT || 5500;

// Iniciar el servidor
app.listen(port, () => {
    console.log(`Servidor en funcionamiento en el puerto ${port}`);
});
node [app.js]


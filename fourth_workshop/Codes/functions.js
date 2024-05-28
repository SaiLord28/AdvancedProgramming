async function callMessage() {
    try {
        const response = await fetch('http://localhost:8000/hello_ud'); // Updated: Fetching from 'http://localhost:8000/hello_ud'
        const data = await response.text();
        document.getElementById('result').innerHTML = data; // Updated: Setting innerHTML instead of textContent
    } catch (error) {
        console.error('Error en la solicitud a hello_ud:', error);
        document.getElementById('result').innerHTML = 'Error al cargar el mensaje'; // Updated: Displaying error message
    }
}

async function callWebService() {
    try {
        const response = await fetch('http://localhost:8000/products'); // Updated: Fetching from 'http://localhost:8000/products'
        if (!response.ok) {
            throw new Error(`Error ${response.status}: ${response.statusText}`);
        }
        try {
            const data = await response.json();
            let table = '<table>';
            table += '<tr><th>ID</th><th>Name</th><th>Description</th></tr>';
            data.forEach(item => {
                table += `<tr><td>${item.id}</td><td>${item.name}</td><td>${item.description}</td></tr>`;
            });
            table += '</table>';
            document.getElementById('result').innerHTML = table;
        } catch (error) {
            console.error('Error al parsear la respuesta como JSON:', error);
            document.getElementById('result').innerHTML = 'Error al cargar los productos'; // Updated: Displaying error message
        }
    } catch (error) {
        console.error('Error en la solicitud a products:', error);
        document.getElementById('result').innerHTML = 'Error al cargar los productos'; // Updated: Displaying error message
    }
}
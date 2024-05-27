async function callMessage() {
    try {
        const response = await fetch('http://localhost:8000/hello_ud');
        const data = await response.text();
        document.getElementById('result').innerHTML = data; // Modificamos para usar innerHTML en lugar de textContent
    } catch (error) {
        console.error('Error:', error);
    }
}

async function callWebService() {
    try {
        const response = await fetch('http://localhost:8000/products');
        const data = await response.json();
        
        let table = '<table>';
        table += '<tr><th>ID</th><th>Name</th><th>Description</th></tr>';
        
        data.forEach(item => {
            table += `<tr><td>${item.id}</td><td>${item.name}</td><td>${item.description}</td></tr>`;
        });
        
        table += '</table>';
        
        document.getElementById('result').innerHTML = table;
    } catch (error) {
        console.error('Error:', error);
    }
}

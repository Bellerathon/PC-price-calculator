function handleChange(value, id) {
    if (value.length > 2) {
        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
                'Access-Control-Max-Age': 1000,
                'Access-Control-Allow-Headers': 'origin, x-csrftoken, content-type, accept',
            },
            body: JSON.stringify({ 'query': value })
        };
        fetch('http://127.0.0.1:3000/CPU', requestOptions)
            .then(response => response.json())
            .then(res => {
                console.log(res)
            });
    }
}

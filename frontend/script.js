const handleChange = (value, id) => {
    if (value.length > 2) {
        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
                'Access-Control-Max-Age': 1000,
                'Access-Control-Allow-Headers': 'origin, x-csrftoken, content-type, accept',
            },
            body: JSON.stringify({ 'part': id, 'name': value })
        };
        fetch('http://127.0.0.1:3000/searchPart', requestOptions)
            .then(response => response.json())
            .then(res => {
                document.getElementById(id.concat('-search-results')).innerHTML = '';
                generateSearchResults(res, id);
            });
    }
}

const searchResultItem = (text) => {
    const searchItem = document.createElement('div');
    searchItem.className = 'search-result-item';
    searchItem.innerText = text;
    return searchItem;
}

const generateSearchResults = (results, id) => {
    const searchResults = document.getElementById(id.concat('-search-results'));
    results.forEach(element => {
        searchResults.appendChild(searchResultItem(element));
    });
}

const elements = document.querySelectorAll('input[type="search"]');
for (let i = 0; i < elements.length; i++) {
    const element = document.getElementById(elements[i].id);
    element.addEventListener('focus', () => {
        document.getElementById(element.id.concat("-search-results")).style.display = 'block';
    });
    element.addEventListener('blur', () => {
        document.getElementById(element.id.concat("-search-results")).style.display = 'none';
    });
    element.addEventListener('input', () => {
        if (element.value === '') {
            document.getElementById(element.id.concat("-search-results")).style.display = 'none';
        }
    });
};
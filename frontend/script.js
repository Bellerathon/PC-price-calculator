// Debounce function from: https://stackoverflow.com/q/24004791/1814486
const debounce = (func, wait, immediate) => {
    let timeout
    return function () {
        const context = this, args = arguments
        const later = function () {
            timeout = null
            if (!immediate) func.apply(context, args)
        }

        const callNow = immediate && !timeout
        clearTimeout(timeout)
        timeout = setTimeout(later, wait)
        if (callNow) func.apply(context, args)
    }
}

let myInputs = document.querySelectorAll('input[type=search]');
for (let i = 0; i < myInputs.length; i++) {
    const element = document.getElementById(myInputs[i].id);
    element.addEventListener('keyup', debounce(() => {
        searchPart(element.value, element.id)
    }, 500));
}

const searchPart = (value, id) => {
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

const searchPartPrice = (name) => {
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
            'Access-Control-Max-Age': 1000,
            'Access-Control-Allow-Headers': 'origin, x-csrftoken, content-type, accept',
        },
        body: JSON.stringify({ 'part': name })
    };
    fetch('http://127.0.0.1:3000/searchPartPrice', requestOptions)
        .then(response => response.json())
        .then(res => {
            console.log(res)
        });
}

const searchResultItem = (text, id) => {
    const searchItem = document.createElement('div');
    searchItem.className = 'search-result-item';
    searchItem.innerText = text;
    searchItem.addEventListener('click', () => {
        document.getElementById(id).value = text;
        searchPartPrice(text);
        document.getElementById(id.concat('-search-results')).style.display = 'none';
    })
    return searchItem;
}

const generateSearchResults = (results, id) => {
    const searchResults = document.getElementById(id.concat('-search-results'));
    results.forEach(element => {
        searchResults.appendChild(searchResultItem(element, id));
    });
}

const elements = document.querySelectorAll('input[type=search]');
for (let i = 0; i < elements.length; i++) {
    const element = document.getElementById(elements[i].id);
    element.addEventListener('focus', () => {
        document.getElementById(element.id.concat('-search-results')).style.display = 'block';
    });
    element.addEventListener('blur', () => {
        setTimeout(() => {
            document.getElementById(element.id.concat('-search-results')).style.display = 'none';
        }, 70);
    });
    element.addEventListener('input', () => {
        if (element.value === '') {
            document.getElementById(element.id.concat('-search-results')).style.display = 'none';
        }
    });
};
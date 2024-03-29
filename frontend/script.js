window.onload = () => {
    document.getElementById("defaultOpen").click();

    const elements = document.querySelectorAll('.part-input');
    for (let i = 0; i < elements.length; i++) {
        console.log(elements[i].id)
        elements[i].addEventListener('focus', () => {
            document.getElementById(elements[i].id.concat('-search-results')).style.display = 'block';
        });
        elements[i].addEventListener('blur', () => {
            setTimeout(() => {
                document.getElementById(elements[i].id.concat('-search-results')).style.display = 'none';
            }, 100);
        });
        elements[i].addEventListener('input', () => {
            if (elements[i].value === '') {
                document.getElementById(elements[i].id.concat('-search-results')).style.display = 'none';
            }
        });
        elements[i].addEventListener('keyup', debounce(() => {
            searchPart(elements[i].value, elements[i].id)
        }, 500));
    };

}

const openTab = (evt, tabName) => {
    let i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

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

const searchPart = (value, id) => {
    console.log(value, id);
    const requestOptions = {
        method: 'POST',
        mode: 'cors',
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

const searchPartPrice = (name, id) => {
    const requestOptions = {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
            'Access-Control-Max-Age': 1000,
            'Access-Control-Allow-Headers': 'origin, x-csrftoken, content-type, accept',
        },
        body: JSON.stringify({ 'part': id, 'name': name })
    };
    fetch('http://127.0.0.1:3000/searchPartPrice', requestOptions)
        .then(response => response.json())
        .then(res => {
            boxplotchart(res, id);
            scatterplotchart(res, id);
        });
}

const searchResultItem = (text, id) => {
    const searchItem = document.createElement('div');
    searchItem.className = 'search-result-item';
    searchItem.innerText = text;
    searchItem.addEventListener('click', () => {
        console.log(id)
        document.getElementById(id).value = text;
        searchPartPrice(text, id);
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

const indexInClass = (id) => {
    let myClass = document.querySelectorAll('.part-input');
    var num = 0;
    for (var i = 0; i < myClass.length; i++) {
        if (myClass[i].id === id) {
            return num;
        }
        num++;
    }
    return 0;
}

const boxplotchart = (prices, id) => {
    let colours = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)', 'rgba(255, 65, 54, 0.5)', 'rgba(207, 114, 255, 0.5)', 'rgba(127, 96, 0, 0.5)', 'rgba(255, 140, 184, 0.5)', 'rgba(79, 90, 117, 0.5)', 'rgba(222, 223, 0, 0.5)', 'rgb(0,128,128)', 'rgb(214,12,140)', 'rgb(10,140,208)'];
    var trace3 = {
        type: 'box',
        boxpoints: 'all',
        x: prices,
        jitter: 0.5,
        whiskerwidth: 0.5,
        fillcolor: colours[indexInClass(id)],
        marker: {
            size: 5,
            color: 'white'
        },
        line: {
            width: 1
        },
        hoverinfo: 'x',
    };

    var data = [trace3];

    var layout = {
        autosize: true,
        height: 100,
        width: 700,
        tooltip: false,
        hovermode: "x",
        yaxis: {
            visible: false,
        },
        xaxis: {
            tickfont: {
                color: 'white',
            }
        },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        margin: {
            l: 0,
            r: 0,
            t: 28,
            b: 28,
        }
    };

    Plotly.newPlot(id.concat('-boxplot'), data, layout);
}

const scatterplotchart = (prices, id) => {
    var data = [
        {
            x: prices,
            y: dates,
            type: 'scatter'
        }
    ];

    Plotly.newPlot(id.concat('-scatterplot'), data);
}
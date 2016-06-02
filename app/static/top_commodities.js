google.charts.load('current', {'packages':['geochart','corechart','bar']});

google.charts.setOnLoadCallback(drawRegionsMap);
google.charts.setOnLoadCallback(drawBarGraph);
google.charts.setOnLoadCallback(drawPieChart);


function drawRegionsMap() {

    var parsed_data = JSON.parse(document.getElementById('embedded_posts').innerHTML);

    var data = google.visualization.arrayToDataTable(parsed_data);

    var options = {
        colors: ['#948979', '#438F3D'],
        width: '100%',
        backgroundColor: '#2a2a2a',
        datalessRegionColor: '#B2BEB5',
    };

    var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

    chart.draw(data, options);
}

function drawBarGraph() {

    var parsed_data = JSON.parse(document.getElementById('embedded_posts').innerHTML);
    var data = google.visualization.arrayToDataTable(parsed_data);

    crop = document.getElementById('chart_div').innerHTML
    console.log(crop)
    length = parsed_data.length
    console.log(length)
    var options = {
        title:crop,
        titleTextStyle:{color: '#fff'},
        backgroundColor: '#2a2a2a',
        colors:['#438F3D', '#438F3D'],
        height: (length * 20),
        fontSize: 14,
        chartArea:{
            height:'95%'
        },
        axes: {
            x: {
                0: { side: 'top', label: 'Tonnes'}
            }
        },
        hAxis: {
            title: 'Tonnes',
            titleTextStyle:{color: '#fff'},
            textStyle:{color: '#fff'},
            gridlines: {color: 'fff'}
        },
        vAxis: {
            title: 'Country',
            titleTextStyle:{color: '#fff'},
            textStyle:{color: '#fff'}
        },
        bar: { groupWidth: "40%" },
        legend: { position: "none" }
    };

    var chart = new google.visualization.BarChart(document.getElementById('chart_div'));

    chart.draw(data, options);
}

function drawPieChart() {

    var parsed_data = JSON.parse(document.getElementById('embedded_posts').innerHTML);

    var data = google.visualization.arrayToDataTable(parsed_data);

    var options = {
        title: crop,
        titleTextStyle:{color: '#fff'},
        backgroundColor: '#2a2a2a',
        width: '100%',
        legend: {
            textStyle:{color: '#fff'}
        }
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));

    chart.draw(data, options);
    }

google.charts.load('current', {'packages':['geochart']});
google.charts.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {

    var parsed_data = JSON.parse(document.getElementById('embedded_posts').innerHTML);
    console.log(parsed_data);

    var data = google.visualization.arrayToDataTable(parsed_data);

    var options = {
        colors: ['#948979', '#438F3D'],
        width: 1200,
        height: 800,
        backgroundColor: '#2a2a2a',
        datalessRegionColor: '#B2BEB5',
        displayMode: 'auto',
        title: 'Crop Production',
        magnifyingGlass: true
    };

    var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

    chart.draw(data, options);
}

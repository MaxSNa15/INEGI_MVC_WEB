document.addEventListener("DOMContentLoaded", function() {
    var dataElement = document.getElementById('chart-data');
    var dataString = dataElement.getAttribute('data-municipalities');
    var data = JSON.parse(dataString);

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'Municipios',
                data: data.population,
                backgroundColor: [
                    '#FF6384',
                    '#36A2EB',
                    '#FFCE56',
                    '#FF6384',
                    '#FFA500',
                ],
                borderColor: [
                    
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Población por Municipio'
            },
            animation: {
                animateScale: true,
                animateRotate: true
            }
        }
    });
});
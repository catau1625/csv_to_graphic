var fechas = datos.header;
var menor39 = datos.body;
var mayor40 = datos.body;
var ctx = document.getElementById('myChart')
var myChart = new Chart(ctx, {
    type: 'bar',
    data:{
        labels: [20, 10],
        datasets: [{
            data: [20, 10],
            label: "Menor de 39",
            backgroundColor: '#0D47A1',
            borderColor: ['black'],
            borderWidth: 1
        }]
    }
});
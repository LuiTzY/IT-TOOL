function fetchOsCounts() {
  //url para hacer la soli
  let url = "http://localhost:8000/counts";

  fetch(url)
    .then(response => response.json())
    .then(servers_counts => {
      // colocamo los nuevos valores pa el grafico
      option.series[0].data[0].value = servers_counts.servers_type.Linux;
      option.series[0].data[1].value = servers_counts.servers_type.Windows;

    })
    .catch(err => {
      console.log("No se pudo obtener la data", err);
    });
}

var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);

var option = {
  tooltip: {
    trigger: 'item'
  },
  legend: {
    top: '5%',
    left: 'center'
  },
  series: [
    {
      name: 'Servidores',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      itemStyle: {
        borderRadius: 10,
        borderColor: '#fff',
        borderWidth: 2
      },
      label: {
        show: false,
        position: 'center'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: 40,
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: false
      },
      data: [
        { value: 0, name: 'Linux' },
        { value: 0, name: 'Windows' }
      ]
    }
  ]
};

// Ejecuta la función para obtener los datos y renderizar el gráfico
fetchOsCounts();
myChart.setOption(option);

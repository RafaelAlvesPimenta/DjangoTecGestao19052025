const ctx = document.getElementById('myChart');
const grosca = document.getElementById('myChart-rosca');



ctx.style.backgroundColor = 'rgba(228, 228, 228, 0)'; 
ctx.style.borderColor = 'rgb(128, 128, 128)'; 

grosca.style.backgroundColor = 'rgba(10, 10, 10, 1)';
grosca.style.borderRadius = '100%';

new Chart (grosca, {
  type: 'doughnut',
  data:{
    labels: [
      'Meta Mensal'
    ],
    datasets: [{
      label: '',
      data: [30, 70],
      backgroundColor: [
        'rgba(255, 0, 0)',
        'rgba(0, 0, 0, 50)'

      ],
      borderWidth: 0,
    }]
  },
  options:{
    responsive: false,
    plugins:{
      legend: {
        display: false,
        position:'bottom'
      }
    },
    cutout: '93%'
  }
});

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Meta-diaria', 'Eficiência da Produção', 'Capacidade de Estoque', 'Margem de Lucro'],
      datasets: [{
        label: '',
        data: [40, 100, 30, 50],
        backgroundColor: [ 
            'rgb(0, 51, 102)'
        ],
        borderWidth: 1
      }]
      
    },
    options: {
        responsive: true, 
        layout: {
            padding: {
                left:0
            }
        },
        plugins: {
            legend: {
                display: false
            }
        },
    indexAxis: 'y',
      scales: {
        x: {
            beginAtZero: true,
            max: 100,
            ticks: {
              callback: function(value) {
                return value + '%'; 
              }
            }
        },
        y: {
          beginAtZero: true,
        }
      }
    }
  });

  let Receita_diarias = 280;
  let new_client = 20;
  let peding_orders = 5;
  let peding_progress = 7;

  const receita_diaria = document.getElementById('Receita-diaria')
  const novo_cliente = document.getElementById('new-Client')
  const peding__orders = document.getElementById('peding-orders')
  const peding__progress = document.getElementById('peding-progress')


  document.addEventListener('DOMContentLoaded', function() {
    receita_diaria.innerText = `R$${Receita_diarias}`;
    novo_cliente.innerText = `${new_client}`;
    peding__orders.innerText = `${peding_orders}`;
    peding__progress.innerText = `${peding_progress}`;
});
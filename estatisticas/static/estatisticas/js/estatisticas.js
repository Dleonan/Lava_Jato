// estatisticas/static/estatisticas/js/estatisticas.js
window.onload = function() {
    function initChart(canvasId, chartData) {
      const ctx = document.getElementById(canvasId).getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              // ativa um pequeno offset nas extremidades
              offset: true,
  
              // empurra levemente para a direita (menos do que antes)
              min: -0.3,
  
              // controla a largura das barras em relação ao espaço de cada categoria
              categoryPercentage: 0.5,
              barPercentage: 0.8
            },
            y: {
              beginAtZero: true
            }
          },
          plugins: {
            legend: {
              position: 'top'
            }
          }
        }
      });
    }
  
    if (window.graficoDiarioData) {
      initChart('grafico_diario', graficoDiarioData);
    }
    if (window.graficoMensalData) {
      initChart('grafico_mensal', graficoMensalData);
    }
  };
  
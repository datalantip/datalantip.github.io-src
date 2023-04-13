Title: Minat Belanja Buah Merosot 0.57% Hingga Pasca Pandemi
Date: 2022-06-13 11:20
Category: Jawa Tengah
Slug: pengeluaran-buah-sebulan
Tags: consumer behavoiur,spending,fruits
Authors: Faris Priadi

<script src="https://cdn.jsdelivr.net/npm/chart.js@3.0.0/dist/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.0.0"></script>
<div id='chart-box' style="padding-top: 50px; padding-bottom: 100px;">
	<canvas id="myChart" width="400" height="100"></canvas>
</div>
<script>
Chart.register(ChartDataLabels);
const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [
						"2018",
						
						"2019",
						
						"2020",
						
						"2021",
						],
        datasets: [{
            label: '',
            data: [
						2.87,
						
						2.75,
						
						2.47,
						
						2.3,
						],
            backgroundColor: [
                'rgba(237, 144, 57, 1)',
                'rgba(237, 144, 57, 1)',
                'rgba(237, 144, 57, 1)',
                'rgba(237, 144, 57, 1)',
            ],
            borderColor: 'rgba(237, 144, 57, 1)',
            datalabels: {
	        	color: 'rgba(237, 144, 57, 1)',
	        	align: 'end',
    			anchor: 'end',
    			color: function(context) {
		          return context.dataset.backgroundColor;
		        },
		        font: function(context) {
		          var w = context.chart.width;
		          return {
		            size: 15,
		            weight: 'bold',
		          };
		        },
      		}
        }],
        
    },
    options: {
    	responsive: true,
    	plugins:  {
	      datalabels: {
	        color: 'optionsrange',
	        padding: 5
	      },
	      legend : {
	      	display: false,
	      }
	    },
	    // Core options
	    aspectRatio: 4 / 1,
	    layout: {
	      padding: {
	        top: 32,
	        right: 20,
	        bottom: 8,
	        left: 20
	      }
	    },
        scales: {
            y: {
                // beginAtZero: true,
                display : false,
                ticks : {
                	stepSize: 0.01

	            },
            },
            x: {
            	grid: {display: false, drawBorder: false},

            }

        }

    }
});
</script>


	    
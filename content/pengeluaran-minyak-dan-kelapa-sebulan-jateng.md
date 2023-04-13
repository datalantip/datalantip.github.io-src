Title: Pasca Pandemi Belanja Minyak dan Kelapa Meningkat 15% dari Tahun 2020
Date: 2022-06-19 10:20
Category: Jawa Tengah
Slug: pengeluaran-minyak-kelapa-sebulan
Tags: consumer behavoiur,spending,oil,coconut
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
        datasets: [ 
        {
            label: '',
            data: [
						1.29,
						
						1.22,
						
						1.21,
						],
            backgroundColor: [
                'grey',
                'grey',
                'rgba(54, 162, 235, 1)',
            ],
            borderColor: 'grey',
            datalabels: {
	        	color: 'grey',
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
        },
        {
            label: '',
            data: [
						1.29,
						
						1.22,
						
						1.21,
						
						1.4,
						],
            backgroundColor: [
            	'grey',
                'grey',
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
            ],
            borderColor: 'rgba(54, 162, 235, 1)',
            datalabels: {
	        	color: 'rgba(54, 162, 235, 1)',
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
	    
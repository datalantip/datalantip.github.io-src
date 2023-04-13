Title: Pemalang Menjadi Kabupaten Dengan Populasi Kerbau Terbesar Yaitu 8251 Ekor
Date: 2022-06-25 10:20
Category: Jawa Tengah
Slug: populasi-kerbau-terbesar-jateng
Tags: livestock, buffalo
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
    type: 'bar',
    data: {
		  labels: [
						"Kabupaten Pemalang",
						
						"Kabupaten Brebes",
						
						"Kabupaten Magelang",
						
						"Kabupaten Tegal",
						
						"Kabupaten Demak",
						],
        datasets: [ 
        {
            label: '',
            data: [
						8251.0,
						
						7365.0,
						
						5811.0,
						
						4150.0,
						
						3170.0,
						],
            backgroundColor: [
            	'rgba(54, 162, 235, 1)',
            	'grey',
                'grey',
                'grey',
                'grey',
                
            ],
            borderColor: [
            	'rgba(54, 162, 235, 1)',
            	'grey',
                'grey',
                'grey',
                'grey',
                
            ],
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
		            // size: 15,
		            weight: 'bold',
		          };
		        },
		        formatter: function(value, context) {
          			return value + ' ekor';
        		},
      		}
		}]
},
options: {
    	responsive: true,
    	plugins:  {
	      datalabels: {
	        color: 'optionsrange',
	        // padding: 5
	      },
	      legend : {
	      	display: false,
	      }
	    },
	    // Core options
	    aspectRatio: 5 / 3,
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
                display : false,
                ticks : {
                	stepSize: 1000.
                }
            },
            x: {
            	grid: {display: false, drawBorder: false},

            }

        }

    }
});
</script>
	    
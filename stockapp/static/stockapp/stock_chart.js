let chart;
function loadChart(symbol) {
    fetch(`/api/price-history/${symbol}/`)
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('stockChart').getContext('2d');
            if (window.stockChartInstance) {
                window.stockChartInstance.destroy(); // clean up old chart if exists
            }

            window.stockChartInstance = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.timestamps,
                    datasets: [{
                        label: symbol + ' Price',
                        data: data.prices,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        tension: 0.1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Time'
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Price (USD)'
                            }
                        }
                    }
                }
            });
        });
}


function reloadChart(symbol) {
    fetch(`/api/chart-data/${symbol}/`)
        .then(res => res.json())
        .then(data => {
            chart.data.labels = data.labels;
            chart.data.datasets[0].data = data.prices;
            chart.update();
        });
}

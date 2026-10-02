Chart.register(ChartDataLabels);

const canvas = document.getElementById("pedidosChart");

new Chart(canvas, {
    type: "bar",

    data: {

        labels: estadosDesdeFlask,

        datasets: [
            {
                label: "Pedidos",

                data: cantidadesDesdeFlask,

                backgroundColor: [
                    "#C65D0E",
                    "#6F1D2E",
                    "#4F6F52",
                    "#008B6A"
                ],

                borderColor: [
                    "#A84D0B",
                    "#5A1726",
                    "#3E5941",
                    "#006E54"
                ],

                borderWidth: 1
            }
        ]

    },

    plugins: [ChartDataLabels],

    options: {
        plugins: {
            datalabels: {
                color: "#000000",
                anchor: "end",
                align: "top"
            }
        }
    }

});

const canalesCanvas = document.getElementById("canalesChart");

new Chart(canalesCanvas, {
    type: "doughnut",

    data: {
        labels: [
            "WhatsApp",
            "Instagram",
            "Llamada",
            "Otro"
        ],

        datasets: [
            {
                label: "Canales",
                data: [56, 22, 11, 11],

                backgroundColor: [
                    "#25D366",
                    "#C13584",
                    "#6F1D2E",
                    "#808080"
                ],

                borderWidth: 1
            }
        ]
    }
});
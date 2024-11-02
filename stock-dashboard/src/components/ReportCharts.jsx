import React, { useState, useEffect } from 'react';
import Chart from 'react-apexcharts';

function StockCandleChart() {

    const stockData = [
        { "date": "2024-10-01", "open": 60000, "high": 60176, "low": 59114, "close": 59632 },
        { "date": "2024-10-02", "open": 59632, "high": 59798, "low": 59069, "close": 59223 },
        { "date": "2024-10-03", "open": 59223, "high": 59409, "low": 58359, "close": 59068 },
        { "date": "2024-10-04", "open": 59068, "high": 60000, "low": 58274, "close": 58591 },
        { "date": "2024-10-05", "open": 58591, "high": 59210, "low": 58410, "close": 58413 },
        { "date": "2024-10-06", "open": 58413, "high": 58990, "low": 58089, "close": 58877 },
        { "date": "2024-10-07", "open": 58877, "high": 59220, "low": 58713, "close": 58823 },
        { "date": "2024-10-08", "open": 58823, "high": 59301, "low": 58019, "close": 58589 },
        { "date": "2024-10-09", "open": 58589, "high": 59118, "low": 58207, "close": 58878 },
        { "date": "2024-10-10", "open": 58878, "high": 59600, "low": 58618, "close": 59203 },
        { "date": "2024-10-11", "open": 59203, "high": 59598, "low": 58890, "close": 59012 },
        { "date": "2024-10-12", "open": 59012, "high": 59789, "low": 58578, "close": 59531 },
        { "date": "2024-10-13", "open": 59531, "high": 59901, "low": 59022, "close": 59288 },
        { "date": "2024-10-14", "open": 59288, "high": 59879, "low": 58892, "close": 59755 },
        { "date": "2024-10-15", "open": 59755, "high": 59999, "low": 59011, "close": 59234 },
        { "date": "2024-10-16", "open": 59234, "high": 59488, "low": 58876, "close": 59309 },
        { "date": "2024-10-17", "open": 59309, "high": 59777, "low": 59012, "close": 59456 },
        { "date": "2024-10-18", "open": 59456, "high": 59921, "low": 59112, "close": 59811 },
        { "date": "2024-10-19", "open": 59811, "high": 60000, "low": 59433, "close": 59567 },
        { "date": "2024-10-20", "open": 59567, "high": 59988, "low": 59021, "close": 59233 },
        { "date": "2024-10-21", "open": 59233, "high": 59709, "low": 58912, "close": 59302 },
        { "date": "2024-10-22", "open": 59302, "high": 60000, "low": 59112, "close": 59823 },
        { "date": "2024-10-23", "open": 59823, "high": 60200, "low": 59501, "close": 59992 },
        { "date": "2024-10-24", "open": 59992, "high": 60500, "low": 59423, "close": 60001 },
        { "date": "2024-10-25", "open": 60001, "high": 60288, "low": 59087, "close": 59713 },
        { "date": "2024-10-26", "open": 59713, "high": 60322, "low": 59512, "close": 60000 },
        { "date": "2024-10-27", "open": 60000, "high": 60400, "low": 59712, "close": 60355 },
        { "date": "2024-10-28", "open": 60355, "high": 60888, "low": 60032, "close": 60721 },
        { "date": "2024-10-29", "open": 60721, "high": 61222, "low": 60312, "close": 61000 },
        { "date": "2024-10-30", "open": 61000, "high": 61500, "low": 60500, "close": 61233 }
    ];
    
    const [data, setData] = useState({
        series: [
            {
                data: [],
            },
        ],
        options: {
            chart: {
                type: 'candlestick',
                height: 350,
                toolbar: {
                    show: false,
                },
            },
            xaxis: {
                type: 'datetime',
            },
            yaxis: {
                tooltip: {
                    enabled: true,
                },
            },
        },
    });

    useEffect(() => {
        const formattedStockData = stockData.map(item => {
            return {
                x: new Date(item.date),
                y: [item.open, item.high, item.low, item.close],
            };
        });
        setData(prevData => ({
            ...prevData,
            series: [{ data: formattedStockData }],
        }));
    }, []);

    return (
        <Chart
            options={data.options}
            series={data.series}
            type="candlestick"
            height={350}
        />
    );
}

export default StockCandleChart;

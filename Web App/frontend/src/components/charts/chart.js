import React, {Component} from 'react';
import { Line } from 'react-chartjs-2';

const data = {
  datasets: [
    {
      label: 'Predicted',
      fill: false,
      lineTension: 0.1,
      backgroundColor: 'rgba(75,192,192,0.4)',
      borderColor: 'rgba(75,192,192,1)',
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: 'rgba(75,192,192,1)',
      pointBackgroundColor: '#fff',
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: 'rgba(75,192,192,1)',
      pointHoverBorderColor: 'rgba(220,220,220,1)',
      pointHoverBorderWidth: 2,
      pointRadius: 1,
      pointHitRadius: 10,
      data: [null]
    },
    {
      label: 'Previous',
      fill: false,
      lineTension: 0.1,
      backgroundColor: 'rgba(192,192,192,0.4)',
      borderColor: 'rgba(192,192,192,1)',
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: 'rgba(75,192,192,1)',
      pointBackgroundColor: '#fff',
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: 'rgba(75,192,192,1)',
      pointHoverBorderColor: 'rgba(220,220,220,1)',
      pointHoverBorderWidth: 2,
      pointRadius: 1,
      pointHitRadius: 10,
      data: [null]
    }
  ]
};

export class LineDemo extends Component 
{
  constructor(props) {
    super(props);
    this.state = {
        data: data
      };
  }

  componentDidMount() {
    const { datasets } = this.refs.chart.chartInstance.data
  }

  componentWillReceiveProps(nextProps) {
    if(nextProps.data != undefined){
      this.getDataFromChild(nextProps.data)
    }
  }

  getDataFromChild = (values) => {
    let time = null
    if(values.time){
      time = values.time
    }
    else{
      time = new Array(values.predicted.length+values.previous.length)
      time = [0,15,30,45,60,75,90,105]
    }
    this.setState({data: {
      labels: time,
      datasets: [
        {
          label: 'Predicted',
          fill: false,
          lineTension: 0.1,
          backgroundColor: 'rgba(75,192,192,0.4)',
          borderColor: 'rgba(75,192,192,1)',
          borderCapStyle: 'butt',
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: 'miter',
          pointBorderColor: 'rgba(75,192,192,1)',
          pointBackgroundColor: '#fff',
          pointBorderWidth: 1,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: 'rgba(75,192,192,1)',
          pointHoverBorderColor: 'rgba(220,220,220,1)',
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: values.predicted
        },
        {
          label: 'Previous',
          fill: false,
          lineTension: 0.1,
          backgroundColor: 'rgba(192,192,192,0.4)',
          borderColor: 'rgba(192,192,192,1)',
          borderCapStyle: 'butt',
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: 'miter',
          pointBorderColor: 'rgba(75,192,192,1)',
          pointBackgroundColor: '#fff',
          pointBorderWidth: 1,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: 'rgba(75,192,192,1)',
          pointHoverBorderColor: 'rgba(220,220,220,1)',
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: values.previous
        }
      ]
    }})
  }

  render() {
    return (
      <div>
        <div className="chart">
            <Line 
                ref="chart"
                data={this.state.data}
                options={{
                    scales: {
                      yAxes: [{
                          stacked: false,
                      }],
                    },
                    layout: {
                      padding: {
                          left: 400,
                          right: 400,
                          bottom: 50,
                          top: 50
                      }
                    }
                }}
            />
        </div>
      </div>
    );
  }
}
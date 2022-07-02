import React, {Component} from 'react';
import {LineDemo} from './../chart'
import submit from './../../../img/submit.jpeg';

export class GetDataGeneration extends Component {

    constructor(props) {
        super(props);
        this.state = {
            data: undefined
        };
    }

    handleSubmit = async () => {
        let data = {
            "hrs": "3",
            "type": "generation"
        }
        let url = "http://localhost:5001/solar_generation"
        let res = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        let previous = res.past
        let predicted = new Array(previous.length).fill(null);
        predicted = predicted.concat(res.predicted[0])
        // Making a connection between the actual values and predicted values
        previous = previous.concat(predicted[previous.length])
        let result = {}
        result.time = res.time_stamp
        result.predicted = predicted
        result.previous = previous
        this.setState({data: result})
    }
    render(){
        return(
            <div className="text-center">
                <h1 >Please click on submit button to view Solar Predictons</h1>
                <div>
                    <input className="btn btn-primary btn-lg" type="submit" value="Submit" onClick={()=>this.handleSubmit()} />
                </div>
                <div>
                    <LineDemo data={this.state.data}/>
                </div>
            </div>
        )
    }
}

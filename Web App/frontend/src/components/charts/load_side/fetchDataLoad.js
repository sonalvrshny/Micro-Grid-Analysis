import React, {Component} from 'react';
import {LineDemo} from './../chart'
 
export class GetDataLoad extends Component {
    constructor(props) {
      super(props);
      this.state = {
          values: [],
          data: undefined
        };
    }

    handleAddmore = (e) => {
        this.setState({values: [...this.state.values,""]})
    }

    handleRemove = (e,index) => {
        let values = this.state.values
        values.splice(index,1)
        this.setState({values: values})
    }

    handleChange = (e,index) => {

        const re = /^[0-9.\b]+$/;
        if (e.target.value === '' || re.test(e.target.value)) {
            this.state.values[index] = e.target.value
            this.setState({values: this.state.values})
        }
    }

    handleSubmit = async (e) => {
        let previous = this.state.values.map(Number);
        let res = await fetch('http://localhost:5001/predict', {
            method: 'post',
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({hrs: 1, past: previous, type: "load"})
            }).then(res=>res.json())
        res = res.result[0]
        let predicted = new Array(previous.length).fill(null);
        predicted = predicted.concat(res)
        // Making a connection between the actual values and predicted values
        previous = previous.concat(predicted[previous.length])
        let result = {}
        result.predicted = predicted
        result.previous = previous
        this.setState({data: result})
    }

    render() {
      return (
        <div>
            <div className="text-center">
                <h1>Input Data</h1>
                {
                    this.state.values.map((value,index)=>{
                        return(
                            <div key={index}>
                                <input value={value} onChange={(e)=>this.handleChange(e, index)}/>
                                <input className="btn btn-primary" type='button' value='Remove' onClick={(e)=>this.handleRemove(e, index)}/>
                            </div>
                        )
                    })
                }        
                <input className="btn btn-primary" type='button' value='add more' onClick={(e)=>this.handleAddmore(e)}/>
                <input className="btn btn-primary" type="submit" value="Submit" onClick={(e)=>this.handleSubmit(e)} />
            </div>
            <div>
                <LineDemo data={this.state.data}/>
            </div>
        </div>
      );
    }
}

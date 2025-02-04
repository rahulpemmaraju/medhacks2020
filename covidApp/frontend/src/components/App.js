import React, { Component } from "react";
import { render } from "react-dom";
import Map from './Map';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/lead")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return(
      <h1></h1>
    )
    /*return (
      <ul>
        {this.state.data.map(contact => {
          return (
            <li key={contact.id}>
              {contact.name} - {contact.population}
            </li>
          );
        })}
        hewllo whats up
        <Map/>
      </ul>
    );*/
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
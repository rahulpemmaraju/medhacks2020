import React,{Component} from 'react';
import { render } from "react-dom";

class Map extends Component{
    
    constructor(props){
        super(props);
        this.state = {stateMap:null};
    }

    componentDidMount(){

        // Create the script tag, set the appropriate attributes
        let script = document.createElement('script');
        script.src = 'https://maps.googleapis.com/maps/api/js?sensor=false&key=AIzaSyBzap1FsjoN_AvQPtRgg8TBD5ndVlxMgSg&callback=initMap';
        script.defer = true;
        
        //let stateVar = this.state;
        let mapCreateFunction = this.createGoogleMapView;
        let stateVar = this.state;
        //Attach your callback function to the `window` object
        window.initMap = function() {
            // JS API is loaded and available
            mapCreateFunction(stateVar);
        };
        //&callback=initMap
        
        document.head.appendChild(script);

        console.log("mounted");

    }

    createGoogleMapView(stateVar){
        //source variable for where the kml file for county is
        let src = "../CountyKMLs/Atlantic.kml";

        // create the map
        stateVar = {stateMap : new google.maps.Map(document.getElementById("NJ"),{
            center: { lat: 40.0583, lng: -74.4057 },
            zoom : 5
        })};

        //center alts:
        //{ lat: 40.0583, lng: -74.4057 }
        //new google.maps.LatLng(40.0583,-74.4057)

        if(stateVar.stateMap != null){
            console.log(stateVar.stateMap);
        }else{
            console.log("map var is null");
        }

        // //create county var and pass in map to it to be shown:
        // let atlanticCounty = new google.maps.KmlLayer(src,{
        //     suppressInfoWindows: true,
        //     preserveViewport: false,
        //     map: stateVar.stateMap
        // });
    }

    render(){
        return(
            <div className="stateMap" id="NJ" sytle={{width:100,height:100}}></div>
        );
    }
}

export default Map;

const container = document.getElementById("app");
render(<Map />, container);


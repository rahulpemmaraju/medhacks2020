
//rizwan added the let something equal simplemaps_statemap_mapdata so we can control the map
let masterMapData = simplemaps_statemap_mapdata={
  main_settings: {
    width: "500",
    background_color: "#FFFFFF",
    background_transparent: "yes",
    popups: "detect",
    state_description: "State description",
    state_color: "#88A4BC",
    state_hover_color: "#3B729F",
    state_url: "https://simplemaps.com",
    border_size: 1.5,
    border_color: "#ffffff",
    all_states_inactive: "no",
    all_states_zoomable: "no",
    location_description: "Location description",
    location_color: "#FF0067",
    location_opacity: 0.8,
    location_hover_opacity: 1,
    location_url: "",
    location_size: 25,
    location_type: "square",
    location_border_color: "#FFFFFF",
    location_border: 2,
    location_hover_border: 2.5,
    all_locations_inactive: "no",
    all_locations_hidden: "no",
    label_color: "#ffffff",
    label_hover_color: "#ffffff",
    label_size: 22,
    label_font: "Arial",
    hide_labels: "no",
    manual_zoom: "no",
    back_image: "no",
    arrow_box: "no",
    navigation_size: "40",
    navigation_color: "#f7f7f7",
    navigation_border_color: "#636363",
    initial_back: "no",
    initial_zoom: -1,
    initial_zoom_solo: "no",
    region_opacity: 1,
    region_hover_opacity: 0.6,
    zoom_out_incrementally: "yes",
    zoom_percentage: 0.99,
    zoom_time: 0.5,
    popup_color: "white",
    popup_opacity: 0.9,
    popup_shadow: 1,
    popup_corners: 5,
    popup_font: "12px/1.5 Verdana, Arial, Helvetica, sans-serif",
    popup_nocss: "no",
    div: "map",
    auto_load: "yes",
    rotate: "0",
    url_new_tab: "yes",
    images_directory: "default",
    import_labels: "no",
    fade_time: 0.1,
    link_text: "View Website"
  },
  state_specific: {
    "34001": {
      name: "Atlantic",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34003": {
      name: "Bergen",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34005": {
      name: "Burlington",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34007": {
      name: "Camden",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34009": {
      name: "Cape May",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34011": {
      name: "Cumberland",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34013": {
      name: "Essex",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34015": {
      name: "Gloucester",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34017": {
      name: "Hudson",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34019": {
      name: "Hunterdon",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34021": {
      name: "Mercer",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34023": {
      name: "Middlesex",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34025": {
      name: "Monmouth",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34027": {
      name: "Morris",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34029": {
      name: "Ocean",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34031": {
      name: "Passaic",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34033": {
      name: "Salem",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34035": {
      name: "Somerset",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34037": {
      name: "Sussex",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34039": {
      name: "Union",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    },
    "34041": {
      name: "Warren",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "default"
    }
  },
  locations: {},
  labels: {}
};

/**
 * Rizwan added code below:
 *  - convert controls to an array of objects:
 *    -- currently they are json object
 * 
 *  - to control the map:
 *    -- at the very begining: request will go out and we will have data on all counties,
 *    at that point map function will be used to change color based on intensity
 *    -- set up the hover events
 *    -- set up predictive event
 * 
 *  - predictive event:
 *    -- may require another http request to django backend
 *    -- will run map again to re-color counties based on predictions
*/

//vars:
let mapcontrolsJSON = masterMapData.state_specific;
let mainBodyName = "mainBody_index";
let mainBody = (document.getElementById(mainBodyName));

let controls = (function convertControlsToArray(){
    return JSON.parse(mapcontrolsJSON);
})();


function updateCountyColorsOnLoad(){
  //gather data from django here

  //since data part not connected we will simply change all the colors to red:
  document.getElementById("Atlantic").onclick(document.getElementById("Atlantic").style={color:"red"});
}
mainBody.addEventListener("load",updateCountyColorsOnLoad);


 
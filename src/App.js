import React from "react";
import data from "./map_files/with_country_codes.json";
import { ZoomableGroup, ComposableMap, Geographies, Geography } from "react-simple-maps";
import './App.css';


function App() {
  return (
    <div className="App">
      <ComposableMap
        projection="geoEqualEarth"
        projectionConfig={{
          center: [0, 55],
          scale: 170,
        }}>
          <ZoomableGroup>
            <Geographies geography={data}>
              {({ geographies }) => 
                geographies.map((geo) => (
                  <Geography key={geo.rsmKey} 
                            geography={geo}
                            style={{
                              default: {
                                fill: "#3A3B3C",
                              },
                              hover: {
                                fill: "#F53",
                              },
                              pressed: {
                                fill: "#E42",
                              },
                            }} />
                ))
              }
            </Geographies>
          </ZoomableGroup>
      </ComposableMap>
    </div>
  );
}

export default App;

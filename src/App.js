import React from "react";
import data from "./with_country_codes.json";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";


function App() {
  return (
    <div className="App">
      <ComposableMap>
        <Geographies geography={data}>
        {({ geographies }) =>
          geographies.map((geo) => (
            <Geography key={geo.rsmKey} geography={geo} />
          ))
        }
        </Geographies>
      </ComposableMap>
    </div>
  );
}

export default App;

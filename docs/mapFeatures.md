Create visualizations for your map, including `arc`s, `node`s, and `geo`s, and customize their appearance.

The map features are located under the path `mapFeatures`.
Arguments:
        
* `data`: `[dict]` = `{}` &rarr; The data to pass to `mapFeatures.data.*`.

The map features data is located under the path `mapFeatures.data.*`.
Arguments:
        
* `type`: `[str]` &rarr; The type of the map feature.
    * Accepted Values:
        * `"arc"`: An `arc` layer
        * `"node"`: A `node` layer
        * `"geo"`: A `geo` layer
* `name`: `[str]` &rarr; The name of the map feature.
* `props`: `[dict]` &rarr; The props that will be rendered in the map feature.
    * See: `cave_utils.api_utils.general.props`
* `data`: `[dict]` &rarr; The data that will be passed to the props.
    * See: `cave_utils.api_utils.general.values`
* `layout`: `[dict]` =`{"type": "grid", "numColumns": "auto", "numRows": "auto"}` &rarr;
    * The layout of the map feature data presented in a map modal.
    * See: `cave_utils.api_utils.general.layout`
* `geoJson`: `[dict]` =`{}` &rarr; A dictionary specifying the GeoJSON data to use.
    * See: `cave_utils.api.mapFeatures.mapFeatures_data_star_geoJson`

The map features data is located under the path `mapFeatures.data.*.data`.
Arguments:
        
* `location`: `[dict]` &rarr; The location lists of the map feature.
    * See: `cave_utils.api.mapFeatures.mapFeatures_data_star_data_location`
* `valueLists`: `[dict]` &rarr; The value lists of the map feature.
    * See: `cave_utils.api_utils.general.valueLists`

The map features data is located under the path `mapFeatures.data.*.data.location`.
        
The location lists you pass will be validated based on other selections in your API spec.

The map feature GeoJSON data is located under the path `mapFeatures.data.*.geoJson`.
Arguments:
        
* `geoJsonLayer`: `[str]` &rarr; The URL of the GeoJSON layer to use.
* `geoJsonProp`: `[str]` &rarr;
    * The `properties` key (from the object fetched from the `geoJsonLayer` URL) to match with the value at `mapFeatures.data.*.data.location.geoJsonValue.*`.
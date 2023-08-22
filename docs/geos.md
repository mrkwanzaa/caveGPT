# `geos`
The `geos` group takes in data and renders it as geographic areas on the "**Map**" view, to visualize spatial distribution of parameters.

The internal structure of `geos` is very similar to that of the `arcs` and `nodes` groups. The most relevant discrepancy is the addition of the special key `geoJson`.

## Common keys
- [`allowModification`](../common_keys/common_keys.md#allowModification)
- [`category`](../common_keys/common_keys.md#category)
- [`colorBy`](../common_keys/common_keys.md#colorBy)
- [`colorByOptions`](../common_keys/common_keys.md#colorByOptions)
- [`column`](../common_keys/common_keys.md#column)
- [`data`](../common_keys/common_keys.md#data)
- [`enabled`](../common_keys/common_keys.md#enabled)
- [`endGradientColor`](../common_keys/common_keys.md#end-gradient)
- [`help`](../common_keys/props.md#help)
- [`icon`](../common_keys/common_keys.md#icon)
- [`name`](../common_keys/common_keys.md#name)
- [`numberFormat`](../common_keys/common_keys.md#number-format)
- [`prop > type`](../common_keys/props.md#prop-type)
- [`props`](../common_keys/common_keys.md#props-short)
- [`sendToApi`](../common_keys/common_keys.md#sendToApi)
- [`sendToClient`](../common_keys/common_keys.md#sendToClient)
- [`startGradientColor`](../common_keys/common_keys.md#start-gradient)
- [`value`](../common_keys/props.md#value)
- [`variant`](../common_keys/props.md#variant)

## Special and custom keys
Key | Default | Description
--- | ------- | -----------
`data.customGeoData*.category`&swarhk;<br>`.customDataChunck*` | | See [`customDataChunck*`](categories.md#customDataChunck).
`data.customGeoData*.category`&swarhk;<br>`.customDataChunck*.customDataKey*` | | See [`customDataKey*`](categories.md#customDataKey).
<a name="geojson-value">`data.customGeoData*.geoJsonValue`</a> | required | The identifier for this geo as identified in the specified geoJson object. This identifier is matched to the `types.customGeoType*.geoJson.geoJsonProp` as it relates to each geoJson object in the file specified at `types.customGeoType*.geoJson.geoJsonLayer`.
`data.customGeoData*.name` | | A name for the geo area that will be displayed as a title in the map modal.
`data.customGeoData*.props`&swarhk;<br>`.customPropKey*` | | See [`customPropKey*`](../common_keys/props.md#customPropKey).
`data.customGeoData*.type` | Required | The `type` key sets the type of `customGeoData*` to a `customGeoType*` key, to match specific visualization preferences for a geo.
`types` | Required | The `types` key allows you to define different types of geos in terms of styling and data viz settings.
<a name="geo-type">`types.customGeoType*`</a> | Required | A wrapper for key-value pairs that match a specific set of data viz preferences for a geo.
<a name="geoJson">`types.customGeoType*.geoJson`</a> | | A wrapper for the [`geoJsonLayer`](#geojson_layer) and [`geoJsonProp`](#geojson_prop) keys in a geo type.
<a name="geoJsonLayer">`types.customGeoType*.geoJson`&swarhk;<br>`.geoJsonLayer`</a> | | Sets the GeoJSON data source of `customGeoType*` to a URL of a GeoJSON data source. Note that this URL is fetched on app startup or, if passed later, when the layer is enabled by the app user.
<a name="geoJsonProp">`types.customGeoType*.geoJson`&swarhk;<br>`.geoJsonProp`</a> | | Contains the name of a [GeoJSON property](#https://datatracker.ietf.org/doc/html/rfc7946#section-1.5) in the data source specified in `geoJsonLayer`.

> Please note that in the CAVE App, the maximum total size of all combined GeoJSON data sources is 50 MiB. Feel free to use a tool like [mapshaper](https://mapshaper.org/) to meet the size requirements.
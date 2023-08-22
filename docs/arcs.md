# `arcs`
The `arcs` group contains data that is typically used to visualize flows between two points on the "**Map**" view. Depending on the nature of the flows and the purpose of the visualization, the flows between two locations can be represented by a single arc (source and destination) or a sequence of arc segments representing a [`path`](#path).

## Common keys
- [`allowModification`](../common_keys/common_keys.md#allowModification)
- [`category`](../common_keys/common_keys.md#category)
- [`colorByOptions`](../common_keys/common_keys.md#colorByOptions)
- [`column`](../common_keys/common_keys.md#column)
- [`data`](../common_keys/common_keys.md#data)
- [`enabled`](../common_keys/common_keys.md#enabled)
- [`endGradientColor`](../common_keys/common_keys.md#end-gradient)
- [`endSize`](../common_keys/common_keys.md#endSize)
- [`help`](../common_keys/props.md#help)
- [`max`](../common_keys/common_keys.md#color-by-max)
- [`min`](../common_keys/common_keys.md#color-by-min)
- [`name`](../common_keys/common_keys.md#name)
- [`numberFormat`](../common_keys/common_keys.md#number-format)
- [`prop > type`](../common_keys/props.md#prop-type)
- [`props`](../common_keys/common_keys.md#props-short)
- [`sendToApi`](../common_keys/common_keys.md#sendToApi)
- [`sendToClient`](../common_keys/common_keys.md#sendToClient)
- [`sizeByOptions`](../common_keys/common_keys.md#sizeByOptions)
- [`startSize`](../common_keys/common_keys.md#startSize)
- [`startGradientColor`](../common_keys/common_keys.md#start-gradient)
- [`value`](../common_keys/props.md#value)
- [`variant`](../common_keys/props.md#variant)

## Special and custom keys
Key | Default | Description
--- | ------- | -----------
<a name="arc-data-point">`data.customArcData*`</a> | Required | A custom key wrapper for the parameters required to visualize an arc flow and the data associated with it in the "**Map**" view.
`data.customArcData*.category`&swarhk;<br>`.customDataChunck*` | | See [`customDataChunck*`](../all_keys/categories.md#customDataChunck).
`data.customArcData*.category`&swarhk;<br>`.customDataChunck*.customDataKey*` | | See [`customDataKey*`](../all_keys/categories.md#customDataKey).
`data.customArcData*.endAltitude` | | The altitude (in meters) for the target location in the "**Map**" view. It takes a float value.
`data.customArcData*.endClick`<br>(*Under construction*) | | Related to the animation frame rate of an arc layer. It takes an integer value.
`data.customArcData*.endLatitude` | Required | The latitude for the target location in the "**Map**" view. It takes a float value.
`data.customArcData*.endLongitude` | Required | The longitude for the target location in the "**Map**" view. It takes a float value.
`data.customArcData*.height` | `1` | The height multiplier relative to the distance between two points for the apex of a `3d` (lineBy) arc. For example, a value of `0` would turn a `3d` (lineBy) arc into the equivalent to a `solid` (lineBy) arc.
`data.customArcData*.name` | | A name for the arc flow that will be displayed as a title in the map modal.
<a name="path">`data.customArcData*.path`</a> | | A list of coordinate points (`[<longitude>, <latitude>]`), such that every two consecutive coordinates represent an arc segment of a path to be rendered in the "**Map**" view. Additionally, a third position can be added to each coordinate (`[<longitude>, <latitude>, <altitude>]`), to visually represent altitude on the map.<br><br>Please note that `path` is not supported for `3d` arcs. If you need to create a "`3d` path", you can do so by joining multiple arcs which start and end coordinates match the segments of the intended path.<br><br>The use of `path` overrides any behavior resulting from the use of the following `data.customArcData*.` keys: `startLongitude`, `startLatitude`, `startAltitude`, `endLongitude`, `endLatitude`, and `endAltitude`.
`data.customArcData*.props`&swarhk;<br>`.customdPropKey*` | | See [`customdPropKey*`](../common_keys/props.md#customdPropKey).
`data.customArcData*.startAltitude` | | The altitude (in meters) for the source location in the "**Map**" view. It takes a float value.
`data.customArcData*.startClick`<br>(*Under construction*) | | Related to the animation frame rate of an arc layer. It takes an integer value.
`data.customArcData*.startLatitude` | Required | The latitude for the source location in the "**Map**" view. It takes a float value.
`data.customArcData*.startLongitude` | Required | The longitude for the source location in the "**Map**" view. It takes a float value.
`data.customArcData*.tilt` | `0` | Expressed in degrees (-90&deg; to 90&deg;), this feature enables you to tilt the arc sideways when dealing with multiple arcs that share the same source and target locations in the "**Map**" view.
`data.customArcData*.type` | Required | The `type` key sets the arc type of `customArcData*` to a `customArcType*` key, to match specific visualization preferences for an arc flow.
`types` | Required | The `types` key allows you to define different arc types in terms of styling and data viz settings.
<a name="arc-type">`types.customArcType*`</a> | | A wrapper for key-value pairs that match a specific set of data viz preferences for an arc flow.
`types.customArcType*.lineBy` | `'solid'` | The pattern of dashes and gaps used to form the shape of an arc's stroke. It takes one of the following values: `'dashed'`, `'dotted'`, `'solid'`, or `'3d'`. This can be set in individual arcs to overwrite the default for the type.
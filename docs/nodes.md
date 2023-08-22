# `nodes`
The `nodes` group contains data that is typically used to visualize single geographic locations in the "**Map**" view.

## Common keys
- [`allowModification`](../common_keys/common_keys.md#allowModification)
- [`category`](../common_keys/common_keys.md#category)
- [`colorByOptions`](../common_keys/common_keys.md#colorByOptions)
- [`column`](../common_keys/common_keys.md#column)
- [`data`](../common_keys/common_keys.md#data)
- [`enabled`](../common_keys/common_keys.md#enabled)
- [`endGradientColor`](../common_keys/common_keys.md#endGradientColor)
- [`endSize`](../common_keys/common_keys.md#endSize)
- [`help`](../common_keys/props.md#help)
- [`icon`](../common_keys/common_keys.md#icon)
- [`name`](../common_keys/common_keys.md#name)
- [`numberFormat`](../common_keys/common_keys.md#number-format)
- [`prop > type`](../common_keys/props.md#prop-type)
- [`props`](../common_keys/common_keys.md#props-short)
- [`sendToApi`](../common_keys/common_keys.md#sendToApi)
- [`sendToClient`](../common_keys/common_keys.md#sendToClient)
- [`sizeByOptions`](../common_keys/common_keys.md#sizeByOptions)
- [`startSize`](../common_keys/common_keys.md#startSize)
- [`startGradientColor`](../common_keys/common_keys.md#startGradientColor)
- [`value`](../common_keys/props.md#value)
- [`variant`](../common_keys/props.md#variant)

## Special and custom keys
Key | Default | Description
--- | ------- | -----------
<a name="node-data-point">`data.customNodeData*`</a> | Required | A custom key wrapper for the parameters required to visualize a node and the data associated with it in the "**Map**" view.
`data.customNodeData*.altitude` | `1` | The altitude of the node (in meters) above sea level. Defaults to 1 to appear on top of `geo` layers.
`data.customNodeData*.category`&swarhk;<br>`.customDataChunck*` | | See [`customDataChunck*`](categories.md#customDataChunck).
`data.customNodeData*.category`&swarhk;<br>`.customDataChunck*.customDataKey*` | | See [`customDataKey*`](categories.md#customDataKey).
`data.customNodeData*.latitude` | Required | The latitude of the node location in the "**Map**" view. It takes a float value.
`data.customNodeData*.longitude` | Required | The longitude of the node location in the "**Map**" view. It takes a float value.
`data.customNodeData*.name` | | A name for the node location that will be displayed as a title in the map modal.
`data.customNodeData*.props`&swarhk;<br>`.customPropKey*` | | See [`customPropKey*`](../common_keys/props.md#customPropKey).
`data.customNodeData*.type` | Required | The `type` key sets the node type of `customNodeData*` to a `customNodeType*` key, to match specific visualization preferences for a node.
`types` | Required | The `types` key allows you to define different types of nodes in terms of styling and data viz settings.
<a name="node-type">`types.customNodeType*`</a> | | A wrapper for key-value pairs that match a specific set of data viz preferences for a node.

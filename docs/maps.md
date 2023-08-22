### `maps`
This key group allows designers to specify information about the starting state of the map, what information is contained and how it is grouped in the legend, and what viewports can be easily jumped to by the user.

## Common keys
- [`allowModification`](../common_keys/common_keys.md#allowModification)
- [`data`](../common_keys/common_keys.md#data)
- [`icon`](../common_keys/common_keys.md#icon)
- [`name`](../common_keys/common_keys.md#name)
- [`order`](../common_keys/common_keys.md#order)
- [`sendToApi`](../common_keys/common_keys.md#sendToApi)
- [`sendToClient`](../common_keys/common_keys.md#sendToClient)

## Special and custom keys
Key | Default | Description
--- | ------- | -----------
<a name="defaultViewport">`customMapKey.defaultViewport`</a> | | A dictionary object containing geo properties that set the map's default field of view. Also used by the "home" viewport button in the app.
`customMapKey.defaultViewport.bearing` | `0` | The initial bearing (rotation) of the map, measured in degrees counter-clockwise from north.
`customMapKey.defaultViewport.pitch` | `0` | The initial pitch (*tilt*) of the viewport in the "**Map**" view, measured in degrees away from the plane of the screen (0&deg; - 85&deg;). A pitch of 0&deg; results in a two-dimensional map, as if your line of sight forms a perpendicular angle with the earth's surface, while a greater value like 60&deg; looks ahead towards the horizon.
`customMapKey.defaultViewport.latitude` | `42.36157` | The center latitude of the viewport in the "**Map**" view. It takes a float value.
`customMapKey.defaultViewport.longitude` | `-71.08463` | The center longitude of the viewport in the "**Map**" view. It takes a float value.
`customMapKey.defaultViewport.maxZoom` | `22` | The maximum zoom level of the viewport in the "**Map**" view. It takes an integer value.
`customMapKey.defaultViewport.minZoom` | `1.5` | The minimum zoom level of the viewport in the "**Map**" view. It takes an integer value.
`customMapKey.defaultViewport.zoom` | `13` | The initial zoom level of the viewport in the "**Map**" view. It takes an integer value. Learn more about the zoom levels [here](#https://docs.mapbox.com/help/glossary/zoom-level/).
<a name="optionalViewports">`customMapKey.optionalViewports`</a> | | A dictionary of optional viewports that can be jumped to by users. Each optional viewport should contain the same keys as `defaultViewport` as well as `name` and `icon` keys.
<a name="legendGroups">`customMapKey.legendGroups`</a> | `{}` | A dictionary object of all layer groupings to display in the map legend. The legend groups are displayed according to their `order` and each has an internal order of `nodes`, `arcs`, and `geos`. Types not included in any legend group cannot be toggled.
`customMapKey.legendGroups.customLegendGroupKey*` | `{}` | A custom key wrapper for a legend group that contains its `name`, its display `order` from top to bottom within the map legend, as well as the initial state of the toggles for [`arc type`](arcs.md#arc-type)s, [`node type`](nodes.md#node-type)s, and [`geo type`](geos.md#geo-type)s.
`customMapKey.legendGroups.customLegendGroupKey*.arcs` | `{}` | A list of all arc types to include in the legend group. Note that settings (`colorBy`, `sizeBy`) are syncronized across the same type in multiple groups.
`customMapKey.legendGroups.customLegendGroupKey*.arcs.customArcType*` | `{value: False}` | A [arc type](arcs.md#arc-type) that matches the initial state of the toggle within the legend group. The inner `value` key is paired with a boolean indicating whether the arc type should be displayed in the "Map" view or not, while the `order` key follows the standard [`order`](../common_keys/common_keys.md#order)ing convention, allowing to set the display order of the arc type within the legend group. The `colorBy` and `sizeBy` keys set the default coloring and sizing props of the arc type.
`customMapKey.legendGroups.customLegendGroupKey*.geos` | `{}` | A list of all geo types to include in the legend group. Note that settings (`colorBy`, `sizeBy`) are syncronized across the same type in multiple groups.
`customMapKey.legendGroups.customLegendGroupKey*.geos.customGeoType*` | `{value: False}` | A [geo type](geos.md#geo-type) that matches the initial state of the toggle within the legend group. The inner `value` key is paired with a boolean indicating whether the geo type should be displayed in the "Map" view or not, while the `order` key follows the standard [`order`](../common_keys/common_keys.md#order)ing convention, allowing to set the display order of the geo type within the legend group. The `colorBy` key set the default coloring prop of the geo type.
`customMapKey.legendGroups.customLegendGroupKey*.nodes` | `{}` | A dictionary of all node types to include in the legend group. Note that settings (`colorBy`, `sizeBy`) are syncronized across the same type in multiple groups.
`customMapKey.legendGroups.customLegendGroupKey*.nodes.customNodeType*` | `{}` | An object to hold the options related to each custom node type
`customMapKey.legendGroups.customLegendGroupKey*.nodes.customNodeType*.value` | `false` | A boolean value to indicate if this layer should be shown
`customMapKey.legendGroups.customLegendGroupKey*.nodes.customNodeType*.order` | | The [`order`](../common_keys/common_keys.md#order) value that this toggle should appear in the legend group
`customMapKey.legendGroups.customLegendGroupKey*.nodes.customNodeType*.colorBy` | `false` | The prop to used to color this node layer
`customMapKey.legendGroups.customLegendGroupKey*.nodes.customNodeType*.sizeBy` | `false` | The prop to used to size this node layer
`customMapKey.legendGroups.customLegendGroupKey*.nodes.customNodeType*.allowGrouping` | `false` | (BETA Feature) A node specific key to determine if this node layer is able to be auto grouped.
`customMapKey.legendGroups.customLegendGroupKey*.nodes.customNodeType*.group` | `false` | (BETA Feature) Group the nodes in this layer (to use this you must set `allowGrouping=true`)
`customMapKey.legendGroups.customLegendGroupKey*.nodes.customNodeType*.groupCalcByColor` | `count` | (BETA Feature) The aggregation method to use on the prop specified in `colorBy`. Options include [`count`,`max`,`min`,`mean`,`median`,`mode`,`sum`]
`customMapKey.legendGroups.customLegendGroupKey*.nodes.customNodeType*.groupCalcBySize` | `count` | (BETA Feature) The aggregation method to use on the prop specified in `sizeBy`. Options include [`count`,`max`,`min`,`mean`,`median`,`mode`,`sum`]
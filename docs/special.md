# `special`
The `special` key allows API designers to trigger user actions such as button presses, open modals, change local settings, and adjust the users current viewport. Unlike other api keys, the current state of `special` isn't always relfected in the api, as many changes happen locally. However, setting a value in `special` will immediately update the associated value for all clients in the session. 

## Special and custom keys
Key | Default | Description
--- | ------- | -----------
`customButton*` | False | Setting buttons value to true simulates a click of that button, dispatching associated api commands and other potential actions. The value is then reset to False to allow for the button to be pressed again.
`customMapKey.viewport` | {} | Setting the value of `customMapKey.viewport` sets the current viewport of the map. Note that this key contains the last set viewport, not necessarily the users current viewport.
`customMapKey.viewport.bearing` | `0` | The initial bearing (rotation) of the map, measured in degrees counter-clockwise from north.
`customMapKey.viewport.pitch` | `0` | The initial pitch (*tilt*) of the viewport in the "**Map**" view, measured in degrees away from the plane of the screen (0&deg; - 85&deg;). A pitch of 0&deg; results in a two-dimensional map, as if your line of sight forms a perpendicular angle with the earth's surface, while a greater value like 60&deg; looks ahead towards the horizon.
`customMapKey.viewport.latitude` | `42.36157` | The center latitude of the viewport in the "**Map**" view. It takes a float value.
`customMapKey.viewport.longitude` | `-71.08463` | The center longitude of the viewport in the "**Map**" view. It takes a float value.
`customMapKey.viewport.maxZoom` | `22` | The maximum zoom level of the viewport in the "**Map**" view. It takes an integer value.
`customMapKey.viewport.minZoom` | `1.5` | The minimum zoom level of the viewport in the "**Map**" view. It takes an integer value.
`customMapKey.viewport.zoom` | `13` | The initial zoom level of the viewport in the "**Map**" view. It takes an integer value ranging from 22(most zoomed in) to 2(most zoomed out).
`openModal` | {} | A dictionary with the shape `{"feature": "arcs", "value": "customArcName"}`, where `feature` can be one of `arcs`, `nodes`, or `geos` and `value` is the name of the feature to open the modal for.
`locals` | {} | A dictionary that is merged with the current local settings for all clients. This key shouldn't be used without first carefully testing the local settings as these aren't documented and may change in updates without warning
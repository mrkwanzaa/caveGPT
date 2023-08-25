# `special`
The `special` key allows API designers to trigger user actions such as button presses, open modals, change local settings, and adjust the users current viewport. Unlike other api keys, the current state of `special` isn't always relfected in the api, as many changes happen locally. However, setting a value in `special` will immediately update the associated value for all clients in the session. 

## Special and custom keys
Key | Default | Description
--- | ------- | -----------
`customButton*` | False | Setting buttons value to true simulates a click of that button, dispatching associated api commands and other potential actions. The value is then reset to False to allow for the button to be pressed again.
`customMapKey.viewport` | {} | Setting the value of `customMapKey.viewport` sets the current viewport of the map. Note that this key contains the last set viewport, not necessarily the users current viewport.
`openModal` | {} | A dictionary with the shape `{"feature": "arcs", "value": "customArcName"}`, where `feature` can be one of `arcs`, `nodes`, or `geos` and `value` is the name of the feature to open the modal for.
`locals` | {} | A dictionary that is merged with the current local settings for all clients. This key shouldn't be used without first carefully testing the local settings as these aren't documented and may change in updates without warning
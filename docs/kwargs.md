# `kwargs`
The `kwargs` group contains special keys that are not actually stored in the data but instead used to instruct the server to do special tasks.

## Special and custom keys
Key | Default | Description
--- | ------- | -----------
`wipeExisting` | `True` | Indicate if all current session data (the current session of the requesting user) should be wiped before overwriting all currently passed data. This can be used to reduce server load. For example given a specific command, if only a single top-level key should be updated, you can simply pass the top-level key dictionary and set `wipeExisting` to `False`. In this case, you would only overwrite that single top-level key and leave the rest unchanged.

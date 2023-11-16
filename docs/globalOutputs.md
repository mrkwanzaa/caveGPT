Create outputs that allow for simple charts and tables to present some totalization or global outcome of the data.

These outputs should be general to the entire application and they can be compared across sessions.

Arguments:

* **`props`**: `[dict]` &rarr; The props that will be rendered as global outputs.
    * **See**: `cave_utils.api_utils.general.props`
* **`values`**: `[dict]` = `None` &rarr;
    * The values to be assigned to the respective props. Each value is associated with its corresponding prop based on the key name used in `props`.
    * **See**: `cave_utils.api_utils.general.values`
* **`layout`**: `[dict]` =`{"type": "grid", "numColumns": "auto", "numRows": "auto"}` &rarr;
    * The layout of the global outputs when the "Overview" chart is selected.
    * **See**: `cave_utils.api_utils.general.layout`
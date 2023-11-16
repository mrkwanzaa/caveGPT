Create grouped outputs for building generalized charts and tables.

Arguments:

* **`groupings`**: `[dict]` &rarr; A dictionary of groupings that are available for the data.
    * **See**: `groupedOutputs.groupings`
* **`data`**: `[dict]` &rarr; The data to be grouped.
    * **See**: `groupedOutputs.data`

The grouped outputs data is located under the path **`groupedOutputs.data.*`**.

Arguments:

* **`stats`**: `[dict]` &rarr; A dictionary of stats that are available for the data.
    * **See**: `cave_utils.api.groupedOutputs.groupedOutputs_data_star_stats`
**`valueLists`**: `[dict]` &rarr; A dictionary of lists that make up the stats for the data.
**`groupLists`**: `[dict]` &rarr; A dictionary of lists that make up the groupings for the data.

The grouped output stats are located under the path **`groupedOutputs.data.*.stats`**.

Arguments:

* **`name`**: `[str]` &rarr; The name of the stat.
* **`calculation`**: `[str]` &rarr; The calculation to generate the stat for each group.
    * **Notes**:
        * This can use operators [`+`, `-`, `*`, `/`, and `groupSum`]
        * This can call in keys from `groupedOutputs.data.*.valueLists.*` as variables
    * **Examples**:
        * Create a variable that can be used to aggregate on your stat demand on arbitrary groupings: `'demand'`.
        * Create a variable that can be used to aggregate your percent of demand met on arbitrary groupings. (This only shows the percent of demand met for each group if they are summed in the chart): `'sales / groupSum("demand")'`
* **`unit`**: `[str]` &rarr; The unit to use for the stat.
    * **Note**: If left unspecified (i.e., `None`), it will default to `settings.defaults.unit`.
* **`unitPlacement`**: `[str]` = `None` &rarr; The position of the `unit` symbol relative to the value.
    * **Accepted Values**:
        * `"after"`: The `unit` appears after the value.
        * `"afterWithSpace"`: The `unit` appears after the value, separated by a space.
        * `"before"`: The `unit` appears before the value.
        * `"beforeWithSpace"`: The unit is placed before the value, with a space in between.
    * **Note**: If left unspecified (i.e., `None`), it will default to `settings.defaults.unitPlacement`.
* **`precision`**: `[int]` = `None` &rarr; The number of decimal places to display.
    * **Notes**:
        * Set the precision to `0` to attach an integer constraint.
        * If left unspecified (i.e., `None`), it will default to `settings.defaults.precision`.
* **`trailingZeros`**: `[bool]` = `None` &rarr; If `True`, trailing zeros will be displayed.
    * **Notes**:
        * This ensures that all precision digits are shown. For example: `1.5` &rarr; `1.500` when precision is `3`.
        * If left unspecified (i.e., `None`), it will default to `settings.defaults.trailingZeros`.

The value lists are located under the path **`groupedOutputs.data.*.valueLists`**.

Accepts any key value pairs as a dictionary structure for the data.

Each value must be a list of integers or floats.

The groupings are located under the path **`groupedOutputs.groupings.*`**.

Arguments:

* **`levels`**: `[dict]` &rarr;
    * A dictionary of levels that are available for the grouping.
    * **See**: `groupedOutputs_groupings_star_levels_star`
* **`data`**: `[dict]` &rarr; The data to be grouped.
    * **See**: `groupedOutputs_groupings_star_data`
* **`name`**: `[str]` &rarr; The name of the grouping.
* **`layoutDirection`**: `[str]` = `"vertical"` &rarr; The direction of the grouping levels in the layout.
    * **Accepted Values**:
        * `"horizontal"`: Plain number formatting
        * `"vertical"`: Resembles the [metric prefix][] system
        * `"scientific"`: [Scientific notation][]
        * `"engineering"`: [Engineering notation][]
* **`grouping`**: `[str]` = `None` &rarr;
    * A group that is created to put similar groupings together in the UI dropdowns when selecting groupings.
    * **Note**: If `None`, the grouping will be placed in the root of the UI dropdowns.

The groupings data is located under the path **`groupedOutputs.groupings.*.data`**.

Arguments:

* **`id`**: `[list]` &rarr; The id of the data to be grouped.
* **`customKeyHere`**: `[list]` &rarr;
    * The names of the data to be grouped for this feature/level.
    * **Note**: Each key listed here must be in `groupedOutputs.groupings.*.levels.*`

The level data is located under the path **`groupedOutputs.groupings.*.levels.*`**.

Arguments:

* **`name`**: `[str]` &rarr; The name of the level.
* **`parent`**: `[str]` &rarr;
    * The key of the parent level. This is used to create a hierarchy of levels.
    * **Notes**:
        * The parent level key must be defined in `groupedOutputs.groupings.*.levels.*`
        * If `None`, this will be considered to be the root of the hierarchy.
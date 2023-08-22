# `stats`
The `stats` group takes parameter data that can be combined with geospatial data to represent it in the "**Map**" view or simply use its raw values to display in a dashboard view.

## Common keys
- [`allowModification`](../common_keys/common_keys.md#allowModification)
- [`category`](../common_keys/common_keys.md#category)
- [`data`](../common_keys/common_keys.md#data)
- [`name`](../common_keys/common_keys.md#name)
- [`numberFormat`](../common_keys/common_keys.md#number-format)
- [`order`](../common_keys/common_keys.md#order)
- [`sendToApi`](../common_keys/common_keys.md#sendToApi)
- [`sendToClient`](../common_keys/common_keys.md#sendToClient)

## Special and custom keys
Key | Default | Description
--- | ------- | -----------
`data.customStatData*` | Required | A custom key wrapper for the [`category`](../common_keys/common_keys.md#category) and [`values`](#values) keys.
`data.customStatData*.category`&swarhk;<br>`.customDataChunck*` | | See [`customDataChunck*`](categories.md#customDataChunck).
`data.customStatData*.category`&swarhk;<br>`.customDataChunck*.customDataKey*` | | See [`customDataKey*`](categories.md#customDataKey).
<a name="values">`data.customStatData*.values`</a> | Required | A wrapper for independent `customStatKey*`s and their values.
<a name="customStatKey">`types.customStatKey*`</a> | Required | A key used to identify a parameter in a `calculation` expression and be referenced by the `values` group.
`types` | Required | The `types` key allows you to define the appearance and logic of the `customStatKey*` parameters. Note that the `customStatKey*`s must not begin with a number value.
`types.customStatKey*.groupByOptions` | All Categories | Limits the options for grouping and subgrouping in dashboards to the specified category keys. If set to an empty list no grouping is availible.
`types.customStatKey*.calculation` | Required | Defines a math expression that allows the calculation of a `customStatKey*` parameter that depends on the value of others. The expression is used to dynamically estimate the value of a parameter when the data containing its independent stats used in the calculation, has changed, e.g. after applying a filter. When a custom stat is independent, the math expression must match its own `customStatKey*`. The CAVE App comes with a software package that provides built-in support for common math functions and operators. For a list of the available operators and examples of math expressions, see the [`expr-eval` documentation](https://github.com/silentmatt/expr-eval#documentation) and [`groupSum`](#groupsum) below. 
## `groupSum`
`groupSum` is a special function provided by the CAVE app that takes an independent stat as input and outputs the sum of that stat across the level (or sub-level if present) specified by the user or API for that [dashboard](#dashboards) chart. Using `groupSum` is different than other [`expr-eval`](https://github.com/silentmatt/expr-eval) functions as the variable must be passed as a string rather than a literal, e.g. **`groupSum("customStat")`** (not `groupSum(customStat)`). When using `groupSum` special consideration should be given to ensure the the dashboard grouping (sum, minimum, maximum, or average) makes it clear to users what the stat represents, as while `groupSum` sums across the level the stat calculation is still done to the individual stats which are then grouped.

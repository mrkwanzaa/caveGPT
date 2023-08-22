# `kpis`
The `kpis` group contains all the KPI data that will be displayed on the "**KPI**" view. These are typically highly aggregated statistics calculated by the api. In general, KPIs are used to compare values across sessions and give a high level overview of output. Filters and aggregations will not affect `kpis`.

## Common keys
- [`allowModification`](../common_keys/common_keys.md#allowModification)
- [`column`](../common_keys/common_keys.md#column)
- [`data`](../common_keys/common_keys.md#data)
- [`icon`](../common_keys/common_keys.md#icon)
- [`layout`](../common_keys/layout.md)
- [`name`](../common_keys/common_keys.md#name)
- [`numberFormat`](../common_keys/common_keys.md#number-format)
- [`sendToApi`](../common_keys/common_keys.md#sendToApi)
- [`sendToClient`](../common_keys/common_keys.md#sendToClient)

## Special and custom keys
Key | Default | Description
--- | ------- | -----------
`customKpi*` | Required | A custom key wrapper for the KPI data.
`customKpi*.mapKpi` | `False` | The `mapKpi` flag allows designers to specify up to six parameters that are displayed on a permanent grid in the "**Map**" view. The grid layout (rows *x* columns) changes with the number of parameters present in the data, scaling up to 2 rows and 3 columns.
`customKpi*.type` | `'num'` | As a direct child of `customKpi*`, the `type` key defines the UI construct used to render the KPI and restricts the set of key-value pairs that can be used with this type.
`customKpi*.value` | | The actual value of the KPI.
<a name="variant">`customKpi*.variant`</a> | | Used to modify the UI for a given KPI `type`. The presentation to the end user changes, but the `value`s should remain with the same structure. For example, you can modify the appearance of a `'head'` KPI in terms of the orientation of its related items (`'column'` or `'row'`).

## KPI `type`s and their `variant`s:

### `'head'`
Allows users to place a header for an individual section, containing a title (via [`name`](common_keys.md#name)) and a [`help`](#help) message. the `mapKpi`, [`numberFormat`](../common_keys/common_keys.md#number-format), and `value` keys are ignored when used along this type.
#### Variants:
>`'column'` (**default**): Acts as a header for a column of related KPI items.<br>
`'row'`: Acts as a header for a row of related KPI items.<br>

### `'num'`
Displays a numeric value. All keys are valid to use with this type.

### `'text'`
Displays a text string. The [`numberFormat`](../common_keys/common_keys.md#number-format) key is ignored when used along this type.

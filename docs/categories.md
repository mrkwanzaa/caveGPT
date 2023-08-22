# `categories`
Both designers and users often need to work with different levels of data aggregation. the `categories` top level key allows for easy and arbitrary aggregation/filtering of data in the UI. They are a core aspect for how chart groupings, chart subgroupgings and general filtering works.

## Common keys
- [`allowModification`](../common_keys/common_keys.md#allowModification)
- [`data`](../common_keys/common_keys.md#data)
- [`name`](../common_keys/common_keys.md#name)
- [`order`](../common_keys/common_keys.md#order)
- [`sendToApi`](../common_keys/common_keys.md#sendToApi)
- [`sendToClient`](../common_keys/common_keys.md#sendToClient)

## Special and custom keys
Key | Default | Description
--- | ------- | -----------
<a name="customCategory">`customCategory*`</a> | Required | A custom key for categorical data. Each `customCategory*` key encloses a well-defined structure. This represents a higher level structure for filtering and aggregation purposes. A simple example is geography which can be represented by a nested structure (`township` &rarr; `state` &rarr; `country` &rarr; `continent`).
`customCategory*.data` | | Dictionary object that contains `customDataChunck*` items.
<a name="customDataChunck">`customCategory*.data.customDataChunck*`</a> | | A wrapper for key-value pairs that are grouped by any categorical context set by the designer. This represents the smallest level of aggregation. For example, an app that groups data geographically to the township level would need one data chunk per township they want to represent.
<a name="customDataKey">`customCategory*.data`&swarhk;<br>`.customDataChunck*.customDataKey*`<br><br>or<br><br>`customCategory*.nestedStructure`&swarhk;<br>`.customDataChunck*.customDataKey*`</a> | | A data property representing a specific group level of data. Following our geographic example, there should be four custom data keys (`township`, `state`, `country` and `continent`) per custom data chunk.
`customCategory*.data`&swarhk;<br>`.customDataKey*.customDataValue*` | | A match value for `customDataKey*`. Can either be string, numeric or boolean. Given our geographic example, a custom data key named `township` could have a data value of `'cambridge'` or any other township.
`customCategory*.grouping` | | When a `grouping` name is assigned to categories, they appear under a collapsible group in the "**Group By**" and "**Sub Group**" drop-down menus of a chart. If a `grouping` name is not assigned, the category will appear separately in the UI and at the same level as the collapsible groups.
`customCategory*.layoutDirection` | `'vertical'` | The direction in which `customDataKey*`s appear in the "**Group By**" and "**Sub Group**" drop-down menus of a chart. It can be `'horizontal'` or `'vertical'`. If omitted, the items will be displayed vertically in the UI.
`customCategory*.nestedStructure` | Required | A container dictionary for specifying the rendering properties of the items that are displayed in the "**Group By**" drop-down menu of a chart in a dashboard view.
`customCategory*.nestedStructure`&swarhk;<br>`.customDataKey*.ordering` | | A special key of a [`customDataChunck*`](#customDataChunck) that sets the position in which the `customDataValue*`s contained in the data chunk are rendered in the "**Group By**" and "**Sub Group**" drop-down menus of a chart. Its value is a list of strings in which the order of `customDataValue*`s is determined by their indices in the list (ascending order). All values that are not included in the list will be sorted alphabetically and placed after the values that are actually present.
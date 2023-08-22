# `dashboards`
The `dashboards` key allows API designers to create custom dashboards for displaying charts and tables of statistics and kpi data. This key allows for default information and layout to be specified, as well as whether the dashboards can be edited by the user.

## Special and custom keys
Key | Default | Description
--- | ------- | -----------
`customDashKey.dashboardLayout` | `[]` | A list of chart items (max of 4 items currently supported) that belong to the current dashboard. Each chart item contains the following keys: `chart`, `grouping`, `statistic`, `category`, `level`, `type`, and `lockedLayout`.
`customDashKey.statOptions` | `[]` | A list of stat type keys that can be displayed in the charts on the dashboard. If the list is empty or no list is passed all stats are availible.
`customDashKey.dashboardLayout.*.*.category` | | The category selected from the "**Group By**" drop-down menu of a chart in a dashboard view. This key is different from the common key [`category`](../common_keys/common_keys.md#category).
`customDashKey.dashboardLayout.*.*.category2` | | The category selected from the "**Sub Group**" drop-down menu of a chart in a dashboard view. This uses the data resulting from "**Group By**" as input and allows you to further divide it based on the selected `category2` and [`level2`](#level2).
`customDashKey.dashboardLayout.*.*.chart` | | The chart type selected from the top-left drop-down menu of a chart in a dashboard view. The `chart` key sets the type of chart to one of these values: `'Bar'`,`'Stacked Bar'`,`'Line'`,`'Cumulative Line'`,`'Table'`,`'Box Plot'`,`'Waterfall'`,`'Stacked Waterfall'`,`'Sunburst'`
`customDashKey.dashboardLayout.*.*.grouping` | | A statistical or mathematical function selected by the user from a predefined set, to be applied over the data and rendered in a chart. It takes one of the following values: `'Sum'`, `'Average'`, `'Minimum'` or `'Maximum'`.
`customDashKey.dashboardLayout.*.*.kpi` | | The KPI key or the list of KPI keys selected from the "**KPIs**" drop-down of a chart in a dashboard view if chart `type='kpis'`.
`customDashKey.dashboardLayout.*.*.level` | | The second-level aggregation selected from the "**Group By**" drop-down menu of a chart in a dashboard view.
<a name="level2">`customDashKey.dashboardLayout.*.*.level2`</a> | | The second-level aggregation selected from the "**Sub Group**" drop-down menu of a chart in a dashboard view.
`customDashKey.dashboardLayout.*.*.lockedLayout` | `False` | A boolean to indicate if the layout on this chart can be changed by users.
`customDashKey.dashboardLayout.*.*.statistic` | | The statistic selected from the "**Statistic**" drop-down menu of a chart in a dashboard view if the chart `type='stats'`
`customDashKey.dashboardLayout.*.*.type` | `'stats'` | This has two options: `'stats'` or `'kpis'`
`customDashKey.lockedLayout` | `False` | If `True`, prevents users from modifying the layout of a dashboard view by adding or removing charts.
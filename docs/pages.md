Configure your application's pages.

The pages are located under the path `pages`.

Arguments:
        
* `current_page`: `[str]` = `None` &rarr; The id of the current page that is being rendered.
* `data`: `[dict]` = `{}` &rarr; The data to pass to `pages.data.*`.

The pages data are located under the path `pages.data`.

 Arguments:
        
* `pageLayout`: `[list]` = `{}` &rarr; The layout of the page.
    * See: `cave_utils.api.pages.pages_data_star_pageLayout`.
* `lockedLayout`: `[bool]` = `False` &rarr; Whether or not the layout should be locked.
    * See: `cave_utils.api.pages.pages_data_star_pageLayout`.

The page layouts are located under the path `pages.data.pageLayout`.

Arguments:
        
* `type`: `[str]` = `"groupedOutput"` &rarr; The type of the page layout.
    * Accepted Values:
        * `"groupedOutput"`: The `unit` appears after the value.
        * `"globalOutput"`: The `unit` appears after the value, separated by a space.
        * `"map"`: The `unit` appears before the value.
* `variant`: `[str]` = `"bar"` &rarr; The variant of the page layout.
    * Accepted Values:
        * When `type` == `"groupedOutput"`:
            * `"area"`: An [area chart][]
            * `"bar"`: A [bar chart][]
            * `"stacked_bar"`: A [stacked bar chart][]
            * `"box_plot"`: A [box plot chart][]
            * `"cumulative_line"`: A cumulative line chart
            * `"gauge"`: A [gauge chart][]
            * `"heatmap"`: A [heatmap chart][]
            * `"line"`: A [line chart][]
            * `"scatter"`: A [scatter chart][]
            * `"stacked_area"`: An [stacked area chart][]
            * `"stacked_waterfall"`: An [stacked waterfall chart][]
            * `"sunburst"`: A [sunburst chart][]
            * `"table"`: A table showing the aggregated values.
            * `"treemap"`: A [treemap chart][]
            * `"waterfall"`: A [waterfall chart][]
        * When `type` == `"globalOutput"`:
            * `"bar"`: A [bar chart][]
            * `"line"`: A [line chart][]
            * `"table"`: A [table chart][]
            * `"overview"`: A summary of the global outputs presented in a KPI-like format
        * Otherwise:
            * `None`
* `mapId`: `[str]` = `None` &rarr; The id of the map to use.
* `groupingId`: `[list]` = `None` &rarr; The ids of the grouping to use.
* `sessions`: `[list]` = `None` &rarr; The ids of the sessions to use.
* `globalOutput`: `[list]` = `None` &rarr; The ids of the global outputs to use.
* `groupingLevel`: `[list]` = `None` &rarr; The ids of the grouping levels to use.
* `lockedLayout`: `[bool]` = `False` &rarr; Whether or not the layout should be locked.
* `statAggregation`: `[str]` = `"sum"` &rarr; A stat aggregation function to apply to the chart data.
    * Accepted Values:
        * `"sum"`: Add up aggregated data
        * `"mean"`: Calculate the mean of the aggregated data
        * `"min"`: Find the minimum values within the aggregated data
        * `"max"`: Find the maximum values the aggregated data
* `groupedOutputDataId`: `[list]` = `None` &rarr; The list of ids representing the grouped output data to use.
* `statId`: `[list]` = `None` &rarr; The list of ids corresponding to the stat(s) to be used.
* `showToolbar`: `[bool]` = `None` &rarr; Whether or not the chart toolbar should be shown.
    * Note: If left unspecified (i.e., `None`), it will default to `settings.showToolbar`.
* `maximized`: `[bool]` = `False` &rarr; Whether or not the layout should be maximized.
    * Note: If more than one chart belonging to the same page layout is set to `True`, the first one found in the list will take precedence.

[area chart]: https://en.wikipedia.org/wiki/Area_chart
[bar chart]: https://en.wikipedia.org/wiki/Bar_chart
[stacked bar chart]: https://en.wikipedia.org/wiki/Bar_chart
[box plot chart]: https://en.wikipedia.org/wiki/Box_plot
[cumulative line chart]: #
[gauge chart]: https://echarts.apache.org/examples/en/index.html#chart-type-gauge
[heatmap chart]: https://en.wikipedia.org/wiki/Heat_map
[line chart]: https://en.wikipedia.org/wiki/Line_chart
[scatter chart]: https://en.wikipedia.org/wiki/Scatter_plot
[stacked area chart]: https://en.wikipedia.org/wiki/Area_chart
[stacked waterfall chart]: https://en.wikipedia.org/wiki/Waterfall_chart
[sunburst chart]: https://en.wikipedia.org/wiki/Pie_chart#Ring_chart,_sunburst_chart,_and_multilevel_pie_chart
[table chart]: #
[treemap chart]: https://en.wikipedia.org/wiki/Treemapping
[waterfall chart]: https://en.wikipedia.org/wiki/Waterfall_chart
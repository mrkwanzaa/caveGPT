Configure the style and UI elements of your application's maps.

The `colorByOptions` group is located at the path `maps.data.*.legendGroups.*.data.*.colorByOptions`.

Arguments:
        
* `startGradientColor`: `[str]` &rarr; The starting color for the gradient.
    * Notes:
        * It must be a valid RGBA string
        * This attribute is only required for numeric props
    * Example: `"rgba(255, 255, 255, 1)"`.
* `endGradientColor`: `[str]` &rarr; The ending color for the gradient.
    * Notes:
        * It must be a valid RGBA string
        * This attribute is only required for numeric props
    * Example: `"rgba(255, 255, 255, 1)"`.
* `customKey`: `[str]` &rarr; A color (RGBA string) assigned to a categorical value.
    * Notes:
        * You should provide one `customKey` per option key in the associated prop.
        * This attribute is only required for numeric props
* `min`: `[float | int]` = `None` &rarr; The minimum value for calculating the gradient.
    * Note: If `None`, the minimum of the relevant data will be used.
* `min`: `[float | int]` = `None` &rarr; The maximum value for calculating the gradient.
    * Note: If `None`, the maximum of the relevant data will be used.
* `nullColor`: `[str]` = `None` &rarr; The color to use for null values.
    * Note: If `None`, null values will not be shown.

The maps are located under the path `maps`.

Arguments:
        
* `additionalMapStyles`: `[dict]` = `{}` &rarr;
    * A dictionary of map specifications that define alternative visual appearances of a map.
* `data`: `[dict]` = `{}` &rarr; The data to pass to `maps.data.*`.

The additional map styles are located under the path `maps.additionalMapStyles.*`.
Arguments:

* `name`: `[str]` &rarr; The name of the map style.
* `icon`: `[str]` = `"md/MdMap"` &rarr; The icon to show in the map selection menu.
* `spec​`: `[dict | str]` &rarr; The spec to generate the map
    * Notes:
        * If `spec​` is a string, it will be treated as a URL to a JSON spec file.
        * `spec​` is only validated for its type, which can be either a `dict` or a `str`.
    * See:
        * Mapbox: https://docs.mapbox.com/api/maps/styles/
        * Carto: https://github.com/CartoDB/basemap-styles/blob/master/docs/basemap_styles.json
        * Raster: https://docs.mapbox.com/mapbox-gl-js/example/map-tiles/
* `fog`: `[dict]` = `None` &rarr; The fog to show in the map selection menu.
    * Note: `fog` is only validated for its type (`dict`).
    * See: https://docs.mapbox.com/mapbox-gl-js/api/map/#map#setfog

The maps are located under the path `maps.data.*`.

Arguments:
        
* `name`: `[str]` &rarr; The name of the map.
* `currentStyle`: `[str]` = `None` &rarr; The map's style id applied when the map is first loaded.
* `currentProjection`: `[str]` = `None` &rarr; The map's projection id applied when the map is first loaded.
    * Accepted Values:
        * `"mercator"`: The [Mercator projection][]
        * `"globe"`: The map is displayed as a 3D globe
* `defaultViewport`: `[dict]` = `None` &rarr; The default viewport to use.
    * Note: The value of this attribute should match the structure of a viewport object.
    * See: `cave_utils.api.maps.viewport`
* `optionalViewports`: `[dict]` = `None` &rarr; The optional viewports that can be selected by the end user.
    * Note: The value of this attribute should match the structure of a dictionary of viewport objects.
    * See: `cave_utils.api.maps.viewport`
* `legendGroups`: `[dict]` = `None` &rarr; The legend groups to show in the map selection menu.

[Mercator projection]: https://en.wikipedia.org/wiki/Mercator_projection

The legend groups are located under the path `maps.data.*.legendGroups.*`.

Arguments:
        
* `name`: `[str]` &rarr; The name of the legend group as displayed in the Map Legend.
* `data`: `[dict]` &rarr; The relevant `data` dictionary for this legend group.
    * See: `cave_utils.api.maps.maps_data_star_legendGroups_star_data_star`

The legend group data is located under the path `maps.data.*.legendGroups.*.data.*`.

Arguments:
        
* `value`: `[bool]` &rarr; Whether or not to show this data layer on the map.
* `sizeBy`: `[str]` = `None` &rarr; The prop id to use for sizing the data layer.
    * Notes:
        * If `None`, the data layer will not be sized
        * Does not apply to shape layers
* `colorBy`: `[str]` = `None` &rarr; The prop id to use for coloring the data layer.
    * Note: If `None`, the data layer will not be colored
* `lineBy`: `[str]` = `"solid"` &rarr; The type of line to use for the data layer.
    * Accepted Values:
        * `"solid"`: Represents a single continuous line.
        * `"dashed"`: A series of dashes or line segments
        * `"dotted"`: A dotted line
    * Note: This attribute is applicable exclusively to `arc` layers.
* `allowGrouping`: `[bool]` = `False` &rarr; Whether or not to allow grouping of the data layer.
    * Note: This attribute is applicable exclusively to `node` layers.
* `group`: `[bool]` = `False` &rarr; Whether or not to group the data layer.
    * Notes:
        * If `False`, the data layer will not be grouped
        * This attribute is applicable exclusively to `node` layers
* `groupCalcBySize`: `[str]` = `"count"` | `"mode"` &rarr; The aggregation function to use on the prop specified in `sizeBy`.
    * Accepted Values:
        * When `sizeBy` prop's `type` == `"num"`:
            * `"count"`: Total number of nodes in the cluster
            * `"sum"`: Total sum of values within the cluster
            * `"mean"`: Average value within the cluster
            * `"median"`: Median value within the cluster
            * `"mode"`: Most frequently occurring value within the cluster
            * `"max"`: Maximum value within the cluster
            * `"min"`: Minimum value within the cluster
        * When `sizeBy` prop's `type` == `"toggle"`:
            * `"mode"`: Most frequently occurring value within the cluster
            * `"and"`: Determine if all values in the cluster are `True`
            * `"or"`: Determine if at least one value in the cluster is `True`
        * When `sizeBy` prop's `type` == `"selector"`:
            * `"mode"`: Most frequently occurring value within the cluster
    * Notes:
        * If `None`, the data layer will not be grouped
        * The calculation is based on the values of the prop specified in `sizeBy`
        * The default value for a `sizeBy` prop of type `"num"` is `"count"`. For other types, the default value is `"mode"`.
        * This attribute is applicable exclusively to `node` layers
* `groupCalcByColor`: `[str]` = `"count"` | `"mode"` &rarr; The aggregation function to use on the prop specified in `colorBy`.
    * Accepted Values:
        * When `colorBy` prop's `type` == `"num"`:
            * `"count"`: Total number of nodes in the cluster
            * `"sum"`: Total sum of values within the cluster
            * `"mean"`: Average value within the cluster
            * `"median"`: Median value within the cluster
            * `"mode"`: Most frequently occurring value within the cluster
            * `"max"`: Maximum value within the cluster
            * `"min"`: Minimum value within the cluster
        * When `colorBy` prop's `type` == `"toggle"`:
            * `"mode"`: Total number of nodes in the cluster
            * `"and"`: Determine if all values in the cluster are `True`
            * `"or"`: Determine if at least one value in the cluster is `True`
        * When `colorBy` prop's `type` == `"selector"`:
            * `"mode"`: Most frequently occurring value within the cluster
    * Notes:
        * If `None`, the data layer will not be grouped
        * The calculation is based on the prop specified in `colorBy`
        * The default value for a `colorBy` prop of type `"num"` is `"count"`. For other types, the default value is `"mode"`.
        * This attribute is applicable exclusively to `node` layers
* `groupScaleWithZoom`: `[bool]` = `False` &rarr; Whether or not to scale the group size with zoom.
    * Notes:
        * If `False`, the group size will be constant as set by `groupScale`
        * This attribute is applicable exclusively to `node` layers
* `groupScale`: `[float | int]` = `None` &rarr; The zoom level at which to conduct grouping of the nodes.
    * Notes:
        * If `None`, the group scale will be determined by the map zoom.
        * This attribute is applicable exclusively to `node` layers
* `colorByOptions`: `[dict]` = `None` &rarr; The options for coloring the data layer.
    * Notes:
        * If `None`, the data layer will not be colored.
        * Does not apply to shape layers
        * Only props of type `"num"`, `"toggle"`, and `"selector"` can be colored.
    * Example:
        ```py
        "colorByOptions": {
            "numericPropExample": {
                "min": 0,
                "max": 20,
                "startGradientColor": "rgba(233, 0, 0, 255)",
                "endGradientColor": "rgba(96, 2, 2, 255)",
            },
            "selectorPropExample": {
                "apple": "rgba(199,55,47,255)",
                "orange": "rgba(255,127,0, 255)",
                "pear": "rgba(209,226,49, 255)",
            }
        }
        ```
    * See: `cave_utils.api.maps.colorByOptions`
* `sizeByOptions`: `[dict]` = `None` &rarr; The options for sizing the data layer.
    * Notes:
        * If `None`, the data layer will not be sized.
        * Does not apply to shape layers
        * Only props of type `"num"` can be sized.
    * Example:
        ```py
        "sizeByOptions": {
            "numericPropExample": {
                "min": 0,
                "max": 20,
                "startSize": "8px",
                "endSize": "32px",
            }
        }
        ```
    * See: `cave_utils.api.maps.sizeByOptions`
* `icon`: `[str]` = `None` &rarr; The icon to use for the data layer.
    * Notes:
        * Arc layer icons are determined by `lineBy`.
        * Shape layer icons are always the default icon.
        * This attribute is applicable exclusively to `node` layers

The `sizeByOptions` group is located at the path `maps.data.*.legendGroups.*.data.*.sizeByOptions`.
Arguments:
        
* `startSize`: `[str]` &rarr; The starting size for the gradient.
    * Notes:
        * It must be a valid pixel string.
        * This attribute is only required for numeric props
    * Example: `"10px"`.
* `endSize`: `[str]` &rarr; The ending size for the gradient.
    * Notes:
        * It must be a valid pixel string.
        * This attribute is only required for numeric props
    * Example: `"10px"`.
* `endSize`: `[str]` &rarr; The ending size for the gradient.
    * Notes:
        * It must be a valid pixel string.
        * This attribute is only required for numeric props
    * Example: `"10px"`.
* `customKey`: `[str]` &rarr; A pixel size assigned to a categorical value.
    * Notes:
        * You should provide one `customKey` per option key in the associated prop.
        * This attribute is only required for numeric props
* `min`: `[float | int]` = `None` &rarr; The minimum value for calculating the size.
    * Note: If `None`, the minimum of the relevant data will be used.
* `min`: `[float | int]` = `None` &rarr; The maximum value for calculating the size.
    * Note: If `None`, the maximum of the relevant data will be used.
* `nullSize`: `[str]` = `None` &rarr; The size to use for null values.
    * Note: If `None`, null values will not be shown.

The viewports can be located at the paths `maps.data.*.defaultViewport` and `maps.data.*.optionalViewports.*`.
Arguments:
        
* `latitude`: `[float | int]` &rarr; The latitude of the viewport.
    * Note: The value must be between -90 and 90.
* `longitude`: `[float | int]` &rarr; The longitude of the viewport.
    * Note: The value must be between -180 and 180.
* `zoom`: `[float | int]` &rarr; The zoom of the viewport.
    * Note: The value must be between 0 and 22.
* `bearing`: `[float | int]` = `None` &rarr; The bearing of the viewport.
    * Note: The value must be between 0 and 360.
* `pitch`: `[float | int]` = `None` &rarr; The pitch of the viewport.
    * Note: The value must be between 0 and 60.
* `maxZoom`: `[float | int]` = `None` &rarr; The maximum zoom of the viewport.
    * Note: The value must be between 0 and 22.
* `minZoom`: `[float | int]` = `None` &rarr; The minimum zoom of the viewport.
    * Note: The value must be between 0 and 22.
* `icon`: `[str]` = `"md/MdGpsFixed"` &rarr; The icon to use for the viewport.
* `name`: `[str]` = `None` &rarr; The name of the viewport.
    * Note: Only used for optional viewports.
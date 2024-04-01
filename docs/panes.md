Panes serve as main containers for UI controls such as toggles, text
and number fields, sliders, etc. They can also contain buttons that
facilitate interaction with actionable data.

The panes are located under the path `panes`.

Arguments:
* `data`: `[str]` &rarr; The data to pass to `panes.data.*`.
* `paneState`: `[dict]` &rarr;
    * A dictionary of pane states per their location in the `appBar` object.
    * Accepted Values:
        * `"left"`: The state of a pane triggered from the left-side app bar.
        * `"center"`: The pane state of a centered modal.
        * `"right"`: The state of a pane triggered from the right-side app bar.
    * Note: In the vast majority of use cases, the `paneState` dictionary is not relevant to the design of the CAVE App, as its primary purpose is to store temporary UI state during user interactions. Nevertheless, a CAVE App designer has the option to prepopulate it if required.

The pane data is located under the path `panes.data.*`.

Arguments:
        
* `name`: `[str]` &rarr; The name of the pane.
* `props`: `[dict]` &rarr; The props that will be rendered in the pane.
    * See: `cave_utils.api_utils.general.props`
* `values`: `[dict]` = `None` &rarr;
    * The values to be assigned to the respective props. Each value is associated with its corresponding prop based on the key name used in `props`.
    * See: `cave_utils.api_utils.general.values`
* `layout`: `[dict]` =`{"type": "grid", "numColumns": "auto", "numRows": "auto"}` &rarr;
    * The layout of the pane.
    * See: `cave_utils.api_utils.general.layout`

The pane states are located under the path `panes.paneState.*`.
Arguments:

* `left`: `[dict]` = `"wall"` &rarr; The state of a pane activated from the left-side app bar.
* `center`: `[dict]` = `"wall"` &rarr; The state of a centered modal.
* `right`: `[dict]` = `"wall"` &rarr; The state of a pane activated from the right-side app bar.

The pane state data is located under the path `panes.paneState.*.*`.

Arguments:
        
* `pin`: `[bool]` = `False` &rarr; Whether or not the pane is pinned.
    * Note: Only used for panes located on `"left"` or `"right"` side app bars.
* `type`: `[str]` = `"pane"` &rarr; The context that activated the current visible pane.
    * Accepted Values:
        * `"pane"`: A pane triggered from the `"left"` or `"right"` side app bars.
        * `"feature"`: Map feature data is displayed in the `"center"` of the screen.
    * Note: In the vast majority of use cases, the `type` attribute is not relevant to the design of the CAVE App, as its primary purpose is to store temporary UI state during user interactions. Nevertheless, a CAVE App designer has the option to prepopulate it if required.
* `open`: `[str | dict]` = `None` &rarr;
    * The id of the open pane or a dictionary containing data related to a specific datapoint of a map feature.
    * Notes:
        * In the vast majority of use cases, the `open` attribute is not relevant to the design of the CAVE App, as its primary purpose is to store temporary UI state during user interactions. Nevertheless, a CAVE App designer has the option to prepopulate it if required.
        * For validation purposes or in advanced use cases, this attribute must correspond with the id (i.e., the dictionary key) of a pane located under `panes.data` when `type` is set to `"pane"`.
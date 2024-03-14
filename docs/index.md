* **`settings`**: `[dict]` &rarr; General settings for your application.
    * **Note**: `settings.iconUrl` is the only required field in `settings`
    * **See**: `cave_utils.api.settings`
* **`appBar`**: `[dict]` &rarr; Configure actions for your app bar(s).
    * **Note**: `appBar.data` is required and should have at least one item in it.
    * **See**: `cave_utils.api.appBar`
* **`panes`**: `[dict]` = `{}` &rarr; Configure panes for your application.
    * **See**: `cave_utils.api.panes`
* **`pages`**: `[dict]` = `{}` &rarr; Configure pages for your application.
    * **See**: `cave_utils.api.pages`
* **`maps`**: `[dict]` = `{}` &rarr; Configure map views and settings for your application, including coloring and sizing of mapFeatures.
    * **See**: `cave_utils.api.maps`
* **`mapFeatures`**: `[dict]` = `{}` &rarr;
    * Configure the prop values for map features (interactive items on the map) for your application.
    * **See**: `cave_utils.api.mapFeatures`
* **`groupedOutputs`**: `[dict]` = `{}` &rarr;
    * Configure data that can be sliced and diced for charts and tables based on arbitrary groups.
    * **See**: `cave_utils.api.groupedOutputs`
* **`globalOutputs`**: `[dict]` = `{}` &rarr;
    * Configure data that is general to the entire application and can be compared across sessions.
    * **See**: `cave_utils.api.globalOutputs`
* **`extraKwargs`**: `[dict]` = `{}` &rarr; Special arguments to be passed to the server.
    * **See**: `cave_utils.api.extraKwargs`
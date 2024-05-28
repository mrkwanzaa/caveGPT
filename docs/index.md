* `settings`: `[dict]` &rarr; General settings for your application. Includes settings for sync, time, and debug mode.
    * See: `cave_utils.api.settings`
* `appBar`: `[dict]` &rarr; Configure actions for your app bar(s).
    * Note: `appBar.data` is required and should have at least one item in it.
    * See: `cave_utils.api.appBar`
* `panes`: `[dict]` = `{}` &rarr; Configure panes for your application and set the currently open pane(s).
    * See: `cave_utils.api.panes`
* `pages`: `[dict]` = `{}` &rarr; Configure pages for your application and set the currently open page(s). This key also modifies the displayed charts.
    * See: `cave_utils.api.pages`
* `maps`: `[dict]` = `{}` &rarr; Configure map views and settings for your application, including coloring and sizing of interactive items on the map.
    * See: `cave_utils.api.maps`
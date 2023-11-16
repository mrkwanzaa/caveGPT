The app bar is a key element of the CAVE App, positioned on the left or

right side of the screen. It provides actions that allow users to
navigate between [pages][], launch [panes][], and interact with the
CAVE API through [predefined][] or [custom][] commands.

If specified, both left and right side app bars can be displayed
simultaneously.

[pages]: pages.html
[panes]: panes.html
[predefined]: #appBar_data_star.spec
[custom]: #appBar_data_star.spec

## Classes

The app bar is located under the path **`appBar`**.

The app bar data is located under the path **`appBar.data`**.

Arguments:

* **`icon`**: `[str]` &rarr; An icon to display in the center of the action element.
    * **Note**: It must be a valid icon name from the [react-icons][] bundle, preceded by the abbreviated name of the icon library source.
    * **Example**: `"md/MdRocket"`.
* **`type`**: `[str]` &rarr; The type of object displayed when the action is triggered.
    * **Accepted Values**:
        * `"session"`: The Session Pane
        * `"settings"`: The Application Settings Pane
        * `"button"`: A button that allows you to send a command to the CAVE API
        * `"pane"`: A [custom pane][]
        * `"page"`: A [page][]
* **`bar`**: `[str]` &rarr; The location of the action element.
    * **Accepted Values**:
        * `"upperLeft"`: Upper section of the left-side bar
        * `"lowerLeft"`: Lower section of the left-side bar
        * `"upperRight"`: Upper section of the right-side bar
        * `"lowerRight"`: Lower section of the right-side bar
* **`variant`**: `[str]` = `None` &rarr; The variant of the button.
    * **Accepted Values**:
        * When **`type`** == `"pane"` | `"page"`:
            * `"modal"`: A [modal pane][]
            * `"wall"`: A [wall pane][]
        * Otherwise:
            * `None`
* **`color`**: `[str]` = `<system-default-value>` &rarr;
    * The color of the button. If omitted, the default value is set by the system.
    * **Note**: It must be a valid RGBA string.
    * **Example**: `"rgba(255, 255, 255, 1)"`.
* **`apiCommand`**: `[str]` = `None` &rarr; The name of the [API command][] to trigger.
* **`apiCommandKeys`**: `[list]` = `None` &rarr;
    * The root API keys to pass to your `execute_command` function if an
    `apiCommand` is provided. If omitted, all API keys are
    passed to `execute_command`.

[page]: pages.html
[pane]: panes.html
[modal pane]: panes.html
[wall pane]: panes.html
[API command]: #appBar_data_star.spec
[react-icons]: https://react-icons.github.io/react-icons/search
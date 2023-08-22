# CAVE API Design
This document describes the data structure scheme used by a CAVE application to render custom user interfaces that accommodate to the use cases and preferences of an API designer. For the purposes of this documentation, an API designer is any person using the CAVE API code to create a CAVE App user experience.

## CAVE API Structure
The CAVE API Structure is the core data structure required for user interface design of the CAVE App. Its primary purpose is to place, rearrange, style, and specify the behavior of most of the UI elements in a CAVE application.

At first glance, the top-level keys in the data structure look like this:
```py
{
    'appBar': {...},
    'arcs': {...},
    'categories': {...},
    'dashboards': {...},
    'geos': {...},
    'kpis': {...},
    'kwargs':{...},
    'maps': {...},
    'nodes': {...},
    'panes': {...},
    'settings': {...},
    'stats': {...}
}
```
Throughout this documentation, we refer to the keys in the data structure above as _top-level keys_ (or _top-level groups_ to point out that these keys contain other key-value pairs).

Each top-level group might include unique elements or sub-keys that are specific to that group. However, other keys like `sendToApi` are meant to attach functionality that is more generic and therefore can be used in different top-level groups.

### Top-Level keys

- #### `appBar`
    The `appBar` key allows API designers to create a custom bar located on the left of the CAVE app. Changing values within this key allows users to switch between viewing the different maps, dashboards, and kpi views, as well as opening panes.

- #### `arcs`
    The `arcs` group contains data that is typically used to visualize flows between two points on the "**Map**" view. Depending on the nature of the flows and the purpose of the visualization, the flows between two locations can be represented by a single arc (source and destination) or a sequence of arc segments representing a path

- #### `dashboards`
    The `dashboards` key allows API designers to create custom dashboards for displaying charts and tables of statistics and kpi data. Editing values within this key allows for information and layout of the charts and tables to be specified, as well as whether the dashboards can be edited by the user.

- #### `geos`
    The `geos` group contains data that is typically used to visualize geographic areas on the "**Map**" view. Geos often represent districts, countries, states, provinces, or zip codes. The property by which geos are colored is set in maps

- #### `kpis`
    The `kpis` group contains all the KPI data that will be displayed on the "**KPI**" view. These are typically highly aggregated statistics calculated by the api. In general, KPIs are used to compare values across sessions and give a high level overview of output. Filters and aggregations will not affect `kpis`. The `kpis` group is also used to set which kpis are shown on the map

- #### `maps`
    This key group allows designers to specify information about the starting state of the map, as well as what node, arc, and geo types are displayed and what the arcs, nodes, and geos are sized and colored by. This group also controls what viewports can be easily jumped to by the user.

- #### `nodes`
    The `nodes` group contains data that is typically used to visualize single geographic locations in the "**Map**" view. Nodes often represent buildings such as warehouses, distribution centers, and stores.

- #### `panes`
    The `panes` group controls the current state of all panes. Panes are constructs primarily used to place UI controls (toggles, text and number fields, sliders, etc.), as well as buttons to allow interaction with actionable data. Custom panes can be designed to enable users to tune up the parameters of a simulation, navigate through different case study scenarios, reset the state of a simulation, synchronize data or settings with other users, and so on. Note that panes are opened or closed through the `appBar` top-level key.

- #### `stats`
    The `stats` group takes parameter data that can use its raw values to display in a dashboard view.

- #### `special`
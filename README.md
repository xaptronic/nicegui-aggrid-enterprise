# NiceGUI AG Grid Enterprise

This is a custom component for NiceGUI that integrates AG Grid Enterprise, a powerful and feature-rich data grid for JavaScript. This component allows you to easily incorporate AG Grid Enterprise into your NiceGUI applications, providing advanced grid functionalities such as sorting, filtering, editing, and enterprise features like row grouping, aggregation, Excel export, and more.

**AG Grid Enterprise Version:** 35.0.0
**Requires:** NiceGUI ≥ 3.0.0

## Installation

To install the NiceGUI AG Grid Enterprise component, use the following pip command:

```bash
pip install nicegui-aggrid-enterprise
```

## Usage

### Basic Example

```python
from nicegui import ui
from nicegui_aggrid_enterprise import aggrid

# Set license key (required for enterprise features)
aggrid.license_key = "MY_AGGRID_LICENSE_KEY"

# Define grid options
options = {
    'columnDefs': [
        {'headerName': 'Make', 'field': 'make'},
        {'headerName': 'Model', 'field': 'model'},
        {'headerName': 'Price', 'field': 'price'}
    ],
    'rowData': [
        {'make': 'Toyota', 'model': 'Celica', 'price': 35000},
        {'make': 'Ford', 'model': 'Mondeo', 'price': 32000},
        {'make': 'Porsche', 'model': 'Boxster', 'price': 72000}
    ],
    'rowSelection': 'single',
    'editable': True
}

# Create an instance of aggrid
grid = aggrid(options)

# Start the NiceGUI application
ui.run()
```

### From Pandas DataFrame

```python
import pandas as pd
from nicegui import ui
from nicegui_aggrid_enterprise import aggrid

aggrid.license_key = "MY_AGGRID_LICENSE_KEY"

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
})

grid = aggrid.from_pandas(df, theme='quartz')

ui.run()
```

### From Polars DataFrame

```python
import polars as pl
from nicegui import ui
from nicegui_aggrid_enterprise import aggrid

aggrid.license_key = "MY_AGGRID_LICENSE_KEY"

df = pl.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
})

grid = aggrid.from_polars(df, theme='alpine')

ui.run()
```

## Features

- **Enterprise Features**: All AG Grid Enterprise features including row grouping, aggregation, pivoting, Excel export, clipboard, master/detail, tree data, and more.
- **Themes**: Support for AG Grid's built-in themes (`quartz`, `balham`, `material`, `alpine`) with automatic dark mode support.
- **Auto-size Columns**: Automatically resize columns to fit the grid width (enabled by default).
- **DataFrame Support**: Create grids directly from Pandas or Polars DataFrames.
- **Full API Access**: Run AG Grid API methods via `run_grid_method()` and `run_row_method()`.
- **Event Handling**: Subscribe to AG Grid events.
- **Client-side Editing**: Get edited data back from the client.

## Parameters

- `options`: Dictionary of AG Grid options
- `html_columns`: List of column indices that should render HTML content (default: `[]`)
- `theme`: AG Grid theme - `"quartz"`, `"balham"`, `"material"`, or `"alpine"` (default: `"quartz"`)
- `auto_size_columns`: Whether to automatically resize columns to fit the grid width (default: `True`)

## License

This package is MIT licensed. Note that AG Grid Enterprise requires a separate commercial license from AG Grid Ltd.

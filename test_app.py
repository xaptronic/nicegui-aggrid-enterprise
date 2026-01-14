"""Test script for nicegui-aggrid-enterprise plugin."""

from nicegui import ui

from nicegui_aggrid_enterprise import AgGridEnterprise, AgGridEnterpriseCharts

# Set your license key here (or leave as None to test without - watermark will show)
AgGridEnterprise.license_key = None  # "YOUR_LICENSE_KEY_HERE"
AgGridEnterpriseCharts.license_key = None  # "YOUR_LICENSE_KEY_HERE"

# Sample data
ROW_DATA = [
    {"make": "Toyota", "model": "Celica", "price": 35000, "available": True},
    {"make": "Ford", "model": "Mondeo", "price": 32000, "available": False},
    {"make": "Porsche", "model": "Boxster", "price": 72000, "available": True},
    {"make": "BMW", "model": "M3", "price": 60000, "available": True},
    {"make": "Audi", "model": "A4", "price": 40000, "available": False},
    {"make": "Mercedes", "model": "C-Class", "price": 45000, "available": True},
]


def main():
    ui.label("AG Grid Enterprise Test").classes("text-2xl font-bold mb-4")

    # Theme selector
    theme_select = ui.select(
        ["quartz", "balham", "material", "alpine"],
        value="quartz",
        label="Theme",
    ).classes("w-48")

    # --- AgGridEnterprise (Community Charts) ---
    ui.label("AgGridEnterprise (with AG Charts Community)").classes("text-lg font-semibold mt-4")

    grid = AgGridEnterprise(
        {
            "columnDefs": [
                {"headerName": "Make", "field": "make", "sortable": True, "filter": True},
                {"headerName": "Model", "field": "model", "sortable": True, "filter": True},
                {
                    "headerName": "Price",
                    "field": "price",
                    "sortable": True,
                    "filter": "agNumberColumnFilter",
                    "editable": True,
                },
                {
                    "headerName": "Available",
                    "field": "available",
                    "cellRenderer": "checkboxRenderer",
                },
            ],
            "rowData": ROW_DATA,
            "rowSelection": {"mode": "multiRow"},  # New v32+ syntax
            "cellSelection": True,  # Replaces enableRangeSelection
            "enableCharts": True,  # Charts enabled (community)
        },
        theme="quartz",
    )

    # --- AgGridEnterpriseCharts (Enterprise Charts) ---
    ui.label("AgGridEnterpriseCharts (with AG Charts Enterprise)").classes("text-lg font-semibold mt-6")

    grid_charts = AgGridEnterpriseCharts(
        {
            "columnDefs": [
                {"headerName": "Make", "field": "make", "sortable": True, "filter": True, "chartDataType": "category"},
                {"headerName": "Model", "field": "model", "sortable": True, "filter": True},
                {
                    "headerName": "Price",
                    "field": "price",
                    "sortable": True,
                    "filter": "agNumberColumnFilter",
                    "chartDataType": "series",
                },
            ],
            "rowData": ROW_DATA,
            "rowSelection": {"mode": "multiRow"},  # New v32+ syntax
            "cellSelection": True,  # Replaces enableRangeSelection
            "enableCharts": True,  # Enterprise charts with full features
        },
        theme="quartz",
    )

    # Update theme when selection changes
    def update_theme():
        grid.theme = theme_select.value
        grid.update()
        grid_charts.theme = theme_select.value
        grid_charts.update()

    theme_select.on_value_change(update_theme)

    # Buttons to demonstrate API
    with ui.row().classes("mt-4 gap-2"):
        ui.button("Get Selected Rows", on_click=lambda: show_selected(grid))
        ui.button("Get All Data", on_click=lambda: show_all_data(grid))
        ui.button("Add Row", on_click=lambda: add_row(grid))

    # Output area
    ui.label("Output:").classes("mt-4 font-bold")
    output = ui.log().classes("w-full h-32")

    async def show_selected(g):
        rows = await g.get_selected_rows()
        output.push(f"Selected rows: {rows}")

    async def show_all_data(g):
        data = await g.get_client_data()
        output.push(f"All data: {data}")

    def add_row(g):
        new_row = {"make": "Tesla", "model": "Model S", "price": 80000, "available": True}
        g.options["rowData"].append(new_row)
        g.update()
        output.push(f"Added row: {new_row}")

    # Dark mode toggle
    dark = ui.dark_mode()
    with ui.row().classes("mt-4"):
        ui.switch("Dark Mode", on_change=lambda e: dark.set_value(e.value))

    # Show pandas example if available
    try:
        import pandas as pd

        ui.label("Pandas DataFrame Example").classes("text-xl font-bold mt-8 mb-4")

        df = pd.DataFrame(
            {
                "Name": ["Alice", "Bob", "Charlie", "Diana"],
                "Age": [25, 30, 35, 28],
                "City": ["New York", "London", "Paris", "Tokyo"],
                "Salary": [50000, 60000, 70000, 55000],
            }
        )

        AgGridEnterprise.from_pandas(df, theme="alpine")

    except ImportError:
        ui.label("Install pandas to see DataFrame example").classes("text-gray-500 mt-4")


if __name__ in {"__main__", "__mp_main__"}:
    main()
    ui.run(title="AG Grid Enterprise Test", reload=False)

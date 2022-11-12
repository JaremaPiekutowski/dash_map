# MAP DASHBOARD
# Imports
from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components.layout import create_layout
from src.data.loader import load_transaction_data

DATA_PATH = "./src/data/regions_data.xlsx"


def main() -> None:
    # load data
    data = load_transaction_data(path=DATA_PATH)
    # run app with Bootstrap styling
    app = Dash(external_stylesheets=[BOOTSTRAP])
    # Set title
    app.title = "Dane dla Województw"
    # Set layout
    app.layout = create_layout(app, data)
    # Run app
    app.run()


if __name__ == "__main__":
    main()

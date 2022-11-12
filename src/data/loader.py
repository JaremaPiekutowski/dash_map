import pandas as pd


class DataSchema:
    ID = "id"
    PO = "po"
    PIS = "pis"
    REGION = "region"
    FLAT_SURFACE = "pow_mieszk"
    TURNOUT = "frekwencja"
    UNEMPLOYMENT = "bezrobocie"
    MATERIAL_SIT = "sytuacja_mat"
    CINEMA_VIS = "kina_widz"
    DOCTORS = "lekarze"


def load_transaction_data(path: str) -> pd.DataFrame:
    # load the data from a CSV file
    data = pd.read_excel(
        path,
        dtype={
            DataSchema.ID: int,
            DataSchema.REGION: str,
            DataSchema.FLAT_SURFACE: float,
            DataSchema.TURNOUT: float,
            DataSchema.UNEMPLOYMENT: float,
            DataSchema.MATERIAL_SIT: float,
            DataSchema.CINEMA_VIS: float,
            DataSchema.DOCTORS: float
        },
    )

    return data

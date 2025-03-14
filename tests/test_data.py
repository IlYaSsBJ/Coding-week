import pandas as pd

DATA_PATH = "data/dataset.csv"

def test_dataset_loading():
    """Test du chargement du dataset"""
    df = pd.read_csv(DATA_PATH)
    assert not df.empty, "⚠ Le dataset est vide"

def test_data_types():
    """Test que les colonnes numériques sont bien au bon format"""
    df = pd.read_csv(DATA_PATH)
    numerical_columns = ["Age", "Height", "Weight"]
    
    for col in numerical_columns:
        assert df[col].dtype in ["int64", "float64"], f"⚠ Mauvais type de données pour {col}"
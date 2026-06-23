from pathlib import Path
import joblib
from .config import MODEL_PATH, METADATA_PATH


def load_model_and_metadata():
    model_path = Path(__file__).parent.parent / MODEL_PATH
    metadata_path = Path(__file__).parent.parent / METADATA_PATH
    model = joblib.load(model_path)
    metadata = joblib.load(metadata_path)
    return model, metadata

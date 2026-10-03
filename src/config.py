from pathlib import Path

# Update USERNAME after creating the repository if using a local clone.
ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
SYNTHETIC_DIR = DATA_DIR / "synthetic"

OUTPUT_DIR = ROOT / "outputs"
MODEL_DIR = OUTPUT_DIR / "models"
METRICS_DIR = OUTPUT_DIR / "metrics"
FIGURE_DIR = OUTPUT_DIR / "figures"

IMAGE_SIZE = 224
BATCH_SIZE = 32
NUM_WORKERS = 2
SEED = 42

LABELS = {
    "clean": 0,
    "motion_artifact": 1,
}

SEVERITY_LEVELS = ["none", "mild", "moderate", "severe"]

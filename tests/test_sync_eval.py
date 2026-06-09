import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.evaluation.evaluate_sync import evaluate_sync

session = "session_02"

evaluate_sync(
    offset_file=f"data/processed/aligned/{session}_offset.npy",
    session=session,
    output_path=f"results/tables/{session}_sync_metrics.json",
    fps=30
)
# Changelog

## 2026-07-07 — repository audit

- Added `.gitignore` entries for datasets and ML model artifacts: `processed_dataset/`, `*.keras`, `*.h5`, `*.onnx`, checkpoints and related outputs.
- Confirmed inspected current files contain no observed credentials.
- Classified project as an ML prototype/public candidate only after dataset/license review and reproducible training docs.

## Current version

- Image format normalization to 224x224 JPEG.
- Folder-based file renaming utility.
- MobileNetV2 transfer-learning classifier saved as `clothing_classifier.keras`.

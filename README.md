<p align="center">
  <img src="https://img.icons8.com/wired/128/007ACC/visual-search.png" width="80" />
</p>

# <p align="center">AuraVision</p>

<p align="center">
  <strong>Forensic Computer Vision and Surface Analysis for Existing Structures.</strong><br>
  Automated detection, segmentation, and volumetric repair estimation for structural pathologies.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Vision-OpenCV-007ACC?style=flat-square" />
  <img src="https://img.shields.io/badge/Logic-Scikit_Image-007ACC?style=flat-square" />
  <img src="https://img.shields.io/badge/Standards-ASTM_E2018-007ACC?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Research_Prototype-444444?style=flat-square" />
</p>

---

## 🔍 Forensic Methodology
AuraVision transforms the qualitative visual inspection process into a quantitative logic pipeline. By applying multi-scale ridge-detection filters, the engine isolates structural discontinuities (cracks) that are nearly invisible to the naked eye.

### Detection Pipeline
- **Ridge Filtering**: Implementing **Frangi** and **Hessian** kernels to enhance linear fractures against surface noise.
- **Morphological Segmentation**: Skeletonization to extract the "center-line" of detected pathologies for precise width calculation.
- **Severity Mapping**: Automatically categorizing defects according to **ASTM E2018** benchmarks (Minor, Moderate, Critical).

## 🏗️ Internal Roadmap

### 1. The Segmenter (`/core`)
- **`pathology_segmenter.py`**: The vision kernel. Supports different detection modes for 'cracks' (ridges) and 'spalling' (blobs).
- **`volume_engine.py`**: Calculates required repair materials (L/m³) based on segmented area and standard material depths.

### 2. The Forensic Lab (`/lab`)
- **`test_ridge_filters.py`**: Testing sensitivity thresholds under various site lighting exposures.

---

## 🚀 Usage

```python
from core.pathology_segmenter import PathologySegmenter

# 1. Initialize Forensic Eye
segmenter = PathologySegmenter(sensitivity=0.4, resolution_mm_px=0.5)

# 2. Process Site Image
result = segmenter.process_scan(img_array, pathology_type="crack")

print(f"Pathology Severity: {result['metrics']['severity_score']}")
```

---
<p align="center">
  <i>Part of the <b>Nexus-Twin</b> Ecosystem | Engineering Strategy by <b>Maycon Alves</b></i>
</p>

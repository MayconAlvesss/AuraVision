# 👁️ AuraVision: Structural Pathology Intelligence

**Automating Forensic Computer Vision and Surface Analysis for Existing Structures.**

AuraVision is a diagnostic engine built to detect, segment, and quantify structural pathologies (cracks, spalling, efflorescence) from raw site imagery and LiDAR scans. It transforms visual inspections from qualitative notes into quantitative, georeferenced engineering data.

---

## 🔬 Forensic Methodology

AuraVision utilizes a multi-stage vision pipeline optimized for concrete and masonry surfaces:

1. **Ridge Detection**: Implementation of multi-scale Frangi and Hessian filters to isolate linear discontinuities (cracks) from surface noise.
2. **Morphological Segmentation**: Cleaning extracted masks to remove non-structural artifacts.
3. **Volumetric Mapping**: Projecting segmented 2D areas onto 3D georeferenced LiDAR planes to calculate exact repair volumes (Liters/m³).

---

## 📂 Internal Roadmap

### Core Logic (`/core`)
- **`pathology_segmenter.py`**: The vision kernel. *[WIP: Optimizing ridge thresholds for low-light site conditions]*.
- **`volumetric_engine.py`**: Estimating material quantities based on standard repair depths (ASTM E2018).

### Experimental Lab (`/lab`)
- **`calibration_test.py`**: Benchmarking detection sensitivity under different exposure settings.

---

## ⚡ Technical Core
Built on **Python 3.12**, leveraging **OpenCV**, **Scikit-Image**, and **NumPy**. The engine is designed to be headless, exposing a high-performance **FastAPI** interface for integration with mobile inspection apps.

---

## 🛣️ 2028 Roadmap
- [ ] **LiDAR-Fusion**: Real-time projection of detected pathologies onto SLAM-generated point clouds.
- [ ] **Temporal Analysis**: Tracking crack propagation speeds over multiple inspection cycles.
- [ ] **Reinforcement Exposure Detection**: Specialized CNN for identifying exposed rebar and corrosion levels.

---

<div align="center">
  <i>Part of the <b>Nexus-Twin</b> Ecosystem</i><br>
  Engineering Strategy & Implementation by **Maycon Alves**
</div>

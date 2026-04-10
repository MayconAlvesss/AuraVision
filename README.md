# AuraVision: A Case for Automated Forensic Inspection

### The Inspection Challenge
Forensic engineering on existing structures often relies on manual, qualitative visual inspection. This introduces significant subjectivity—different engineers may categorize the same crack width or spalling severity differently. Furthermore, georeferencing these pathologies onto a 3D building model (BIM) is traditionally a slow, manual process.

### The AuraVision Solution
**AuraVision** was developed to bridge this gap by automating the detection and quantification of structural pathologies using forensic-grade computer vision and LiDAR projection.

---

### The Vision Detection Pipeline
The engine (`/core/pathology_segmenter.py`) utilizes a multi-stage approach to isolate structural defects from surface noise:

1. **Ridge Filtering**: Implementing multi-scale **Frangi** and **Hessian** filters to detect linear discontinuities (cracks) that are nearly invisible to the naked eye under poor lighting.
2. **Morphological Cleanup**: Using skeletonization to find the "center-line" of a fracture, allowing for the calculation of an average physical width.
3. **Severity Classification**: Automatically mapping detected area and density to **ASTM E2018** standards (Minor, Moderate, Critical).

### Volumetric Estimation & Repair Forecasting
Once a pathology is segmented, the `volume_engine.py` calculates the required material (Liters/m³) needed for repair. This is achieved by assuming standard repair depths for different spalling types, providing a high-fidelity procurement estimate directly from a site scan.

### Project Roadmap & Experimental Lab
- **`/lab`**: Contains benchmarking scripts for testing filter sensitivity under high-exposure site photos.
- **Future Integration**: Real-time LiDAR fusion to project 2D masks onto 3D georeferenced point clouds.

---

## 🛠️ Getting Started
AuraVision is a Python-based core engine with a FastAPI wrapper.

```bash
# 1. Setup
pip install -r requirements.txt

# 2. Test Detection
python lab/test_ridge_filters.py

# 3. Launch Forensic API
uvicorn api.main:app
```

---
*Developed by Maycon Alves | Advancing Building Technology and Structural Forensics.*

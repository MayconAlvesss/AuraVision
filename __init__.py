"""
AuraVision — Computer Vision & LiDAR Engine
===========================================
Forensic intelligence applied to automated structural inspection.
Integrates image processing with point cloud coordinates.

Architecture:
  core/      - Segmentation and vector decomposition logic
  api/       - FastAPI endpoints for site scan processing
  lab/       - Demonstration scripts for visual validation
  ml/        - Crack classification and pathology detection
"""

import os
from setuptools import setup, find_packages

setup(
    name="auravision",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "scikit-image",
        "numpy",
        "scipy",
        "pandas",
        "fastapi",
        "uvicorn",
        "plotly"
    ]
)

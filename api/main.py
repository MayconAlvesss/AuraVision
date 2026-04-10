"""
AuraVision — FastAPI Interface
==============================
Exposes the forensic vision engine as a RESTful service.
Allows external BIM/CDE platforms to submit site photos for pathology analysis.
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
import numpy as np
import cv2
from typing import List

from core.pathology_segmenter import PathologySegmenter

app = FastAPI(
    title="AuraVision API",
    description="Computer Vision & LiDAR Engine for Structural Inspection",
    version="1.0.0"
)

segmenter = PathologySegmenter(sensitivity=0.6)

@app.get("/")
async def root():
    return {"status": "AuraVision Engine Online", "visual_engines": ["frangi", "hessian", "lidar_projection"]}

@app.post("/analyze/scan")
async def analyze_scan(file: UploadFile = File(...)):
    """
    Receives a site photo and returns segmented pathology metrics.
    """
    # 1. Read image file into memory
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if image is None:
        raise HTTPException(status_code=400, detail="Invalid image file.")

    # 2. Process with forensic engine
    results = segmenter.process_scan(image)
    
    return {
        "filename": file.filename,
        "pathology_metrics": results,
        "diagnostic_summary": f"Detected {results['crack_length_px']}px of structural discontinuities."
    }

@app.post("/analyze/lidar-fusion")
async def fusion(image_file: UploadFile = File(...), cloud_json: dict = None):
    """
    Experimental: Fuses visual pathologies with LiDAR point cloud coordinates.
    """
    # Fusion logic skeleton
    return {"status": "Point cloud fusion algorithm not yet calibrated."}

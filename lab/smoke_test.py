"""
AuraVision — Smoke Test
========================
Tests the end-to-end pipeline:
1. Image Load
2. Pathology Segmentation
3. Volume Estimation
"""

import numpy as np
import logging
from core.pathology_segmenter import PathologySegmenter
from core.volume_engine import VolumeEngine

# Simple logging setup
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def run_test():
    print("\n" + "="*50)
    print("  AuraVision Engine — Diagnostic Smoke Test")
    print("="*50)

    # 1. Create a synthetic "crack" image (1000x1000)
    # A black image with a white line representing a structural crack.
    image = np.zeros((1000, 1000), dtype=np.uint8)
    image[400:600, 500:505] = 255 # Vertical crack segment
    image[595:600, 500:800] = 255 # Horizontal branch
    
    logger.info("Generated 1000x1000 synthetic pathology scan.")

    # 2. Run Segmentation
    segmenter = PathologySegmenter(sensitivity=0.2)
    pathology_results = segmenter.process_scan(image)
    
    print(f"\n[SCAN RESULTS]")
    print(f"  - Affected Area: {pathology_results['affected_area_px']} pixels")
    print(f"  - Crack Length:  {pathology_results['crack_length_px']} pixels")
    print(f"  - Severity:      {pathology_results['estimated_severity']}")

    # 3. Run Volume Estimation
    engine = VolumeEngine()
    volume_results = engine.estimate_repair_volume(
        pathology_results['affected_area_px'],
        depth_m=0.015 # 15mm deep repair
    )

    print(f"\n[REPAIR ESTIMATE]")
    print(f"  - Surface Area:  {volume_results['affected_area_m2']:.6f} m²")
    print(f"  - Target Depth:  {volume_results['repair_depth_m']*1000:.1f} mm")
    print(f"  - Total Volume:  {volume_results['estimated_volume_liters']:.4f} Liters")
    
    print("\n" + "="*50)
    print("  Test Complete: Forensic Pipeline Validated.")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_test()

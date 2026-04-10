"""
AuraVision — Volume Engine
==========================
Calculates estimated repair volumes based on segmented pathology areas.
Helps in automated cost estimation and material procurement for structural repair.
"""

import logging

logger = logging.getLogger(__name__)

# Standard constants for structural repair
DEFAULT_REPAIR_DEPTH_M = 0.01  # 10mm standard depth for surface epoxy/mortar
PX_TO_M_RATIO          = 0.001 # Mock calibration: 1px = 1mm (0.001m)

class VolumeEngine:
    """
    Engine for transforming 2D pathology pixels into 3D material volume estimates.
    """
    
    def __init__(self, pixel_resolution: float = PX_TO_M_RATIO):
        self.res = pixel_resolution
        logger.info("VolumeEngine initialized with resolution: %f m/px", pixel_resolution)

    def estimate_repair_volume(self, affected_area_px: int, depth_m: float = DEFAULT_REPAIR_DEPTH_M) -> dict:
        """
        Calculates the volume of material needed for a repair.
        Returns volume in Liters and Cubic Meters.
        """
        # Area in m^2
        area_m2 = affected_area_px * (self.res ** 2)
        
        # Volume in m^3
        volume_m3 = area_m2 * depth_m
        
        # Volume in Liters (1 m^3 = 1000 L)
        volume_l = volume_m3 * 1000.0
        
        logger.info("Calculated repair volume: %.4f L for %d px", volume_l, affected_area_px)
        
        return {
            "affected_area_m2": float(area_m2),
            "repair_depth_m": float(depth_m),
            "estimated_volume_m3": float(volume_m3),
            "estimated_volume_liters": float(volume_l),
            "unit": "Liters"
        }

    def estimate_material_mass(self, volume_l: float, density_kg_l: float = 1.8) -> float:
        """
        Estimates the mass of repair material (e.g., concrete/epoxy).
        Standard epoxy density is roughly 1.1-1.8 kg/L depending on aggregate.
        """
        return volume_l * density_kg_l

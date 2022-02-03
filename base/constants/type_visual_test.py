from enum import Enum

class TypeVisualTest(Enum):
    """
    Enumera los tipos de evaluación visual que maneja el sistema
    Asignando un código a cada uno
    """

    """Virual Test"""
    STEREOSCOPIC_VISION = "vt001"
    VISUAL_DEPTH_PERCEPTION = "vt002"
    VISUAL_PERCEPTION_OF_COLOR = "vt003"
    VISUAL_FIELD = "vt004"

    
    """Clasic Test"""
    LANG = 'L'
    ISHIHARA = 'I'
    TITMUS = 'T'   


from enum import Enum


class GradingSystem(Enum):
    GIA = "GIA"
    AGS = "AGS"


class AgsGrade(Enum):
    AGS_IDEAL = "IDEAL"
    AGS_EXCELLENT = "EX"
    AGS_VERY_GOOD = "VG"
    AGS_GOOD = "G"
    AGS_FAIR = "F"
    AGS_POOR = "P"


class GiaGrade(Enum):
    GIA_EXCELLENT = "GIA_EXCELLENT"
    GIA_VERY_GOOD = "AGS_VERY_GOOD"
    GIA_GOOD = "AGS_GOOD"
    GIA_FAIR = "AGS_FAIR"
    GIA_POOR = "AGS_POOR"

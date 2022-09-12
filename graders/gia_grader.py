from enum import Enum


class GiaGrade(Enum):
    GIA_EXCELLENT = "GIA_EXCELLENT"
    GIA_VERY_GOOD = "AGS_VERY_GOOD"
    GIA_GOOD = "AGS_GOOD"
    GIA_FAIR = "AGS_FAIR"
    GIA_POOR = "AGS_POOR"


class GiaGrader:
    def __init__(self):
        pass

    def get_grade(self, table, crown_angle, pavilion_angle):
        pass


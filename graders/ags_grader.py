from enum import Enum


class AgsGrade(Enum):
    AGS_IDEAL = "IDEAL"
    AGS_EXCELLENT = "EX"
    AGS_VERY_GOOD = "VG"
    AGS_GOOD = "G"
    AGS_FAIR = "F"
    AGS_POOR = "P"


class AgsGrader:
    def __init__(self):
        self.grading_tables_ = None

    def get_grade(self, table, crown_angle, pavilion_angle):
        pass


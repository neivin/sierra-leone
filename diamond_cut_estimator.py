from graders.ags_grader import AgsGrade
from graders.gia_grader import GiaGrade


class DiamondCutEstimator:
    def __init__(self):
        pass

    def get_gia_grade(self, table, crown_angle, pavilion_angle):
        return GiaGrade.GIA_EXCELLENT

    def get_ags_grade(self, table, crown_angle, pavilion_angle):
        return AgsGrade.AGS_EXCELLENT

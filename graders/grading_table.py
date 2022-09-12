from enum import Enum
import os
from graders.ags_grader import AgsGrade
from graders.gia_grader import GiaGrade

# AGS Chart: https://www.diamondscreener.com/wp-content/uploads/reference/agsl_proportion_charts.pdf
# GIA Chart: https://www.diamondscreener.com/wp-content/uploads/reference/booklet_cut_estimation_tables_lowres.pdf

# AGS Crown angle range 21.5 - 40.5
# GIA Crown angle range 22.0 - 40.0
# Multiply by 10 to get floats since range doesn't take float as args
CROWN_ANGLE_ARRAY = [i / 10 for i in range(215, 410, 5)]

# AGS Pavilion angle range 38.6 - 43.2
# GIA Pavilion angle range 38.8 - 43.0
PAVILION_ANGLE_ARRAY = [i / 10 for i in range(386, 434, 2)]


class GradingSystem(Enum):
    GIA = "GIA"
    AGS = "AGS"


class GradingTable:
    def __init__(self, grading_system, table_pct, grading_table_path):
        self.grading_system = grading_system
        self.table_pct = table_pct
        self.grading_table_ = [[] for crown_angle in CROWN_ANGLE_ARRAY]

        if self.grading_system == GradingSystem.AGS:
            self.init_ags_table_(grading_table_path)
        elif self.grading_system == GradingSystem.GIA:
            self.init_gia_table_(grading_table_path)
        else:
            raise ValueError

    def init_ags_table_(self, relative_path):
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        abs_grading_table_path = os.path.join(script_dir, relative_path)
        with open(abs_grading_table_path, "r") as file:
            i = 0
            for line in file:
                crown_angle_grades = line.rstrip().split(" ")
                self.grading_table_[i] = map(lambda x: AgsGrade(x), crown_angle_grades)
                i += 1

    def init_gia_table_(self):
        """
        Initialize a GIA table for a given table percent
        """
        raise NotImplementedError

    def get_grade(self, crown_angle, pavilion_angle):
        raise NotImplementedError
# grading table config
# for every crown angle -> [pavilion angles]
# map of crown angle -> map (starting pavilion angle to grade)

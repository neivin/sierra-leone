from graders.grading_system import GradingSystem
from graders.grading_system import AgsGrade
from graders.grading_system import GiaGrade

# AGS Chart: https://www.diamondscreener.com/wp-content/uploads/reference/agsl_proportion_charts.pdf
# GIA Chart: https://www.diamondscreener.com/wp-content/uploads/reference/booklet_cut_estimation_tables_lowres.pdf

# AGS Crown angle range 21.5 - 40.5
# GIA Crown angle range 22.0 - 40.0
# Multiply by 10 to get floats since range doesn't take float as args
CROWN_ANGLE_ARRAY = [i / 10 for i in range(215, 410, 5)]

# AGS Pavilion angle range 38.6 - 43.2
# GIA Pavilion angle range 38.8 - 43.0
PAVILION_ANGLE_ARRAY = [i / 10 for i in range(386, 434, 1)]


class GradingTable:
    def __init__(self, grading_system, table_pct, grading_table_path):
        self.grading_system = grading_system
        self.table_pct = table_pct
        self.grading_table_ = []

        if self.grading_system == GradingSystem.AGS:
            self.init_ags_table_(grading_table_path)
        elif self.grading_system == GradingSystem.GIA:
            self.init_gia_table_(grading_table_path)
        else:
            raise ValueError

    def init_ags_table_(self, abs_grading_table_path):
        with open(abs_grading_table_path, "r") as file:
            i = 0
            for line in file:
                pavilion_angle_grades = line.rstrip().split(" ")
                self.grading_table_.append(list(map(lambda x: AgsGrade(x), pavilion_angle_grades)))
                i += 1

    def init_gia_table_(self):
        """
        Initialize a GIA table for a given table percent
        """
        raise NotImplementedError

    def get_grade(self, crown_angle, pavilion_angle):
        crown_angle_index = CROWN_ANGLE_ARRAY.index(crown_angle)
        pavilion_angle_index = PAVILION_ANGLE_ARRAY.index(pavilion_angle)

        return self.grading_table_[pavilion_angle_index][crown_angle_index]

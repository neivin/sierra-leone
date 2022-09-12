from enum import Enum
import os
from graders.grading_table import GradingTable
from graders.grading_system import GradingSystem


class AgsGrader:
    AGS_TABLES_DIR_BASE_PATH = "../ags_tables/"
    GIA_TABLES_DIR_BASE_PATH = "../gia_tables/"

    def __init__(self):
        self.grading_tables_ = {}

        script_dir = os.path.dirname(__file__)
        ags_grading_tables_list = os.listdir(os.path.join(script_dir, self.AGS_TABLES_DIR_BASE_PATH))
        for table in ags_grading_tables_list:
            table_pct = int(table[-2:])  # "ags_56" -> "56" -> 56
            abs_path = os.path.join(script_dir, self.AGS_TABLES_DIR_BASE_PATH, table)
            self.grading_tables_[table_pct] = GradingTable(GradingSystem.AGS, table_pct, abs_path)

    def get_grade(self, table, crown_angle, pavilion_angle):
        if table not in self.grading_tables_:
            raise ValueError

        return self.grading_tables_[table].get_grade(crown_angle, pavilion_angle)

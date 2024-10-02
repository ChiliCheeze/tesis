def calculate_final_grade(self):
    std_year_curriculum = grd_system.curriculum[self.year]
    tgp = 0  
    valid_units = 0  # Valid units that correspond to passing grades
    sub_failed = 0 

    for grade, units in zip(self.grades, std_year_curriculum["units"]):
        if grade < 4.00:  # Only count valid grades
            tgp += grade * units
            valid_units += units  # Only count units for passing grades
        else:
            sub_failed += units
            return sub_failed

    final_grade = tgp / valid_units if valid_units > 0 else "N/A"
    return round(tgp, 2), valid_units, round(final_grade, 2) if final_grade != "N/A" else final_grade


def __str__(self):
    return f"Student Name: {self.name}, Year Level: {self.year}, Student Number: {self.stdNum}, Grades: {self.grades}, Final Grade: {self.final_grade}"
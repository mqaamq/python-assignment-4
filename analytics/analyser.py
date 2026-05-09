class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"

class GpaAnalyser(DataAnalyser):
    def analyse(self):
        gpas = [float(s['GPA']) for s in self.students if 'GPA' in s]
        if not gpas: return
        
        self.result = {
            "total_students": len(gpas),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": len([g for g in gpas if g > 3.5])
        }

    def print_results(self):
        print("\nGPA ANALYSIS REPORT")
        print("==============================")
        super().print_results()
        print("==============================")

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"
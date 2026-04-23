import os
import csv
import json


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please check the file.")
            return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)

            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return []

        except Exception as e:
            print(f"General error while reading file: {e}")
            return []

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("------------------------------")
        for row in self.students[:n]:
            print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
        print("------------------------------")


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        high_performers = 0

        for student in self.students:
            try:
                gpa = float(student['GPA'])
                gpas.append(gpa)

                if gpa > 3.5:
                    high_performers += 1

            except ValueError:
                print(f"Warning: could not convert value for student {student['student_id']} — skipping row.")
                continue

            except KeyError:
                print("Warning: missing GPA field — skipping row.")
                continue

        if len(gpas) == 0:
            self.result = {
                "analysis": "GPA Statistics",
                "total_students": 0,
                "average_gpa": 0,
                "max_gpa": 0,
                "min_gpa": 0,
                "high_performers": 0
            }
            return self.result

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(gpas),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": high_performers
        }

        return self.result

    def print_results(self):
        print("------------------------------")
        print("GPA Analysis")
        print("------------------------------")
        print(f"Total students : {self.result['total_students']}")
        print(f"Average GPA : {self.result['average_gpa']}")
        print(f"Highest GPA : {self.result['max_gpa']}")
        print(f"Lowest GPA : {self.result['min_gpa']}")
        print(f"Students GPA>3.5 : {self.result['high_performers']}")
        print("------------------------------")

    def lambda_filter_report(self):
        print("------------------------------")
        print("Lambda / Map / Filter")
        print("------------------------------")

        try:
            high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, self.students))
            print(f"Students with GPA > 3.8 : {len(high_gpa)}")
        except Exception as e:
            print(f"Error in GPA filter: {e}")

        try:
            gpa_values = list(map(lambda s: float(s['GPA']), self.students))
            print(f"GPA values (first 5) : {gpa_values[:5]}")
        except Exception as e:
            print(f"Error in GPA map: {e}")

        try:
            hard_workers = list(filter(lambda s: float(s['study_hours_per_day']) > 4, self.students))
            print(f"Students studying > 4 hrs : {len(hard_workers)}")
        except Exception as e:
            print(f"Error in study hours filter: {e}")

        print("------------------------------")


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)

            print(f"Result saved to {self.output_path}")

        except Exception as e:
            print(f"Error saving JSON: {e}")


def test_wrong_file():
    print("\nTesting file error handling:")
    temp_loader = DataLoader("wrong_file.csv")
    temp_loader.load()


fm = FileManager("students.csv")
if not fm.check_file():
    print("Stopping program.")
    exit()

fm.create_output_folder()

dl = DataLoader("students.csv")
students = dl.load()

if students:
    dl.preview()

    analyser = DataAnalyser(students)
    analyser.analyse()
    analyser.print_results()
    analyser.lambda_filter_report()

    saver = ResultSaver(analyser.result, "output/result.json")
    saver.save_json()

test_wrong_file()
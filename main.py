from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser

if __name__ == "__main__":
    fm = FileManager("students.csv")
    if fm.check_file():
        fm.create_output_folder()
        dl = DataLoader("students.csv")
        students = dl.load()

        if students:
            analyser = GpaAnalyser(students)
            saver = ResultSaver(analyser.result, "output/result.json")
            report = Report(analyser, saver)
            report.generate()
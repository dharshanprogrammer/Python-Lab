import pandas as pd
import numpy as np

FILE_NAME = 'msc_marks_data.csv'
try:
    df = pd.read_csv(FILE_NAME)
    print(f"Data successfully loaded from {FILE_NAME}")
except FileNotFoundError:
    print(f"File '{FILE_NAME}' not found. Creating sample data.")
    data = {
        'Batch': [2018, 2018, 2018, 2019, 2019, 2019, 2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022, 2022],
        'Semester': [1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2],
        'Course_Name': ['Algorithms', 'Linear Algebra', 'Stats', 'Algorithms', 'Linear Algebra', 'Stats', 'Algorithms',
                        'Linear Algebra', 'Stats', 'Algorithms', 'Linear Algebra', 'Stats', 'Algorithms',
                        'Linear Algebra', 'Stats'],
        'Faculty_ID': ['F001', 'F002', 'F003', 'F001', 'F002', 'F003', 'F004', 'F002', 'F001', 'F004', 'F002', 'F003',
                       'F001', 'F002', 'F004'],
        'Marks': [85, 75, 70, 92, 80, 68, 88, 72, 75, 95, 88, 80, 72, 90, 83]
    }
    df = pd.DataFrame(data)
df['Marks'] = pd.to_numeric(df['Marks'], errors='coerce')
df.dropna(subset=['Marks'], inplace=True)
print("\nGenerating CAR_Coursewise_Report.csv (Algorithms)...")
course_analysis = df[df['Course_Name'] == 'Algorithms'].groupby('Batch')['Marks'].mean().reset_index()
course_analysis.rename(columns={'Marks': 'Avg_Marks_Algorithms'}, inplace=True)
course_analysis.to_csv('CAR_Coursewise_Report.csv', index=False)
print("-> Report saved: CAR_Coursewise_Report.csv")
print("Generating CAR_Classwise_Report.csv (Overall Batch Avg)...")
class_analysis = df.groupby('Batch')['Marks'].mean().reset_index()
class_analysis.rename(columns={'Marks': 'Overall_Batch_Avg'}, inplace=True)
class_analysis.to_csv('CAR_Classwise_Report.csv', index=False)
print("-> Report saved: CAR_Classwise_Report.csv")
print("Generating CAR_Semesterwise_Report.csv...")
semester_analysis = df.groupby(['Semester', 'Batch'])['Marks'].mean().unstack()
semester_analysis.to_csv('CAR_Semesterwise_Report.csv')
print("-> Report saved: CAR_Semesterwise_Report.csv")
print("Generating CAR_Facultywise_Report.csv...")
faculty_batch_analysis = df.groupby(['Faculty_ID', 'Batch'])['Marks'].mean().unstack()
faculty_batch_analysis.to_csv('CAR_Facultywise_Report.csv')
print("-> Report saved: CAR_Facultywise_Report.csv")
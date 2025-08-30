import pandas as pd

def analyze_results(excel_file):
    try:
        
        df = pd.read_excel(excel_file)

        print(" Loaded Data:")
        print(df.head())

        
        df.columns = df.columns.str.strip()

        
        df_numeric = df.apply(pd.to_numeric, errors='coerce')


        df_numeric = df_numeric.dropna(axis=1, how='all')

        print("\nSubject-wise Averages:")
        print(df_numeric.mean())

   
        if 'Gender' in df.columns:
            print("\n Gender-wise Averages:")
         
            combined = pd.concat([df['Gender'], df_numeric], axis=1)
            print(combined.groupby('Gender').mean())
        else:
            print("\n 'Gender' column not found in the Excel file.")

    except FileNotFoundError:
        print("Error: Excel file not found.")
    except Exception as e:
        print(f" Error: {e}")

analyze_results(r"D:\All Folders\Python Lab\Students Semester Result.xlsx")

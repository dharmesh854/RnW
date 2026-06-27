import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class DataVisualization:
    
    # ----------------- LOAD DATA -----------------
    
    def load_data(self):
        data_name = input("Enter the path of the Dataset (CSV File): ")
        
        try:
            df = pd.read_csv(data_name)
            print("Data loaded successfully !")
            return df
            
        except Exception:
            print("This file not found !")
            
    # ----------------- EXPLORE DATA -----------------     
    
    def explore_data_1(self,df):
        print(df.head())
        
    def explore_data_2(self,df):
        print(df.tail())
    
    def explore_data_3(self,df):
        print(df.columns)
        
    def explore_data_4(self,df):
        print(df.dtypes)
        
    def explore_data_5(self,df):
        df.info()
        
    # ----------------- HANDLE MISSING DATA ----------------- 
    
    def missing_value_1(self, df):
        print(df.isna().sum())
    
    def missing_value_2(self,df):
        column = input("Enter the column name you want to fill: ")
        
        if column not in df.columns:
            print(f"{column} column not found in dataset ! !")
            
        if df[column].dtype in ['int64','float64']:
            df[column].fillna(df[column].mean(), inplace=True)
            print("Missing values successfully filled with mean !")
        else:
            print("Mean can be applied only on numeric columns !")
        
    def missing_value_3(self,df):
        df.dropna(inplace=True)
        print("Missing value rows dropped successfully !")
    
    def missing_value_4(self,df):
        column = input("Enter the column name you want to fill: ")
        if column in df.columns:
            value = input("Enter the value you want to replace with: ")
    
            df[column] = df[column].astype(object)
            df[column].fillna(value, inplace=True)
            print(f"{column} column's missing values successfully filled with {value} !")
            
        if column not in df.columns:
            print(f"{column} column not found in dataset !")
        
        
        
    # ----------------- PERFORM DATAFRAME OPERATIONS -----------------
        
    def sample_rows(self,df):
        rows = int(input("Enter the number of rows you want: "))
        
        try:
            print(df.sample(rows))
        except ValueError:
            print(" Please enter a valid number !")      
            
    
    
    def sort_values(self, df):
        column = input("Enter the column name you want to sort: ")

        if column not in df.columns:
            print("Column not found!")
            return

        if df[column].dtype in ['int64', 'float64']:
            df.sort_values(by=column, inplace=True)
            print(f"Data sorted successfully by '{column}'")
            print(df)
        else:
            print(f"{column} column cannot be sorted")
            print("Only numerical columns can be sorted")

             
             
    def delete_column(self,df):
        column = input("Enter the column name you want to delete: ")
        
        if column in df.columns:
            df.drop(columns=[column], inplace=True)
            print(f"{column} column deleted successfully.")  
        else:
            print(f"{column} column not found in Dataset !")
            
        
        
        
    # ----------------- GENERATE DESCRIPTIVE STATISTICS -----------------
    
    def descriptive_stat(self,df):
        column = input("Enter the column name you want to generate it's descriptive statistics: ")
        
        if column not in df.columns:
            print(f"{column} column not exist !")
            
        if df[column].dtype in ['int64','float64']:
            print(df[column].describe())
            
        else:
            print("Descriptive Statistics can only genetate on numerical column !")
        
    
    
    # ----------------- DATA VISUALIZATION -----------------
    
    def visualization_1(self,df):
        x = input("Enter x-axis column name: ")
        y = input("Enter y-axis column name: ")
        title = input("Enter the title of Bar Chart: ")
      
        if x in df.columns and y in df.columns:
            
            data = df.groupby(x)[y].sum()
            plt.figure(figsize=(10,6))
            plt.bar(data.index, data.values,color='blue', alpha=0.7)
            plt.title(title)
            plt.xlabel(x)
            plt.ylabel(y)
            plt.show()
            
        if x not in df.columns and y not in df.columns:
            print(f"{x} and {y} columns not found in Data !")
            
            
    def visualization_2(self,df):
        x = input("Enter x-axis column name: ")
        y = input("Enter y-axis column name: ")
        title = input("Enter the title of Line Chart: ")
        
        if x in df.columns and y in df.columns:
            
            data = df.groupby(by=x)[y].sum()
            plt.figure(figsize=(10,6))
            plt.plot(data.index,data.values, marker='o', markersize=5, color='black', markerfacecolor='yellow')
            plt.title(title)
            plt.xlabel(x)
            plt.ylabel(y)
            plt.show()
            
        if x not in df.columns or y not in df.columns:
            print(f"{x} and {y} columns not found in Data !")
            
            
    def visualization_3(self,df):
        x = input("Enter x-axis column name: ")
        y = input("Enter y-axis column name: ")
        title = input("Enter the title of Scatter Plot: ")
        
        if x in df.columns and y in df.columns:
            
            plt.figure(figsize=(10,6))
            data = df.groupby(by=x)[y].sum()
            plt.scatter(data.index,data.values, color='blue', edgecolor='black')
            plt.grid(True, linestyle="--", alpha=0.6, axis="both")
            plt.title(title)
            plt.xlabel(x)
            plt.ylabel(y)
            plt.show()
            
        if x not in df.columns or y not in df.columns:
            print(f"{x} and {y} columns not found in Data !")
            
        
    def visualization_4(self,df):
        x = input("Enter index column name: ")
        y = input("Enter value column name: ")
        title = input("Enter the title of Pie Chart: ")
        counts = df[y].value_counts()

        if x in df.columns and y in df.columns:
            
                plt.pie(
                    counts,
                    labels=counts.index, 
                    startangle=90, 
                    autopct='%1.1f%%')
                plt.title(title)
                plt.legend(title=y,loc='best')
                plt.show()
    
        else:
            print(f"{x} or {y} not found in Dataset !")
                
    
    
    # ----------------- SAVE VISUALIZATION -----------------
    
    def save_fig(self):
        
        try:
            save_file_name = input("Enter file name to save the plot(e.g. scatter_plot.png): ")
            plt.savefig(save_file_name, dpi=300)
            plt.close()
            print("Chart saved successfully !")
            
        except Exception as MistakeinChart:
            print("There are some mistakes in your chart !")
            print(MistakeinChart)
        
        
        
        
    
        
        
obj = DataVisualization()


while True:
    print("\n======= Data Analysis & Visualization Program =======")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Enter number only !")
        
    try:
        if choice == 1:
            df = obj.load_data()
            
        elif choice == 2:
            while True:
                print("\n== Explore Data ==")
                print("1. Display the first 5 rows")
                print("2. Display the last 5 rows")
                print("3. Display the column names")
                print("4. Display the datatypes")
                print("5. Display basic info")
                print("0. Go to Main Menu")
                
                try:
                    sbc = int(input("\nEnter your choice: "))
                except ValueError:
                    print("Enter number only!")
                    continue
                
                if sbc == 1:
                    obj.explore_data_1(df)
                elif sbc == 2:
                    obj.explore_data_2(df)
                elif sbc == 3:
                    obj.explore_data_3(df)
                elif sbc == 4:
                    obj.explore_data_4(df)
                elif sbc == 5:
                    obj.explore_data_5(df)
                elif sbc == 0:
                    print("Going to Main Menu...")
                    break
                else:
                    print("Invalid Choice !")
                    
                
        elif choice == 3:
            while True:
                print("\n== DataFrame Operations ==")
                print("1. Display random rows")
                print("2. Sort values")
                print("3. Delete Column")
                print("0. Go to Main Menu")
                
                try:
                    sbc = int(input("\nEnter your choice: "))
                except ValueError:
                    print("Enter number only!")
                    continue
                
                if sbc == 1:
                    obj.sample_rows(df)
                elif sbc == 2:
                    obj.sort_values(df)
                elif sbc == 3:
                    obj.delete_column(df) 
                elif sbc == 0:
                    print("Going to Main Menu...")
                    break
                else:
                    print("Invalid Choice !")
                
        
        elif choice == 4:
            while True:
                print("\n== Handle Missing Data ==")
                print("1. Display rows with missing values")
                print("2. Fill missing values with mean")
                print("3. Drop rows with missing values")
                print("4. Replace missing value with a specific value")
                print("0. Go to Main Menu")
                
                try:
                    sbc = int(input("\nEnter your choice: "))
                except ValueError:
                    print("Enter number only!")
                    continue
                
                if sbc == 1:
                    obj.missing_value_1(df)
                elif sbc == 2:
                    obj.missing_value_2(df)
                elif sbc == 3:
                    obj.missing_value_3(df)
                elif sbc == 4:
                    obj.missing_value_4(df)
                elif sbc == 0:
                    print("Going to Main Menu...")
                    break
                else:
                    print("Invalid Choice !")
        
        elif choice == 5:
            obj.descriptive_stat(df)
        
        elif choice == 6:
            while True:
                print("\n== Data Visualization ==")
                print("1. Bar Plot")
                print("2. Line Plot")
                print("3. Scatter Plot")
                print("4. Pie Chart")
                print("0. Go to Main Menu")
                
                try:
                    sbc = int(input("\nEnter your choice: "))
                except ValueError:
                    print("Enter number only!")
                    continue
                
                if sbc == 1:
                    obj.visualization_1(df)
                elif sbc == 2:
                    obj.visualization_2(df)
                elif sbc == 3:
                    obj.visualization_3(df)
                elif sbc == 4:
                    obj.visualization_4(df)
                elif sbc == 0:
                    print("Going to Main Menu...")
                    break
                else:
                    print("Invalid Choice !")
        
        elif choice == 7: 
            obj.save_fig()
        
        elif choice == 8:
            print("Going to Main Menu...")
            break
        
        else:
            print("Invalid Choice !")
            
    except ValueError:
        print("Please enter a valid choice !")
        
              
    
    

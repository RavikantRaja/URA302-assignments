import scipy as sp
import pandas as pd
#q1
print(sp.__version__)
print(pd.__version__)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Print the DataFrame
print("\nCreated DataFrame:")
print(df)

#q2
# 2.1 Creating a Series

s1 = pd.Series([100, 200, 300, 400, 500])

# Print the Series
print("2.1 S1 Series:")
print(s1)
print("\n")

# 2.2 Accessing Elements in a Series

second_element = s1.iloc[1]
fourth_element = s1.iloc[3]

# Print the accessed elements
print("2.2 Second and fourth elements:")
print(f"Second element: {second_element}")
print(f"Fourth element: {fourth_element}")
print("\n")

# 2.3 Series Operations
# Create a second Series S2
s2 = pd.Series([10, 20, 30, 40, 50])

# Perform element-wise addition between S1 and S2
addition_result = s1 + s2

# Print the result
print("2.3 Result of S1 + S2:")
print(addition_result)


#q3

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# 3.1 DataFrame Column Access
print("3.1 'Name' and 'City' columns:")
print(df[['Name', 'City']])

# 3.2 Adding a New Column
df['Salary'] = [50000, 60000, 70000]
print("\n3.2 DataFrame after adding 'Salary' column:")
print(df)

# 3.3 Basic Statistics on DataFrames
average_age = df['Age'].mean()
total_salary = df['Salary'].sum()

print(f"\n3.3 Basic Statistics:")
print(f"Average Age: {average_age}")
print(f"Total Sum of Salary: {total_salary}")


#q4

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 22],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']}
df = pd.DataFrame(data)

# Filter the DataFrame where Age is greater than 28
filtered_df = df[df['Age'] > 28]

print("Filtered DataFrame (Age > 28):")
print(filtered_df)

#q5
# 5.1 Reading a CSV File

csv_data = """Name,Department,Salary
John,Sales,50000
Jane,Marketing,60000
Emily,HR,55000"""

# Read the CSV data into a Pandas DataFrame
df = pd.read_csv(io.StringIO(csv_data))

# Print the contents of the DataFrame
print("Original DataFrame:")
print(df)

# 5.2 CSV Data Manipulation
# Filter the rows where the Salary is greater than 55000
filtered_df = df[df['Salary'] > 55000]

# Print only the Name and Department columns for the filtered rows
print("\nFiltered rows (Salary > 55000) - Name and Department columns:")
print(filtered_df[['Name', 'Department']])

#q6


data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Department': ['HR', 'IT', 'HR', 'Finance', 'IT'],
        'Salary': [60000, 75000, 62000, 80000, 78000]}
df = pd.DataFrame(data)

# Group by 'Department' and calculate the average 'Salary'
average_salary_by_department = df.groupby('Department')['Salary'].mean()

# Print the result
print("Average Salary by Department:")
print(average_salary_by_department)


#q7
# Create the first DataFrame
df1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR']
})

# Create the second DataFrame
df2 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Experience (Years)': [5, 7, 3]
})

# Merge the two DataFrames on the 'Name' column
merged_df = pd.merge(df1, df2, on='Name')

# Print the merged DataFrame
print(merged_df)


#q8
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Experience (Years)': [5, 10, 3, 8],
        'Salary': [60000, 80000, 45000, 75000]}
df = pd.DataFrame(data)

# Sort the DataFrame by 'Experience (Years)' in descending order
sorted_df = df.sort_values(by='Experience (Years)', ascending=False)

# Print the sorted DataFrame
print(sorted_df)
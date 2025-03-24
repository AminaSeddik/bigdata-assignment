import pandas as pd

def preprocess_data(df):
    # Drop columns with too many missing values
    df = df.drop(columns=['Cabin'], errors='ignore')
    
    # Fill missing values for 'Age'
    if 'Age' in df.columns:
        df['Age'].fillna(df['Age'].median(), inplace=True)
    
    # Fill missing values for 'Embarked'
    if 'Embarked' in df.columns:
        df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    
    # Convert categorical to numerical using one-hot encoding
    df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True, dtype=int)
    
    return df

if __name__ == "__main__":
    try:
        df = pd.read_csv("Titanic_Dataset.csv")
        df_cleaned = preprocess_data(df)
        df_cleaned.to_csv("res_dpre.csv", index=False)
        print("Preprocessing complete, saved as res_dpre.csv")
    except FileNotFoundError:
        print("Error: The file 'Titanic_Dataset.csv' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("res_dpre.csv")

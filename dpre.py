import pandas as pd

def preprocess_data(df):
    # Drop columns with too many missing values
    df = df.drop(columns=['Cabin'], errors='ignore')
    # Fill missing values
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    # Convert categorical to numerical
    df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
    return df

if __name__ == "__main__":
    df = pd.read_csv("Titanic_Dataset.csv")
    df_cleaned = preprocess_data(df)
    df_cleaned.to_csv("res_dpre.csv", index=False)
    print("Preprocessing complete, saved as res_dpre.csv")
    print("res_dpre.csv")
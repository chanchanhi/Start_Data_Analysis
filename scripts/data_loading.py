import pandas as pd

def load_data(file_path):
    """
    데이터 로딩 함수.
    """
    return pd.read_csv(file_path)

def preprocess_data(df):
    """
    결측치 처리 및 정규화 수행.
    """
    from sklearn.preprocessing import StandardScaler
    
    df.fillna(df.mean(), inplace=True)
    scaler = StandardScaler()
    df[['Age', 'Score']] = scaler.fit_transform(df[['Age', 'Score']])
    return df

def add_encoded_name(df):
    """
    범주형 변수 'Name'을 숫자로 인코딩.
    """
    df['Name_encoded'] = pd.factorize(df['Name'])[0]
    return df

def add_score_category(df):
    """
    파생 변수 'Score_category' 생성.
    """
    df['Score_category'] = df['Score'].apply(lambda x: 'High' if x > 0 else 'Low')
    return df

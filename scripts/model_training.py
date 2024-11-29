from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_and_evaluate_model(df):
    """
    머신러닝 모델 학습 및 평가 함수.
    """
    # 데이터 분리
    X = df[['Age', 'Score', 'Name_encoded']]
    y = df['Score_category'].apply(lambda x: 1 if x == 'High' else 0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 모델 학습
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # 모델 평가
    y_pred = model.predict(X_test)
    print("\n✅ 모델 평가 결과:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

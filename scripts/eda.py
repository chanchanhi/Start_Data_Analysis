import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_distribution(df):
    """
    나이 분포 시각화 함수.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Age'], bins=5, kde=True, color='blue')
    plt.title('Age Distribution')
    plt.xlabel('Age (Scaled)')
    plt.ylabel('Frequency')
    plt.show()

def plot_correlation_matrix(df):
    """
    상관관계 분석 함수.
    """
    plt.figure(figsize=(6, 4))
    sns.heatmap(df[['Age', 'Score']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

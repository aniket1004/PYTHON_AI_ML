from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import VotingClassifier

df_true = pd.read_csv("True.csv")
df_true["label"] = 1
print("Shape of true news dataset : ", df_true.shape)

df_true.drop(columns=["date", "subject"], inplace=True)
print(df_true.isnull().sum())
df_true.dropna(inplace=True)

df_fake = pd.read_csv("Fake.csv")
df_fake["label"] = 0
print("Shape of false news dataset : ", df_fake.shape)

df_fake.drop(columns=["date", "subject"], inplace=True)
print(df_fake.isnull().sum())
df_fake.dropna(inplace=True)

df = pd.concat([df_true,df_fake], axis=0)
print("Shape of dataset after merging : ", df.shape)

df = df.sample(frac=1).reset_index(drop=True)
df.dropna(inplace=True)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"].tolist())
Y = df["label"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

logistic_model = LogisticRegression(max_iter=1000)
tree_model = DecisionTreeClassifier()

logistic_model.fit(X_train, Y_train)
tree_model.fit(X_train, Y_train)

hard_voting = VotingClassifier(
    estimators=[
        ('lr', logistic_model),
        ('dt', tree_model)
    ],
    voting='hard'
)

hard_voting.fit(X_train, Y_train)
Y_pred = hard_voting.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy score Hard Voting : ", accuracy*100)
print("Confusion matrix  Hard Voting \n", confusion_matrix(Y_test, Y_pred))

soft_voting = VotingClassifier(
    estimators=[
        ('lr', logistic_model),
        ('dt', tree_model)
    ],
    voting='soft'
)

soft_voting.fit(X_train, Y_train)
Y_pred = soft_voting.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy score Soft Voting : ", accuracy*100)
print("Confusion matrix Soft Voting \n", confusion_matrix(Y_test, Y_pred))

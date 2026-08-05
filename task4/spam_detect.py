# ======================================================
# SPAM EMAIL DETECTION USING SCIKIT-LEARN
# Predictive Model for Message Classification
# ======================================================

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import matplotlib.pyplot as plt


# ======================================================
# STEP 1: Create Dataset
# ======================================================

data = {
    'message':[
        'Win a free iPhone now',
        'Meeting at 10 AM tomorrow',
        'Claim your cash reward today',
        'Can you send the notes?',
        'Congratulations you won a lottery',
        'Project submission is tomorrow',
        'Limited offer buy now',
        'Lunch at 1 PM?',
        'Earn money quickly from home',
        'Please attend the class',
        'Get free recharge now',
        'Your assignment is uploaded',
        'Exclusive discount available',
        'Call me when you reach home',
        'You have won 10000 rupees',
        'Join the meeting at 5 PM',
        'Click here for free gifts',
        'Submit your lab record',
        'Urgent! Claim your prize now',
        'Happy birthday have a nice day'
    ],

    'label':[
        'spam',
        'ham',
        'spam',
        'ham',
        'spam',
        'ham',
        'spam',
        'ham',
        'spam',
        'ham',
        'spam',
        'ham',
        'spam',
        'ham',
        'spam',
        'ham',
        'spam',
        'ham',
        'spam',
        'ham'
    ]
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df.head())


# ======================================================
# STEP 2: Separate Features and Labels
# ======================================================

X = df['message']
y = df['label']


# ======================================================
# STEP 3: Convert Text to Numerical Data
# ======================================================

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)


# ======================================================
# STEP 4: Split Dataset
# ======================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)


# ======================================================
# STEP 5: Train Model
# ======================================================

model = MultinomialNB()

model.fit(X_train, y_train)

print("\nModel trained successfully")


# ======================================================
# STEP 6: Make Predictions
# ======================================================

predictions = model.predict(X_test)

print("\nPredictions:")
print(predictions)


# ======================================================
# STEP 7: Evaluate Model
# ======================================================

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", accuracy)

print("\nClassification Report:\n")

print(classification_report(
    y_test,
    predictions
))


# ======================================================
# STEP 8: Confusion Matrix
# ======================================================

cm = confusion_matrix(y_test, predictions)

plt.figure(figsize=(6,5))

plt.imshow(cm)

plt.title("Confusion Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.colorbar()

plt.show()


# ======================================================
# STEP 9: Test with New Message
# ======================================================

while True:

    message = input(
        "\nEnter a message to test (or type exit): "
    )

    if message.lower() == "exit":
        break

    transformed_message = vectorizer.transform(
        [message]
    )

    prediction = model.predict(
        transformed_message
    )

    print("\nPrediction:", prediction[0])

    if prediction[0] == "spam":
        print("⚠ Spam Message")
    else:
        print("✓ Not Spam")
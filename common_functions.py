import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    matthews_corrcoef,
    balanced_accuracy_score,
    roc_auc_score,
    precision_score,
    recall_score,
    f1_score,
)


# function to calculate evaluation metrics
def eval_metrics(y, y_pred):
    matthews = matthews_corrcoef(y, y_pred)
    accuracy = balanced_accuracy_score(y, y_pred)
    roc = roc_auc_score(y, y_pred)
    precision = precision_score(y, y_pred)
    recall = recall_score(y, y_pred)
    f1 = f1_score(y, y_pred)

    return matthews, accuracy, roc, precision, recall, f1


# function to plot confusion matrix
def plot_cm(cm):
    # Set up the matplotlib figure
    plt.figure(figsize=(8, 6))

    # Create a heatmap
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Normal", "Fraud"],
        yticklabels=["Normal", "Fraud"],
    )
    # Add labels and title
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.title("Confusion Matrix")

    # Show the plot
    plt.show()

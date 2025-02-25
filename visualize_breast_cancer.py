import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Set Seaborn style for aesthetics
sns.set(style="whitegrid")

# Create results directory if it doesn't exist
if not os.path.exists("results"):
    os.makedirs("results")

# ---------------------------
# 1. Load and Prepare the Dataset
# ---------------------------
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df['diagnosis'] = df['target'].map({0: 'malignant', 1: 'benign'})

# ---------------------------
# 2. Distribution of Diagnosis (Count Plot)
# ---------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x='diagnosis', data=df, palette='viridis')
plt.title("Distribution of Diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Count")
plt.savefig("results/diagnosis_distribution.png")
plt.close()

# ---------------------------
# 3. Correlation Heatmap of Features
# ---------------------------
plt.figure(figsize=(12, 10))
corr = df.drop(['target', 'diagnosis'], axis=1).corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title("Correlation Heatmap of Features")
plt.savefig("results/correlation_heatmap.png")
plt.close()

# ---------------------------
# 4. Pair Plot of Top 4 High-Variance Features
# ---------------------------
top_features = df.drop(['target', 'diagnosis'], axis=1).var().sort_values(ascending=False).head(4).index.tolist()
pair_plot = sns.pairplot(df[top_features + ['diagnosis']], hue='diagnosis', palette='bright')
pair_plot.fig.suptitle("Pairplot of Top 4 Features by Variance", y=1.02)
pair_plot.savefig("results/pair_plot.png")
plt.close()

# ---------------------------
# 5. PCA Scatter Plot
# ---------------------------
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df.drop(['target', 'diagnosis'], axis=1))
df['pca1'] = pca_result[:, 0]
df['pca2'] = pca_result[:, 1]

plt.figure(figsize=(8, 6))
sns.scatterplot(x='pca1', y='pca2', hue='diagnosis', data=df, palette='Set1', alpha=0.8)
plt.title("PCA Scatter Plot")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.savefig("results/pca_scatter.png")
plt.close()

# ---------------------------
# 6. t-SNE Visualization
# ---------------------------
tsne = TSNE(n_components=2, random_state=42)
tsne_result = tsne.fit_transform(df.drop(['target', 'diagnosis', 'pca1', 'pca2'], axis=1))
df['tsne1'] = tsne_result[:, 0]
df['tsne2'] = tsne_result[:, 1]

plt.figure(figsize=(8, 6))
sns.scatterplot(x='tsne1', y='tsne2', hue='diagnosis', data=df, palette='Set2', alpha=0.8)
plt.title("t-SNE Visualization")
plt.xlabel("t-SNE Dimension 1")
plt.ylabel("t-SNE Dimension 2")
plt.savefig("results/tsne_plot.png")
plt.close()

# ---------------------------
# 7. Histograms for Each Feature
# ---------------------------
features = df.drop(['target', 'diagnosis', 'pca1', 'pca2', 'tsne1', 'tsne2'], axis=1).columns
num_features = len(features)
cols = 5
rows = (num_features // cols) + (1 if num_features % cols != 0 else 0)

fig, axes = plt.subplots(rows, cols, figsize=(20, 15))
axes = axes.flatten()

for i, feature in enumerate(features):
    sns.histplot(df[feature], ax=axes[i], kde=True, color='skyblue')
    axes[i].set_title(feature)
    
# Remove empty subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])
    
plt.tight_layout()
plt.suptitle("Histograms of Features", y=1.02)
plt.savefig("results/feature_histograms.png")
plt.close()

# ---------------------------
# 8. Boxplots for Each Feature by Diagnosis
# ---------------------------
fig, axes = plt.subplots(rows, cols, figsize=(20, 15))
axes = axes.flatten()

for i, feature in enumerate(features):
    sns.boxplot(x='diagnosis', y=feature, data=df, ax=axes[i], palette='pastel')
    axes[i].set_title(feature)
    
# Remove empty subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])
    
plt.tight_layout()
plt.suptitle("Boxplots of Features by Diagnosis", y=1.02)
plt.savefig("results/feature_boxplots.png")
plt.close()

# Breast Cancer Data Visualization

This repository provides a comprehensive suite of visualizations to explore the [Breast Cancer Wisconsin Diagnostic Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)) as well as the version available via scikit-learn’s `load_breast_cancer()` function. The dataset contains 569 samples with 30 real-valued features derived from digitized images of fine needle aspirates (FNAs) of breast masses, along with a binary target indicating whether a tumor is **malignant** or **benign**.

## Visualizations

The project includes several visualization techniques:

1. **Diagnosis Distribution:**  
   A count plot displaying the number of benign vs. malignant cases.  
   ![Diagnosis Distribution](results/diagnosis_distribution.png)

2. **Correlation Heatmap:**  
   A heatmap illustrating the correlation between different features.  
   ![Correlation Heatmap](results/correlation_heatmap.png)

3. **Pair Plot of Top 4 Features:**  
   A pair plot for the top 4 high-variance features to show pairwise relationships, colored by diagnosis.  
   ![Pair Plot](results/pair_plot.png)

4. **PCA Scatter Plot:**  
   A scatter plot of the dataset projected onto the first two principal components, highlighting class separation.  
   ![PCA Scatter Plot](results/pca_scatter.png)

5. **t-SNE Visualization:**  
   A t-SNE plot for nonlinear dimensionality reduction, offering another perspective on class separability.  
   ![t-SNE Plot](results/tsne_plot.png)

6. **Histograms for Each Feature:**  
   Histograms (with KDE overlays) for all 30 features, providing insight into their distributions.  
   ![Feature Histograms](results/feature_histograms.png)

7. **Boxplots by Diagnosis:**  
   Boxplots of each feature grouped by diagnosis, which help in identifying differences between benign and malignant cases.  
   ![Feature Boxplots](results/feature_boxplots.png)

## How to Run the Project

### Prerequisites

- Python 3.x
- The following Python libraries:
  - numpy
  - pandas
  - matplotlib
  - seaborn
  - scikit-learn

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/gnn-breast-cancer-visualizations.git
   cd gnn-breast-cancer-visualizations

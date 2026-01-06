# Medium Task: Hybrid Audio–Lyrics Music Clustering

## Overview

This task extends the audio-only baseline by introducing a **hybrid clustering
approach** that combines acoustic features with textual information extracted
from song lyrics. The goal is to evaluate whether incorporating semantic content
from lyrics improves unsupervised music clustering performance.

A Variational Autoencoder (VAE) is used to learn latent representations from audio
features, which are then combined with TF-IDF-based lyric features to form a
multimodal representation for clustering.

---

## Methodology

### Audio Feature Extraction
- Audio tracks are processed using Mel-Frequency Cepstral Coefficients (MFCCs).
- A standard Variational Autoencoder (VAE) is trained on MFCC features.
- Latent dimension: **16**

### Lyric Feature Extraction
- Song lyrics are represented using TF-IDF vectorization.
- Textual features capture semantic information complementary to audio features.

### Hybrid Representation
- Audio latent vectors learned by the VAE are concatenated with lyric TF-IDF
  vectors.
- The resulting hybrid feature space combines acoustic and semantic information.

### Clustering
- Clustering is performed on the hybrid feature space using:
  - K-Means
  - Agglomerative Clustering
  - DBSCAN
- Clustering quality is evaluated using standard unsupervised metrics.

---

## Results

### Quantitative Evaluation

The hybrid audio–lyrics representation significantly improves clustering
performance compared to the audio-only baseline.

**K-Means Clustering**
- Silhouette Score: **0.4165**
- Davies–Bouldin Index: **1.0579**

**Agglomerative Clustering**
- Silhouette Score: **0.3947**
- Davies–Bouldin Index: **1.1546**

DBSCAN produced a single cluster or labeled most samples as noise, which is a
known behavior for high-dimensional feature spaces.

---

## Discussion

The results demonstrate that incorporating lyric-based semantic information
substantially enhances clustering quality. Compared to the audio-only approach,
the hybrid model achieves higher Silhouette Scores and more compact clusters.

This confirms that multimodal representations provide richer information for
unsupervised music analysis than acoustic features alone.

---

## How to Run

Install dependencies from the project root directory:

```bash
pip install -r ../requirements.txt
```
Train the audio VAE model:
```bash
python train_vae.py

```
Run hybrid clustering:

```bash
python clustering_hybrid.py

```
---
## Output
1. Hybrid audio–lyrics feature representations
2.Clustering evaluation metrics for multiple algorithms
---

## Notes
The lyric text data (`lyrics.csv`) used in this task is included in the repository.Raw audio files are not included due to dataset size constraints.The publicly available GTZAN Genre Dataset can be added locally to reproduce the experiments.This task builds directly on the Easy Task baseline.


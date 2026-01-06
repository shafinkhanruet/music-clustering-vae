# Hard Task: Music Clustering using Beta-Variational Autoencoder

## Overview

This task explores an advanced unsupervised music clustering approach using a
**Beta-Variational Autoencoder (Beta-VAE)**. The objective is to learn more
disentangled and interpretable latent representations by increasing the weight
of the KL-divergence term in the VAE loss function.

The Hard Task builds upon the audio-only baseline by investigating the trade-off
between clustering performance and latent space interpretability.

---

## Methodology

### Audio Feature Extraction
- Audio tracks are processed using Mel-Frequency Cepstral Coefficients (MFCCs).
- Each track is converted into a fixed-length feature vector for model input.

### Beta-Variational Autoencoder
- A fully connected Beta-VAE is trained on MFCC-based audio features.
- Latent dimension: **16**
- A higher KL-divergence weight (**β > 1**) is used to encourage disentangled
  latent representations.
- The model is trained in an unsupervised manner using reconstruction loss and
  weighted KL divergence.

### Clustering
- Latent representations learned by the Beta-VAE are used for clustering.
- K-Means clustering is applied to the latent space.
- Clustering quality is evaluated using standard unsupervised metrics.

---

## Results

### Quantitative Evaluation

The clustering performance achieved using Beta-VAE latent representations is
summarized below:

- **Silhouette Score:** 0.1948  
- **Calinski–Harabasz Index:** 307.46  
- **Davies–Bouldin Index:** 1.3293  

Compared to the standard VAE baseline, the Beta-VAE yields slightly lower
clustering scores. This behavior is expected, as stronger regularization
prioritizes disentanglement over reconstruction accuracy and cluster compactness.

---

## Discussion

The results highlight a key trade-off in representation learning. While the
Beta-VAE encourages more interpretable and factorized latent dimensions, this
often comes at the cost of reduced clustering performance. Despite lower
quantitative scores, the learned latent space is better structured for
understanding underlying generative factors in the data.

This makes Beta-VAE particularly suitable for analysis and interpretability
rather than purely optimization-driven clustering performance.

---

## How to Run

Install dependencies from the project root directory:

```bash
pip install -r ../requirements.txt
```
Train the Beta-VAE model: 

```bash
python train_beta_vae.py
```
Run clustering on the learned latent representations:

```bash
python clustering_beta_vae.py
```
---
## Output
1. Trained Beta-VAE model (`beta_vae_model.pth`)
2. Latent representations
3. Clustering evaluation metrics
---

## Notes
Raw audio files are not included due to dataset size constraints. The publicly available **GTZAN Genre Dataset** is used and can be added locally to reproduce the experiments. This task represents the most advanced experimental setup in the project.

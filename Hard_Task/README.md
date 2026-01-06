## Hard Task: Beta-VAE for Disentangled Music Representations

This task explores an advanced Variational Autoencoder variant, Beta-VAE,
to encourage disentangled latent representations for music clustering.

### Methodology
- Audio features are extracted using MFCCs.
- A Beta-VAE is trained by introducing a weighting factor (beta) on the
  KL-divergence term of the VAE loss function.
- The increased regularization encourages the model to learn more interpretable
  and disentangled latent factors.

### Clustering and Evaluation
- Latent representations learned by the Beta-VAE are clustered using K-Means.
- Clustering performance is evaluated using Silhouette Score,
  Calinski–Harabasz Index, and Davies–Bouldin Index.

### Outcome
While the Beta-VAE may slightly reduce clustering compactness compared to the
standard VAE, it provides improved interpretability of latent dimensions and
demonstrates the trade-off between disentanglement and clustering performance.

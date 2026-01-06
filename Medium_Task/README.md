## Medium Task: Hybrid Audio–Lyrics Music Clustering

This task extends the baseline audio-only clustering approach by incorporating
textual information from song lyrics. The goal is to improve clustering quality
by leveraging multimodal features.

### Methodology

* Audio features are extracted using Mel-Frequency Cepstral Coefficients (MFCCs).
* A Variational Autoencoder (VAE) is trained to learn compact latent representations
  from audio features.
* Lyrics are processed using TF-IDF vectorization to obtain text-based features.
* Audio latent vectors and lyric features are concatenated to form a hybrid
  representation.

### Clustering and Evaluation

* Clustering is performed using K-Means, Agglomerative Clustering, and DBSCAN.
* Performance is evaluated using Silhouette Score and Davies–Bouldin Index.

### Outcome

The hybrid audio–lyrics representation demonstrates improved clustering quality
compared to the audio-only baseline, highlighting the benefit of multimodal
feature integration.


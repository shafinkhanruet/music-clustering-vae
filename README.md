#  Unsupervised Music Clustering using Variational Autoencoders

##  Overview

This project presents an **unsupervised framework for music clustering** using **Variational Autoencoders (VAEs)**.  
The objective is to learn **compact and meaningful latent representations** from audio signals and perform clustering in the learned latent space to identify **structural similarities between music tracks**.

The pipeline is **fully reproducible** and designed to be **easily extensible** with additional modalities (such as lyrics or metadata) and alternative clustering algorithms.  
The project is organized into **Easy**, **Medium**, and **Hard** tasks to reflect progressive levels of methodological complexity.

---

##  Methodology

###  Audio Feature Extraction

- Audio tracks are processed using **Mel-Frequency Cepstral Coefficients (MFCCs)**, which capture perceptually relevant spectral characteristics.
- Each track is transformed into a **fixed-length feature vector** suitable for neural network input.

---

###  Variational Autoencoder (Easy Task)

- A **fully connected Variational Autoencoder** is trained on MFCC-based audio features.
- **Latent dimension:** 16
- The model is trained in an **unsupervised manner** using:
  - Reconstruction loss  
  - Kullback–Leibler (KL) divergence
- Latent representations learned by the VAE are used for clustering.

---

###  Clustering

- **K-Means clustering** is applied to the learned latent representations.
- **Number of clusters:** 10
- Clustering quality is evaluated using standard **unsupervised metrics**.

---

## Results

### Quantitative Evaluation (Audio-Only)

| Metric                    | Value   |
|---------------------------|---------|
| Silhouette Score          | 0.2267  |
| Calinski–Harabasz Index   | 452.61  |

These results indicate that the VAE successfully captures **meaningful structure** in the audio data, enabling effective unsupervised clustering.

---

## Hybrid Audio–Lyrics Extension (Medium Task)

An extended experiment integrates **textual information** by combining:

- VAE-based **audio latent representations**
- **TF-IDF features** extracted from song lyrics

The resulting **hybrid feature space** is evaluated using multiple clustering algorithms:

- K-Means  
- Agglomerative Clustering  
- DBSCAN  

The hybrid representation **significantly improves clustering quality**, achieving:
- Higher **Silhouette Scores**
- Lower **Davies–Bouldin Index** values  

This demonstrates the benefit of incorporating **semantic information from lyrics** alongside acoustic features.

---

## Advanced Extension: Beta-VAE (Hard Task)

An advanced experiment employs a **Beta-VAE** to encourage **disentangled latent representations** by increasing the weight of the KL-divergence term.

- Clustering performance is **slightly reduced** compared to the standard VAE
- Latent dimensions are **more interpretable and factorized**

These results highlight the trade-off between:
- **Clustering compactness**
- **Latent space interpretability**

This trade-off is a key characteristic of **disentangled representation learning**.

---

##  Visualization

A **t-SNE visualization** of the VAE latent space illustrates the separation of clusters learned by the audio-only model.


::contentReference[oaicite:0]{index=0}


**Path:**  
Easy_Task/results/tsne_latent_space.png

---

## 🏁 Conclusion

This project demonstrates that **Variational Autoencoders** are effective for learning **compact latent representations** from music audio features, enabling meaningful **unsupervised clustering**.

The progressive extension from:
- Audio-only clustering  
- Multimodal audio–lyrics learning  
- Disentangled representation learning (Beta-VAE)  

provides a **comprehensive exploration of modern unsupervised techniques** for music analysis.

The **modular design** of the framework allows for straightforward extension with additional data modalities and learning objectives, making it suitable for both **academic research** and **practical applications** in **Music Information Retrieval (MIR)**.

---

##  Dataset Availability

Due to dataset size constraints, **raw audio files are not included** in this repository.

- Experiments were conducted using the **GTZAN Genre Dataset**, which is publicly available.
- To reproduce the results, download the dataset separately and place it under: `data/audio/`




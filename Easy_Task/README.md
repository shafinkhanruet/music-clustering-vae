# Audio-Only Music Clustering Using a Variational Autoencoder (VAE)

This repository implements a **baseline unsupervised approach** for music clustering using **audio features only**.  
A **Variational Autoencoder (VAE)** is trained on **Mel-Frequency Cepstral Coefficients (MFCCs)** to learn compact latent representations of music tracks.  
Clustering is then performed in the learned latent space to identify **structural similarities** between tracks.

---

## Overview

- **Input**: Raw audio tracks  
- **Feature Representation**: MFCCs  
- **Model**: Fully connected Variational Autoencoder  
- **Latent Dimension**: 16  
- **Clustering Algorithm**: K-Means  
- **Learning Paradigm**: Unsupervised  

---

## Methodology

### Audio Feature Extraction

- Music tracks are processed using **Mel-Frequency Cepstral Coefficients (MFCCs)**.
- Each track is converted into a **fixed-length feature vector** to ensure consistency across the dataset.

### Variational Autoencoder

- A fully connected VAE is trained in an unsupervised manner.
- The model compresses high-dimensional MFCC features into a compact latent space.

**Training Objective**
- Reconstruction Loss: Mean Squared Error (MSE)
- Regularization Term: Kullback–Leibler (KL) divergence

The combined objective encourages faithful reconstruction while enforcing a smooth latent distribution.

### Clustering

- **Algorithm**: K-Means
- **Input Space**: 16-dimensional latent vectors learned by the VAE
- **Goal**: Group tracks with similar musical structure based on latent similarity

---

## Results

### Quantitative Evaluation

Cluster quality is evaluated using standard unsupervised metrics.

| Metric                    | Value  |
|---------------------------|--------|
| Silhouette Score          | 0.2267 |
| Calinski–Harabasz Index   | 452.61 |

These results indicate that the VAE learns **meaningful latent representations** that capture structural similarities between music tracks.

### Visualization

A t-SNE projection of the latent space illustrates the separation of clusters learned by the audio-only VAE.

![image alt]([image_url](https://github.com/shafinkhanruet/music-clustering-vae/blob/ae421d02b34b4b24206632821b7643d1a6b02b1e/Easy_Task/results/tsne_latent_space.png))

---

## How to Run

### Install Dependencies

From the project root:

```bash
pip install -r ../requirements.txt
```

Train the Variational Autoencoder
```bash
python train_vae.py
```
Run Clustering and Visualization
```bash
python clustering.py
```

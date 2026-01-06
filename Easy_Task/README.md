## \# Easy Task: Audio-Only Music Clustering using VAE

## 

## \## Overview

## 

## This task implements the baseline approach for unsupervised music clustering

## using audio features only. A standard Variational Autoencoder (VAE) is trained

## on Mel-Frequency Cepstral Coefficients (MFCCs) extracted from music tracks to

## learn compact latent representations. Clustering is then performed in the

## learned latent space to identify structural similarities between tracks.

## 

## ---

## 

## \## Methodology

## 

## \### Audio Feature Extraction

## \- Music tracks are processed using Mel-Frequency Cepstral Coefficients (MFCCs).

## \- Each track is converted into a fixed-length feature vector for consistency.

## 

## \### Variational Autoencoder

## \- A fully connected VAE is trained in an unsupervised manner.

## \- Latent dimension: 16

## \- The training objective combines reconstruction loss and KL divergence.

## 

## \### Clustering

## \- K-Means clustering is applied to the learned latent representations.

## \- Cluster quality is evaluated using standard unsupervised metrics.

## 

## ---

## 

## \## Results

## 

## \### Quantitative Evaluation

## \- \*\*Silhouette Score:\*\* 0.2267  

## \- \*\*Calinski–Harabasz Index:\*\* 452.61  

## 

## These results indicate that the VAE learns meaningful latent representations

## that capture structural similarities between music tracks.

## 

## \### Visualization

## A t-SNE visualization of the latent space is provided to illustrate the

## separation of clusters learned by the audio-only VAE.

## 

## <p align="center">

## &nbsp; <img src="results/tsne\_latent\_space.png" width="600">

## </p>

## 

## ---

## 

## \## How to Run

## 

## Install dependencies from the project root:

## 

## ```bash

## pip install -r ../requirements.txt


Train the Variational Autoencoder:
python train\_vae.py


Run clustering and visualization:
python clustering.py




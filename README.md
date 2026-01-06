# Music Clustering using Variational Autoencoders

This repository contains an unsupervised music clustering project implemented
using Variational Autoencoders (VAEs). The project is structured to clearly
separate Easy, Medium, and Hard task requirements.

Each task is organized in a dedicated folder for clarity and ease of evaluation.

---

## Repository Structure

music-clustering-vae/
│
├── Easy_Task/
│ ├── train_vae.py
│ ├── clustering.py
│ └── README.md
│
├── Medium_Task/
│ ├── train_vae.py
│ ├── clustering_hybrid.py
│ └── README.md
│
├── Hard_Task/
│ ├── beta_vae.py
│ ├── train_beta_vae.py
│ ├── clustering_beta_vae.py
│ └── README.md
│
├── results/
│ └── (saved models and figures)
│
├── requirements.txt
└── README.md


---

## Task Overview

### Easy Task
Audio-only music clustering using MFCC features and a standard Variational Autoencoder (VAE).
Clustering is performed on the learned latent representations.

### Medium Task
Hybrid clustering using both audio features and textual lyric features.
Multiple clustering algorithms are applied to evaluate clustering performance.

### Hard Task
Advanced clustering using a Beta-VAE to encourage disentangled latent representations.

---

## Dataset

This project uses a publicly available music dataset (e.g., GTZAN).
Due to size constraints, raw audio files are not included in the repository.
The dataset can be added locally in a `data/` directory to reproduce experiments.

---

## Setup and Usage

Install dependencies:

```bash
pip install -r requirements.txt

Run any task separately, for example:

cd Easy_Task
python train_vae.py
python clustering.py


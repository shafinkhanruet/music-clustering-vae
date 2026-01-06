import os
import torch
from torch.utils.data import DataLoader

from dataset import MusicDataset
from beta_vae import BetaVAE

# -----------------------------
# Paths
# -----------------------------
AUDIO_DIR = "../data/audio"
MODEL_PATH = "../results/beta_vae_model.pth"

# -----------------------------
# Hyperparameters
# -----------------------------
BATCH_SIZE = 16
EPOCHS = 10
LATENT_DIM = 16
LEARNING_RATE = 5e-4
BETA = 4.0  # Beta-VAE regularization strength

# -----------------------------
# Dataset & Dataloader
# -----------------------------
dataset = MusicDataset(AUDIO_DIR)
input_dim = len(dataset[0])

dataloader = DataLoader(
    dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

# -----------------------------
# Model & Optimizer
# -----------------------------
model = BetaVAE(
    input_dim=input_dim,
    latent_dim=LATENT_DIM,
    beta=BETA
)

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE
)

# -----------------------------
# Training Loop
# -----------------------------
model.train()
for epoch in range(EPOCHS):
    total_loss = 0.0

    for batch in dataloader:
        optimizer.zero_grad()

        recon, mu, logvar = model(batch)
        loss = model.loss_function(recon, batch, mu, logvar)

        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(dataloader)
    print(f"Epoch {epoch + 1}/{EPOCHS}, Loss: {avg_loss:.4f}")

# -----------------------------
# Save Model
# -----------------------------
os.makedirs("../results", exist_ok=True)
torch.save(model.state_dict(), MODEL_PATH)

print("Beta-VAE model saved to", MODEL_PATH)

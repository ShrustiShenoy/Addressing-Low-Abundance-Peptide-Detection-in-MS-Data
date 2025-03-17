import numpy as np
import os

def generate_cancer_sample():
    mz = np.arange(200, 1000, 0.1)
    intensity = (
        10000 * np.exp(-((mz - 500) ** 2) / 200) +
        8000 * np.exp(-((mz - 800) ** 2) / 150) +
        500 * np.exp(-((mz - 320) ** 2) / 100) +
        300 * np.exp(-((mz - 650) ** 2) / 80) +
        np.random.normal(0, 200, len(mz)) +
        1000 * np.sin(mz / 100)
    )
    return mz, intensity

if __name__ == "__main__":
    mz, intensity = generate_cancer_sample()
    # Ensure data/ exists and save there
    os.makedirs("data", exist_ok=True)
    np.savez("data/cancer_sample.npz", mz=mz, intensity=intensity)
    print("Synthetic data saved to data/cancer_sample.npz")
import matplotlib.pyplot as plt

def plot_spectrum(mz, intensity, peak_mz, peak_intensity):
    plt.figure(figsize=(14, 6))
    plt.plot(mz, intensity, color='blue', label='Spectrum', alpha=0.6)
    low_mask = peak_intensity < 1000
    plt.scatter(peak_mz[low_mask], peak_intensity[low_mask], color='green', 
                label='Low-Abundance Peaks', zorder=5)
    plt.scatter(peak_mz[~low_mask], peak_intensity[~low_mask], color='red', 
                label='High-Abundance Peaks', zorder=5)
    plt.xlabel('m/z')
    plt.ylabel('Intensity')
    plt.title('Cancer Proteomics MS: Low-Abundance Peak Detection')
    plt.legend()
    plt.savefig('results/cancer_spectrum.png')
    plt.close()
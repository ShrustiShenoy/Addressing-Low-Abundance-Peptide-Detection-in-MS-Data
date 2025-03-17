import os
from preprocess import load_npz, adaptive_baseline_correction, filter_noise
from analyze import detect_peaks, summarize_peaks
from visualize import plot_spectrum

def main():
    data_path = 'data/cancer_sample.npz'
    output_table = 'results/peak_summary.csv'

    if not os.path.exists(data_path):
        print("Run data/generate_cancer_sample.py first!")
        return

    mz, intensity = load_npz(data_path)
    intensity = adaptive_baseline_correction(intensity)
    mz, intensity = filter_noise(mz, intensity)

    peak_mz, peak_intensity = detect_peaks(mz, intensity)
    peak_df = summarize_peaks(peak_mz, peak_intensity)
    peak_df.to_csv(output_table, index=False)
    print(f"Detected {sum(peak_df['Abundance'] == 'Low')} low-abundance peaks.")

    plot_spectrum(mz, intensity, peak_mz, peak_intensity)
    print("Outputs saved in results/")

if __name__ == "__main__":
    main()
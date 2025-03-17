from scipy.signal import find_peaks_cwt
import numpy as np
import pandas as pd

def detect_peaks(mz, intensity, widths=np.arange(5, 50), min_snr=1.5):
    peak_indices = find_peaks_cwt(intensity, widths=widths, min_snr=min_snr)
    return mz[peak_indices], intensity[peak_indices]

def summarize_peaks(peak_mz, peak_intensity):
    df = pd.DataFrame({'m/z': peak_mz, 'Intensity': peak_intensity})
    df['Abundance'] = df['Intensity'].apply(lambda x: 'Low' if x < 1000 else 'High')
    return df
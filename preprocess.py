import numpy as np
from scipy.signal import savgol_filter

def load_npz(file_path):
    data = np.load(file_path)
    return data['mz'], data['intensity']

def adaptive_baseline_correction(intensity, window_size=201, poly_order=3):
    baseline = savgol_filter(intensity, window_size, poly_order)
    return np.where(intensity - baseline < 0, 0, intensity - baseline)

def filter_noise(mz, intensity, percentile_threshold=10):
    threshold = np.percentile(intensity, percentile_threshold)
    mask = intensity > threshold
    return mz[mask], intensity[mask]
    
    

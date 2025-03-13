# MassSpecBioinformatics

A bioinformatics pipeline designed to address the challenge of detecting low-abundance peptides in noisy mass spectrometry data, with applications in cancer proteomics.

## Problem Addressed

In mass spectrometry-based proteomics, low-abundance peptides—such as phosphorylated peptides or cancer biomarkers—are frequently missed due to:
- **Noise Interference**: Background noise and baseline drift obscure weak signals in complex samples.
- **Insufficient Sensitivity**: Traditional peak detection methods (e.g., thresholding) lack the sensitivity to identify subtle peaks amidst dominant signals.

This issue is critical in cancer research, where low-abundance peptides often represent biologically significant targets (e.g., signaling proteins). Standard pipelines fail to reliably detect these signals, limiting biomarker discovery and quantitative accuracy (e.g., as noted in challenges with PRIDE datasets).

## Solution

This project implements a targeted pipeline to improve detection of low-abundance peptides:
- **Preprocessing**: Adaptive baseline correction using Savitzky-Golay filtering to preserve weak signals while removing noise and drift.
- **Peak Detection**: Continuous Wavelet Transform (CWT) optimized for sensitivity to low-intensity peaks in noisy spectra.
- **Validation**: Tested on a synthetic dataset mimicking a cancer proteomics sample with known low-abundance peaks.

## Features

- **Enhanced Signal Processing**: Differentiates low-abundance signals from noise with minimal loss of data.
- **Modular Design**: Separates preprocessing, analysis, and visualization for scalability and reusability.
- **Practical Outputs**: Generates visual plots and tabular summaries for downstream analysis.

## Project Structure
MassSpecBioinformatics/
├── data/
│   ├── cancer_sample.npz         # Synthetic cancer proteomics data
│   └── generate_cancer_sample.py # Script to generate sample data
├── src/
│   ├── preprocess.py             # Baseline correction and noise filtering
│   ├── analyze.py                # CWT-based peak detection
│   ├── visualize.py              # Spectrum plotting
│   └── main.py                   # Main pipeline
├── results/
│   ├── cancer_spectrum.png       # Output plot (example)
│   └── peak_summary.csv          # Output peak table (example)
├── README.md                     # Project documentation
├── requirements.txt              # Dependencies
└── LICENSE                       # MIT License

# Real-Time Tremor Analysis and Visualization for Essential Tremor Diagnosis

This project is a biomedical engineering application designed to analyze tremors in real time for the diagnosis of **Essential Tremor (ET)**. Using data from an accelerometer (ADXL362), the system captures, filters, and visualizes tremor signals, and identifies the dominant frequency of the tremor using signal processing techniques. The analysis provides key insights into tremor characteristics, aiding in diagnosis and monitoring.

## Features
- **Real-Time Tremor Data Acquisition**: Captures Y-axis acceleration data from an accelerometer via a serial port.
- **Low-Pass Filtering**: Smooths the raw tremor signal to remove noise.
- **Frequency Analysis**: Identifies the dominant frequency of tremor using Fast Fourier Transform (FFT).
- **Dynamic Visualization**: Displays raw and filtered tremor data in real time.
- **Medical Insights**: Provides objective metrics to assist in diagnosing Essential Tremor.

## Prerequisites
- **Hardware**:
  - ADXL362 accelerometer securely attached to the patient’s body part (e.g., hand, arm) experiencing tremor.
  - Microcontroller (e.g., Arduino) for data acquisition and communication.
  - PC for running the Python analysis.
- **Software**:
  - Python 3.6+
  - Required Python Libraries: `serial`, `matplotlib`, `numpy`, `scipy`

## Setup
### Hardware Configuration
1. Attach the ADXL362 accelerometer to the patient's limb experiencing tremors.
2. Connect the accelerometer to a microcontroller configured to transmit data in the following format via serial:

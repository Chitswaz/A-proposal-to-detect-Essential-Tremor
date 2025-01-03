import serial
import matplotlib.pyplot as plt
import time
import numpy as np
from scipy.signal import butter, lfilter
from scipy.fft import fft

ser = serial.Serial('COM3', 9600)

# Set up the plot
plt.ion() # Turn on interactive mode
fig, ax = plt.subplots()
line_raw, = ax.plot([], []) # Create an empty line for the raw data
line_filtered, = ax.plot([], []) # Create an empty line for the filtered data
ax.set_xlabel('Time (s)')
ax.set_ylabel('Y Acceleration')

# Initialize the filter
cutoff_freq = 7   # cutoff frequency in Hz
sampling_freq = 100  # sampling frequency in Hz
order = 2   # order of the filter
nyquist_freq = 0.5 * sampling_freq
cutoff_freq_norm = cutoff_freq / nyquist_freq
b, a = butter(order, cutoff_freq_norm, btype='low')

# Read and plot the y values from the ADXL362
t0 = time.time() # Get the start time
t = []
y_raw = []
y_filtered_list = []
dominant_freqs = []

while True:
    data = ser.readline().decode().strip() # Read the data from the serial port  
    values = data.split('\t') # Split the data into separate values using tabs
    if len(values) == 4:
        # Extract the y value
        y_raw_val = int(values[1].split('=')[1])
        
        # Filter the y value using the lowpass filter
        y_filtered_val = lfilter(b, a, [y_raw_val])[0]
        
        # Append the current time and y values to the lists
        t.append(time.time() - t0)
        y_raw.append(y_raw_val)
        y_filtered_list.append(y_filtered_val)
        
        # Extract the dominant frequency using the Fourier transform
        sample_rate = len(y_filtered_list) / t[-1] # calculate the sample rate
        fft_data = fft(y_filtered_list)
        freq_axis = np.linspace(0, sample_rate / 2, len(y_filtered_list) // 2 + 1)
        dominant_freq_index = np.argmax(np.abs(fft_data[:len(y_filtered_list) // 2 + 1]))
        dominant_freq = freq_axis[dominant_freq_index]
        dominant_freqs.append(dominant_freq)
        
        # Update the plot every 0.2 seconds
        if t[-1] >= 0.2:
            line_raw.set_data(t, y_raw)
            line_filtered.set_data(t, y_filtered_list)
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw()
            fig.canvas.flush_events()

            # Print the dominant frequency to the console
            print("Dominant frequency:", dominant_freq)
            
            # Reset the time and data lists
            t = []
            y_raw = []
            y_filtered_list = []

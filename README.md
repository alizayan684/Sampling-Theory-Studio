# Signal Sampler
![Main Picture](screenshots/home.png)


## Description

- Desktop Application Designed To Demonstrate The Principles Of Signal Sampling & Recovery Based On The Nyquist–Shannon Sampling Theorem
- User-Friendly Interface For Easy Visualization Of Different Samping Scenarios
- Provides Additional Reconstruction Methods

## Tech Stack Used

|**Functionality** | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)|
|--- | --- |
|**UI** | ![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)|
|**Styling** | [![CSS](https://img.shields.io/badge/CSS-1572B6?logo=css3&logoColor=fff)](#)|

## Features
### 1. Signal Browsing
- Browse A Signal File (Make Sure Its Format & Extension Are The Same As The Files Inside `signals` Directory)

### 2. Signal Mixer
- Sample At Different Frequncies, Showcasing The Difference Between Complete Reconstruction & Aliasing In Real Time

![Sampling GIF](screenshots/sampling.gif)
&nbsp;
- Add A Sinusoidal Signal Of Custom Amplitude, Frequency & Phase

![Adding Component GIF](screenshots/add.gif)
&nbsp;
- Remove A Sinusoidal Signal From The Combined Signal
   
![Removing Component GIF](screenshots/remove.gif)
### 3. Noise Addition
- Add Noise To The Combined Signal Using Controllable SNR Slider
   
![Adding Noise GIF](screenshots/noise.gif)
### 4. Different Reconstruction Methods
- Reconstruct The Signal Using Different Methods
   
![Rectangular Interpolation GIF](screenshots/rectangular.gif)
### 5. Testing Scenarios
- Generate Premade Test Scenarios Having Different Combined Signals
   
![Scenarios GIF](screenshots/scenarios.gif)


## Installation

1. Make Sure That Pip & Python Are Installed On Your System

2. Clone The Repo Onto Your Local System or Download The Zip File & Extract It
   ```bash
    git clone https://github.com/mostafa-aboelmagd/signal-sampling-visualizer.git
    ```

3. Nagivate To The Project's Directory 
   
4. Install The Required Libraries
    ```bash
    pip install -r requirements.txt
    ```

5. Run `MainWindow.py` File
    ```bash
    python MainWindow.py
    ```

## Contributors

| Name | GitHub | LinkedIn |
| ---- | ------ | -------- |
| Mostafa Ayman | [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/mostafa-aboelmagd) | [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mostafa--aboelmagd/) |
| Ali Zayan | [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/alizayan684) | [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/%D8%B9%D9%84%D9%8A-%D8%B2%D9%8A%D8%A7%D9%86-%F0%9F%94%BB%F0%9F%87%B5%F0%9F%87%B8-b98239264/) |
| Zeyad Amr | [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/Zisco2002)| [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zeyad-amr-3506b225b/) |
| Mostafa Mousa | [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/MostafaMousaaa) | [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mostafa-mousa-b81b8322a/) |
| Omar Khaled | [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](#)| [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/omar-khaled-064b7930a/) |

# Spinal Cord Injury Application

## What is this codebase about?

It contains the code for an iOS mobile application that provides educational content on spinal cord injuries (SCIs). There is also a Python inference server and machine learning code that is utlized by the mobile application to predict ASIA scores at hospital discharge time.

## How is the codebase structured?

|     Path                                           |     What does it   contain?                                           |
|----------------------------------------------------|-----------------------------------------------------------------------|
|     ~/                                             |     Everything (including this file)                                  |
|     ~/src/                                         |     All code                                                          |
|     ~/src/server/                                  |     Server-side API code                                              |
|     ~/src/shared/                                  |     Anaconda environment files                                        |
|     ~/src/mobile_app/SCI Recovery/                 |     iOS project                                                       |
|     ~/src/mobile_app/SCI Recovery/SCI Recovery/    |     Core iOS Swift code                                               |
|     ~/src/ml/                                      |     All ML code                                                       |
|     ~/src/ml/notebooks/                            |     ML ad hoc research code                                           |
|     ~/src/ml/modelling/                            |     ML training, testing, and feature   importance code               |
|     ~/src/ml/modelling/pickles/                    |     ML model training outputs                                         |
|     ~/src/ml/modelling/plots/                      |     ML feature importance graphs                                      |
|     ~/src/ml/data/                                 |     ML data handling and transformation code                          |
|     ~/src/ml/data/csvs/                            |     Raw dataset                                                       |
|     ~/src/ml/data/docs/                            |     Raw dataset documentation                                         |
|     ~/src/ml/data/utils/                           |     Commonly used utilities for data handling   and transformation    |

## Requirements to run machine learning server

- Either Ubuntu or Windows 10
- Git
- Anaconda or Miniconda (https://www.anaconda.com/)
- [Optional] NSCISC Dataset (https://www.nscisc.uab.edu/Research/NSCISC_DatabasePublicUse)

## Steps to setup machine learning server

*Steps here are shown for Ubuntu, but similar steps can be followed for Windows.*

1. Clone repository: `git clone https://github.com/kapoor1992/spinal_cord_injury_recovery.git`
2. Navigate to the shared directory: `cd src/shared`
3. Create the conda environment: `conda env create --file environment_ubuntu.yml` 
4. Activate the environment: `conda activate sci`

## Steps to build machine learning model

*If you want to use the existing model in `src/ml/modelling/pickles/`, then skip these steps entirely.*

1. Copy `f1_public.csv` from NSCISC into `src/ml/data/csvs/`
2. Activate conda environment: `conda activate sci`
3. Navigate to the modelling directory: `cd src/ml/modelling`
4. Run model training (intepret flag is optional): `python sklearn_model_runs.py --interpret`
5. Verify that `model.pkl` was output in `src/ml/modelling/pickles/`
6. If `--interpret` was used, verify that `importance.png` can be seen in `src/ml/modelling/plots/`

## Requirements to run inference server

- Either Ubuntu or Windows 10
- Machine learning server has been setup

## Steps to setup inference server

None!

## Steps to run inference server

1. Activate conda environment: `conda activate sci`
2. Navigate to server code: `cd src/server`
3. Run server: `python server.py`

Server will be running on port 8000 at the POST endpoint `/PostInference`
Sample REST body can be found at `src/ml/modelling/input.json` to test the server.

## Requirements to run mobile client (Simulator)

- macOS 12 or up
- XCode 13 or up
- Cocoapods installed (https://guides.cocoapods.org/using/getting-started.html)

## Steps to run mobile client (Simulator)

Path: "mobile app/SCI Recovery"

1. Install pods: `pod install`
2. Open XCode
3. Open `SCI Recovery.xcworkspace` once pods are installed
4. Run with any desired iOS Simulator

# [DEPRECATED]

### Requirements to run mobile client (iOS Device)
- An iOS device running iOS 13 or up

### Steps to run mobile client (iOS Device)
![QR Code for the Testflight URL](TestflightQR.jpg)
1. Using your iOS device scan the QR Code above or navigate to https://testflight.apple.com/join/qWvhNwVF
2. Get the Apple's official TestFlight app through the App Store
3. Come back to the URL and click "Start Testing" button to get the application through TestFlight
4. After installing through the TestFlight, you may start using the mobile application

# Spinal Cord Injury Application

## What is this codebase about?

It contains the code for predicting ASIA classification after a spinal cord injury.

## How is the codebase structured?

|     Path                                           |     What does it   contain?                                           |
|----------------------------------------------------|-----------------------------------------------------------------------|
|     ~/                                             |     Everything (including this file)                                  |
|     ~/src/                                         |     All code                                                          |
|     ~/src/ml/                                      |     All ML code                                                       |
|     ~/src/ml/notebooks/                            |     ML ad hoc research code                                           |
|     ~/src/ml/modelling/                            |     ML training, testing, and feature   importance code               |
|     ~/src/ml/modelling/pickles/                    |     ML model training outputs                                         |
|     ~/src/ml/modelling/plots/                      |     ML feature importance graphs                                      |
|     ~/src/ml/data/                                 |     ML data handling and transformation code                          |
|     ~/src/ml/data/csvs/                            |     Raw dataset                                                       |
|     ~/src/ml/data/docs/                            |     Raw dataset documentation                                         |
|     ~/src/ml/data/utils/                           |     Commonly used utilities for data handling   and transformation    |

## Requirements to run machine learning

- Windows 10
- Git
- Anaconda or Miniconda (https://www.anaconda.com/)
- NSCISC Dataset (https://www.nscisc.uab.edu/Research/NSCISC_DatabasePublicUse)

## Steps to setup machine learning (Anaconda Terminal)

1. Clone repository: `git clone https://github.com/kapoor1992/spinal_cord_injury_recovery.git`
2. Navigate to the shared directory: `cd src/ml`
3. Create the conda environment: `conda env create --file environment_windows.yml` 
4. Activate the environment: `conda activate sci`

## Steps to run machine learning (Anaconda Terminal)

1. Copy `f1_public.csv` from NSCISC into `src/ml/data/csvs/`
2. Activate conda environment: `conda activate sci`
3. Navigate to the modelling directory: `cd src/ml/modelling`
4. Run model training (flags are optional): `python model_runs.py --interpret --drop-patients-who-worsened`
5. If `--interpret` was used, verify that `importance.png` can be seen in `src/ml/modelling/plots/`

# Air Quality Analysis: Aotizhongxin Station🌍

## Live Dashboard
Explore the live dashboard here : [Air Quality Dashboard](https://airqualitydata-ds.streamlit.app/)

## Libraries Used
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- Numpy
- Plotly

## Data Source
The air quality data used in this project was obtained from the Aotizhongxin Station. The dataset contains measurements of various air pollutant with a focus on PM2.5. The goal is to identify patterns, seasonal fluctuations, and how various weather conditions affect the air quality.

## Key Insight
- The analysis reveals a clear seasonal pattern in pollutant levels with PM2.5 concentrations peaking during winter months
- Impact of wind speed, rainfall's role, and wind direction on air quality
- Correlation between PM2.5 levels and weather conditions

## How to Run the Dashboard
### 1. Create and Activate a Python Environtment:

  - **Using Conda** : [Conda](https://docs.conda.io/en/latest/)
    ```bash
    conda create --name airquality-ds python=3.9
    conda activate airquality-ds
    ```
  - **Using venv** :
    ```bash
    python -m airquality-ds
    #Mac/Linux users
    source airquality-ds/bin/activate
    #Windows users
    airquality-ds\Scripts\activate
    ```

### 2. Install Requirements Packages:
- Install the following packages for running the analysis and dashboard:
  ```bash
  pip install pandas matplotlib seaborn streamlit numpy plotly
  ```

- or install the requirements.txt:
  ```bash
  pip install -r requirements.txt
  ```

## Run the Streamlit App
- After installing the dependencies, run the Streamlit app with:
  ```bash
  streamlit run dashboard.py
  ```

## Additional Files
A detailed Python notebook [Air_Quality_Analysis_Jessica.ipnyb](https://colab.research.google.com/drive/1gJ-fCBJChavRsVhwGt1xGeCsJD_bHqvF?usp=sharing) contains data analysis and visualization.
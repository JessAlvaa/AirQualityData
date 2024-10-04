import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import numpy as np

# Read data
air_data = pd.read_csv('Air_Quality_Aotizhongxin.csv')

# Add date column
air_data['date'] = pd.to_datetime(air_data[['year', 'month', 'day', 'hour']], errors='coerce')

st.title("Air Quality Analysis")
st.write("This dashboard shows the visualization of air quality data from 2013 until 2017 at Aotizhongxin station.")

# Filter data for PM2.5 only (pertahankan filter tahun untuk Question 1)
year = 2017
data_filter = air_data[air_data['year'] == year]

# Shows filtered data for PM2.5
st.header(f'Data Overview for Year {year}')
st.write(data_filter[['date', 'PM2.5', 'TEMP', 'DEWP', 'WSPM']])

st.header("Question 1")
st.write("What is the correlation between PM2.5 concentrations and other variables such as temperature, humidity, and wind speed over the past year?")

# Heatmap for PM2.5 correlations
st.subheader(f'Correlation Heatmap for PM2.5 in {year}')
plt.figure(figsize=(10, 8))
matrix_corr = data_filter[['PM2.5', 'TEMP', 'DEWP', 'WSPM']].corr()
sns.heatmap(matrix_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title(f'Correlation Heatmap for PM2.5 in {year}')
st.pyplot(plt)

# Pairplot
st.subheader('Pairplot')
st.write("The pairplot provides a visual comparison of the relationships between PM2.5 and other variables such as temperature (TEMP), dew point (DEWP), and wind speed (WSPM). Each plot in the matrix represents a bivariate relationship between two variables, allowing us to observe patterns or correlations.")
pairplot_col = ['PM2.5', 'TEMP', 'DEWP', 'WSPM']
pairplot_fig = sns.pairplot(data_filter[pairplot_col])
st.pyplot(pairplot_fig.fig)

# Question 2 - Average PM2.5 by wind direction for all years
st.header("Question 2")
st.write("Which wind direction contributed the most to PM2.5 pollution levels from 2013 - 2017 in Aotizhongxin?")

# Hitung rata-rata PM2.5 berdasarkan arah angin dari seluruh data
wind_direction_avg = air_data.groupby('wd')['PM2.5'].mean().sort_values(ascending=False)
st.subheader('Average PM2.5 by Wind Direction from 2013 to 2017')
plt.figure(figsize=(10, 5))
plt.bar(wind_direction_avg.index, wind_direction_avg.values, color='green')
plt.title('Average PM2.5 by Wind Direction from 2013 to 2017')
plt.xlabel('Wind Direction')
plt.ylabel('Average PM2.5')
st.pyplot(plt)

# Wind Direction Distribution
st.subheader('Wind Direction Distribution for PM2.5')
wind_data = air_data.groupby('wd')['PM2.5'].mean()
fig = plt.figure(figsize=(8, 6))
colors = cm.Blues(wind_data.values / max(wind_data.values))
ax = fig.add_subplot(111, polar=True)

# Convert wd to theta for polar plot
st.write("Color Gradient: The varying shades of blue represent different PM2.5 levels. Darker shades indicate higher concentrations, while lighter shades indicate lower concentrations.")
theta = np.linspace(0, 2 * np.pi, len(wind_data), endpoint=False)
bars = ax.bar(theta, wind_data.values, align='center', color=colors, alpha=0.5)
ax.set_xticks(theta)
ax.set_xticklabels(wind_data.index)
plt.title('PM2.5 Levels by Wind Direction from 2013 to 2017')
st.pyplot(fig)

st.subheader('Conclusion')
st.write(""" 
- The dashboard provides an overview of PM2.5 levels across different years and wind directions.
- This analysis helps monitor and understand how PM2.5 levels are affected by wind conditions.
- Strong wind from the NE direction tends to reduce PM2.5 levels, while low wind from SSE contributes to higher pollution levels.
""")

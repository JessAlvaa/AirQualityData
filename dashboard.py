#import all the library
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import streamlit as st
import numpy as np
import plotly.express as px
sns.set(style='dark')

# Load the dataset
data = pd.read_csv("Air_Quality_Aotizhongxin.csv")

st.title("Air Quality Analysis")
st.write("This dashboard shows the visualization of air quality data from 2013 until 2017 at Aotizhongxin station.")

# Change to datetime for column date
data['date'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']], errors='coerce')

# Sidebar
st.sidebar.header("Choose Air Pollutant")

# Input to select year
year = st.sidebar.slider("Years", int(data["year"].min()), int(data["year"].max()), int(data["year"].min()))

#Create sidebar 
pollutant = st.sidebar.selectbox("All Pollutant", ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"])

# Filter the data
pollutant_filtered = data[(data["year"] == year)]
pollutant_filtered = pollutant_filtered.drop(columns=['direction_degrees'])

# Display the dataset
st.subheader(f"Air Quality Data for {year}")
st.write(pollutant_filtered)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
display_heatmap = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES']
pollutant_corr = pollutant_filtered[display_heatmap].corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(pollutant_corr, annot=True, fmt=".2f", cmap='coolwarm', square=True, ax=ax)
st.pyplot(fig)

# Histogram
st.subheader(f"Histogram of {pollutant}")
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(pollutant_filtered[pollutant], bins=20, color='purple')
ax.set_xlabel(pollutant)
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Line graph
st.subheader(f"Line Graphic for {pollutant}")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(pollutant_filtered["date"], pollutant_filtered[pollutant], color='purple')
ax.set_xlabel("Date")
ax.set_ylabel(pollutant)
st.pyplot(fig)

# Display Pollutant Average per month
st.subheader("Pollutant Average per Month")
month_average = pollutant_filtered.groupby(pollutant_filtered['date'].dt.month)[pollutant].mean()
# Make sure all the data is in index
all_months = pd.Index(range(1, 13))
month_average = month_average.reindex(all_months)
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(month_average.index, month_average.values, marker='o', color='purple')
ax.set_xlabel("Month")
ax.set_ylabel(f"Average {pollutant}")
ax.set_title(f"Average {pollutant} by Month")
ax.set_xticks(all_months)
ax.set_xticklabels(month_labels)
st.pyplot(fig)

# Count Average Heatmap for PM2.5
st.subheader('Hourly Averages of PM2.5')
# Ensure correct data types and handle missing values
data['hour'] = data['hour'].astype(int)
data['PM2.5'] = pd.to_numeric(data['PM2.5'], errors='coerce') #handle value that can't be converted to numeric
data['PM2.5'].ffill(inplace=True)
hour_average = data.groupby('hour')['PM2.5'].mean()
# Create the heatmap
fig, ax = plt.subplots(figsize=(10, 4))
sns.heatmap(hour_average.to_numpy().reshape(1, -1), annot=False, fmt=".2f", cmap='viridis', cbar=True, ax=ax)
ax.set_xticklabels(range(24), rotation=45)
# Hide y-axis label
ax.set_yticklabels([''])  
ax.set_xlabel("Hour")
st.pyplot(fig)

#Rain vs pollutant
st.subheader(f"Relationship between Rain and {pollutant}")
fig = px.scatter(pollutant_filtered, x="RAIN", y=pollutant,
                labels={"RAIN": "Rainfall (mm)", pollutant: pollutant},
                title=f"Scatter Plot of Rain VS {pollutant}",  color_continuous_scale="Inferno"
                ) 
st.plotly_chart(fig)

# Scatter Plot Polutan and Wind
st.subheader(f"Relationship between Wind and {pollutant}")
fig = px.scatter(pollutant_filtered, x="WSPM", y="wd", color=pollutant,
                 labels={"WSPM": "Wind Speed (m/s)" ,"wd": "Wind Direction"},
                 title=f"Scatter Plot of Wind VS {pollutant}")
st.plotly_chart(fig)


#Wind Direction
st.subheader('Wind Direction')
wind_data = pollutant_filtered.groupby('wd')[pollutant].mean()
fig = plt.figure(figsize=(5,6))
colors = cm.Blues(wind_data.values/max(wind_data.values))
ax = fig.add_subplot(111, polar=True)
#convert wd to theta for polar plot
theta = np.linspace(0, 2 * np.pi, len(wind_data))
bars = ax.bar(theta, wind_data.values, align='center', color = colors, alpha=0.5)
plt.title(f"{pollutant} Levels by Wind")
st.pyplot(fig)


st.subheader('Conclusion')
st.write(""" 
- Users can explore this dashboard to understand air quality trends
- This dashboard offers various interactive visualization of all pollutant distribution
- Provides insight the distribution of air quality and wind affects, assisting in monitoring and mitigating the impact of air pollution
""")



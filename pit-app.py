import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
def load_data():
    df = pd.read_csv("2007-2023-Combined-PIT-Counts-by-CoC.csv")
    return df

# Sidebar for user input
st.sidebar.title("Select CoC")
# Load data and get unique CoC numbers
data = load_data()
coc_numbers = data["CoC Number"].unique().tolist()
selected_coc = st.sidebar.selectbox("Choose a CoC", coc_numbers)

# Main content
st.title("PIT Count Visualization App")

# Filter data based on selected CoC
filtered_data = data[data["CoC Number"] == selected_coc]

# Bar chart
st.subheader(f"Overall Homeless Over Time - {selected_coc}")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="Year", y="Overall Homeless", data=filtered_data, ax=ax)
plt.xlabel("Year")
plt.ylabel("Overall Homeless")
st.pyplot(fig)

# Display the raw data
st.subheader("Raw Data")
st.write(filtered_data)

import streamlit as st  # Import necessary libraries
import matplotlib.pyplot as plt
from fractions import Fraction

#steps for the app!
st.title("Welcome to Yousef's Fraction Visualizer App! 🍕")
st.write("""
## **Steps to Use This App:**
1. **Pick a color** 🎨 – This will be used to highlight your selected fraction in the pie chart.
2. **Select a fraction** 🔢 – Use the slider to choose a fraction of a whole pizza.
3. **View the pie chart** 📊 – The chart will display the selected fraction and the remaining portion.
""")

color = st.color_picker("Pick A Color", "#00f900")  #variable for color
st.write("The current color is", color) 

fraction = st.select_slider( #variable for fraction selected
    "Select a fraction",
    options=[
        Fraction(1, 64),
        Fraction(1, 32),
        Fraction(1, 16),
        Fraction(1, 8),
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(1, 1),
    ],
)

st.write("Here is a pie chart of the fraction:", fraction)  #shows selected fraction

fraction_data = [fraction, 1 - fraction]  #stores fraction and remaining portion
labels = [f"Selected Fraction: {fraction}", f"Remaining: {1 - fraction}"]

fig, ax = plt.subplots()
ax.pie(fraction_data, labels=labels, autopct='%1.1f%%', startangle=90, colors=['grey', color])
ax.axis('equal') 

st.pyplot(fig) #show chart

import streamlit as st
import matplotlib.pyplot as plt
from fractions import Fraction

# Set Page Title and Icon
st.set_page_config(page_title="Yousef's Fraction Visualizer", page_icon="🍕")

# App Title and Instructions
st.title("🍕 Yousef's Fraction Visualizer App")
st.markdown("""
## **How to Use This App**
1. **Pick a color** 🎨 – This color will highlight your selected fraction.
2. **Choose a fraction** 🔢 – Use the slider to select a fraction of a pizza.
3. **View the chart** 📊 – The pie chart displays your selection.
""")

# Color Picker
color = st.color_picker("🎨 Pick a Highlight Color", "#00f900")
st.write(f"**Current color:** `{color}`")

# Fraction Selection
fraction = st.select_slider(
    "🔢 Select a Fraction",
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
st.write(f"📊 **Selected Fraction:** `{fraction}`")

# Pie Chart Data
fraction_data = [fraction, 1 - fraction]
labels = [f"🍕 Selected: {fraction}", f"🍕 Remaining: {1 - fraction}"]

# Plot the Pie Chart with Better Styling
fig, ax = plt.subplots(figsize=(5, 5))  # Adjust figure size
wedges, texts, autotexts = ax.pie(
    fraction_data, 
    labels=labels, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=[color, "whitesmoke"],  # Highlight color & soft background
    wedgeprops={"edgecolor": "black", "linewidth": 1},  # Add border
    textprops={"fontsize": 12}  # Improve readability
)
ax.axis('equal')  # Keep the pie chart circular

st.pyplot(fig)  # Display the chart

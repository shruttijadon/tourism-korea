import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tourism Analysis", layout="centered")

st.title("South Korea Tourism Recovery (2020-2024)")

# Data
data = {
    'Year': [2020, 2021, 2022, 2023, 2024],
    'Inbound_Tourists': [2519, 967, 3198, 11032, 16370]
}
df = pd.DataFrame(data)

# Graph
fig, ax = plt.subplots()
ax.plot(df['Year'], df['Inbound_Tourists'], marker='o', color='blue', label='Tourists')
ax.set_title("Inbound Tourism Recovery Trend")
ax.set_xlabel("Year")
ax.set_ylabel("Number (in thousands)")
st.pyplot(fig)

st.write("### Key Analysis")
st.write("The graph shows a V-shaped recovery, with a significant surge in tourism by 2024.")

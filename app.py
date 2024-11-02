import streamlit as st 
import pandas as pd
import numpy as np
from prediction import predict

# Set background image
def add_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url({image_url});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with the URL or local path to an image
add_background_image("background image2.webp")  # Replace with your image path

# Customize title and subtitle
st.markdown(
    "<h1 style='text-align: center; color: #FF6347;'>🚑 Medical Provider Fraud Detection 🚑</h1>", 
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='text-align: center; color: #4682B4;'>Empowering healthcare with AI-driven fraud detection</h3>", 
    unsafe_allow_html=True
)

# Tutorial section for guiding the user
with st.expander("📘 How to Use This App", expanded=True):
    st.write("""
    This application helps classify medical providers as potentially fraudulent based on their claim patterns. 
    Follow these steps to make a prediction:
    """)
    st.markdown("1. **In-patient and Out-patient Details**: Enter relevant details of the provider's in-patient and out-patient claims in the input fields provided.")
    st.markdown("2. **Adjust Parameters**: Use the number inputs to specify characteristics such as the average stay, total claims, and diagnosis codes.")
    st.markdown("3. **Predict**: Once all details are entered, click on **🔍 Predict Fraudulent Provider** to get a prediction.")
    st.write("")

    st.info("💡 Tip: Hover over the info icon next to each input field to get more details about it.")

# Design the input sections with color accents and icons
st.write("")
st.markdown("<h2 style='color: #2E8B57;'>Provider Features</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔶 In-patient Characteristics")
    IP_days_in_hospital = st.number_input(
        'Average stay of in-patient claims', 
        min_value=0, max_value=40, value=5, help="The average length of stay for inpatient claims."
    )
    IP_TotalClaims = st.number_input(
        'Total no of in-patient claims filed by the provider', 
        min_value=0, max_value=500, value=10, help="Total number of inpatient claims."
    )

with col2:
    st.subheader("🔷 Out-patient Characteristics")
    OP_TotalClaims = st.number_input(
        'Total no of out-patient claims filed by the provider', 
        min_value=0, max_value=40, value=5, help="Total number of outpatient claims."
    )
    OP_RenalDiseaseIndicator = st.number_input(
        'Fraction of patients with renal disease in Outpatient claims', 
        min_value=0.00, max_value=1.00, value=0.05, format="%.2f", step=0.01,
        help="Percentage of patients with renal disease in outpatient claims."
    )
    OP_NoClmDiagnosisCodes  = st.number_input(
        'Total no of outpatient diagnosis codes in claims filed by the provider', 
        min_value=0, max_value=20, value=3, help="Total diagnosis codes in outpatient claims."
    )

# Predict button with an action icon
st.write("")
if st.button("🔍 Predict Fraudulent Provider"):
    # Predict and display result
    result = predict(np.array([OP_TotalClaims, IP_days_in_hospital, OP_RenalDiseaseIndicator, IP_TotalClaims, OP_NoClmDiagnosisCodes]).reshape(1, -1))

    if result <= 0.5:
        st.markdown(
            f'<h2 style="color:#008000;font-size:24px;">✅ Provider is NOT fraudulent with a probability of {round(1.0 - result, 2)}</h2>', 
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<h2 style="color:#FF0000;font-size:24px;">🚨 Provider is FRAUDULENT with a probability of {round(result, 2)}</h2>', 
            unsafe_allow_html=True
        )

# Footer for a professional touch
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 14px; color: #888;'>Developed with ❤️ by P.V. Tharunn Raj</p>", 
    unsafe_allow_html=True
)

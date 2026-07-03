import streamlit as st

from config import (
    APP_TITLE,
    ALLOWED_AUDIO_TYPES
)

from utils.file_utils import save_uploaded_file

# ======================================
# Application Title
# ======================================

st.title(APP_TITLE)

# ======================================
# Patient Details
# ======================================

name = st.text_input("Enter Patient Name")

age = st.number_input(
    "Enter Age",
    min_value=0,
    max_value=120,
    step=1
)

gender = st.selectbox(
    "Select Gender",
    ["Male", "Female", "Other"]
)

# ======================================
# Upload Audio
# ======================================

uploaded_file = st.file_uploader(
    "Upload Doctor Recording",
    type=ALLOWED_AUDIO_TYPES
)

# ======================================
# Generate Summary Button
# ======================================

if st.button("Generate AI Summary"):

    if uploaded_file is not None:

        # Save uploaded audio using utility function
        file_path = save_uploaded_file(uploaded_file)

        st.success("Audio uploaded successfully!")

        st.write("Saved to:", file_path)

        # Display Patient Details
        st.subheader("Patient Details")

        st.write("**Name:**", name)
        st.write("**Age:**", age)
        st.write("**Gender:**", gender)

    else:

        st.error("Please upload an audio file.")
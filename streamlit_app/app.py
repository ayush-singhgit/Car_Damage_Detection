
import streamlit as st
from model_helper import predict

st.set_page_config(
    page_title="Vehicle Damage Detection",
    page_icon="🚗",
    layout="centered"
)

st.title("Vehicle Damage Detection")
st.write("Upload a vehicle image to detect its damage category.")

uploaded_file = st.file_uploader(
    "Upload vehicle image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(
        uploaded_file,
        caption="Uploaded Vehicle Image",
        use_container_width=True
    )

    if st.button("Predict Damage", type="primary"):
        with st.spinner("Analyzing vehicle image..."):
            try:
                prediction = predict(uploaded_file)
                st.success(f"Predicted Class: {prediction}")
            except Exception as e:
                st.error(f"Prediction failed: {e}")

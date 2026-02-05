import streamlit as st

st.title("AI-Based Fertilizer Overuse Detector")

st.write("Enter fertilizer usage details")

# Input fields
crop = st.selectbox("Select Crop", ["Wheat", "Rice", "Maize"])
nitrogen = st.number_input("Nitrogen used (kg)", 0)
phosphorus = st.number_input("Phosphorus used (kg)", 0)
potassium = st.number_input("Potassium used (kg)", 0)

# Safe limits (knowledge base)
safe_limits = {
    "Wheat": {"N": 120, "P": 60, "K": 40},
    "Rice": {"N": 150, "P": 75, "K": 60},
    "Maize": {"N": 100, "P": 50, "K": 40}
}

if st.button("Check Overuse"):

    safe = safe_limits[crop]

    st.subheader("Results")

    def check(name, used, safe):
        if used > safe:
            over = ((used - safe) / safe) * 100
            st.error(f"{name} Overused by {over:.2f}%")
        else:
            st.success(f"{name} is within safe limit")

    check("Nitrogen", nitrogen, safe["N"])
    check("Phosphorus", phosphorus, safe["P"])
    check("Potassium", potassium, safe["K"])

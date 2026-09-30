import streamlit as st
import pandas as pd
import joblib

# Load trained Random Forest model
model = joblib.load("flood_gradient_boosting_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Flood Prediction System",
    page_icon="🌊",
    layout="centered"
)

# Title
st.title("🌊 Flood Prediction System")

st.write(
    "Enter the environmental, infrastructure, and geographical "
    "factors to predict flood probability."
)

# -----------------------------
# Input fields
# -----------------------------

MonsoonIntensity = st.slider("Monsoon Intensity", 0, 20, 5)
TopographyDrainage = st.slider("Topography Drainage", 0, 20, 5)
RiverManagement = st.slider("River Management", 0, 20, 5)
Deforestation = st.slider("Deforestation", 0, 20, 5)
Urbanization = st.slider("Urbanization", 0, 20, 5)
ClimateChange = st.slider("Climate Change", 0, 20, 5)
DamsQuality = st.slider("Dams Quality", 0, 20, 5)
Siltation = st.slider("Siltation", 0, 20, 5)
AgriculturalPractices = st.slider("Agricultural Practices", 0, 20, 5)
Encroachments = st.slider("Encroachments", 0, 20, 5)
IneffectiveDisasterPreparedness = st.slider(
    "Ineffective Disaster Preparedness", 0, 20, 5
)
DrainageSystems = st.slider("Drainage Systems", 0, 20, 5)
CoastalVulnerability = st.slider("Coastal Vulnerability", 0, 20, 5)
Landslides = st.slider("Landslides", 0, 20, 5)
Watersheds = st.slider("Watersheds", 0, 20, 5)
DeterioratingInfrastructure = st.slider(
    "Deteriorating Infrastructure", 0, 20, 5
)
PopulationScore = st.slider("Population Score", 0, 20, 5)
WetlandLoss = st.slider("Wetland Loss", 0, 20, 5)
InadequatePlanning = st.slider("Inadequate Planning", 0, 20, 5)
PoliticalFactors = st.slider("Political Factors", 0, 20, 5)


# -----------------------------
# Prediction
# -----------------------------

if st.button("🔍 Predict Flood Risk"):

    input_data = pd.DataFrame([[
        MonsoonIntensity,
        TopographyDrainage,
        RiverManagement,
        Deforestation,
        Urbanization,
        ClimateChange,
        DamsQuality,
        Siltation,
        AgriculturalPractices,
        Encroachments,
        IneffectiveDisasterPreparedness,
        DrainageSystems,
        CoastalVulnerability,
        Landslides,
        Watersheds,
        DeterioratingInfrastructure,
        PopulationScore,
        WetlandLoss,
        InadequatePlanning,
        PoliticalFactors
    ]], columns=[
        "MonsoonIntensity",
        "TopographyDrainage",
        "RiverManagement",
        "Deforestation",
        "Urbanization",
        "ClimateChange",
        "DamsQuality",
        "Siltation",
        "AgriculturalPractices",
        "Encroachments",
        "IneffectiveDisasterPreparedness",
        "DrainageSystems",
        "CoastalVulnerability",
        "Landslides",
        "Watersheds",
        "DeterioratingInfrastructure",
        "PopulationScore",
        "WetlandLoss",
        "InadequatePlanning",
        "PoliticalFactors"
    ])

    # Predict
    prediction = model.predict(input_data)[0]

    # Keep probability within 0-1
    prediction = max(0, min(1, prediction))

    probability = prediction * 100

    # Display result
    st.subheader("📊 Prediction Result")

    st.metric(
        "Flood Probability",
        f"{probability:.2f}%"
    )

    if prediction >= 0.5:
        st.error("⚠️ HIGH FLOOD RISK")
    else:
        st.success("✅ LOW FLOOD RISK")
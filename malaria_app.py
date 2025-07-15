import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.pipeline import Pipeline
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="AI Malaria Scan",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #A23B72;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .info-box {
        background-color: #F18F01;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
        font-weight: 500;
    }
    
    .warning-box {
        background-color: #C73E1D;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
        font-weight: 500;
    }
    
    .success-box {
        background-color: #2E8B57;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
        font-weight: 500;
    }
    
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #2E86AB;
    }
    
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    
    .stButton > button {
        background-color: #2E86AB;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #A23B72;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# Load the model
@st.cache_resource
def load_model():
    try:
        model = joblib.load('malaria_complete_model.joblib')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Navigation
def main():
   
    st.markdown('<h1 class="main-header">🩺 AI Malaria Scan Powered By MozBioMed AI!</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header"> Supporting Malaria Detection In Mozambique with Artificial Intelligence <img src="https://flagcdn.com/w40/mz.png" width="40" style="vertical-align: middle;"></h2>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.markdown("### 🧭 Navigation")
    page = st.sidebar.selectbox(
        "Choose a section:",
        ["🏠 Home", "🔬 AI Malaria Scan", "📊 Health Dashboard", "💡 Recommendations", "ℹ️ About Malaria"]
    )
    
    if page == "🏠 Home":
        show_home()
    elif page == "🔬 AI Malaria Scan":
        show_ai_scan()
    elif page == "📊 Health Dashboard":
        show_dashboard()
    elif page == "💡 Recommendations":
        show_recommendations()
    elif page == "ℹ️ About Malaria":
        show_about_malaria()

def show_home():
    logo = Image.open("Logo_MozBioMed.AI.jpg")
    st.image(logo)
    st.markdown("""
                <h4>Mozambique is one of the countries most heavily burdened by Malaria, a life-
                threatening disease caused by Plasmodium parasites transmitted through infected
                female Anopheles mosquitoes.</h4>
                """, unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">Welcome to AI Malaria Scan</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🔬 Why AI matters</h3>
            <p>Early and accurate malaria diagnosis saves lives. This app uses AI to help identify 
                    malaria infected cells.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>📊 Real-time Analysis</h3>
            <p>Get instant results and comprehensive health insights based on your laboratory values.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>💡 Smart Recommendations</h3>
            <p>Receive personalized health recommendations and next steps based on your results.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ### Quick Start Guide
    
    1. **Navigate to AI Malaria Scan** - Input your laboratory test results
    2. **Get Instant Analysis** - Our AI will analyze your data in real-time
    3. **Review Dashboard** - Check your health indicators and trends
    4. **Follow Recommendations** - Get personalized advice for your health
    
    ### ⚠️ Important Disclaimer
    This tool is designed to assist healthcare professionals and should not replace professional medical advice, diagnosis, or treatment.
    """)

def show_about_malaria():
    st.markdown('<h2 class="sub-header">About Malaria</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3>🦟 What is Malaria?</h3>
        <p>Malaria is a life-threatening disease caused by parasites that are transmitted to people through the bites of infected female Anopheles mosquitoes. It is preventable and curable.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 Key Symptoms
        - High fever and chills
        - Headache and muscle aches
        - Fatigue and weakness
        - Nausea and vomiting
        - Sweating
        - Abdominal pain
        """)
        
        st.markdown("""
        ### 🔬 Laboratory Indicators
        - Decreased red blood cell count
        - Low hemoglobin levels
        - Reduced hematocrit
        - Altered white blood cell count
        - Changes in platelet count
        """)
    
    with col2:
        st.markdown("""
        ### 🛡️ Prevention
        - Use insecticide-treated bed nets
        - Apply insect repellent
        - Wear protective clothing
        - Take antimalarial medication when traveling
        - Eliminate mosquito breeding sites
        """)
        
        st.markdown("""
        ### 🏥 Treatment
        - Early diagnosis is crucial
        - Antimalarial medications
        - Supportive care for symptoms
        - Hospitalization for severe cases
        - Follow-up monitoring
        """)

def show_ai_scan():
    st.markdown('<h2 class="sub-header">🔬 AI Malaria Scan</h2>', unsafe_allow_html=True)
    
    model = load_model()
    if model is None:
        st.error("Model could not be loaded. Please check the model file.")
        return
    
    st.markdown("### Enter Your Laboratory Test Results")
    
    # Create input form
    with st.form("malaria_scan_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**🌡️ General Parameters**")
            temperature = st.number_input("Temperature (°C)", min_value=20.0, max_value=50.0, value=37.0, step=0.1)
            
            st.markdown("**🔴 Red Blood Cell Parameters**")
            rbc_count = st.number_input("RBC Count (×10¹²/L)", min_value=1.0, max_value=10.0, value=4.5, step=0.1)
            hb_level = st.number_input("Hemoglobin (g/dL)", min_value=5.0, max_value=20.0, value=12.0, step=0.1)
            hematocrit = st.number_input("Hematocrit (%)", min_value=10.0, max_value=90.0, value=40.0, step=0.1)
            mean_cell_volume = st.number_input("Mean Cell Volume (fL)", min_value=10.0, max_value=200.0, value=85.0, step=0.1)
            mean_corp_hb = st.number_input("Mean Corpuscular Hb (pg)", min_value=10.0, max_value=60.0, value=30.0, step=0.1)
            mean_cell_hb_conc = st.number_input("Mean Cell Hb Concentration (g/dL)", min_value=20.0, max_value=60.0, value=33.0, step=0.1)
            rbc_dist_width = st.number_input("RBC Distribution Width (%)", min_value=4.0, max_value=20.0, value=13.0, step=0.1)
        
        with col2:
            st.markdown("**⚪ White Blood Cell Parameters**")
            wbc_count = st.number_input("WBC Count (×10⁹/L)", min_value=2.0, max_value=40.0, value=7.0, step=0.1)
            neutrophils_percent = st.number_input("Neutrophils (%)", min_value=10.0, max_value=90.0, value=60.0, step=0.1)
            lymphocytes_percent = st.number_input("Lymphocytes (%)", min_value=10.0, max_value=60.0, value=30.0, step=0.1)
            mixed_cells_percent = st.number_input("Mixed Cells (%)", min_value=1.0, max_value=30.0, value=8.0, step=0.1)
            neutrophils_count = st.number_input("Neutrophils Count (×10⁹/L)", min_value=1.0, max_value=15.0, value=4.0, step=0.1)
            lymphocytes_count = st.number_input("Lymphocytes Count (×10⁹/L)", min_value=0.5, max_value=12.0, value=2.0, step=0.1)
            mixed_cells_count = st.number_input("Mixed Cells Count (×10⁹/L)", min_value=0.1, max_value=2.0, value=0.5, step=0.1)
        
        with col3:
            st.markdown("**🟡 Platelet Parameters**")
            platelet_count = st.number_input("Platelet Count (×10⁹/L)", min_value=50.0, max_value=550.0, value=250.0, step=1.0)
            platelet_distr_width = st.number_input("Platelet Distribution Width", min_value=3.0, max_value=30.0, value=12.0, step=0.1)
            mean_platelet_vl = st.number_input("Mean Platelet Volume (fL)", min_value=6.0, max_value=15.0, value=9.0, step=0.1)
            
            st.markdown("**📍 Additional Information**")
            location = st.selectbox("Location", ["Urban", "Rural", "Suburban"])
            bednet = st.selectbox("Bed Net Usage", ["Yes", "No"])
            fever_symptom = st.selectbox("Fever Symptoms", ["Yes", "No"])
        
        submitted = st.form_submit_button("🔍 Analyze for Malaria", use_container_width=True)
        
        if submitted:
            # Prepare input data
            input_data = pd.DataFrame({
                'location': [location],
                'bednet': [bednet],
                'fever_symptom': [fever_symptom],
                'temperature': [temperature],
                'wbc_count': [wbc_count],
                'rbc_count': [rbc_count],
                'hb_level': [hb_level],
                'hematocrit': [hematocrit],
                'mean_cell_volume': [mean_cell_volume],
                'mean_corp_hb': [mean_corp_hb],
                'mean_cell_hb_conc': [mean_cell_hb_conc],
                'platelet_count': [platelet_count],
                'platelet_distr_width': [platelet_distr_width],
                'mean_platelet_vl': [mean_platelet_vl],
                'neutrophils_percent': [neutrophils_percent],
                'lymphocytes_percent': [lymphocytes_percent],
                'mixed_cells_percent': [mixed_cells_percent],
                'neutrophils_count': [neutrophils_count],
                'lymphocytes_count': [lymphocytes_count],
                'mixed_cells_count': [mixed_cells_count],
                'RBC_dist_width_Percent': [rbc_dist_width]
            })
            
            # Make prediction
            try:
                # Ensure compatibility with different sklearn versions
                import warnings
                warnings.filterwarnings('ignore')
                
                prediction = model.predict(input_data)[0]
                prediction_proba = model.predict_proba(input_data)[0]
                
                # Store results in session state
                st.session_state.last_prediction = prediction
                st.session_state.last_prediction_proba = prediction_proba
                st.session_state.last_input_data = input_data
                
                # Display results
                st.markdown("---")
                st.markdown("### 🎯 Analysis Results")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if prediction == 1:
                        st.markdown("""
                        <div class="success-box">
                            <h3>✅ NO MALARIA DETECTED</h3>
                            <p>The AI analysis indicates a low probability of malaria infection, but proceed to the Health Dashboard to
                                    access the risk Factors.</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div class="warning-box">
                            <h3>⚠️ MALARIA DETECTED</h3>
                            <p>The AI analysis indicates a high probability of malaria infection.</p>
                        </div>
                        """, unsafe_allow_html=True)

                        
                
                with col2:
                    # Confidence gauge
                    confidence = max(prediction_proba) * 100
                    labels = ['No Malaria', 'Malaria']
                    values = [prediction_proba[1] * 100, prediction_proba[0] * 100]
                    colors = ['lightgreen', 'salmon']  # Feel free to adjust colors

                    fig = go.Figure(data=[go.Pie(
                        labels=labels,
                        values=values,
                        hole=0.6,  # Makes it a donut chart
                        marker=dict(colors=colors),
                        textinfo='label+percent',
                        hoverinfo='label+percent+value',
                    )])

                    fig.update_layout(
                        title_text="Malaria Prediction Likelihood",
                        annotations=[dict(text=f'{confidence:.1f}%', x=0.5, y=0.5, font_size=20, showarrow=False)],
                        height=300
                    )

                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown("""
                    ### ⚠️ Important Disclaimer !!
                    This tool is designed to assist healthcare professionals and should not replace professional medical advice, diagnosis, or treatment.
                    """)    
                
                
            except Exception as e:
                st.error(f"Error during prediction: {e}")

def show_dashboard():
    st.markdown('<h2 class="sub-header">📊 Health Dashboard</h2>', unsafe_allow_html=True)
    
    if 'last_input_data' not in st.session_state:
        st.info("Please run an AI Malaria Scan first to see your health dashboard.")
        return
    
    data = st.session_state.last_input_data.iloc[0]
    
    # Health indicators with normal ranges
    st.markdown("### Health Indicators Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔴 Red Blood Cell Parameters")
        
        # RBC Count
        rbc_normal = (4.0, 5.5)  # Normal range for RBC
        rbc_value = data['rbc_count']
        rbc_status = "Normal" if rbc_normal[0] <= rbc_value <= rbc_normal[1] else "Abnormal"
        rbc_color = "normal" if rbc_status == "Normal" else "inverse"
        
        st.metric("RBC Count", f"{rbc_value:.1f} ×10¹²/L", 
                 delta=f"{rbc_status}", delta_color=rbc_color)
        
        if rbc_value < rbc_normal[0]:
            st.markdown("""
            <div class="warning-box">
                ⚠️ Low RBC count detected. This may indicate anemia, which is
                         common in malaria infections.
            </div>
            """, unsafe_allow_html=True)
        elif rbc_value > rbc_normal[1]:
            st.markdown("""
            <div class="info-box">
                ℹ️ Elevated RBC count detected. This may indicate dehydration or other conditions.
            </div>
            """, unsafe_allow_html=True)
        
        # Hemoglobin
        hb_normal = (12.0, 16.0)  # Normal range for Hemoglobin
        hb_value = data['hb_level']
        hb_status = "Normal" if hb_normal[0] <= hb_value <= hb_normal[1] else "Abnormal"
        hb_color = "normal" if hb_status == "Normal" else "inverse"
        
        st.metric("Hemoglobin", f"{hb_value:.1f} g/dL", 
                 delta=f"{hb_status}", delta_color=hb_color)
        
        if hb_value < hb_normal[0]:
            st.markdown("""
            <div class="warning-box">
                ⚠️ Low hemoglobin detected. This is a key indicator of anemia and potential malaria infection.
            </div>
            """, unsafe_allow_html=True)
        
        # Platelet Count
        platelet_normal = (150, 400)  # Normal range for platelets
        platelet_value = data['platelet_count']
        platelet_status = "Normal" if platelet_normal[0] <= platelet_value <= platelet_normal[1] else "Abnormal"
        platelet_color = "normal" if platelet_status == "Normal" else "inverse"
        
        st.metric("Platelet Count", f"{platelet_value:.0f} ×10⁹/L", 
                 delta=f"{platelet_status}", delta_color=platelet_color)
        
        if platelet_value < platelet_normal[0]:
            st.markdown("""
            <div class="warning-box">
                ⚠️ Low platelet count (thrombocytopenia) detected. This is commonly associated with malaria infections.
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### ⚪ White Blood Cell Parameters")
        
        # WBC Count
        wbc_normal = (4.0, 11.0)  # Normal range for WBC
        wbc_value = data['wbc_count']
        wbc_status = "Normal" if wbc_normal[0] <= wbc_value <= wbc_normal[1] else "Abnormal"
        wbc_color = "normal" if wbc_status == "Normal" else "inverse"
        
        st.metric("WBC Count", f"{wbc_value:.1f} ×10⁹/L", 
                 delta=f"{wbc_status}", delta_color=wbc_color)
        
        if wbc_value < wbc_normal[0]:
            st.markdown("""
            <div class="warning-box">
                ⚠️ Low WBC count detected. This may indicate immune system suppression.
            </div>
            """, unsafe_allow_html=True)
        elif wbc_value > wbc_normal[1]:
            st.markdown("""
            <div class="info-box">
                ℹ️ Elevated WBC count detected. This may indicate an active infection or immune response.
            </div>
            """, unsafe_allow_html=True)
        
        # Temperature
        temp_normal = (36.1, 37.2)  # Normal body temperature range
        temp_value = data['temperature']
        temp_status = "Normal" if temp_normal[0] <= temp_value <= temp_normal[1] else "Fever"
        temp_color = "normal" if temp_status == "Normal" else "inverse"
        
        st.metric("Temperature", f"{temp_value:.1f} °C", 
                 delta=f"{temp_status}", delta_color=temp_color)
        
        if temp_value > temp_normal[1]:
            st.markdown("""
            <div class="warning-box">
                ⚠️ Fever detected. This is a primary symptom of malaria and requires immediate attention.
            </div>
            """, unsafe_allow_html=True)
    
    # Risk factors analysis
    st.markdown("---")
    st.markdown("### Risk Factors Analysis")
    
    risk_score = 0
    risk_factors = []
    
    if data['fever_symptom'] == 'Yes':
        risk_score += 3
        risk_factors.append("Fever symptoms present")
    
    if data['bednet'] == 'No':
        risk_score += 2
        risk_factors.append("No bed net protection")
    
    if data['location'] == 'Rural':
        risk_score += 1
        risk_factors.append("Rural location (higher mosquito exposure)")
    
    if rbc_value < rbc_normal[0]:
        risk_score += 2
        risk_factors.append("Low RBC count")
    
    if hb_value < hb_normal[0]:
        risk_score += 2
        risk_factors.append("Low hemoglobin")
    
    if platelet_value < platelet_normal[0]:
        risk_score += 2
        risk_factors.append("Low platelet count")
    
    if temp_value > temp_normal[1]:
        risk_score += 3
        risk_factors.append("Elevated temperature")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if risk_score >= 8:
            risk_level = "High"
            risk_color = "#C73E1D"
        elif risk_score >= 4:
            risk_level = "Moderate"
            risk_color = "#F18F01"
        else:
            risk_level = "Low"
            risk_color = "#2E8B57"
        
        st.markdown(f"""
        <div style="background-color: {risk_color}; padding: 1rem; border-radius: 10px; color: white;">
            <h3>Risk Level: {risk_level}</h3>
            <p>Risk Score: {risk_score}/15</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if risk_factors:
            st.markdown("**Identified Risk Factors:**")
            for factor in risk_factors:
                st.markdown(f"• {factor}")
        else:
            st.markdown("**No significant risk factors identified.**")

def show_recommendations():
    st.markdown('<h2 class="sub-header">💡 Health Recommendations</h2>', unsafe_allow_html=True)
    
    if 'last_prediction' not in st.session_state:
        st.info("Please run an AI Malaria Scan first to get personalized recommendations.")
        return
    
    prediction = st.session_state.last_prediction
    data = st.session_state.last_input_data.iloc[0]
    
    if prediction == 0:
        st.markdown("""
        <div class="warning-box">
            <h3>🚨 URGENT: Malaria Detected - Immediate Action Required</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        ### 🏥 Immediate Medical Attention
        
        **SEEK EMERGENCY MEDICAL CARE IMMEDIATELY**
        
        - Visit the nearest hospital or healthcare facility
        - Inform healthcare providers about potential malaria
        - Bring these test results with you
        - Do not delay treatment - malaria can be life-threatening
        
        ### 💊 Expected Treatment Protocol
        
        - **Rapid Diagnostic Test (RDT)** or microscopy confirmation
        - **Antimalarial medication** (artemisinin-based combination therapy)
        - **Supportive care** for symptoms (fever, dehydration)
        - **Monitoring** for complications
        
        ### 🏠 Home Care While Seeking Treatment
        
        - **Stay hydrated** - drink plenty of fluids
        - **Rest** - avoid physical exertion
        - **Monitor temperature** - use fever reducers as directed
        - **Isolate** - prevent mosquito bites to avoid transmission
        """)
        
        # Additional recommendations based on specific parameters
        if data['temperature'] > 38.5:
            st.markdown("""
            <div class="warning-box">
                ⚠️ High fever detected. Use cooling measures and fever reducers while seeking medical care.
            </div>
            """, unsafe_allow_html=True)
        
        if data['hb_level'] < 10:
            st.markdown("""
            <div class="warning-box">
                ⚠️ Severe anemia detected. This requires immediate medical intervention.
            </div>
            """, unsafe_allow_html=True)
        
        if data['platelet_count'] < 100:
            st.markdown("""
            <div class="warning-box">
                ⚠️ Severe thrombocytopenia detected. Risk of bleeding complications - seek immediate care.
            </div>
            """, unsafe_allow_html=True)
    
    else:
        st.markdown("""
        <div class="success-box">
            <h3>✅ No Malaria Detected - Preventive Care Recommended</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        ### 🛡️ Prevention Strategies
        
        **Continue protective measures to prevent malaria:**
        
        - **Use insecticide-treated bed nets** every night
        - **Apply insect repellent** containing DEET, picaridin, or oil of lemon eucalyptus
        - **Wear protective clothing** (long sleeves, long pants) especially during dawn and dusk
        - **Eliminate standing water** around your home to reduce mosquito breeding
        
        ### 🏥 Follow-up Care
        
        - **Monitor symptoms** - watch for fever, chills, headache
        - **Regular check-ups** if you live in or travel to malaria-endemic areas
        - **Repeat testing** if symptoms develop
        """)
        
        # Specific recommendations based on parameters
        recommendations = []
        
        if data['hb_level'] < 12:
            recommendations.append({
                'title': '🍎 Address Mild Anemia',
                'content': 'Your hemoglobin is slightly low. Consider iron-rich foods (spinach, red meat, beans) and consult a healthcare provider about iron supplements.'
            })
        
        if data['platelet_count'] < 150:
            recommendations.append({
                'title': '🩸 Monitor Platelet Count',
                'content': 'Your platelet count is below normal. Follow up with your healthcare provider to determine the cause and appropriate treatment.'
            })
        
        if data['wbc_count'] < 4:
            recommendations.append({
                'title': '🛡️ Boost Immune System',
                'content': 'Your white blood cell count is low. Focus on a healthy diet, adequate sleep, regular exercise, and stress management.'
            })
        
        if data['temperature'] > 37.5:
            recommendations.append({
                'title': '🌡️ Monitor Temperature',
                'content': 'You have a mild fever. Rest, stay hydrated, and monitor for other symptoms. Seek medical care if fever persists or worsens.'
            })
        
        if data['bednet'] == 'No':
            recommendations.append({
                'title': '🛏️ Use Bed Nets',
                'content': 'You indicated no bed net usage. This is crucial for malaria prevention. Obtain and use insecticide-treated bed nets immediately.'
            })
        
        if recommendations:
            st.markdown("### 🎯 Personalized Health Recommendations")
            for rec in recommendations:
                st.markdown(f"""
                <div class="info-box">
                    <h4>{rec['title']}</h4>
                    <p>{rec['content']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # General health tips
    st.markdown("---")
    st.markdown("""
    ### 🌟 General Health Tips
    
    **Maintain Overall Health:**
    
    - **Balanced Diet** - Include fruits, vegetables, whole grains, and lean proteins
    - **Regular Exercise** - Maintain physical fitness to support immune function
    - **Adequate Sleep** - 7-9 hours per night for optimal health
    - **Stress Management** - Practice relaxation techniques and maintain mental health
    - **Regular Health Screenings** - Stay up to date with routine medical check-ups
    
    **Travel Considerations:**
    
    - **Consult Travel Medicine Specialist** before visiting malaria-endemic areas
    - **Prophylactic Medication** may be recommended for high-risk travel
    - **Travel Insurance** that covers medical emergencies
    - **Emergency Contacts** - know local healthcare facilities at your destination
    """)
    
    # Emergency contacts section
    st.markdown("---")
    st.markdown("""
    
    **When to Seek Immediate Medical Care:**
    - High fever (>39°C/102°F)
    - Severe headache
    - Persistent vomiting
    - Difficulty breathing
    - Confusion or altered mental state
    - Severe weakness or fatigue
    
    """)

if __name__ == "__main__":
    main()


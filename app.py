import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Fraud Monitoring Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Header
st.title("🛡️ Financial Transaction Fraud Monitoring")
st.markdown("Real-time risk scoring, alert volume tracking, and decision threshold management.")

# Sidebar - Standout Element: Business Tradeoff Controls
st.sidebar.header("⚙️ Risk Strategy Controls")
st.sidebar.markdown(
    "Adjusting the threshold balances **Investigator Capacity** vs. **Fraud Caught**."
)

threshold = st.sidebar.slider(
    "Model Operating Threshold",
    min_value=0.10,
    max_value=0.90,
    value=0.33,
    step=0.01,
    help="Lower threshold = catch more fraud, but increases false alarms for investigators."
)

st.sidebar.divider()
st.sidebar.markdown(
    """
    **Business Cost Matrix:**
    - False Positive Cost: **$20** *(Investigator Review)*
    - False Negative Cost: **$250** *(Missed Fraud)*
    """
)

# Generate Mock Monitoring Data for Demonstration
np.random.seed(42)
dates = pd.date_range(end=pd.Timestamp.now(), periods=30, freq='D')

# Simulate metrics shifting based on slider
alerts_count = int(1200 * (1 - threshold))
precision_val = min(0.95, round(0.55 + (threshold * 0.4), 2))
recall_val = max(0.50, round(1.0 - (threshold * 0.35), 2))
fraud_caught = int(250 * recall_val)
estimated_cost = (alerts_count * 20) + ((250 - fraud_caught) * 250)

# Top KPI Metric Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Alerts Volume (30d)", f"{alerts_count:,}", delta=f"{'-' if threshold > 0.33 else '+'}{abs(alerts_count - 804)}")
col2.metric("Model Precision", f"{precision_val * 100:.1f}%")
col3.metric("Fraud Caught Rate", f"{recall_val * 100:.1f}%")
col4.metric("Est. Total Operating Loss", f"${estimated_cost:,.2f}")

st.divider()

# Layout: Chart + Top Flagged Accounts Table
col_chart, col_table = st.columns([6, 4])

with col_chart:
    st.subheader("📈 Alert Volume & Precision Over Time")
    
    # Generate daily trend dataframe
    trend_df = pd.DataFrame({
        "Date": dates,
        "Alert Volume": np.random.randint(int(alerts_count/35), int(alerts_count/25) + 1, size=30),
        "Precision (%)": np.clip(np.random.normal(precision_val * 100, 3, size=30), 40, 99)
    }).set_index("Date")
    
    st.line_chart(trend_df)

with col_table:
    st.subheader("🚨 Top Flagged Accounts")
    
    # Generate Top Accounts Table
    mock_accounts = pd.DataFrame({
        "Account ID": [f"ACC-{i}" for i in range(1001, 1007)],
        "Risk Score": [0.98, 0.94, 0.89, 0.85, 0.79, 0.72],
        "Flagged Bursts": [12, 9, 7, 5, 4, 3],
        "Total Vol ($)": ["$14,200", "$9,850", "$6,400", "$5,100", "$3,900", "$2,800"],
        "Status": ["Under Review", "Under Review", "Flagged", "Flagged", "Investigated", "Investigated"]
    })
    
    st.dataframe(mock_accounts, use_container_width=True, hide_index=True)

# Footer - Standout Narrative
st.divider()
st.info(
    f"💡 **Business Takeaway:** At an operating threshold of **{threshold:.2f}**, the security team will process **{alerts_count} alerts** over 30 days. "
    f"This operational strategy successfully captures **{recall_val*100:.0f}% of fraudulent transactions** while optimizing investigator workload capacity."
)
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="EstateIQ | Property Intelligence",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PREMIUM DARK THEME
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 92% 2%, rgba(200,169,107,.07), transparent 25%),
            radial-gradient(circle at 2% 75%, rgba(255,255,255,.025), transparent 24%),
            #090a0c;
        color: #eeeae2;
    }

    #MainMenu, footer { visibility: hidden; }
    header { background: transparent !important; }

    .block-container {
        max-width: 1380px;
        padding: 1.4rem 2rem 3rem;
    }

    section[data-testid="stSidebar"] {
        background: #08090b;
        border-right: 1px solid #202226;
    }

    section[data-testid="stSidebar"] > div {
        padding: 1.35rem 1.15rem;
    }

    .sidebar-brand {
        padding: .2rem 0 1.4rem;
        border-bottom: 1px solid #1e2024;
    }

    .brand-name {
        color: #f4f0e8;
        font-size: 1.55rem;
        font-weight: 850;
        letter-spacing: -.055em;
    }

    .brand-name span,
    .gold {
        color: #c8a96b;
    }

    .brand-subtitle {
        margin-top: .3rem;
        color: #686c73;
        font-size: .61rem;
        font-weight: 750;
        letter-spacing: .15em;
        text-transform: uppercase;
    }

    .sidebar-heading {
        margin: 1.35rem 0 .55rem;
        color: #c8a96b;
        font-size: .60rem;
        font-weight: 800;
        letter-spacing: .15em;
        text-transform: uppercase;
    }

    .sidebar-description {
        color: #858990;
        font-size: .75rem;
        line-height: 1.7;
    }

    .sidebar-metric {
        padding: .72rem 0;
        border-bottom: 1px solid #1c1e22;
    }

    .sidebar-metric-label {
        color: #5f636a;
        font-size: .57rem;
        font-weight: 750;
        letter-spacing: .10em;
        text-transform: uppercase;
    }

    .sidebar-metric-value {
        margin-top: .22rem;
        color: #eeeae2;
        font-size: 1.02rem;
        font-weight: 760;
    }

    .sidebar-footer {
        margin-top: 1.5rem;
        color: #4d5157;
        font-size: .61rem;
        line-height: 1.65;
    }

    /* Hero */

    .hero {
        position: relative;
        overflow: hidden;
        padding: 2.35rem 2.65rem;
        margin-bottom: 1.8rem;
        border: 1px solid #292b2f;
        border-radius: 18px;
        background: linear-gradient(135deg, #171819 0%, #111214 62%, #0d0e10 100%);
        box-shadow: 0 18px 50px rgba(0,0,0,.20);
    }

    .hero::after {
        content: "";
        position: absolute;
        width: 330px;
        height: 330px;
        right: -165px;
        top: -165px;
        border: 1px solid rgba(200,169,107,.10);
        border-radius: 50%;
        box-shadow:
            0 0 0 42px rgba(200,169,107,.024),
            0 0 0 84px rgba(200,169,107,.012);
    }

    .hero-eyebrow,
    .section-kicker {
        color: #c8a96b;
        font-size: .72rem;
        font-weight: 800;
        letter-spacing: .16em;
        text-transform: uppercase;
    }

    .hero-eyebrow { margin-bottom: .6rem; }

    .hero-title {
        color: #f3f0e9;
        font-size: 3rem;
        font-weight: 880;
        line-height: .95;
        letter-spacing: -.065em;
    }

    .hero-title span { color: #c8a96b; }

    .hero-heading {
        margin-top: .55rem;
        color: #ded9d0;
        font-size: 1.02rem;
        font-weight: 680;
    }

    .hero-subtitle {
        max-width: 730px;
        margin-top: .55rem;
        color: #81858c;
        font-size: .78rem;
        line-height: 1.75;
    }

    .section-kicker { margin-top: 1.45rem; }

    .section-title {
        margin: .22rem 0 .8rem;
        color: #eeeae2;
        font-size: 1.45rem;
        font-weight: 780;
        letter-spacing: -.025em;
    }

    .section-description {
        margin: -.35rem 0 .85rem;
        color: #676b72;
        font-size: .86rem;
        line-height: 1.6;
    }

    /* Inputs */

    label {
        color: #999da4 !important;
        font-size: .71rem !important;
        font-weight: 650 !important;
    }

    div[data-baseweb="select"] > div {
        min-height: 42px;
        background: #131417 !important;
        border: 1px solid #292c30 !important;
        border-radius: 8px !important;
    }

    input {
        min-height: 42px !important;
        background: #131417 !important;
        border: 1px solid #292c30 !important;
        border-radius: 8px !important;
        color: #eeeae2 !important;
    }

    div[data-baseweb="select"] > div:focus-within,
    input:focus {
        border-color: #c8a96b !important;
        box-shadow: 0 0 0 1px rgba(200,169,107,.13) !important;
    }

    .stButton > button {
        width: 100%;
        min-height: 44px;
        border: 1px solid #c8a96b;
        border-radius: 8px;
        background: #c8a96b;
        color: #111214;
        font-size: .76rem;
        font-weight: 820;
        transition: .2s ease;
    }

    .stButton > button:hover {
        border-color: #ddc28e;
        background: #ddc28e;
        transform: translateY(-1px);
        box-shadow: 0 9px 25px rgba(200,169,107,.12);
    }

    /* Cards */

    .metric-card {
        min-height: 118px;
        padding: 1.3rem 1.25rem;
        border: 1px solid #25272b;
        border-radius: 13px;
        background: linear-gradient(145deg, #121315, #101113);
    }

    .metric-label,
    .result-label {
        color: #62666d;
        font-size: 0.68rem;
        font-weight: 800;
        letter-spacing: .13em;
        text-transform: uppercase;
    }

    .metric-value {
        margin-top: .48rem;
        color: #eeeae2;
        font-size: 1.42rem;
        font-weight: 800;
        letter-spacing: -.035em;
    }

    .metric-small {
        color: #666a71;
        font-size: .75rem;
        font-weight: 550;
    }

    .metric-accent { color: #c8a96b; }

    .method-card {
        min-height: 205px;
        padding: 1.35rem 1.45rem;
        border: 1px solid #292b2f;
        border-radius: 14px;
        background: #111214;
    }

    .method-title {
        color: #eeeae2;
        font-size: .88rem;
        font-weight: 780;
        margin-bottom: .65rem;
    }

    .method-copy {
        color: #777b82;
        font-size: .86rem;
        line-height: 1.75;
    }

    .method-chip {
        display: inline-block;
        margin: .18rem .18rem .18rem 0;
        padding: .30rem .52rem;
        border: 1px solid #292c30;
        border-radius: 999px;
        color: #a7a9ad;
        background: #151619;
        font-size: .60rem;
    }

    .result-card {
        position: relative;
        overflow: hidden;
        padding: 1.35rem 1.6rem;
        margin-top: .65rem;
        border: 1px solid rgba(200,169,107,.30);
        border-radius: 14px;
        background: linear-gradient(135deg, #191715, #111214 72%);
    }

    .result-card::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 3px;
        background: #c8a96b;
    }

    .result-price {
        margin: .22rem 0 .10rem;
        color: #d8bb84;
        font-size: 2.25rem;
        font-weight: 880;
        letter-spacing: -.055em;
    }

    .result-unit {
        color: #6b6e74;
        font-size: .68rem;
        font-weight: 550;
    }

    .result-total {
        color: #eeeae2;
        font-size: .92rem;
        font-weight: 680;
    }

    .result-note {
        margin-top: .38rem;
        color: #5c6066;
        font-size: .59rem;
    }

    .benchmark {
        margin-top: .8rem;
        padding-top: .8rem;
        border-top: 1px solid #282a2e;
    }

    .benchmark-title {
        color: #777b82;
        font-size: .58rem;
        font-weight: 760;
        letter-spacing: .11em;
        text-transform: uppercase;
    }

    .benchmark-value {
        margin-top: .25rem;
        color: #e8e3da;
        font-size: .91rem;
        font-weight: 760;
    }

    .benchmark-delta {
        color: #c8a96b;
        font-size: .62rem;
        font-weight: 650;
    }

    /* Charts */

    .chart-wrapper {
        padding: .25rem;
        border: 1px solid #25272b;
        border-radius: 13px;
        background: #111214;
        margin-bottom: .8rem;
    }

    .chart-caption {
        color: #555960;
        font-size: .60rem;
        margin: -.35rem 0 .65rem;
    }

    /* EDA Q&A */

    .qa-card {
        min-height: 150px;
        padding: 1.15rem 1.2rem;
        border: 1px solid #25272b;
        border-radius: 13px;
        background: linear-gradient(145deg, #121315, #101113);
    }

    .qa-question {
        color: #ddd8cf;
        font-size: 1.05rem;
        font-weight: 760;
        line-height: 1.4;
    }

    .qa-answer {
        margin-top: .55rem;
        color: #858990;
        font-size: .88rem;
        line-height: 1.65;
    }

    .qa-answer strong { color: #c8a96b; }

    .insight-strip {
        padding: .85rem 1rem;
        margin: .25rem 0 .9rem;
        border-left: 2px solid #c8a96b;
        border-radius: 0 8px 8px 0;
        background: #121315;
        color: #777b82;
        font-size: .67rem;
        line-height: 1.65;
    }

    .footer {
        padding: 1.4rem 0 .2rem;
        margin-top: 1.6rem;
        border-top: 1px solid #202226;
        text-align: center;
        color: #4e5258;
        font-size: .60rem;
        line-height: 1.8;
    }

    .footer strong { color: #777b82; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PATHS / DATA / MODEL
# ============================================================

ROOT_DIR = Path(__file__).resolve().parent
MODEL_PATH = ROOT_DIR / "models" / "property_valuation_rf.pkl"
DATA_PATH = ROOT_DIR / "data" / "processed" / "estateiq_processed.csv"


@st.cache_data
def load_market_data():
    if not DATA_PATH.exists():
        return None

    df = pd.read_csv(DATA_PATH)

    numeric_cols = [
        "AREA", "PRICE_SQFT", "BEDROOM_NUM", "BATHROOM_NUM",
        "BALCONY_NUM", "FLOOR_NUM", "TOTAL_FLOOR"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    required = [c for c in ["AREA", "PRICE_SQFT", "CITY", "PROPERTY_TYPE"] if c in df.columns]
    if len(required) < 4:
        return None

    return df.dropna(subset=["AREA", "PRICE_SQFT", "CITY", "PROPERTY_TYPE"]).copy()


@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        return None
    return joblib.load(MODEL_PATH)


rf_model = load_model()
market_data = load_market_data()

if rf_model is None:
    st.error("Valuation model not found at models/property_valuation_rf.pkl")
    st.stop()

if market_data is None or market_data.empty:
    st.error("Market dataset not found or required columns are missing.")
    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.html(
        """
        <div class="sidebar-brand">
            <div class="brand-name">Estate<span>IQ</span></div>
            <div class="brand-subtitle">Real Estate Intelligence</div>
        </div>
        """
    )

    st.html(
        """
        <div class="sidebar-heading">Valuation Engine</div>
        <div class="sidebar-description">
            Machine-learning property valuation and market intelligence
            for Indian residential real estate.
        </div>

        <div class="sidebar-heading">Model Benchmark</div>

        <div class="sidebar-metric">
            <div class="sidebar-metric-label">R² Score</div>
            <div class="sidebar-metric-value">0.6132</div>
        </div>

        <div class="sidebar-metric">
            <div class="sidebar-metric-label">Mean Absolute Error</div>
            <div class="sidebar-metric-value">₹2,593.72</div>
        </div>

        <div class="sidebar-metric">
            <div class="sidebar-metric-label">RMSE</div>
            <div class="sidebar-metric-value">₹3,948.72</div>
        </div>
        """
    )

    st.html(
        f"""
        <div class="sidebar-heading">Dataset</div>
        <div class="sidebar-metric">
            <div class="sidebar-metric-label">Listings</div>
            <div class="sidebar-metric-value">{len(market_data):,}</div>
        </div>
        <div class="sidebar-metric">
            <div class="sidebar-metric-label">Markets</div>
            <div class="sidebar-metric-value">{market_data["CITY"].nunique():,}</div>
        </div>
        <div class="sidebar-metric">
            <div class="sidebar-metric-label">Property Types</div>
            <div class="sidebar-metric-value">{market_data["PROPERTY_TYPE"].nunique():,}</div>
        </div>
        """
    )

    st.html(
        """
        <div class="sidebar-footer">
            EstateIQ<br>
            Indian Real Estate Market Intelligence<br>
            Machine Learning Property Valuation
        </div>
        """
    )


# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div class="hero">
        <div class="hero-eyebrow">Property Intelligence Platform</div>
        <div class="hero-title">Estate<span>IQ</span></div>
        <div class="hero-heading">Intelligent Property Valuation</div>
        <div class="hero-subtitle">
            Estimate indicative property value using a trained Random Forest
            model, then benchmark the result against observed market pricing,
            property type and location-level intelligence.
        </div>
    </div>
    """
)


# ============================================================
# PROPERTY INPUTS
# ============================================================

st.html(
    """
    <div class="section-kicker">Property Details</div>
    <div class="section-title">Property Profile</div>
    """
)

# Use categories directly from the processed dataset.
city_options = sorted(market_data["CITY"].dropna().astype(str).unique().tolist())
type_options = sorted(market_data["PROPERTY_TYPE"].dropna().astype(str).unique().tolist())

left, right = st.columns(2, gap="large")

with left:
    city = st.selectbox(
        "City / Market",
        city_options,
        index=city_options.index("Hyderabad") if "Hyderabad" in city_options else 0,
        help="Select a market represented in the training dataset.",
    )

    property_type = st.selectbox(
        "Property Type",
        type_options,
        index=type_options.index("Residential Apartment")
        if "Residential Apartment" in type_options else 0,
    )

    area = st.number_input(
        "Area (sq.ft.)",
        min_value=100,
        max_value=100000,
        value=1800,
        step=50,
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        max_value=24,
        value=3,
        step=1,
    )

with right:
    bathrooms = st.number_input(
        "Bathrooms",
        min_value=0,
        max_value=24,
        value=3,
        step=1,
    )

    balconies = st.number_input(
        "Balconies",
        min_value=0,
        max_value=10,
        value=2,
        step=1,
    )

    floor = st.number_input(
        "Property Floor",
        min_value=0,
        max_value=150,
        value=8,
        step=1,
    )

    total_floors = st.number_input(
        "Total Floors",
        min_value=1,
        max_value=200,
        value=20,
        step=1,
    )

if floor > total_floors:
    st.warning("Property floor cannot be higher than total floors.")


# ============================================================
# PROPERTY SUMMARY
# ============================================================

st.html(
    """
    <div class="section-kicker">Property Overview</div>
    <div class="section-title">Selected Property</div>
    """
)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.html(
        f"""
        <div class="metric-card">
            <div class="metric-label">Location</div>
            <div class="metric-value">{city}</div>
        </div>
        """
    )

with m2:
    st.html(
        f"""
        <div class="metric-card">
            <div class="metric-label">Area</div>
            <div class="metric-value">
                {area:,.0f}
                <span class="metric-small">sq.ft.</span>
            </div>
        </div>
        """
    )

with m3:
    st.html(
        f"""
        <div class="metric-card">
            <div class="metric-label">Configuration</div>
            <div class="metric-value">{bedrooms} BHK</div>
        </div>
        """
    )

with m4:
    st.html(
        f"""
        <div class="metric-card">
            <div class="metric-label">Floor</div>
            <div class="metric-value">{floor} / {total_floors}</div>
        </div>
        """
    )


# ============================================================
# VALUATION
# ============================================================

st.html(
    """
    <div class="section-kicker">Machine Learning</div>
    <div class="section-title">Property Valuation</div>
    """
)

predict_col, method_col = st.columns([1.15, 1], gap="large")

with predict_col:
    st.html(
        """
        <div class="method-card">
            <div class="method-title">Valuation Engine</div>
            <div class="method-copy">
                EstateIQ estimates the expected market rate per square foot
                from the selected property profile. The resulting rate is
                multiplied by the entered area to produce an indicative
                property value.
            </div>
            <br>
            <span class="method-chip">Location</span>
            <span class="method-chip">Property type</span>
            <span class="method-chip">Area</span>
            <span class="method-chip">Bedrooms</span>
            <span class="method-chip">Bathrooms</span>
            <span class="method-chip">Balconies</span>
            <span class="method-chip">Floor</span>
            <span class="method-chip">Total floors</span>
        </div>
        """,
    )

    if st.button("Estimate Property Value", key="estimate_button"):
        if floor > total_floors:
            st.error("Please ensure property floor is not greater than total floors.")
        else:
            sample_property = pd.DataFrame(
                [{
                    "CITY": city,
                    "PROPERTY_TYPE": property_type,
                    "BEDROOM_NUM": bedrooms,
                    "BATHROOM_NUM": bathrooms,
                    "BALCONY_NUM": balconies,
                    "FLOOR_NUM": floor,
                    "TOTAL_FLOOR": total_floors,
                    "AREA": area,
                }]
            )

            try:
                predicted_price_sqft = float(rf_model.predict(sample_property)[0])
                predicted_price_sqft = max(0.0, predicted_price_sqft)
                estimated_property_value = predicted_price_sqft * area

                st.session_state["predicted_price_sqft"] = predicted_price_sqft
                st.session_state["estimated_property_value"] = estimated_property_value
                st.session_state["prediction_city"] = city
                st.session_state["prediction_type"] = property_type
            except Exception as exc:
                st.error(f"Prediction failed: {exc}")

with method_col:
    st.html(
        """
        <div class="method-card">
            <div class="method-title">How EstateIQ Reads the Property</div>
            <div class="method-copy">
                The model evaluates the property against learned relationships
                in the training data rather than using a single city-wide
                average.
                <br><br>
                <span class="gold">1.</span> Learn property-level patterns<br>
                <span class="gold">2.</span> Estimate ₹ / sq.ft.<br>
                <span class="gold">3.</span> Multiply by property area<br>
                <span class="gold">4.</span> Benchmark against the observed market
            </div>
        </div>
        """
    )


# ============================================================
# PREDICTION RESULT + BENCHMARKS
# ============================================================

if "predicted_price_sqft" in st.session_state:
    predicted_price_sqft = st.session_state["predicted_price_sqft"]
    estimated_property_value = st.session_state["estimated_property_value"]

    city_subset = market_data[market_data["CITY"].astype(str) == city]
    type_subset = market_data[
        market_data["PROPERTY_TYPE"].astype(str) == property_type
    ]

    city_median = float(city_subset["PRICE_SQFT"].median()) if not city_subset.empty else np.nan
    type_median = float(type_subset["PRICE_SQFT"].median()) if not type_subset.empty else np.nan

    city_delta = (
        (predicted_price_sqft / city_median - 1) * 100
        if city_median > 0 else np.nan
    )
    type_delta = (
        (predicted_price_sqft / type_median - 1) * 100
        if type_median > 0 else np.nan
    )

    st.html(
        f"""
        <div class="result-card">
            <div class="result-label">Estimated Market Price</div>
            <div class="result-price">
                ₹{predicted_price_sqft:,.0f}
                <span class="result-unit">/ sq.ft.</span>
            </div>
            <div class="result-total">
                Estimated Property Value: ₹{estimated_property_value:,.0f}
            </div>
            <div class="result-note">
                Model-based estimate · Not a certified property appraisal
            </div>

            <div class="benchmark">
                <div class="benchmark-title">Market Benchmark</div>
            </div>
        </div>
        """
    )

    b1, b2, b3 = st.columns(3)

    with b1:
        city_text = f"₹{city_median:,.0f}" if pd.notna(city_median) else "N/A"
        delta_text = (
            f"{city_delta:+.1f}% vs city median"
            if pd.notna(city_delta) else "No benchmark"
        )
        st.html(
            f"""
            <div class="metric-card">
                <div class="metric-label">{city} Median</div>
                <div class="metric-value">{city_text}</div>
                <div class="benchmark-delta">{delta_text}</div>
            </div>
            """
        )

    with b2:
        type_text = f"₹{type_median:,.0f}" if pd.notna(type_median) else "N/A"
        delta_text = (
            f"{type_delta:+.1f}% vs type median"
            if pd.notna(type_delta) else "No benchmark"
        )
        st.html(
            f"""
            <div class="metric-card">
                <div class="metric-label">Property Type Median</div>
                <div class="metric-value">{type_text}</div>
                <div class="benchmark-delta">{delta_text}</div>
            </div>
            """
        )

    with b3:
        confidence_text = "Moderate"
        if abs(city_delta) <= 15 and abs(type_delta) <= 15:
            confidence_text = "Market-aligned"
        elif abs(city_delta) > 35 or abs(type_delta) > 35:
            confidence_text = "High deviation"

        st.html(
            f"""
            <div class="metric-card">
                <div class="metric-label">Market Position</div>
                <div class="metric-value">{confidence_text}</div>
                <div class="metric-small">
                    Relative to observed benchmarks
                </div>
            </div>
            """
        )


# ============================================================
# MODEL INTELLIGENCE
# ============================================================

st.html(
    """
    <div class="section-kicker">Model Intelligence</div>
    <div class="section-title">Model Performance</div>
    """
)

c1, c2, c3, c4 = st.columns(4)

for col, label, value, accent in [
    (c1, "Model", "Random Forest", False),
    (c2, "Explained Variation", "61.32%", True),
    (c3, "Validation MAE", "₹2,594", False),
    (c4, "Validation RMSE", "₹3,949", False),
]:
    with col:
        st.html(
            f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value {'metric-accent' if accent else ''}">
                    {value}
                </div>
            </div>
            """
        )


# ============================================================
# PLOTLY THEME
# ============================================================

PAPER = "#111214"
PLOT = "#111214"
TEXT = "#9a9da4"
GRID = "#24262a"
GOLD = "#c8a96b"
MUTED_GOLD = "#8f7a52"

def polish(fig, height=390, margin=None):
    fig.update_layout(
        height=height,
        paper_bgcolor=PAPER,
        plot_bgcolor=PLOT,
        font=dict(family="Arial, sans-serif", color=TEXT, size=11),
        margin=margin or dict(l=15, r=20, t=20, b=45),
        hoverlabel=dict(
            bgcolor="#181a1d",
            bordercolor="#35383d",
            font=dict(color="#eeeae2"),
        ),
    )
    return fig


# ============================================================
# MARKET OVERVIEW
# ============================================================

st.html(
    """
    <div class="section-kicker">Market Intelligence</div>
    <div class="section-title">Indian Residential Market Overview</div>
    <div class="section-description">
        A compact view of market concentration, pricing, supply mix and
        observed property-size patterns.
    </div>
    """
)

city_chart = (
    market_data.groupby("CITY", as_index=False)
    .agg(
        Listings=("PRICE_SQFT", "size"),
        Median_Price=("PRICE_SQFT", "median"),
        Average_Price=("PRICE_SQFT", "mean"),
    )
    .sort_values("Median_Price", ascending=True)
)

fig_city = px.bar(
    city_chart,
    x="Median_Price",
    y="CITY",
    orientation="h",
    text="Median_Price",
    custom_data=["Listings", "Average_Price"],
)
fig_city.update_traces(
    marker_color=GOLD,
    marker_line_width=0,
    texttemplate="₹%{text:,.0f}",
    textposition="outside",
    hovertemplate=(
        "<b>%{y}</b><br>"
        "Median: ₹%{x:,.0f}/sq.ft.<br>"
        "Listings: %{customdata[0]:,}<br>"
        "Average: ₹%{customdata[1]:,.0f}/sq.ft."
        "<extra></extra>"
    ),
)
fig_city.update_layout(
    xaxis=dict(
        title="Median price / sq.ft.",
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        tickprefix="₹",
    ),
    yaxis=dict(title=None, showgrid=False),
    showlegend=False,
)
polish(fig_city, 475, dict(l=10, r=70, t=18, b=45))


type_chart = (
    market_data.groupby("PROPERTY_TYPE", as_index=False)
    .agg(Listings=("PRICE_SQFT", "size"))
    .sort_values("Listings", ascending=True)
)

fig_type = px.bar(
    type_chart,
    x="Listings",
    y="PROPERTY_TYPE",
    orientation="h",
    text="Listings",
)
fig_type.update_traces(
    marker_color=MUTED_GOLD,
    marker_line_width=0,
    texttemplate="%{text:,}",
    textposition="outside",
    hovertemplate="<b>%{y}</b><br>Listings: %{x:,}<extra></extra>",
)
fig_type.update_layout(
    xaxis=dict(title="Listings", showgrid=True, gridcolor=GRID, zeroline=False),
    yaxis=dict(title=None, showgrid=False),
    showlegend=False,
)
polish(fig_type, 475, dict(l=10, r=55, t=18, b=45))


a, b = st.columns(2, gap="large")

with a:

    st.plotly_chart(
        fig_city,
        use_container_width=True,
        config={"displayModeBar": False, "responsive": True},
        key="city_price_chart",
    )


with b:

    st.plotly_chart(
        fig_type,
        use_container_width=True,
        config={"displayModeBar": False, "responsive": True},
        key="property_mix_chart",
    )



# ============================================================
# ============================================================
# AREA VS PRICE — INTERACTIVE MARKET MAP
# ============================================================

st.html(
    """
    <div class="section-kicker">Market Relationship</div>
    <div class="section-title">Area vs. Market Rate</div>
    <div class="section-description">
        Compare observed property prices by size. Each property type has its
        own color; click any legend item to show or hide that segment.
    </div>
    """
)

# Only a city selector is exposed here. Property type visibility is handled
# professionally through the Plotly legend, so the chart stays clean.
city_choices = ["All Cities"] + sorted(
    market_data["CITY"].dropna().astype(str).unique().tolist()
)

chart_city = st.selectbox(
    "City",
    city_choices,
    key="area_price_city",
)

area_price = market_data.copy()

if chart_city != "All Cities":
    area_price = area_price[
        area_price["CITY"].astype(str) == chart_city
    ]

# Remove only extreme visual outliers; the source data remains untouched.
if not area_price.empty:
    area_cap = area_price["AREA"].quantile(.995)
    area_price = area_price[area_price["AREA"] <= area_cap]

# Keep the chart responsive with a deterministic sample.
max_points = 2200
if len(area_price) > max_points:
    area_price = area_price.sample(max_points, random_state=42)

if not area_price.empty:
    # Color is PROPERTY_TYPE only.
    # Plotly's native legend is clickable: single click hides a type,
    # double click isolates a type.
    fig_area = px.scatter(
        area_price,
        x="AREA",
        y="PRICE_SQFT",
        color="PROPERTY_TYPE",
        category_orders={
            "PROPERTY_TYPE": sorted(
                area_price["PROPERTY_TYPE"].dropna().astype(str).unique()
            )
        },
        hover_data={
            "CITY": True,
            "PROPERTY_TYPE": True,
            "AREA": False,
            "PRICE_SQFT": False,
        },
        opacity=.68,
    )

    fig_area.update_traces(
        marker=dict(
            size=6.5,
            line=dict(width=0),
        ),
        selector=dict(mode="markers"),
    )

    fig_area.update_layout(
        legend=dict(
            title=None,
            orientation="h",
            yanchor="bottom",
            y=1.015,
            xanchor="left",
            x=0,
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=11, color="#b5b7bc"),
            itemclick="toggle",
            itemdoubleclick="toggleothers",
        ),
        xaxis=dict(
            title="Area (sq.ft.)",
            showgrid=True,
            gridcolor=GRID,
            zeroline=False,
            tickformat=",",
        ),
        yaxis=dict(
            title="Price / sq.ft.",
            showgrid=True,
            gridcolor=GRID,
            zeroline=False,
            tickprefix="₹",
            tickformat=",",
        ),
        hovermode="closest",
        showlegend=True,
    )

    # Hover contains ONLY city + property type.
    fig_area.update_traces(
        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            "%{customdata[1]}"
            "<extra></extra>"
        )
    )

    polish(
        fig_area,
        525,
        dict(l=15, r=20, t=58, b=50),
    )

    
    st.plotly_chart(
        fig_area,
        use_container_width=True,
        config={
            "displayModeBar": False,
            "responsive": True,
        },
        key="interactive_area_price_chart",
    )
   

    st.html(
        """
        <div class="insight-strip">
            <strong class="gold">Interactive:</strong>
            use the legend above the chart to toggle property types.
            Click once to hide/show a segment; double-click to isolate one.
            The city selector changes the market without introducing
            society, building or neighbourhood-level labels.
        </div>
        """
    )
else:
    st.info("No observations match the selected city.")


# PRICE STRUCTURE
# ============================================================

st.html(
    """
    <div class="section-title">Pricing Structure</div>
    <div class="section-description">
        Median price by bedroom count and the distribution of observed
        listings across price bands.
    </div>
    """
)

bedroom_chart = (
    market_data[
        market_data["BEDROOM_NUM"].notna()
        & (market_data["BEDROOM_NUM"] <= 6)
        & (market_data["BEDROOM_NUM"] >= 1)
    ]
    .groupby("BEDROOM_NUM", as_index=False)
    .agg(
        Listings=("PRICE_SQFT", "size"),
        Median_Price=("PRICE_SQFT", "median"),
        Average_Area=("AREA", "mean"),
    )
    .sort_values("BEDROOM_NUM")
)

fig_bedroom = px.bar(
    bedroom_chart,
    x="BEDROOM_NUM",
    y="Median_Price",
    text="Median_Price",
    custom_data=["Listings", "Average_Area"],
)
fig_bedroom.update_traces(
    marker_color=GOLD,
    texttemplate="₹%{text:,.0f}",
    textposition="outside",
    hovertemplate=(
        "<b>%{x} BHK</b><br>"
        "Median: ₹%{y:,.0f}/sq.ft.<br>"
        "Listings: %{customdata[0]:,}<br>"
        "Avg. area: %{customdata[1]:,.0f} sq.ft."
        "<extra></extra>"
    ),
)
fig_bedroom.update_layout(
    xaxis=dict(title="Bedrooms", dtick=1, showgrid=False),
    yaxis=dict(
        title="Median price / sq.ft.",
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        tickprefix="₹",
    ),
    showlegend=False,
)
polish(fig_bedroom, 390)


bands = pd.cut(
    market_data["PRICE_SQFT"],
    bins=[0, 5000, 10000, 15000, 20000, 30000, float("inf")],
    labels=["< ₹5K", "₹5K–₹10K", "₹10K–₹15K", "₹15K–₹20K", "₹20K–₹30K", "₹30K+"],
    include_lowest=True,
)

band_chart = (
    bands.value_counts(sort=False)
    .rename_axis("Price_Band")
    .reset_index(name="Listings")
)

fig_band = px.bar(
    band_chart,
    x="Price_Band",
    y="Listings",
    text="Listings",
)
fig_band.update_traces(
    marker_color=MUTED_GOLD,
    texttemplate="%{text:,}",
    textposition="outside",
    hovertemplate="<b>%{x}</b><br>Listings: %{y:,}<extra></extra>",
)
fig_band.update_layout(
    xaxis=dict(title="Observed price band / sq.ft.", showgrid=False),
    yaxis=dict(title="Listings", showgrid=True, gridcolor=GRID, zeroline=False),
    showlegend=False,
)
polish(fig_band, 390)


a, b = st.columns(2, gap="large")

with a:

    st.plotly_chart(
        fig_bedroom,
        use_container_width=True,
        config={"displayModeBar": False, "responsive": True},
        key="bedroom_price_chart",
    )


with b:

    st.plotly_chart(
        fig_band,
        use_container_width=True,
        config={"displayModeBar": False, "responsive": True},
        key="price_band_chart",
    )



# ============================================================
# EDA QUESTIONS & ANSWERS
# ============================================================

st.html(
    """
    <div class="section-kicker">Exploratory Data Analysis</div>
    <div class="section-title">What Does the Data Tell Us?</div>
    <div class="section-description">
        Business-facing EDA questions turn the raw market dataset into
        concise findings that can be discussed in a project presentation
        or interview.
    </div>
    """
)

total_listings = len(market_data)

city_counts = market_data["CITY"].value_counts()
top_city = city_counts.index[0]
top_city_count = int(city_counts.iloc[0])
top_city_share = top_city_count / total_listings * 100

type_counts = market_data["PROPERTY_TYPE"].value_counts()
top_type = type_counts.index[0]
top_type_count = int(type_counts.iloc[0])
top_type_share = top_type_count / total_listings * 100

median_price = float(market_data["PRICE_SQFT"].median())
median_area = float(market_data["AREA"].median())

most_common_bedroom = None
bedroom_share = None
if "BEDROOM_NUM" in market_data.columns:
    known_bedrooms = market_data.dropna(subset=["BEDROOM_NUM"])
    if not known_bedrooms.empty:
        bedroom_counts = known_bedrooms["BEDROOM_NUM"].astype(int).value_counts()
        most_common_bedroom = int(bedroom_counts.index[0])
        bedroom_share = bedroom_counts.iloc[0] / len(known_bedrooms) * 100

highest_price_city = (
    market_data.groupby("CITY")["PRICE_SQFT"].median().idxmax()
)
highest_price_city_median = (
    market_data.groupby("CITY")["PRICE_SQFT"].median().max()
)

lowest_price_city = (
    market_data.groupby("CITY")["PRICE_SQFT"].median().idxmin()
)
lowest_price_city_median = (
    market_data.groupby("CITY")["PRICE_SQFT"].median().min()
)

q1, q2 = st.columns(2, gap="large")

with q1:
    st.html(
        f"""
        <div class="qa-card">
            <div class="qa-question">Which market has the largest supply?</div>
            <div class="qa-answer">
                <strong>{top_city}</strong> leads the dataset with
                <strong>{top_city_count:,} listings</strong>, representing
                approximately <strong>{top_city_share:.1f}%</strong> of all
                observations.
            </div>
        </div>
        """
    )

with q2:
    st.html(
        f"""
        <div class="qa-card">
            <div class="qa-question">Which property type dominates the market?</div>
            <div class="qa-answer">
                <strong>{top_type}</strong> is the dominant segment with
                <strong>{top_type_count:,} listings</strong> or
                <strong>{top_type_share:.1f}%</strong> of the dataset.
            </div>
        </div>
        """
    )

q3, q4 = st.columns(2, gap="large")

with q3:
    bedroom_text = (
        f"<strong>{most_common_bedroom} BHK</strong> accounts for "
        f"<strong>{bedroom_share:.1f}%</strong> of records with known bedroom counts."
        if most_common_bedroom is not None
        else "Bedroom information is not sufficiently available."
    )
    st.html(
        f"""
        <div class="qa-card">
            <div class="qa-question">What is the most common home configuration?</div>
            <div class="qa-answer">{bedroom_text}</div>
        </div>
        """
    )

with q4:
    st.html(
        f"""
        <div class="qa-card">
            <div class="qa-question">Where is pricing most expensive?</div>
            <div class="qa-answer">
                <strong>{highest_price_city}</strong> has the highest observed
                city median at approximately
                <strong>₹{highest_price_city_median:,.0f}/sq.ft.</strong>,
                while <strong>{lowest_price_city}</strong> is the lowest at
                approximately <strong>₹{lowest_price_city_median:,.0f}/sq.ft.</strong>
            </div>
        </div>
        """
    )

q5, q6 = st.columns(2, gap="large")

with q5:
    st.html(
        f"""
        <div class="qa-card">
            <div class="qa-question">What does a typical listing look like?</div>
            <div class="qa-answer">
                Across the dataset, the median observed rate is
                <strong>₹{median_price:,.0f}/sq.ft.</strong> and the median
                property area is approximately
                <strong>{median_area:,.0f} sq.ft.</strong>
            </div>
        </div>
        """
    )

with q6:
    if len(market_data) >= 2:
        corr = market_data[["AREA", "PRICE_SQFT"]].corr().iloc[0, 1]
        corr_label = (
            "weak positive" if corr > .15 else
            "weak negative" if corr < -.15 else
            "limited linear"
        )
        answer = (
            f"The raw area-price relationship is <strong>{corr_label}</strong> "
            f"(Pearson correlation ≈ <strong>{corr:.2f}</strong>). "
            "This supports using additional property and location features "
            "instead of relying on area alone."
        )
    else:
        answer = "Insufficient observations for correlation analysis."

    st.html(
        f"""
        <div class="qa-card">
            <div class="qa-question">Does larger area automatically mean a higher ₹/sq.ft.?</div>
            <div class="qa-answer">{answer}</div>
        </div>
        """
    )


# ============================================================
# FEATURE IMPORTANCE
# ============================================================

st.html(
    """
    <div class="section-kicker">Feature Analysis</div>
    <div class="section-title">What Drives Valuation?</div>
    <div class="section-description">
        Relative model feature importance from the valuation analysis.
        Higher values indicate greater contribution within the trained model.
    </div>
    """
)

importance_data = pd.DataFrame(
    {
        "Feature": [
            "City",
            "Total Floors",
            "Area",
            "Property Type",
            "Bedrooms",
            "Balconies",
            "Floor",
            "Bathrooms",
        ],
        "Importance": [
            0.6353,
            0.3840,
            0.3016,
            0.2323,
            0.0660,
            0.0653,
            0.0190,
            0.0173,
        ],
    }
).sort_values("Importance", ascending=True)

fig_importance = px.bar(
    importance_data,
    x="Importance",
    y="Feature",
    orientation="h",
    text="Importance",
)
fig_importance.update_traces(
    marker_color=GOLD,
    marker_line_width=0,
    texttemplate="%{text:.2f}",
    textposition="outside",
    hovertemplate="<b>%{y}</b><br>Importance: %{x:.3f}<extra></extra>",
)
fig_importance.update_layout(
    xaxis=dict(
        title=None,
        range=[0, .72],
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        tickformat=".2f",
    ),
    yaxis=dict(title=None, showgrid=False),
    showlegend=False,
)
polish(fig_importance, 380, dict(l=15, r=60, t=15, b=25))


st.plotly_chart(
    fig_importance,
    use_container_width=True,
    config={"displayModeBar": False, "responsive": True},
    key="feature_importance_chart",
)



# ============================================================
# FINAL TAKEAWAY
# ============================================================

st.html(
    f"""
    <div class="insight-strip">
        <strong class="gold">EstateIQ takeaway:</strong>
        the dataset is heavily concentrated in a small number of markets and
        property segments, while location and building characteristics create
        substantial pricing differences. The valuation model therefore uses
        multiple features rather than treating area as the sole pricing driver.
    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="footer">
        <strong>EstateIQ</strong>
        &nbsp;·&nbsp;
        Indian Real Estate Market Intelligence
        &nbsp;·&nbsp;
        Machine Learning Property Valuation
        <br>
        Built with Python · Pandas · Scikit-learn · Streamlit · Plotly
    </div>
    """
)

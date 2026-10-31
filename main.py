
import streamlit as st
import pandas as pd
import plotly.express as px

from data_preparation import (
    load_datasets,
    prepare_yearly_monthly_data
)

# -----------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------

st.set_page_config(
    page_title="Global Food Security Dashboard",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------
# LOAD DATA
# -----------------------------------------

@st.cache_data
def get_data():
    panel, indicators = load_datasets()
    yearly = prepare_yearly_monthly_data(panel)
    return panel, indicators, yearly


panel_df, indicators_df, yearly_df = get_data()

# -----------------------------------------
# CUSTOM DESIGN
# -----------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

/* FONT STYLE */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body {
    font-family: 'Poppins', sans-serif;
}

h1, h2, h3, h4, p, label, li,
[data-testid="stMarkdownContainer"],
[data-testid="stMetric"] {
    font-family: 'Poppins', sans-serif;
}

/* Restore Streamlit icons */
[data-testid="stIconMaterial"] {
    font-family: 'Material Symbols Rounded' !important;
}

/* Main page titles */
h1 {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
}

/* Section headings */
h2, h3 {
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
}

/* Regular text */
p, label, li {
    font-family: 'Poppins', sans-serif;
    font-weight: 400;
}

/* Main page */
.stApp {
    background-color: #F7F5EF;
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #173D32;
}

section[data-testid="stSidebar"] * {
    color: #F7F5EF;
}

/* Sidebar radio buttons */
section[data-testid="stSidebar"] label {
    color: #F7F5EF !important;
}

/* Main headings */
h1, h2, h3 {
    color: #214C3A;
}

/* KPI cards */
.kpi-card {
    background-color: #FFFFFF;
    border-left: 5px solid #2F6B4F;
    border-radius: 10px;
    padding: 18px;
    min-height: 115px;
    box-shadow: 0 2px 8px rgba(30, 60, 45, 0.07);
}

.kpi-label {
    color: #68776D;
    font-size: 13px;
    margin-bottom: 10px;
}

.kpi-value {
    color: #214C3A;
    font-size: 27px;
    font-weight: 700;
}

.kpi-description {
    color: #8A958D;
    font-size: 11px;
    margin-top: 7px;
}

/* Divider */
hr {
    border-color: #DCE3DA;
}

/* SIDEBAR DESIGN */
section[data-testid="stSidebar"] {
    background-color: #173D32;
}

/* Sidebar title */
section[data-testid="stSidebar"] h2 {
    color: #FFFFFF;
    font-size: 23px;
    font-weight: 700;
    padding-bottom: 5px;
}

/* Navigation label */
section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
    color: #D8B56D;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
}

/* Navigation options */
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    padding: 9px 12px;
    border-radius: 8px;
    margin-bottom: 5px;
    transition: background-color 0.2s ease;
}

/* Hover effect */
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background-color: #285443;
}

/* Selected navigation option */
section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
    background-color: #2F6B4F;
    border-left: 4px solid #D8B56D;
}

/* Navigation text */
section[data-testid="stSidebar"] div[role="radiogroup"] label p {
    color: #F7F5EF;
    font-size: 14px;
    font-weight: 500;
}

/* Sidebar captions */
section[data-testid="stSidebar"] .stCaption {
    color: #A9BDB1;
}

/* LIGHT GREEN INFO BOX */
div[data-testid="stAlert"][data-baseweb="notification"] {
    background-color: #E5F0E7 !important;
    border: 1px solid #C5DCC9 !important;
    border-left: 5px solid #2F6B4F !important;
    border-radius: 10px !important;
}

/* INFO BOX TEXT */
div[data-testid="stAlert"][data-baseweb="notification"] p {
    color: #214C3A !important;
}

/* INFO BOX ICON */
div[data-testid="stAlert"][data-baseweb="notification"] svg {
    fill: #2F6B4F !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------
# HELPER FUNCTION FOR KPI CARDS
# -----------------------------------------

def show_kpi(label, value, description):

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-description">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def style_chart(fig):
    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(family="Poppins", size=12, color="#26372E"),
        title=dict(
            font=dict(family="Poppins", size=17, color="#254D3A"),
            x=0.02,
            xanchor="left"
        ),
        margin=dict(l=25, r=25, t=65, b=35),
        hovermode="x unified",
        legend=dict(bgcolor="rgba(255,255,255,0.7)", borderwidth=0),
        xaxis=dict(showgrid=False, zeroline=False, linecolor="#DCE3DA"),
        yaxis=dict(showgrid=True, gridcolor="#EDF0EA", zeroline=False, linecolor="#DCE3DA")
    )
    return fig

# -----------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------

st.sidebar.markdown(
    "<h2 style='color:#FFFFFF;'>🌾 Food Security</h2>",
    unsafe_allow_html=True
)

st.sidebar.caption("GLOBAL DATA ANALYTICS")

st.sidebar.divider()

page = st.sidebar.radio(
    "DASHBOARD NAVIGATION",
    [
        "Overview",
        "Food Price Analysis",
        "Fertilizer Cost Analysis",
        "Agricultural Production",
        "Food Insecurity Analysis",
        "Relationship Analysis",
        "Key Findings"
    ]
)

st.sidebar.divider()

st.sidebar.caption("Data coverage: 1961–2024")
st.sidebar.caption("Food Security Analytics Project")

# -----------------------------------------
# DASHBOARD HEADER
# -----------------------------------------

st.markdown(
    """
    <h1 style="color:#214C3A; margin-bottom:0;">
        🌾 Global Food Security Dashboard
    </h1>
    <p style="color:#68776D; font-size:16px;">
        Exploring food prices, fertilizer costs,
        agricultural production, and food insecurity.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------------------
# OVERVIEW PAGE
# -----------------------------------------

if page == "Overview":

    st.subheader("Dashboard Overview")

    st.write(
        "Monitor important food security indicators "
        "and explore how they have changed over time."
    )

    # Calculate KPI values
    avg_undernourishment = (
        indicators_df["undernourishment_pct"].mean()
    )

    latest_production = (
        indicators_df["food_production_index"]
        .dropna()
        .iloc[-1]
    )

    latest_food_price = panel_df["ffpi_overall"].iloc[-1]

    latest_fertilizer = (
        panel_df["fertiliser_composite_idx"].iloc[-1]
    )

    # KPI cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        show_kpi(
            "Average Undernourishment",
            f"{avg_undernourishment:.2f}%",
            "Available annual observations"
        )

    with col2:
        show_kpi(
            "Latest Food Production Index",
            f"{latest_production:.2f}",
            "Most recent available annual value"
        )

    with col3:
        show_kpi(
            "Latest Food Price Index",
            f"{latest_food_price:.2f}",
            "Latest monthly observation"
        )

    with col4:
        show_kpi(
            "Latest Fertilizer Index",
            f"{latest_fertilizer:.2f}",
            "Latest monthly observation"
        )

    st.write("")
    st.divider()

    # -------------------------------------
    # FOOD PRICE CHART
    # -------------------------------------

    st.subheader("Food Price Index Trend")

    fig = px.line(
        panel_df,
        x="date",
        y="ffpi_overall",
        title="Monthly Overall Food Price Index (1990–2024)",
        labels={
            "date": "Year",
            "ffpi_overall": "Food Price Index"
        }
    )

    fig.update_traces(
        line=dict(color="#2F6B4F", width=2)
    )

    fig = style_chart(fig)

    st.plotly_chart(
        fig,
        width="stretch",
        key="food_price_chart"
    )

    st.divider()

    # -------------------------------------
    # UNDERNOURISHMENT CHART
    # -------------------------------------

    st.subheader("Undernourishment Trend")

    fig2 = px.line(
        indicators_df,
        x="year",
        y="undernourishment_pct",
        title="Annual Undernourishment Percentage (1961–2023)",
        labels={
            "year": "Year",
            "undernourishment_pct": "Undernourishment (%)"
        }
    )

    fig2.update_traces(
        line=dict(color="#B38A3E", width=2),
        connectgaps=False
    )

    fig2 = style_chart(fig2)

    st.plotly_chart(
        fig2,
        width="stretch",
        key="undernourishment_chart"
    )

    st.caption(
        "Note: Missing observations are left blank and are not "
        "treated as zero."
    )


# -----------------------------------------
# FOOD PRICE ANALYSIS PAGE
# -----------------------------------------

elif page == "Food Price Analysis":

    st.subheader("Food Price Analysis")

    st.write(
        "Explore changes in global food prices and compare "
        "the movement of major food commodities over time."
    )

    st.divider()

    # DATE FILTER

    st.markdown("### Filter by Date")

    min_date = panel_df["date"].min().date()
    max_date = panel_df["date"].max().date()

    selected_dates = st.date_input(
        "Select date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        key="food_price_date_filter"
    )

    if len(selected_dates) == 2:

        start_date, end_date = selected_dates

        filtered_df = panel_df[
            (panel_df["date"].dt.date >= start_date) &
            (panel_df["date"].dt.date <= end_date)
        ].copy()

    else:
        filtered_df = panel_df.copy()

    if filtered_df.empty:

        st.warning("No data available for the selected date range.")

    else:

        # FOOD PRICE INDEX COMPARISON

        st.markdown("### Food Price Index Trends")

        index_df = filtered_df[
            ["date", "ffpi_overall", "ffpi_cereals"]
        ].melt(
            id_vars="date",
            var_name="Index",
            value_name="Price Index"
        )

        index_df["Index"] = index_df["Index"].map({
            "ffpi_overall": "Overall Food Price Index",
            "ffpi_cereals": "Cereals Food Price Index"
        })

        fig = px.line(
            index_df,
            x="date",
            y="Price Index",
            color="Index",
            title="Overall vs. Cereals Food Price Index",
            labels={
                "date": "Year",
                "Price Index": "Index Value",
                "Index": "Food Price Index"
            },
            color_discrete_sequence=["#2F6B4F", "#B38A3E"]
        )

        fig = style_chart(fig)

        st.plotly_chart(
            fig,
            width="stretch",
            key="food_price_index_comparison"
        )

        st.divider()

        # COMMODITY PRICE COMPARISON

        st.markdown("### Major Food Commodity Prices")

        commodity_columns = {
            "wheat_usd_mt": "Wheat",
            "maize_usd_mt": "Maize",
            "soybean_oil_usd_mt": "Soybean Oil"
        }

        commodity_df = filtered_df[
            ["date"] + list(commodity_columns.keys())
        ].melt(
            id_vars="date",
            var_name="Commodity",
            value_name="Price (USD/MT)"
        )

        commodity_df["Commodity"] = (
            commodity_df["Commodity"].map(commodity_columns)
        )

        fig2 = px.line(
            commodity_df,
            x="date",
            y="Price (USD/MT)",
            color="Commodity",
            title="Monthly Prices of Major Food Commodities",
            labels={
                "date": "Year",
                "Price (USD/MT)": "Price (USD per Metric Ton)",
                "Commodity": "Commodity"
            },
            color_discrete_sequence=[
                "#2F6B4F",
                "#B38A3E",
                "#9B6A50"
            ]
        )

        fig2 = style_chart(fig2)

        st.plotly_chart(
            fig2,
            width="stretch",
            key="commodity_price_comparison"
        )

        st.caption(
            "Commodity prices are expressed in USD per metric ton. "
            "The date filter applies to both charts."
        )


# -----------------------------------------
# FERTILIZER COST ANALYSIS PAGE
# -----------------------------------------

elif page == "Fertilizer Cost Analysis":

    st.subheader("Fertilizer Cost Analysis")

    st.write(
        "Examine changes in global fertilizer prices and explore "
        "their relationship with food commodity prices."
    )

    st.divider()

    # DATE FILTER

    st.markdown("### Filter by Date")

    min_date = panel_df["date"].min().date()
    max_date = panel_df["date"].max().date()

    selected_dates = st.date_input(
        "Select date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        key="fertilizer_date_filter"
    )

    if len(selected_dates) == 2:

        start_date, end_date = selected_dates

        filtered_df = panel_df[
            (panel_df["date"].dt.date >= start_date) &
            (panel_df["date"].dt.date <= end_date)
        ].copy()

    else:
        filtered_df = panel_df.copy()

    if filtered_df.empty:

        st.warning("No data available for the selected date range.")

    else:

        # -------------------------------------
        # FERTILIZER PRICE TRENDS
        # -------------------------------------

        st.markdown("### Fertilizer Price Trends")

        fertilizer_columns = {
            "dap_fertiliser_usd_mt": "DAP Fertilizer",
            "mop_potash_usd_mt": "MOP Potash"
        }

        fertilizer_df = filtered_df[
            ["date"] + list(fertilizer_columns.keys())
        ].melt(
            id_vars="date",
            var_name="Fertilizer",
            value_name="Price (USD/MT)"
        )

        fertilizer_df["Fertilizer"] = (
            fertilizer_df["Fertilizer"].map(fertilizer_columns)
        )

        fig = px.line(
            fertilizer_df,
            x="date",
            y="Price (USD/MT)",
            color="Fertilizer",
            title="Monthly DAP and MOP Fertilizer Prices",
            labels={
                "date": "Year",
                "Price (USD/MT)": "Price (USD per Metric Ton)",
                "Fertilizer": "Fertilizer Type"
            },
            color_discrete_sequence=["#2F6B4F", "#B38A3E"]
        )

        fig = style_chart(fig)

        st.plotly_chart(
            fig,
            width="stretch",
            key="fertilizer_price_trends"
        )

        st.divider()

        # -------------------------------------
        # FERTILIZER COMPOSITE INDEX
        # -------------------------------------

        st.markdown("### Fertilizer Composite Index")

        fig2 = px.line(
            filtered_df,
            x="date",
            y="fertiliser_composite_idx",
            title="Monthly Fertilizer Composite Index",
            labels={
                "date": "Year",
                "fertiliser_composite_idx": "Composite Index"
            }
        )

        fig2.update_traces(
            line=dict(color="#9B6A50", width=2)
        )

        fig2 = style_chart(fig2)

        st.plotly_chart(
            fig2,
            width="stretch",
            key="fertilizer_composite_trend"
        )

        st.divider()

        # -------------------------------------
        # DAP FERTILIZER VS. WHEAT PRICE
        # -------------------------------------

        st.markdown("### Fertilizer vs. Food Commodity Price")

        fig3 = px.scatter(
            filtered_df,
            x="dap_fertiliser_usd_mt",
            y="wheat_usd_mt",
            title="Relationship Between DAP Fertilizer and Wheat Prices",
            labels={
                "dap_fertiliser_usd_mt": "DAP Price (USD/MT)",
                "wheat_usd_mt": "Wheat Price (USD/MT)"
            },
            color_discrete_sequence=["#2F6B4F"],
            hover_data=["date"]
        )

        fig3 = style_chart(fig3)

        st.plotly_chart(
            fig3,
            width="stretch",
            key="fertilizer_wheat_scatter"
        )

        st.divider()

        # -------------------------------------
        # DAP-TO-WHEAT RATIO
        # -------------------------------------

        st.markdown("### DAP-to-Wheat Price Ratio")

        fig4 = px.line(
            filtered_df,
            x="date",
            y="dap_to_wheat_ratio",
            title="DAP Fertilizer Price Relative to Wheat Price",
            labels={
                "date": "Year",
                "dap_to_wheat_ratio": "DAP-to-Wheat Ratio"
            }
        )

        fig4.update_traces(
            line=dict(color="#B38A3E", width=2)
        )

        fig4 = style_chart(fig4)

        st.plotly_chart(
            fig4,
            width="stretch",
            key="dap_wheat_ratio_chart"
        )

        st.caption(
            "Note: Fertilizer and commodity prices are expressed "
            "in USD per metric ton. The DAP-to-wheat ratio shows "
            "the relative price of DAP fertilizer compared with wheat."
        )



# -----------------------------------------
# AGRICULTURAL PRODUCTION PAGE
# -----------------------------------------

elif page == "Agricultural Production":

    st.subheader("Agricultural Production")

    st.write(
        "Explore changes in global agricultural production, "
        "cereal yield, and the availability of arable land."
    )

    st.divider()

    # YEAR FILTER

    st.markdown("### Filter by Year")

    min_year = int(indicators_df["year"].min())
    max_year = int(indicators_df["year"].max())

    selected_years = st.slider(
        "Select year range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
        key="agriculture_year_filter"
    )

    filtered_df = indicators_df[
        (indicators_df["year"] >= selected_years[0]) &
        (indicators_df["year"] <= selected_years[1])
    ].copy()

    # FOOD PRODUCTION INDEX

    st.markdown("### Food Production Index")

    fig = px.line(
        filtered_df,
        x="year",
        y="food_production_index",
        title="Annual Food Production Index",
        labels={
            "year": "Year",
            "food_production_index": "Food Production Index"
        }
    )

    fig.update_traces(
        line=dict(color="#2F6B4F", width=2),
        connectgaps=False
    )

    fig = style_chart(fig)

    st.plotly_chart(
        fig,
        width="stretch",
        key="food_production_trend"
    )

    st.divider()

    # CEREAL YIELD

    st.markdown("### Cereal Yield")

    fig2 = px.line(
        filtered_df,
        x="year",
        y="cereal_yield_kg_ha",
        title="Annual Cereal Yield",
        labels={
            "year": "Year",
            "cereal_yield_kg_ha": "Cereal Yield (kg/ha)"
        }
    )

    fig2.update_traces(
        line=dict(color="#B38A3E", width=2),
        connectgaps=False
    )

    fig2 = style_chart(fig2)

    st.plotly_chart(
        fig2,
        width="stretch",
        key="cereal_yield_trend"
    )

    st.divider()

    # ARABLE LAND

    st.markdown("### Arable Land Percentage")

    fig3 = px.line(
        filtered_df,
        x="year",
        y="arable_land_pct",
        title="Annual Arable Land Percentage",
        labels={
            "year": "Year",
            "arable_land_pct": "Arable Land (%)"
        }
    )

    fig3.update_traces(
        line=dict(color="#9B6A50", width=2),
        connectgaps=False
    )

    fig3 = style_chart(fig3)

    st.plotly_chart(
        fig3,
        width="stretch",
        key="arable_land_trend"
    )

    st.divider()

    # PRODUCTION AND CEREAL YIELD COMPARISON

    st.markdown("### Production Indicators Comparison")

    comparison_df = filtered_df[
        ["year", "food_production_index", "cereal_yield_kg_ha"]
    ].melt(
        id_vars="year",
        var_name="Indicator",
        value_name="Value"
    )

    comparison_df["Indicator"] = comparison_df["Indicator"].map({
        "food_production_index": "Food Production Index",
        "cereal_yield_kg_ha": "Cereal Yield (kg/ha)"
    })

    fig4 = px.line(
        comparison_df,
        x="year",
        y="Value",
        color="Indicator",
        title="Food Production and Cereal Yield Over Time",
        labels={
            "year": "Year",
            "Value": "Recorded Value",
            "Indicator": "Indicator"
        },
        color_discrete_sequence=["#2F6B4F", "#B38A3E"]
    )

    fig4 = style_chart(fig4)

    st.plotly_chart(
        fig4,
        width="stretch",
        key="production_comparison"
    )

    st.caption(
        "Note: These indicators use annual observations. "
        "Missing values are left blank and are not treated as zero. "
        "The comparison chart uses different measurement units, "
        "so compare the direction of changes rather than the raw values."
    )


# -----------------------------------------
# FOOD INSECURITY ANALYSIS PAGE
# -----------------------------------------

elif page == "Food Insecurity Analysis":

    st.subheader("Food Insecurity Analysis")

    st.write(
        "Explore undernourishment trends and examine food price "
        "crises and supply stress indicators over time."
    )

    st.divider()

    # -------------------------------------
    # YEAR FILTER
    # -------------------------------------

    st.markdown("### Filter by Year")

    min_year = int(panel_df["year"].min())
    max_year = int(panel_df["year"].max())

    selected_years = st.slider(
        "Select year range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
        key="food_insecurity_year_filter"
    )

    # Filter annual data
    filtered_indicators = indicators_df[
        (indicators_df["year"] >= selected_years[0]) &
        (indicators_df["year"] <= selected_years[1])
    ].copy()

    # Filter monthly data
    filtered_panel = panel_df[
        (panel_df["year"] >= selected_years[0]) &
        (panel_df["year"] <= selected_years[1])
    ].copy()

    # -------------------------------------
    # UNDERNOURISHMENT TREND
    # -------------------------------------

    st.markdown("### Undernourishment Trend")

    fig = px.line(
        filtered_indicators,
        x="year",
        y="undernourishment_pct",
        title="Annual Undernourishment Percentage",
        labels={
            "year": "Year",
            "undernourishment_pct": "Undernourishment (%)"
        }
    )

    fig.update_traces(
        line=dict(color="#2F6B4F", width=2),
        connectgaps=False
    )

    fig = style_chart(fig)

    st.plotly_chart(
        fig,
        width="stretch",
        key="undernourishment_analysis_trend"
    )

    st.divider()

    # -------------------------------------
    # FOOD SHOCK SCORE
    # -------------------------------------

    st.markdown("### Food Shock Score")

    fig2 = px.line(
        filtered_panel,
        x="date",
        y="food_shock_score",
        title="Monthly Food Shock Score",
        labels={
            "date": "Year",
            "food_shock_score": "Food Shock Score"
        }
    )

    fig2.update_traces(
        line=dict(color="#B38A3E", width=2),
        connectgaps=False
    )

    fig2 = style_chart(fig2)

    st.plotly_chart(
        fig2,
        width="stretch",
        key="food_shock_score_trend"
    )

    st.divider()

    # -------------------------------------
    # FOOD PRICE CRISIS PERIODS
    # -------------------------------------

    st.markdown("### Food Price Crisis Periods")

    crisis_df = (
        filtered_panel.groupby("year")["ffpi_crisis_flag"]
        .sum()
        .reset_index()
    )

    fig3 = px.bar(
        crisis_df,
        x="year",
        y="ffpi_crisis_flag",
        title="Number of Food Price Crisis Months per Year",
        labels={
            "year": "Year",
            "ffpi_crisis_flag": "Number of Crisis Months"
        }
    )

    fig3.update_traces(
        marker_color="#9B6A50"
    )

    fig3 = style_chart(fig3)

    st.plotly_chart(
        fig3,
        width="stretch",
        key="food_price_crisis_chart"
    )

    st.divider()

    # -------------------------------------
    # SUPPLY STRESS PERIODS
    # -------------------------------------

    st.markdown("### Supply Stress Periods")

    stress_df = (
        filtered_panel.groupby("year")["supply_stress_flag"]
        .sum()
        .reset_index()
    )

    fig4 = px.bar(
        stress_df,
        x="year",
        y="supply_stress_flag",
        title="Number of Supply Stress Months per Year",
        labels={
            "year": "Year",
            "supply_stress_flag": "Number of Supply Stress Months"
        }
    )

    fig4.update_traces(
        marker_color="#2F6B4F"
    )

    fig4 = style_chart(fig4)

    st.plotly_chart(
        fig4,
        width="stretch",
        key="supply_stress_chart"
    )

    st.caption(
        "Note: Crisis and supply stress charts count the months "
        "flagged by the dataset. These indicators do not independently "
        "measure the percentage of people experiencing food insecurity."
    )



# -----------------------------------------
# RELATIONSHIP ANALYSIS PAGE
# -----------------------------------------

elif page == "Relationship Analysis":

    st.subheader("Relationship Analysis")

    st.write(
        "Explore the relationships between food prices, fertilizer "
        "costs, agricultural production, and undernourishment."
    )

    st.divider()

    # COMBINE YEARLY PRICE DATA WITH ANNUAL INDICATORS
    relationship_df = pd.merge(
        yearly_df,
        indicators_df,
        on="year",
        how="inner"
    )

    # YEAR FILTER
    st.markdown("### Filter by Year")

    min_year = int(relationship_df["year"].min())
    max_year = int(relationship_df["year"].max())

    selected_years = st.slider(
        "Select year range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
        key="relationship_year_filter"
    )

    filtered_relationship = relationship_df[
        (relationship_df["year"] >= selected_years[0]) &
        (relationship_df["year"] <= selected_years[1])
    ].copy()

    st.divider()

    # CORRELATION EXPLANATION
    st.markdown("### Understanding Correlation")

    st.write(
        "Pearson correlation measures the strength and direction "
        "of a linear relationship between two variables."
    )

    st.write(
        "- Close to +1: Strong positive relationship\n"
        "- Close to -1: Strong negative relationship\n"
        "- Close to 0: Weak or no linear relationship"
    )

    st.caption(
        "Remember: Correlation does not prove that one variable causes another."
    )

    st.divider()

    # DEFINE RELATIONSHIPS TO ANALYZE
    relationships = [
        (
            "fertiliser_composite_idx",
            "ffpi_overall",
            "Fertilizer Composite Index",
            "Overall Food Price Index",
            "Fertilizer Prices vs. Food Prices"
        ),
        (
            "ffpi_overall",
            "undernourishment_pct",
            "Overall Food Price Index",
            "Undernourishment (%)",
            "Food Prices vs. Undernourishment"
        ),
        (
            "food_production_index",
            "undernourishment_pct",
            "Food Production Index",
            "Undernourishment (%)",
            "Food Production vs. Undernourishment"
        ),
        (
            "cereal_yield_kg_ha",
            "undernourishment_pct",
            "Cereal Yield (kg/ha)",
            "Undernourishment (%)",
            "Cereal Yield vs. Undernourishment"
        ),
        (
            "arable_land_pct",
            "undernourishment_pct",
            "Arable Land (%)",
            "Undernourishment (%)",
            "Arable Land vs. Undernourishment"
        )
    ]


    st.markdown("### Relationship Scatter Plots")

    # DISPLAY SCATTER PLOTS
    for i in range(0, len(relationships), 2):

        cols = st.columns(2)

        for j, col in enumerate(cols):

            if i + j >= len(relationships):
                break

            x_col, y_col, x_label, y_label, chart_title = relationships[i + j]

            chart_df = filtered_relationship[
                ["year", x_col, y_col]
            ].dropna()

            with col:

                st.markdown(f"#### {chart_title}")

                if len(chart_df) >= 2:

                    correlation = chart_df[x_col].corr(chart_df[y_col])

                    fig = px.scatter(
                        chart_df,
                        x=x_col,
                        y=y_col,
                        hover_data=["year"],
                        title=chart_title,
                        labels={
                            x_col: x_label,
                            y_col: y_label
                        }
                    )

                    fig.update_traces(
                        marker=dict(
                            color="#2F6B4F",
                            size=9,
                            opacity=0.75
                        )
                    )

                    fig = style_chart(fig)

                    st.plotly_chart(
                        fig,
                        width="stretch",
                        key=f"relationship_scatter_{i+j}"
                    )

                    st.metric(
                        "Pearson Correlation",
                        f"{correlation:.3f}"
                    )

                    st.caption(
                        f"Number of valid yearly observations: {len(chart_df)}"
                    )

                else:
                    st.warning(
                        "Not enough valid data to calculate this relationship."
                    )

    st.divider()

    # CORRELATION HEATMAP
    st.markdown("### Correlation Heatmap")

    correlation_columns = [
        "ffpi_overall",
        "fertiliser_composite_idx",
        "undernourishment_pct",
        "food_production_index",
        "cereal_yield_kg_ha",
        "arable_land_pct"
    ]

    correlation_labels = {
        "ffpi_overall": "Food Price Index",
        "fertiliser_composite_idx": "Fertilizer Index",
        "undernourishment_pct": "Undernourishment",
        "food_production_index": "Food Production",
        "cereal_yield_kg_ha": "Cereal Yield",
        "arable_land_pct": "Arable Land"
    }

    correlation_matrix = filtered_relationship[
        correlation_columns
    ].corr()

    correlation_matrix = correlation_matrix.rename(
        index=correlation_labels,
        columns=correlation_labels
    )

    fig_heatmap = px.imshow(
        correlation_matrix,
        text_auto=".2f",
        color_continuous_scale="RdYlGn",
        zmin=-1,
        zmax=1,
        title="Correlation Between Food Security Indicators"
    )

    fig_heatmap = style_chart(fig_heatmap)

    st.plotly_chart(
        fig_heatmap,
        width="stretch",
        key="relationship_correlation_heatmap"
    )

    st.caption(
        "Note: Correlations are calculated using available yearly data. "
        "Missing values are excluded from each variable pair. "
        "Different pairs may therefore have different observation counts."
    )

    
    st.divider()

    # YEAR-TO-YEAR CHANGE ANALYSIS
    st.markdown("### Year-to-Year Change Analysis")

    st.write(
        "This section examines whether annual increases or decreases "
        "in one indicator are associated with increases or decreases "
        "in another indicator."
    )

    # Calculate changes using the complete yearly dataset first
    change_columns = [
        "fertiliser_composite_idx",
        "ffpi_overall",
        "undernourishment_pct",
        "food_production_index",
        "cereal_yield_kg_ha",
        "arable_land_pct"
    ]

    change_df = relationship_df[
        ["year"] + change_columns
    ].copy()

    change_df = change_df.sort_values("year").reset_index(drop=True)

    # Calculate year-to-year differences
    change_df[change_columns] = change_df[change_columns].diff()

    # Exclude differences where years are not consecutive
    consecutive_years = change_df["year"].diff() == 1

    change_df.loc[
        ~consecutive_years,
        change_columns
    ] = float("nan")

    # Apply the selected year filter after calculating differences
    filtered_changes = change_df[
        (change_df["year"] >= selected_years[0]) &
        (change_df["year"] <= selected_years[1])
    ].copy()

    change_relationships = [
        (
            "Fertilizer Price Change",
            "Food Price Change",
            "fertiliser_composite_idx",
            "ffpi_overall",
            "Fertilizer vs. Food Price Changes"
        ),
        (
            "Food Price Change",
            "Undernourishment Change",
            "ffpi_overall",
            "undernourishment_pct",
            "Food Price vs. Undernourishment Changes"
        ),
        (
            "Production Change",
            "Undernourishment Change",
            "food_production_index",
            "undernourishment_pct",
            "Production vs. Undernourishment Changes"
        ),
        (
            "Cereal Yield Change",
            "Undernourishment Change",
            "cereal_yield_kg_ha",
            "undernourishment_pct",
            "Cereal Yield vs. Undernourishment Changes"
        ),
        (
            "Arable Land Change",
            "Undernourishment Change",
            "arable_land_pct",
            "undernourishment_pct",
            "Arable Land vs. Undernourishment Changes"
        )
    ]

    change_results = []

    for x_label, y_label, x_col, y_col, chart_title in change_relationships:

        valid_data = filtered_changes[
            ["year", x_col, y_col]
        ].dropna()

        if len(valid_data) >= 2:

            correlation = valid_data[x_col].corr(valid_data[y_col])

            change_results.append({
                "Relationship": chart_title,
                "Correlation": correlation,
                "Observations": len(valid_data)
            })

    if change_results:

        change_results_df = pd.DataFrame(change_results)

        # Display correlation values
        st.markdown("#### Year-to-Year Correlation Results")

        for i in range(0, len(change_results_df), 2):

            cols = st.columns(2)

            for j, col in enumerate(cols):

                if i + j >= len(change_results_df):
                    break

                result = change_results_df.iloc[i + j]

                with col:
                    st.metric(
                        result["Relationship"],
                        f'{result["Correlation"]:.3f}'
                    )

                    st.caption(
                        f'Valid observations: {result["Observations"]}'
                    )

        # Display correlation comparison chart
        fig_changes = px.bar(
            change_results_df,
            x="Relationship",
            y="Correlation",
            title="Year-to-Year Correlation Comparison",
            labels={
                "Relationship": "Indicator Relationship",
                "Correlation": "Pearson Correlation"
            },
            color="Correlation",
            color_continuous_scale="RdYlGn",
            range_color=[-1, 1]
        )

        fig_changes = style_chart(fig_changes)

        fig_changes.update_layout(
            yaxis=dict(range=[-1, 1]),
            xaxis_tickangle=-25
        )

        st.plotly_chart(
            fig_changes,
            width="stretch",
            key="year_to_year_correlation_chart"
        )

    else:
        st.warning(
            "Not enough valid data to calculate year-to-year correlations."
        )

    st.caption(
        "Note: Year-to-year changes are calculated as the current "
        "year's value minus the previous consecutive year's value. "
        "Missing observations and gaps between years are excluded."
    )


# -----------------------------------------
# KEY FINDINGS PAGE
# -----------------------------------------

elif page == "Key Findings":

    st.subheader("Key Findings")

    st.write(
        "This section presents the major insights gathered from "
        "the analysis of food prices, fertilizer costs, agricultural "
        "production, and food insecurity indicators."
    )

    st.divider()

    # PREPARE YEARLY DATA
    findings_df = pd.merge(
        yearly_df,
        indicators_df,
        on="year",
        how="inner"
    )

    # HELPER FUNCTION FOR CORRELATION
    def calculate_correlation(df, column1, column2):

        valid_data = df[[column1, column2]].dropna()

        if len(valid_data) < 2:
            return None, len(valid_data)

        correlation = valid_data[column1].corr(
            valid_data[column2]
        )

        return correlation, len(valid_data)

    # HELPER FUNCTION FOR INTERPRETATION
    def interpret_correlation(value):

        if value is None or pd.isna(value):
            return "Not enough valid data to determine the relationship."

        if value >= 0.7:
            strength = "strong positive"
        elif value >= 0.3:
            strength = "moderate positive"
        elif value > 0:
            strength = "weak positive"
        elif value <= -0.7:
            strength = "strong negative"
        elif value <= -0.3:
            strength = "moderate negative"
        elif value < 0:
            strength = "weak negative"
        else:
            strength = "no linear"

        if strength == "no linear":
            return "The variables show little to no linear relationship."

        return f"The variables show a {strength} relationship."

    # -----------------------------------------
    # 1. HIGHEST FOOD PRICE YEAR
    # -----------------------------------------

    st.markdown("### 1. Food Price Trends")

    highest_price_row = yearly_df.loc[
        yearly_df["ffpi_overall"].idxmax()
    ]

    highest_price_year = int(highest_price_row["year"])
    highest_price_value = highest_price_row["ffpi_overall"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Highest Food Price Index",
            f"{highest_price_value:.2f}"
        )

    with col2:
        st.metric(
            "Year Recorded",
            highest_price_year
        )

    st.write(
        f"The highest annual average Overall Food Price Index "
        f"was recorded in **{highest_price_year}**, reaching "
        f"**{highest_price_value:.2f}**. This identifies the year "
        f"with the highest average food price index in the observed "
        f"monthly dataset."
    )

    st.divider()

    # -----------------------------------------
    # 2. FERTILIZER AND FOOD PRICE RELATIONSHIP
    # -----------------------------------------

    st.markdown("### 2. Fertilizer Prices and Food Prices")

    fertilizer_corr, fertilizer_count = calculate_correlation(
        yearly_df,
        "fertiliser_composite_idx",
        "ffpi_overall"
    )

    if fertilizer_corr is not None:

        st.metric(
            "Fertilizer and Food Price Correlation",
            f"{fertilizer_corr:.3f}"
        )

        st.write(
            interpret_correlation(fertilizer_corr)
        )

        st.write(
            "The result indicates how fertilizer costs and overall "
            "food prices moved together across the observed years. "
            "A positive correlation means that higher fertilizer "
            "prices tended to occur alongside higher food prices."
        )

        st.caption(
            f"Based on {fertilizer_count} valid yearly observations."
        )

    else:
        st.warning("Not enough data to calculate this relationship.")

    st.divider()

    # -----------------------------------------
    # 3. FOOD PRICES AND UNDERNOURISHMENT
    # -----------------------------------------

    st.markdown("### 3. Food Prices and Undernourishment")

    price_hunger_corr, price_hunger_count = calculate_correlation(
        findings_df,
        "ffpi_overall",
        "undernourishment_pct"
    )

    if price_hunger_corr is not None:

        st.metric(
            "Food Price and Undernourishment Correlation",
            f"{price_hunger_corr:.3f}"
        )

        st.write(
            interpret_correlation(price_hunger_corr)
        )

        st.write(
            "This relationship examines whether changes in the "
            "overall food price index are associated with changes "
            "in the percentage of the population experiencing "
            "undernourishment."
        )

        st.caption(
            f"Based on {price_hunger_count} valid yearly observations."
        )

    else:
        st.warning("Not enough data to calculate this relationship.")

    st.divider()

    # -----------------------------------------
    # 4. AGRICULTURAL PRODUCTION AND UNDERNOURISHMENT
    # -----------------------------------------

    st.markdown("### 4. Agricultural Production and Undernourishment")

    production_corr, production_count = calculate_correlation(
        findings_df,
        "food_production_index",
        "undernourishment_pct"
    )

    cereal_corr, cereal_count = calculate_correlation(
        findings_df,
        "cereal_yield_kg_ha",
        "undernourishment_pct"
    )

    arable_corr, arable_count = calculate_correlation(
        findings_df,
        "arable_land_pct",
        "undernourishment_pct"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Production vs. Undernourishment",
            f"{production_corr:.3f}" if production_corr is not None else "N/A"
        )

    with col2:
        st.metric(
            "Cereal Yield vs. Undernourishment",
            f"{cereal_corr:.3f}" if cereal_corr is not None else "N/A"
        )

    with col3:
        st.metric(
            "Arable Land vs. Undernourishment",
            f"{arable_corr:.3f}" if arable_corr is not None else "N/A"
        )

    st.write(
        "**Food Production:** "
        + interpret_correlation(production_corr)
    )

    st.write(
        "**Cereal Yield:** "
        + interpret_correlation(cereal_corr)
    )

    st.write(
        "**Arable Land:** "
        + interpret_correlation(arable_corr)
    )

    st.caption(
        "These correlations use available yearly observations. "
        "The number of observations may differ because of missing data."
    )

    st.divider()

    
    # -----------------------------------------
    # YEAR-TO-YEAR CHANGE FINDINGS
    # -----------------------------------------

    st.markdown("### 5. Year-to-Year Change Analysis")

    st.write(
        "While long-term correlations show how yearly indicator "
        "values move together, year-to-year correlations examine "
        "whether their annual increases or decreases are associated."
    )

    change_columns = [
        "fertiliser_composite_idx",
        "ffpi_overall",
        "undernourishment_pct",
        "food_production_index",
        "cereal_yield_kg_ha",
        "arable_land_pct"
    ]

    yearly_changes = findings_df[
        ["year"] + change_columns
    ].copy()

    yearly_changes = yearly_changes.sort_values(
        "year"
    ).reset_index(drop=True)

    yearly_changes[change_columns] = (
        yearly_changes[change_columns].diff()
    )

    consecutive_years = yearly_changes["year"].diff() == 1

    yearly_changes.loc[
        ~consecutive_years,
        change_columns
    ] = float("nan")

    change_findings = [
        (
            "Fertilizer vs. Food Price Changes",
            "fertiliser_composite_idx",
            "ffpi_overall"
        ),
        (
            "Food Price vs. Undernourishment Changes",
            "ffpi_overall",
            "undernourishment_pct"
        ),
        (
            "Production vs. Undernourishment Changes",
            "food_production_index",
            "undernourishment_pct"
        ),
        (
            "Cereal Yield vs. Undernourishment Changes",
            "cereal_yield_kg_ha",
            "undernourishment_pct"
        ),
        (
            "Arable Land vs. Undernourishment Changes",
            "arable_land_pct",
            "undernourishment_pct"
        )
    ]

    for title, x_col, y_col in change_findings:

        valid_data = yearly_changes[
            [x_col, y_col]
        ].dropna()

        correlation, observation_count = calculate_correlation(
            valid_data,
            x_col,
            y_col
        )

        st.markdown(f"**{title}**")

        if correlation is not None:

            st.metric(
                "Year-to-Year Correlation",
                f"{correlation:.3f}"
            )

            st.caption(
                f"Valid observations: {observation_count}"
            )

            st.write(
                interpret_correlation(correlation)
            )

        else:
            st.warning("Not enough valid data.")

        st.divider()

    st.write(
        "The results show that fertilizer and food price changes "
        "have a strong positive relationship. However, the annual "
        "changes in food prices, agricultural production, cereal "
        "yield, and arable land show little to no linear relationship "
        "with annual changes in undernourishment."
    )

    st.caption(
        "Year-to-year correlations are based on consecutive yearly "
        "observations. Different relationships may have different "
        "sample sizes because of missing data."
    )

    # -----------------------------------------
    # 5. FOOD PRICE CRISIS PERIODS
    # -----------------------------------------

    st.markdown("### 5. Food Price Crisis Periods")

    crisis_yearly = (
        panel_df.groupby("year")["ffpi_crisis_flag"]
        .sum()
        .reset_index()
    )

    highest_crisis_row = crisis_yearly.loc[
        crisis_yearly["ffpi_crisis_flag"].idxmax()
    ]

    crisis_year = int(highest_crisis_row["year"])
    crisis_months = int(highest_crisis_row["ffpi_crisis_flag"])

    st.metric(
        "Year with the Most Crisis Months",
        crisis_year,
        delta=f"{crisis_months} flagged months",
        delta_color="off"
    )

    st.write(
        f"The year **{crisis_year}** recorded the highest number "
        f"of months flagged as food price crisis periods, with "
        f"**{crisis_months} months**."
    )

    st.divider()

    # -----------------------------------------
    # 6. SUPPLY STRESS PERIODS
    # -----------------------------------------

    st.markdown("### 6. Supply Stress Periods")

    stress_yearly = (
        panel_df.groupby("year")["supply_stress_flag"]
        .sum()
        .reset_index()
    )

    highest_stress_row = stress_yearly.loc[
        stress_yearly["supply_stress_flag"].idxmax()
    ]

    stress_year = int(highest_stress_row["year"])
    stress_months = int(highest_stress_row["supply_stress_flag"])

    st.metric(
        "Year with the Most Supply Stress Months",
        stress_year,
        delta=f"{stress_months} flagged months",
        delta_color="off"
    )

    st.write(
        f"The year **{stress_year}** recorded the highest number "
        f"of months flagged for supply stress, with "
        f"**{stress_months} months**."
    )

    st.divider()

    # -----------------------------------------
    # 7. GENERAL INTERPRETATION
    # -----------------------------------------

    st.markdown("### Overall Interpretation")

    st.write(
        "The findings show how food prices, fertilizer costs, "
        "agricultural production, and undernourishment are connected "
        "within the observed dataset. The correlation results help "
        "identify patterns and associations among these indicators."
    )

    st.markdown(
    """
    <div style="
        background-color: #E5F0E7;
        border: 1px solid #C5DCC9;
        border-left: 5px solid #2F6B4F;
        border-radius: 10px;
        padding: 16px 20px;
        margin: 12px 0;
        color: #214C3A;
        font-family: 'Poppins', sans-serif;
        font-size: 14px;
        line-height: 1.7;
    ">
        <strong>Important:</strong>
        Correlation does not establish causation.
        The results describe statistical relationships in the
        available dataset and should not be interpreted as proof
        that one factor directly causes another.
    </div>
    """,
    unsafe_allow_html=True
    )

    st.caption(
        "Source: Global Food Security dataset. Findings are calculated "
        "from the available monthly and annual records."
    )

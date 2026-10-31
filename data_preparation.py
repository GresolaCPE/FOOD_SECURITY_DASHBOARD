
import pandas as pd

# File paths
PANEL_PATH = "data/food_security_panel.csv"
INDICATORS_PATH = "data/food_security_indicators.csv"


def load_datasets():
    """Load both food security datasets."""

    panel_df = pd.read_csv(PANEL_PATH)
    indicators_df = pd.read_csv(INDICATORS_PATH)

    # Convert date column into proper datetime format
    panel_df["date"] = pd.to_datetime(panel_df["date"])

    # Sort records by date and year
    panel_df = panel_df.sort_values("date")
    indicators_df = indicators_df.sort_values("year")

    return panel_df, indicators_df


def prepare_yearly_monthly_data(panel_df):
    """
    Calculate yearly averages from monthly price
    and food price index data.
    """

    monthly_columns = [
        "soybean_oil_usd_mt",
        "maize_usd_mt",
        "wheat_usd_mt",
        "dap_fertiliser_usd_mt",
        "mop_potash_usd_mt",
        "fertiliser_composite_idx",
        "ffpi_overall",
        "ffpi_cereals",
        "ffpi_volatility_12m"
    ]

    yearly_df = (
        panel_df.groupby("year")[monthly_columns]
        .mean()
        .reset_index()
    )

    return yearly_df


def inspect_dataset(df, name):
    """Display basic information about a dataset."""

    print("\n" + "=" * 50)
    print(f"DATASET: {name}")
    print("=" * 50)

    print("\nDataset Shape:")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn Information:")
    df.info()

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst Five Records:")
    print(df.head())


if __name__ == "__main__":

    panel_df, indicators_df = load_datasets()

    # Prepare yearly averages from monthly data
    yearly_df = prepare_yearly_monthly_data(panel_df)

    inspect_dataset(panel_df, "Monthly Food Security Panel")
    inspect_dataset(indicators_df, "Annual Food Security Indicators")

    print("\n" + "=" * 50)
    print("YEARLY SUMMARY FROM MONTHLY DATA")
    print("=" * 50)

    print(yearly_df.head())
    print("\nYearly Summary Shape:", yearly_df.shape)


# TEMPORARY DATA ACCURACY CHECK

if __name__ == "__main__":

    panel_df, indicators_df = load_datasets()
    yearly_df = prepare_yearly_monthly_data(panel_df)

    findings_df = pd.merge(
        yearly_df,
        indicators_df,
        on="year",
        how="inner"
    )

    print("\n========== DATA ACCURACY CHECK ==========")

    print("\n1. Highest Food Price Index:")
    print(
        yearly_df.loc[
            yearly_df["ffpi_overall"].idxmax(),
            ["year", "ffpi_overall"]
        ]
    )

    print("\n2. Fertilizer vs. Food Price Correlation:")
    print(
        yearly_df[
            ["fertiliser_composite_idx", "ffpi_overall"]
        ].corr()
    )

    print("\n3. Food Price vs. Undernourishment:")
    print(
        findings_df[
            ["ffpi_overall", "undernourishment_pct"]
        ].corr()
    )

    print("\n4. Production vs. Undernourishment:")
    print(
        findings_df[
            ["food_production_index", "undernourishment_pct"]
        ].corr()
    )

    print("\n5. Cereal Yield vs. Undernourishment:")
    print(
        findings_df[
            ["cereal_yield_kg_ha", "undernourishment_pct"]
        ].corr()
    )

    print("\n6. Arable Land vs. Undernourishment:")
    print(
        findings_df[
            ["arable_land_pct", "undernourishment_pct"]
        ].corr()
    )

    print("\n7. Missing Values:")
    print(findings_df.isnull().sum())

    print("\n=========================================")


# YEAR-TO-YEAR CHANGE CORRELATION CHECK

if __name__ == "__main__":

    panel_df, indicators_df = load_datasets()
    yearly_df = prepare_yearly_monthly_data(panel_df)

    findings_df = pd.merge(
        yearly_df,
        indicators_df,
        on="year",
        how="inner"
    ).sort_values("year").reset_index(drop=True)

    # Select variables for comparison
    change_columns = [
        "fertiliser_composite_idx",
        "ffpi_overall",
        "undernourishment_pct",
        "food_production_index",
        "cereal_yield_kg_ha",
        "arable_land_pct"
    ]

    # Calculate year-to-year changes
    change_df = findings_df[["year"] + change_columns].copy()

    change_df[change_columns] = change_df[change_columns].diff()

    # Exclude differences across gaps in the year sequence
    consecutive_years = findings_df["year"].diff() == 1

    change_df.loc[~consecutive_years, change_columns] = float("nan")

    # Display correlations
    change_relationships = [
        (
            "Fertilizer Change vs. Food Price Change",
            "fertiliser_composite_idx",
            "ffpi_overall"
        ),
        (
            "Food Price Change vs. Undernourishment Change",
            "ffpi_overall",
            "undernourishment_pct"
        ),
        (
            "Production Change vs. Undernourishment Change",
            "food_production_index",
            "undernourishment_pct"
        ),
        (
            "Cereal Yield Change vs. Undernourishment Change",
            "cereal_yield_kg_ha",
            "undernourishment_pct"
        ),
        (
            "Arable Land Change vs. Undernourishment Change",
            "arable_land_pct",
            "undernourishment_pct"
        )
    ]

    print("\n========== YEAR-TO-YEAR CORRELATIONS ==========")

    for title, x_col, y_col in change_relationships:

        valid_data = change_df[[x_col, y_col]].dropna()

        print(f"\n{title}")

        if len(valid_data) >= 2:

            correlation = valid_data[x_col].corr(valid_data[y_col])

            print(f"Correlation: {correlation:.4f}")
            print(f"Valid observations: {len(valid_data)}")

        else:
            print("Not enough valid observations.")

    print("\n===============================================")

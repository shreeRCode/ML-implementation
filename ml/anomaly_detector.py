import pandas as pd


def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:

    # Use zscore from P1 (correct approach)
    df["zscore"] = df["zscore_base"]

    # Detect anomalies using threshold (both high and low deviations)
    df["is_anomaly"] = df["zscore"].abs() > 1

    # Placeholder for ML score
    df["isolation_score"] = -df["zscore"]

    # Combined score (placeholder logic for now)
    df["combined_score"] = (
        0.5 * df["zscore"] +
        0.5 * df["isolation_score"]
    )

    # Return required schema
    return df[
        [
            "log_id",
            "isolation_score",
            "zscore",
            "combined_score",
            "is_anomaly"
        ]
    ]
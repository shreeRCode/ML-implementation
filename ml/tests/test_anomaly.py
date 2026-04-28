import pandas as pd
from ml.anomaly_detector import detect_anomalies

def test_dummy_pipeline():
    data = {
        "log_id": ["L1", "L2", "L3", "L4", "L5"],
        "session_id": ["S1", "S1", "S1", "S2", "S2"],
        "frequency_score": [0.9, 0.2, 0.8, 0.1, 2.0],
        "burstiness_score": [0.7, 0.1, 0.6, 0.2, 0.9],
        "zscore_base": [1.5, -0.5, 1.2, -1.0, 2.0],
        "time_delta_prev": [2, 50, 5, 100, 1],
        "severity_weight": [1.0, 0.4, 0.8, 0.2, 1.0],
        "counter_proximity": [1, 0, 1, 0, 1]
    }

    df = pd.DataFrame(data)

    result = detect_anomalies(df)

    print("INPUT:")
    print(df)
    print("\nOUTPUT:")
    print(result)


if __name__ == "__main__":
    test_dummy_pipeline()
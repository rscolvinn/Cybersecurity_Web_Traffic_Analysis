2. **Run the Scripts**:
- Preprocess the data:
  ```
  python scripts/data_preprocessing.py
  ```
- Perform analysis:
  ```
  python scripts/analysis.py
  ```
- Detect anomalies (Upcoming):
  ```
  python scripts/anomaly_detection.py
  ```

## Dataset
The dataset includes:
- **`bytes_in`**: Bytes received by the server.
- **`bytes_out`**: Bytes sent from the server.
- **`src_ip`**: Source IP address.
- **`detection_types`**: Type of detection applied.
- **Additional Metadata**: Information such as `protocol`, `timestamps`, and `country code`.

## Goals
- **Detect Anomalies**: Identify unusual patterns in web traffic.
- **Visualize Trends**: Highlight suspicious activity through data visualizations.
- **Classify Traffic**: Differentiate between normal and suspicious traffic.

## Results
Findings and visualizations are stored in the **`images/`** folder, including:
- Distribution of `bytes_in`.
- Relationship between `bytes_in` and `bytes_out`.
- Count of detection types.

## Next Steps
- Implement anomaly detection in `anomaly_detection.py`.
- Enhance visualizations with interactivity.
- Conduct further classification of suspicious traffic using machine learning techniques.

## About
This project demonstrates practical data analysis and cybersecurity skills, integrating Python, Pandas, and Matplotlib/Seaborn to extract insights from suspicious web traffic data.


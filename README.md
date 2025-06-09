# Weather Data Analysis Project

This project demonstrates analysis of weather-related data using Hadoop MapReduce and Apache Spark. It includes Python scripts for processing wind and visibility data, as well as instructions and outputs documented in the final project report. This project was done as a part of Big Data course at CSUEB. 

---

## Project Files

- `MedianWind.py`  
  Python MapReduce script to calculate median wind speed using Hadoop streaming.

- `MRStationVisibility.py`  
  Python MapReduce script to analyze station visibility data on Hadoop.

- `Range.py`  
  Python script to compute range values using Apache Spark (runs locally).

- `je7800_Final_Project.pdf`  
  Final project report describing project setup, commands run, and output results.

---

## Usage Instructions

### Running MapReduce Jobs on Hadoop

1. Create input directory in HDFS:
   ```bash
   hdfs dfs -mkdir /home/13student13/input_Project
   ```

2. Copy project data to HDFS:
   ```bash
   hdfs dfs -copyFromLocal Project_Data /home/13student13/input_Project
   ```

3. Run MapReduce job (example with MedianWind.py):
   ```bash
   python MedianWind.py -r hadoop hdfs:///home/13student13/input_Project/Project_Data --output-dir=hdfs:///home/13student13/output_ProjectPart13
   ```

4. View output:
   ```bash
   hdfs dfs -cat /home/13student13/output_ProjectPart13/part-00000
   ```

### Running Spark Job Locally

Use `spark-submit` to run the `Range.py` script locally:

```bash
spark-submit --master local Range.py
```

---

## Data Processing and Analysis

- The MapReduce scripts process large weather datasets stored on HDFS.
- The visibility data output is saved and loaded for further analysis in Pig and Hive (commands included in the project report).
- Apache Pig scripts filter and group visibility data.
- Hive is used to create tables and compute aggregated statistics on visibility.

---

## Contact / Questions

For any questions or issues with this project, please contact me at osheengupta1994@gmail.com



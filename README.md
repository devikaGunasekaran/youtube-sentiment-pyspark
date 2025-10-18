# youtube-sentiment-pyspark

A PySpark-based sentiment and hate speech analysis system for YouTube comments. Collects data using the YouTube Data API and implements ML Pipeline.

## 🧠 Project Overview

This project focuses on:  
- Collecting and analyzing YouTube comments using Google’s YouTube API.  
- Cleaning text (removing emojis, punctuation, and noise).  
- Applying **TF-IDF vectorization** and **Random Forest** in a PySpark ML pipeline.  
- Handling **class imbalance** using **class weights**.  
- Supporting **scalable and distributed data processing** using Apache Spark.

## 📊 Dataset

This project uses the **Davidson Hate Speech and Offensive Language Dataset**, which contains around **24,000 labeled tweets** categorized as:
- **0 → Hate Speech**
- **1 → Offensive Language**
- **2 → Neither (Neutral)**

## 🏗️ Technologies Used  

| Technology | Purpose |
|-------------|----------|
| **Apache Spark (PySpark)** | Distributed data processing and ML pipeline creation |
| **YouTube Data API v3** | Collecting YouTube comments dynamically |
| **Python** | Core programming language for data processing and analysis |
| **Pandas** | Data manipulation and exploration |
| **NLTK** | Natural language text preprocessing (tokenization, stopword removal, etc.) |
| **Scikit-learn** | Model evaluation and metric computation |

## 📸 Sneak Peak
<img width="1920" height="1008" alt="Screenshot 2025-10-18 072003" src="https://github.com/user-attachments/assets/2a3a2173-3a13-46c5-9111-466a90f4ebfc" />

<img width="1920" height="901" alt="Screenshot 2025-10-18 072439" src="https://github.com/user-attachments/assets/26ff1c18-8f28-4a6c-8424-fe77d645aef2" />



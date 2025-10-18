# 🎥 YouTube Sentiment Analysis using PySpark  

A **PySpark-based sentiment and hate speech analysis system** for YouTube comments.  
Collects data using the **YouTube Data API** and **web scraping**, and implements a complete **ML Pipeline** for scalable analysis.


## 🧠 Project Overview  

This project focuses on:  
- Collecting and analyzing YouTube comments using **Google’s YouTube API** and **web scraping**.  
- Cleaning and preprocessing text (removing emojis, punctuation, and noise).  
- Applying **TF-IDF vectorization** and **Random Forest** in a PySpark ML pipeline.  
- Handling **class imbalance** using **class weights**.  
- Supporting **scalable and distributed data processing** using **Apache Spark**.  


## 🌐 Web Scraping  

Alongside the YouTube Data API, we implemented **web scraping** techniques to gather additional comments and metadata from YouTube videos where API access was limited.  

This involved:  
- Using **BeautifulSoup** and **Selenium** for scraping comments dynamically.  
- Extracting video titles, comment text, timestamps, and like counts.  
- Cleaning and structuring scraped data for analysis in Spark.  

This dual data collection approach (API + Scraping) ensured **richer, more diverse datasets** for accurate sentiment and hate speech classification.


## 📊 Dataset  

We utilized the **Davidson Hate Speech and Offensive Language Dataset**, containing approximately **24,000 labeled tweets**, categorized as:  
- **0 → Hate Speech**  
- **1 → Offensive Language**  
- **2 → Neither (Neutral)**  

## 🏗️ Technologies Used  

| Technology | Purpose |
|-------------|----------|
| **Apache Spark (PySpark)** | Distributed data processing and ML pipeline creation |
| **YouTube Data API v3** | Collecting YouTube comments dynamically |
| **Web Scraping (BeautifulSoup, Selenium)** | Extracting comments and metadata beyond API limits |
| **Python** | Core programming language for data processing and analysis |
| **Pandas** | Data manipulation and exploration |
| **NLTK** | Natural language text preprocessing (tokenization, stopword removal, etc.) |
| **Scikit-learn** | Model evaluation and metric computation |


## 📸 Sneak Peek  

<img width="1920" height="1008" alt="Screenshot 2025-10-18 072003" src="https://github.com/user-attachments/assets/2a3a2173-3a13-46c5-9111-466a90f4ebfc" />

<img width="1920" height="901" alt="Screenshot 2025-10-18 072439" src="https://github.com/user-attachments/assets/26ff1c18-8f28-4a6c-8424-fe77d645aef2" />


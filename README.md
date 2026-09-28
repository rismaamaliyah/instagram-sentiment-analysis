# Instagram User Sentiment Analysis: An NLP Approach using Machine Learning

## Project Overview
This project aims to analyze user opinions toward the Instagram mobile application using Natural Language Processing (NLP) and machine learning techniques. More than 10k user reviews were independently collected from Google Play Store and transformed into a structured dataset for sentiment classification.

The project focuses on identifying whether user reviews express positive, neutral, or negative sentiment. Multiple preprocessing techniques, feature extraction methods, and machine learning algorithms were evaluated to determine the most effective approach for sentiment classification.

## Problem Statement
Instagram is one of the most widely used social media platforms, generating thousands of user reviews regarding application performance, features, usability, and user experience.

However, manually analyzing large volumes of user feedback is time-consuming and inefficient.

**How can machine learning and NLP techniques be used to automatically classify Instagram user reviews into positive, neutral, and negative sentiment categories?**

## Objectives

### Main Objectives
Develop a sentiment analysis model capable of automatically classifying Instagram app review into three sentiment categories.

### Specific Objectives
- Collect user reviews from Google Play Store through independent data scraping.
- Perform text preprocessing and normalization on user-generation content.
- Generate sentiment labels based on user ratings.
- Compare multiple machine learning and feature engineering approaches.
- Evaluate model performance using classification metrics and cross-validation.
- Produce an inference system capable of predicting sentiment for new reviews.

## Dataset / Data Source

### Source
Google Play Store

### Application
Instagram

### Collection Method
Independent web scraping using `Python` and the `google-play-scraper` library.

### Dataset Characteristics
- More than 10k user reviews
- Indonesian-language reviews
- Review text (content)
- Rating scores (1-5 stars)
- Automatically labeled into:
  - Negative (-1)
  - Neutral (0)
  - Positive (1)

## Tools & Technologies

### Programming Language
- Python

### Data Collection
- Google Plat Store

### Data Processing
- Pandas
- NumPy

### NLP
- NLTK
- Sastrawi
- LangDetect

### Feature Extraction
- TF-IDF Vectorizer
- Word2Vec (Gensim)

### Machine Learning
- Linear SVM
- Random Forest

### Evaluation & Visualization
- Scikit-Learn
- Matplotlib
- Seaborn

### Development Environment
- Jupyter Notebook

## Methodology / Process

### 1. Data Collection
- Scraped Instagram reviews from Google Play Store.
- Collected over 10k user reviews.

### 2. Data Preparation
- Removed numbers, punctuation, and special characters.
- Converted text into lowercase.
- Tokenized review text.
- Removed stopwords.
- Applied Indonesian stemming using Sastrawi.
- Performed slang and text normalization.

### 3. Sentiment Labeling
Rating scores were transformed into sentiment classes:
| Rating | Sentiment |
| ------ | --------- |
| 1- 2 | Negative |
| 3 | Neutral |
| 4-5 | Positive |

### 4. Feature Extraction
Two feature engineering approaches were evaluated:
- TF-IDF
- Word2Vec Embedding

### 5. Model Development

#### Experiment 1
- SVM
- TF-IDF
- Train/test Split 80:20

#### Experiment 2
- Random Forest
- Word2Vec
- Train/test Split 70:30

#### #xperiment 3
- Random Forest
- TF-IDF
- Train/Test Split 70:30

### 6. Model Evaluation
Performance was evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- Cross Validation
- Confusion Matrix

### 7. Inference Testing
Performed sentiment prediction on unseen review samples to validate model usability.

## Key Findings / Insights

### Technical Findings
- TF-IDF combined with SVM achieved excellent classification performance.
- Word2Vec embedding also produced strong results when combines with Random Forest.
- All experimental models exceeded the minimum performance requirement of 85%.
- Cross-validation scores demonstrated stable model performance across multiple folds.
- The models successfully classified user reviews into three sentiment categories with high consistency.

### Business Insights
- User reviews contain valuable information regarding application performance, features, and user satisfaction.
- Sentiment analysis can help organizations automatically monitor user feedback at scale.
- Automated sentiment classification enables faster identification of recruiting complaints and highly appreciated features.
- NLP-based review analysis can support data-driven product improvement and user experience optimization.

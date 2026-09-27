# TrendMutation — Multilingual Trend & Sentiment Analytics

TrendMutation is a multilingual analytics dashboard that explores topics, sentiment, emotions, keywords, and language patterns from a large-scale social media dataset.

The project uses Python and Streamlit to transform raw multilingual text data into interactive visual insights.

## Problem Statement

Large volumes of multilingual social media data contain valuable information about what people are discussing and how they are reacting.

However, analyzing this data manually is difficult because:

- The dataset contains hundreds of thousands of records.
- Multiple languages are present.
- Different topics have different sentiment patterns.
- Emotions and frequently used keywords can reveal additional context.

TrendMutation aims to organize this information into an easy-to-understand analytical dashboard.

## Objectives

- Analyze topic popularity across a large multilingual dataset.
- Study sentiment patterns across different topics.
- Identify dominant emotions.
- Extract important keywords for each topic.
- Analyze the distribution of languages.
- Present the results through an interactive Streamlit dashboard.
- Provide a foundation for multilingual trend and sentiment analysis.

## Key Features

### 📊 Topic Analysis
Identifies the most frequently discussed topics and compares their mention counts.

### 😊 Sentiment Analysis
Classifies records into:

- Positive
- Negative
- Neutral

The dashboard also compares average sentiment across topics.

### 💭 Emotion Analysis
Analyzes the dominant emotions present in the dataset, including emotions such as:

- Neutral
- Admiration
- Curiosity
- Approval
- Annoyance
- Gratitude
- Joy
- Love
- Disapproval
- Confusion

### 🔑 Keyword Analysis
Extracts frequently occurring keywords for each major topic.

### 🌍 Multilingual Analysis
Analyzes content across multiple languages and displays language distribution.

### 🔎 Topic Explorer
Allows users to explore individual topics using:

- Mentions
- Average sentiment
- Top emotion
- Keywords

## Dataset

The project uses a large multilingual social media dataset containing approximately **456,000 cleaned records** across **116 languages**.

The available fields include information related to:

- Date
- Original text
- Language
- Primary topic
- Keywords
- Sentiment
- Main emotion
- Secondary themes

The current dataset represents a snapshot from **14 November 2024**, so the dashboard should be interpreted as snapshot-based analytics rather than a historical time-series analysis.

The raw Parquet dataset is kept locally and is excluded from GitHub using `.gitignore` because of its large file size.

## Technologies Used

- Python
- Pandas
- Streamlit
- PyArrow
- Git
- GitHub
- Parquet
- CSV

## Project Workflow

```text
Raw Multilingual Dataset
          ↓
Data Cleaning
          ↓
Topic Analysis
          ↓
Sentiment Analysis
          ↓
Emotion Analysis
          ↓
Keyword Extraction
          ↓
Language Analysis
          ↓
Summary CSV Files
          ↓
Streamlit Dashboard

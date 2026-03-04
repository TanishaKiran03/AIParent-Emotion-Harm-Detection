# AIParent – Emotion & Harm Detection System

## Overview
AIParent is an NLP-based safety system that analyzes user text to detect emotional tone and harmful or toxic content.

The system combines two transformer models:
1. Emotion detection using a pretrained GoEmotions DistilBERT model
2. Harmful content detection using a fine-tuned DistilBERT toxicity classifier

---

## Features
- Emotion classification with top emotion scores
- Toxic / harmful comment detection
- Transformer-based NLP pipeline
- Model training using HuggingFace Trainer
- Evaluation using accuracy, precision, recall, and F1-score

---

## Tech Stack
Python  
PyTorch  
HuggingFace Transformers  
Scikit-learn  
Pandas  
Google Colab

---

## Models Used
- `joeddav/distilbert-base-uncased-go-emotions-student`
- `distilbert-base-uncased` (fine-tuned for toxicity detection)

---

## Project Structure
AIParent-Emotion-Harm-Detection
│
├── emotion_detection_model.ipynb
├── harm_detection_model.ipynb
├── models/
│   ├── emotion_model.zip
│   └── harm_detection_model.zip
└── README.md

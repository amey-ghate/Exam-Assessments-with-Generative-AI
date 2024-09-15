# Exam Assessments with Generative AI

## Overview
This project leverages Generative AI using **Llama 3.1**, **Ollama**, and **LangChain** to tackle a real-world problem: **Consistent Answer Checking for Open-Ended Questions** in exams. By integrating **Streamlit** for an intuitive user interface, the project allows users to compare student answers with model answers, ensuring consistency and fairness in grading. The solution mimics a human teacher’s evaluation process while eliminating bias, providing feedback on both the content and language of the student’s answer.

## Problem Statement
In educational settings, consistency in grading is crucial. While a single teacher can maintain uniformity, variations arise when multiple assessors evaluate the same answers, particularly in competitive exams. This inconsistency can lead to unfair outcomes, even with predefined model answers and grading rubrics. Our system aims to address this challenge by automating the evaluation of open-ended answers with the help of large language models (LLMs).

## Solution
This system combines the capabilities of **Llama 3.1**, **Ollama**, **LangChain**, and **Streamlit** to:
- **Evaluate content**: It compares the student’s answer with a model answer, ensuring that key points are articulated correctly.
- **Assess language**: It analyzes the language and grammar of the student's answer, offering suggestions for improvement.
- **Calculate scores**: The system assigns a score based on the coverage of content and the language quality, ensuring fairness and consistency.
- **Provide feedback**: It highlights areas for improvement, both in terms of content and language, helping students learn and improve.

## Features
- **Content Evaluation**: The system identifies key points in the student’s answer that match the model answer and highlights areas for improvement.
- **Language Assessment**: It assesses the language consistency and grammar of the student’s answer, identifying strong constructs and areas that need refinement.
- **Customizable Scoring**: Scores are generated based on customizable weightings for content and language, providing flexibility in grading.
- **Privacy-First Approach**: The entire solution runs locally using **Ollama**, ensuring privacy and security for exam content.
- **Real-Time Feedback**: Using **Streamlit**, the system provides real-time feedback and scoring for exam assessors.

## How It Works
1. **Input**: Users input the model answer, student answer, subject, student’s grade level, and total marks.
2. **Processing**:
   - The system compares the student’s answer with the model answer, highlighting accurate points and suggesting improvements.
   - It assesses the language quality, offering additional insights into grammatical constructs and improvements.
3. **Output**: The system outputs the evaluation, highlighting the score and providing constructive feedback for both content and language.
4. **Score Calculation**: The final marks are calculated by combining the scores for content (80%) and language (20%), ensuring a balanced assessment.

## Setup Instructions

### Prerequisites
- Python 3.7+
- Install the required libraries using `pip`:
  ```bash
  pip install streamlit langchain ollama pydantic

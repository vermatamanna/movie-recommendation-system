# Movie Recommendation System

## Project Overview
This project is a simple Movie Recommendation System built using Python and Machine Learning concepts. It recommends movies based on genre similarity using CountVectorizer and Cosine Similarity.

## Objective
The objective of this project is to recommend similar movies based on genre information using Machine Learning techniques such as CountVectorizer and Cosine Similarity.

## Features
- Movie recommendation based on genres
- Text vectorization using CountVectorizer
- Similarity calculation using Cosine Similarity
- Fast and simple recommendation engine
- Easy to understand implementation

## Technologies Used
- Python
- Pandas
- Scikit-learn

## Skills Demonstrated

- Python Programming
- Data Processing with Pandas
- Feature Extraction using CountVectorizer
- Similarity Measurement using Cosine Similarity
- Basic Recommendation Systems
- GitHub Project Documentation

## Dataset
A small dataset containing movie titles and their genres is used for generating recommendations.

### Sample Movies
- Avengers
- Iron Man
- Batman
- Superman
- Doctor Strange

## Algorithm Used

### CountVectorizer
Converts movie genres into numerical vectors that can be processed by machine learning algorithms.

### Cosine Similarity
Measures the similarity between movie genre vectors and recommends the most similar movies.

## Project Workflow
1. Create movie dataset
2. Convert genres into numerical vectors
3. Calculate cosine similarity matrix
4. Select a movie
5. Find similar movies
6. Display recommendations

## Requirements
pandas
scikit-learn

## Repository structure
movie-recommendation-system/
│
├── .gitignore
├── movie_recommender.py
└── README.md

## Installation

```bash
pip install pandas scikit-learn
```

## Run the Project

```bash
python movie_recommender.py
```

## Sample Output

```text
Recommendations for Avengers:

Iron Man
Doctor Strange
Batman
```

## output 
<img width="366" height="97" alt="image" src="https://github.com/user-attachments/assets/7efc528c-88b8-4180-a34c-ac3b26344d34" />


## Future Improvements
- Add larger movie datasets
- Include movie ratings
- Add movie descriptions and cast information
- Build a graphical user interface
- Deploy as a web application

## Conclusion
This project demonstrates how recommendation systems work using Machine Learning techniques. By using CountVectorizer and Cosine Similarity, the system recommends movies that are most similar to the selected movie based on genre information.

## Author
Tamanna Verma

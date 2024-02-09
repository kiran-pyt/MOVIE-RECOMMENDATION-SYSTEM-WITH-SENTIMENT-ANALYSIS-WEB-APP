# MOVIE-RECOMMENDATION-SYSTEM-WITH-SENTIMENT-ANALYSIS-WEB-APP

![image](https://github.com/kiran-pyt/MOVIE-RECOMMENDATION-SYSTEM-WITH-SENTIMENT-ANALYSIS-WEB-APP/assets/120393460/fa72890e-2649-44e5-a877-79061441d24d)Certainly! Here's a description you can use for your GitHub project:

---

## Movie Recommender System with Sentiment Analysis

This project combines the power of machine learning and web scraping to create a comprehensive movie recommendation system with sentiment analysis of user reviews. The system is built using Python and leverages popular libraries such as Streamlit for the user interface, BeautifulSoup for web scraping IMDb reviews, and scikit-learn for sentiment analysis.

### Key Features:

1. **Movie Recommendation:** Users can select a movie from a dropdown list of available titles. The system then suggests five similar movies based on content similarity.

2. **Sentiment Analysis:** The system scrapes user reviews of the selected movie from IMDb and performs sentiment analysis on them. Each review is classified as either "Good" or "Bad" based on the sentiment.

3. **Interactive Interface:** The interface allows users to view the recommended movies along with their posters. Users can also explore the sentiment analysis results of IMDb reviews.

### How it Works:

- **Movie Recommendation:** The system uses a collaborative filtering technique to recommend similar movies. It calculates the similarity between movies based on their features and suggests the most similar ones.

- **Sentiment Analysis:** IMDb reviews are scraped using BeautifulSoup, and each review is passed through a pre-trained machine learning model for sentiment analysis. The model predicts whether the review is positive or negative.

### Technologies Used:

- **Python:** The primary programming language used for development.
- **Streamlit:** For building the interactive web application.
- **BeautifulSoup:** For web scraping IMDb reviews.
- **scikit-learn:** For sentiment analysis using machine learning models.
- **pickle:** For loading pre-trained models and data.

### How to Use:

1. Clone the repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Run the Streamlit application using the command `streamlit run app.py`.
4. Select a movie from the dropdown list to see recommendations and sentiment analysis results.

### Future Improvements:

- **Enhanced UI:** Improve the user interface for a more engaging experience.
- **Real-time Updates:** Implement real-time updating of recommendations and sentiment analysis results.
- **Additional Features:** Add features such as user authentication, personalized recommendations, and more.

### Contributing:

Contributions are welcome! Feel free to open issues for bug fixes or feature requests. Pull requests are also encouraged for enhancements to the project.









#  News Classifier (AG News Dataset)

A production-ready **Machine Learning web application** that classifies news articles into categories such as **World, Sports, Business, and Technology** using Natural Language Processing (NLP).

Built with **Scikit-learn** and deployed using **Streamlit**, this project demonstrates a complete end-to-end ML pipeline from data preprocessing to model deployment.

---

##  Features

*  Real-world dataset (AG News)
*  Machine Learning model (Naive Bayes)
*  Text preprocessing & cleaning pipeline
*  TF-IDF vectorization
*  Interactive web UI using Streamlit
*  Real-time news classification
*  Confidence score for predictions
*  One-click execution with `run.bat`

---

##  Project Structure

```

news-classifier/
│
├── data/
│   └── news.csv
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   └── predict.py
├── images/
│   └── homepage.png
├── app.py
└── requirements.txt
```

---

##  Dataset

This project uses the **AG News Dataset**, which contains thousands of labeled news articles across four categories:

* World
* Sports
* Business
* Sci/Tech

### Dataset Format:

```
class_index, title, description
```

The model combines `title` and `description` into a single text feature for training.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit-Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

---
##  Installation

### 1. Clone the repository

```
git clone https://github.com/hassan-ali786/news-classifier.git
cd news-classifier
```

### 2. Add dataset

* Download AG News dataset
* Rename `train.csv` → `news.csv`
* Place inside:

```
data/news.csv
```

---

##  Run the Application

### Manual run

```
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python src/train_model.py
streamlit run app.py
```

---

##  Model Details

* **Algorithm:** Multinomial Naive Bayes
* **Vectorizer:** TF-IDF (max_features=5000)
* **Text Processing:** Lowercasing, regex cleaning
* **Input:** News article text
* **Output:** Category + Confidence Score

---

##  Application UI

* Enter any news article
* Click **"Classify News"**
* Get:

  * Predicted Category
  * Confidence Score

---

##  Requirements

* Python 3.8+
* Streamlit
* Pandas
* Scikit-learn

Install all dependencies:

```
pip install -r requirements.txt
```

---

##  Future Improvements

* Add accuracy & evaluation metrics
* Use advanced models (Logistic Regression, SVM, BERT)
* Deploy on Streamlit Cloud / AWS
* Add multi-language support
* Improve UI/UX

---

##  Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

##  License

This project is open-source and available under the MIT License.

---

##  Author

**Hassan Ali**
Data Scientist & ML Engineer


---

##  Application Screenshot

![Home Page](https://raw.githubusercontent.com/hassan-ali786/news-classifier/main/images/homepage.png)

---

 If you like this project, consider giving it a star on GitHub!

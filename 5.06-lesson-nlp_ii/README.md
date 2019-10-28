# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Natural Language Processing II

---

## Materials We Provide


| Topic | Description | Link |
| --- | --- | --- |
| Lesson | NLP II Notebook | [Link](./introduction-to-nlp.ipynb)|

> **Dataset description:** SMS spam/ham messages

---

## Learning Objectives

*After this lesson, students will be able to:*
1. **Define** and **implement** `CountVectorizer` and `TfidfVectorizer`.
2. **Understand** some of the parameters that can be tuned in a `CountVectorizer`.
3. **Model** an NLP dataset using `CountVectorizer` and `LogisticRegression` in a `Pipeline`.
4. **Tune** the `Pipeline` using `GridSearchCV`


---

## Student Requirements

*Before this lesson(s), students should already be able to:*

1. Construct linear and logistic regression models.
2. Understand the basics of tokenizing, stemming and lemmatization

---

## Lesson Outline

> **Total Time: 90 mins**

I. **Count Vectorization** (30 minutes total)
- Evaluate feature matrix
- Explore various parameters

II. **NLP Model** (60 minutes total)
- Prep a dataset for modeling
- Create a `Pipeline` using `CountVectorizer` and `LogisticRegression`
- Tune the `Pipeline` using `GridSearchCV`

III. **TF-IDF**
- Compare/Contrast TF-IDF vs Count Vectorization
- Explore the TF-IDF algorithm
- Run an instance of `TfidfVectorizer`

---

## Additional Resources

- Check out this [Yelp blog post](http://engineeringblog.yelp.com/2015/09/automatically-categorizing-yelp-businesses.html) on how it completed a classification task (with more than 1,000 response variables) using restaurant review text.
- Always check documentation: 
    - [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html). 
    - [HashingVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html). 
    - [TF-IDF](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html).
- A list of all stop words is available [here](https://github.com/ga-students/DSI-DC-2/blob/master/curriculum/Week-05/5.04-nlp/stop-words.txt).
- Wikipedia's [feature hashing](https://github.com/generalassembly-studio/DSI-course-materials/tree/master/curriculum/04-lessons/week-06/4.1-lesson) and [hash functions](https://en.wikipedia.org/wiki/Hash_function) entries are a great place to turn for more information on hashing.
- Check out Charlie Greenbacker's [introduction to NLP](http://spark-public.s3.amazonaws.com/nlp/slides/intro.pdf), which he delivered at the [DC-NLP Meetup](http://www.meetup.com/DC-NLP/).
- Wikipedia also has a [walk through](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) of TF-IDF.
- We played with Google's [ngram tool](https://books.google.com/ngrams/graph?content=data+science&year_start=1800&year_end=2000&corpus=15&smoothing=3&share=&direct_url=t1%3B%2Cdata%20science%3B%2Cc0).
- A hilarious data scientist has gone rogue and used NLP and eigenfaces (eigenvalues for face recognition) [for Tinder](http://dataconomy.com/hacking-tinder-with-facial-recognition-nlp/).
- We referenced KPCB's 2016 internet trends. If you're into startups, check out [this insightful deck](http://www.kpcb.com/internet-trends).
- [Count vectorizer documentation](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html).
- [Choosing a stemmer](https://www.elastic.co/guide/en/elasticsearch/guide/current/choosing-a-stemmer.html).
- [Feature hashing](https://en.wikipedia.org/wiki/Feature_hashing).
- [Term frequency-inverse document frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).
- [TF-IDF vectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html).

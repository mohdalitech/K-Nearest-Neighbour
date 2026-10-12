# K-Nearest Neighbors (KNN) Web App

A lightweight, interactive **K-Nearest Neighbors (KNN)** classification web application built with **Python**, **Streamlit**, and **MySQL**.
It calculates Euclidean distances from a user-defined input (Height and Weight) to historical records stored in a database, performs a $k$-nearest neighbor search, 
and outputs a classification prediction (e.g., Underweight, Normal, or Overweight).

---

## Features

* **Interactive Interface:** Built using Streamlit for easy user input and visualization.
* **Database Integration:** Connects seamlessly to a MySQL database using `mysql.connector` and configuration settings loaded via `tomllib`.
* **Dynamic Distance Calculation:** Computes Euclidean distance between user coordinates (`Height`, `Weight`) and dataset examples.
* **Majority Voting Mechanism:** Aggregates the top $k$ nearest neighbors to predict the final classification category.
* **Input Validation & Error Handling:** Validates range boundaries for $k$ (1 to 5) and manages non-numeric data entry exceptions.

---

## Prerequisites & Tech Stack

* **Python** (3.11+ recommended for built-in `tomllib`)
* **Streamlit**
* **MySQL Connector for Python**

---


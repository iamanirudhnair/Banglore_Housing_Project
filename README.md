# Bangalore Housing Price Prediction Project

## Overview
This project demonstrates the process of building a real estate price prediction website using machine learning, specifically linear regression. The model predicts the price of properties in Bangalore based on input features like square footage, number of bedrooms, etc. This project involves data cleaning, feature engineering, model training, hyperparameter tuning, and web deployment. The application uses Python, Flask for the backend, and HTML/CSS/JavaScript for the front end, and the project is hosted on AWS Cloud.

## Project Components
1. **Model Building with Scikit-Learn**: We built a machine learning model using linear regression to predict property prices. The dataset used is from Kaggle, containing data on home prices in Bangalore.
2. **Flask Server**: A Python Flask server was implemented to serve the trained model and handle HTTP requests from the front end.
3. **Web Application**: The front end was developed using HTML, CSS, and JavaScript, allowing users to input property details and receive a predicted price.
4. **Deployment on AWS**: The entire application, including the Flask server and the trained model, was deployed on AWS Cloud to make it accessible from anywhere.

## Techniques Used

- **Data Cleaning**: 
  - Removed unnecessary features and handled missing (NA) values in the dataset.
  - Applied normalization to property sizes, converting the range of values into an average of the min and max values.
  
- **Feature Engineering**: 
  - Converted the dataset into useful features, transforming categorical features and normalizing numerical features.
  - Used domain knowledge to select relevant features that impact property prices.
  
- **Outlier Detection and Removal**: 
  - Outliers were detected using statistical methods and were removed to ensure that the model is not influenced by extreme values.
  
- **Dimensionality Reduction**:
  - Techniques such as feature scaling and dimensionality reduction (if necessary) were applied to improve the model’s performance and speed.
  
- **Model Building**:
  - Used **Linear Regression** to predict housing prices based on selected features.
  - Applied **GridSearchCV** for hyperparameter tuning to improve model performance and ensure it generalizes well.
  
- **Model Evaluation**: 
  - Utilized **K-fold Cross Validation** to assess the stability and accuracy of the model.
  
- **Web Development**:
  - Built a simple UI with HTML/CSS/JavaScript that allows users to input property details (e.g., square footage, number of bedrooms).
  - The Flask server receives these inputs, processes them using the trained model, and returns a predicted property price to the user.
  
- **Deployment**:
  - Deployed the entire system to **AWS Cloud** to make the application accessible to users on the internet.

## Challenges Faced

1. **Handling Missing Data**:
   - Missing values in the dataset were challenging, as they could negatively impact model performance. We addressed this by imputing or removing missing values based on context.

2. **Feature Selection and Engineering**:
   - Identifying and creating the right features was a challenge. For example, property size ranged in intervals, so we had to calculate the average of the range (e.g., 2100-3250) to convert it into a usable feature.
   - We spent significant time in feature engineering to create a robust set of inputs for the model.

3. **Outlier Detection and Removal**:
   - Identifying outliers that were skewing the model's predictions was time-consuming. After detecting these outliers, they were carefully removed to ensure the model's accuracy.

4. **Hyperparameter Tuning**:
   - Tuning the hyperparameters of the linear regression model using **GridSearchCV** was a bit tricky and time-consuming, as it required experimenting with different parameters to improve model accuracy.

5. **Web Deployment**:
   - Deploying the model with a Flask server and ensuring smooth communication between the backend and the frontend was another challenge. However, we were able to overcome this by debugging step-by-step and using AWS for deployment.

6. **Model Optimization**:
   - Linear regression was a simple approach, but improving the model’s performance with feature engineering and hyperparameter tuning allowed us to get better predictions.

## Solutions to Challenges

1. **Handling Missing Data**: 
   - We imputed missing values using mean or median imputation and, in cases where data couldn’t be imputed reasonably, we removed the rows with missing data.

2. **Feature Engineering**: 
   - We worked on transforming and normalizing features, such as normalizing the property size by averaging the min and max values in the range. This helped the model handle the data better.

3. **Outlier Removal**: 
   - We used statistical methods to detect outliers and removed them using interquartile range (IQR) methods, ensuring the model wasn’t skewed.

4. **Hyperparameter Tuning**: 
   - We used **GridSearchCV** for automated hyperparameter tuning, experimenting with different regularization values to optimize the model for better performance.

5. **Web Deployment**: 
   - We used Flask’s built-in development server to integrate the trained model and the web UI. By deploying on AWS, we ensured the system was accessible globally.

## Technologies Used

- **Programming Languages**: Python, HTML, CSS, JavaScript
- **Data Science Libraries**: 
  - **Pandas** and **Numpy** for data cleaning and manipulation.
  - **Matplotlib** for data visualization.
  - **Scikit-Learn** for model building and machine learning techniques.
- **Development Tools**: 
  - **Jupyter Notebook** for data analysis and model building.
  - **VS Code** and **PyCharm** for development.
- **Backend Framework**: Python **Flask** for building the server to serve predictions.
- **Web Framework**: **HTML/CSS** for frontend development and **JavaScript** for interactivity.
- **Deployment**: **AWS Cloud** for deploying the model and web server.

## What I Learned

This project provided deep insights into various aspects of machine learning and web development. Some of the key lessons learned include:

- **End-to-end Data Science Workflow**: I learned how to clean and preprocess real-world data, select relevant features, train and evaluate a machine learning model, and deploy it as a web application.
- **Feature Engineering and Outlier Removal**: I gained experience in preprocessing and transforming data into a format suitable for machine learning models.
- **Flask and Web Development**: I learned how to integrate machine learning models into a live web application using Flask, which can serve predictions to end-users.
- **Cloud Deployment**: I gained experience deploying machine learning models to the cloud using AWS, making it accessible globally.
- **Model Optimization and Tuning**: I got hands-on experience tuning models and evaluating them to improve prediction accuracy.

## Conclusion

The Bangalore Housing Price Prediction project was a comprehensive and challenging exercise that provided hands-on experience with machine learning, web development, and cloud deployment. The project covers various aspects of the data science workflow, from cleaning the data to building and deploying a model, offering a practical approach to solving real-world problems.

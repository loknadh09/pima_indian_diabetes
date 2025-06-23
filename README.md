🩺 PIMA Indian Diabetes Prediction App
An interactive web application that predicts the probability of diabetes using a machine learning model trained on the PIMA Indian Diabetes dataset.

🚀 Features
🧠 Predicts diabetes probability using medical input data

📈 Trained with scikit-learn classification model

📊 Real-time prediction with a user-friendly interface

⚖️ Input features are scaled using a trained StandardScaler

🧪 Technologies Used
Python

Streamlit – web app framework

scikit-learn – ML model and preprocessing

pandas – data manipulation

joblib – model and scaler persistence

📂 Project Structure
bash
Copy
Edit
pima_indian_diabetes/
├── app.py               # Streamlit app
├── model.pkl            # Trained classification model
├── scaler.pkl           # StandardScaler for preprocessing
├── diabetes.csv         # Dataset used for training
├── Untitled1.ipynb      # Model training notebook
📊 Input Features
Pregnancies

Glucose

Blood Pressure

Skin Thickness

Insulin

BMI

Diabetes Pedigree Function

Age

💻 Run Locally
Clone the repository:

bash
Copy
Edit
git clone https://github.com/loknadh09/pima_indian_diabetes.git
cd pima_indian_diabetes
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Launch the app:

bash
Copy
Edit
streamlit run app.py
🧠 Example Inputs
Feature	Non-Diabetic	Diabetic
Pregnancies	1	6
Glucose	95	160
Blood Pressure	70	90
Skin Thickness	20	35
Insulin	85	180
BMI	24.5	36.0
Diabetes Pedigree Function	0.2	0.75
Age	25	50


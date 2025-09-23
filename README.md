# HealthInsight: Healthcare Analytics Platform

## Introduction
HealthInsight is a comprehensive healthcare analytics platform that combines machine learning with a user-friendly web interface to provide two key medical predictions:
1. Stroke Risk Assessment
2. Disease Diagnosis

The project implements the complete machine learning lifecycle—from data preprocessing to model deployment—creating reliable healthcare prediction systems accessible through an intuitive web interface.

## Features
- **Stroke Risk Prediction:** Assess stroke risk based on health parameters
- **Disease Diagnosis:** Predict possible diseases based on symptoms
- **Interactive Web Interface:** Easy-to-use Streamlit application
- **Pre-trained Models:** Ready-to-use machine learning models
- **Data Visualization:** Comprehensive health insights with visual representations

## Quick Start

### Prerequisites
- Python 3.12.4 or higher
- Virtual environment (recommended)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/Suvramoy/HealthInsight.git
cd HealthInsight
```

2. Create and activate virtual environment:
```bash
python -m venv env
# On Windows
.\env\Scripts\activate
# On Unix or MacOS
source env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
streamlit run Home.py
```
The application will open in your default web browser.

## Project Structure
```
HealthInsight/
├── data/                    # Dataset files
├── models/                  # Trained ML models
├── pages/                   # Streamlit page components
├── src/                     # Source code and notebooks
└── images/                  # Image assets
```

## Technical Details

### Problem Statements

#### 1. Stroke Risk Prediction
- **Goal:** Predict stroke likelihood based on health indicators
- **Features:** Age, hypertension, heart disease, BMI, glucose levels, etc.
- **Challenge:** Imbalanced dataset (only 5% stroke cases)

#### 2. Disease Diagnosis
- **Goal:** Predict possible diseases based on symptoms
- **Features:** Various medical symptoms and patient characteristics
- **Implementation:** Multi-class classification problem

### Data Processing & Model Development

#### Data Preprocessing
- Missing value handling using median imputation
- Outlier detection with 3-sigma rule
- Feature correlation analysis using Chi-squared test
- Categorical encoding with OneHotEncoder
- Numerical feature scaling with PowerTransformer and StandardScaler
- Class imbalance handling using SMOTE

#### Model Architecture
1. **Stroke Prediction Model:**
   - Algorithm: Random Forest Classifier
   - Performance: 92% accuracy, 0.90 F1-score
   - Optimized for recall to minimize false negatives

2. **Disease Prediction Model:**
   - Algorithm: Random Forest Classifier
   - Features: Symptom-based prediction
   - Comprehensive disease classification

### Web Application

#### Features
- Intuitive user interface
- Real-time predictions
- Health insights visualization
- Medical professional search integration

#### Implementation
- Built with Streamlit
- Modular code structure
- Separate pages for different functionalities
- Responsive design

## Model Performance

### Stroke Prediction Model
- Accuracy: 92%
- F1-Score: 0.90
- Priority on recall to ensure high-risk patient identification
- Validated through k-fold cross-validation

### Disease Prediction Model
- Multi-class classification for various diseases
- Symptom-based prediction system
- Comprehensive validation process

## Future Improvements
- Integration with electronic health records
- Addition of more specialized disease models
- Enhanced visualization capabilities
- Mobile application development
- API endpoint creation for external integration

## Learning Outcomes
- Handling imbalanced healthcare datasets
- Implementation of ML in medical diagnosis
- Feature selection using statistical tests
- Pipeline development for medical predictions
- Web application development for healthcare

## Technologies Used
- **Data Processing:** Python, NumPy, Pandas
- **Machine Learning:** scikit-learn, joblib
- **Data Visualization:** Matplotlib, Seaborn
- **Web Interface:** Streamlit
- **Development:** Git, Virtual Environment

## Contributing
Contributions to improve HealthInsight are welcome! Please follow these steps:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Dataset source: Kaggle
- Healthcare professionals for domain insights
- Open source community for tools and libraries
- Machine learning can provide impactful healthcare solutions.

---
### Resources
- **Dataset:** [Kaggle Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- **Libraries Used:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Imbalanced-learn

Feel free to explore, contribute, or reach out for discussions on improving healthcare AI solutions! 🚀

### Deployed on Streamlit Cloud [here](https://healthinsinght.streamlit.app/heart_stroke))

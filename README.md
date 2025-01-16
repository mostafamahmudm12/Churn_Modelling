# Bank Customer Churn Prediction System

## 📁 Project Structure
```
project_root/
│   .env                    # Environment variables (private)
│   .env.example           # Environment variables template
│   .gitignore             # Git ignore rules
│   mainroot.py            # FastAPI main application
│   README.md              # Project documentation
│   requirements.txt       # Project dependencies
│   Sttr_app.py           # Streamlit application
│
├───.devcontainer/
│       devcontainer.json  # Development container configuration
│
├───Datasets/
│       Churn_Modelling.csv    # Customer churn dataset
│
├───models/
│       forest_tuned.pkl       # Tuned Random Forest model
│       Preprocessor.pkl       # Data preprocessing pipeline
│       XGoost.pkl            # XGBoost model
│
├───Notebooks/
│       main.ipynb            # Model development notebook
│
└───utils/
    │   config.py            # Configuration settings
    │   CustumerData.py      # Data model definitions
    │   inference.py         # Prediction logic
    │   __init__.py          # Package initialization
    │
    └───__pycache__/        # Python cache files
```

## 🚀 Features
- Dual interface:
  - FastAPI backend for API access
  - Streamlit web interface for interactive use
- Multiple ML models:
  - Random Forest (tuned)
  - XGBoost
- Secure API with key authentication
- Comprehensive data preprocessing
- Docker container support

## 📋 Prerequisites
- Python 3.12
- Docker (for development container)
- Git

## 🔧 Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd <project-directory>
```

2. **Set up environment:**
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings:
APP_NAME=ChurnPredictor
VERSION=1.0.0
SECRET_KEY_TOKEN=your-secret-key
```

3. **Create virtual environment:**
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/MacOS
source venv/bin/activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 💻 Usage

### FastAPI Application
```bash
python mainroot.py
```
Access API documentation: `http://localhost:8000/docs`

### Streamlit Interface
```bash
streamlit run Sttr_app.py
```
Access web interface: `http://localhost:8501`

### Docker Development Container
```bash
# Open in VS Code
code .

# Click "Reopen in Container" when prompted
```

## 🧪 Testing

### Running API Tests
```bash
# Install test dependencies
pip install pytest pytest-cov httpx

# Run all tests
pytest tests/

# Run with coverage
pytest --cov=app tests/
```

### Model Testing
```bash
# Run model validation
pytest tests/test_models.py

# Run preprocessing tests
pytest tests/test_preprocessing.py
```

### Create Test Files:

1. **API Tests** (`tests/test_api.py`):
```python
import pytest
from fastapi.testclient import TestClient
from mainroot import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200

def test_predict_forest():
    headers = {"X-API-Key": "test-key"}
    test_data = {
        "CreditScore": 700,
        "Geography": "France",
        "Gender": "Male",
        "Age": 35,
        "Tenure": 5,
        "Balance": 75000.0,
        "NumOfProducts": 2,
        "HasCrCard": 1,
        "IsActiveMember": 1,
        "EstimatedSalary": 50000.0
    }
    response = client.post("/predict/forest", json=test_data, headers=headers)
    assert response.status_code == 200
```

2. **Model Tests** (`tests/test_models.py`):
```python
import pytest
import joblib
from utils.inference import predict_new
from utils.CustumerData import CustmerData

def test_model_loading():
    forest_model = joblib.load('models/forest_tuned.pkl')
    xgboost_model = joblib.load('models/XGoost.pkl')
    preprocessor = joblib.load('models/Preprocessor.pkl')
    assert all([forest_model, xgboost_model, preprocessor])

def test_prediction():
    test_data = CustmerData(
        CreditScore=700,
        Geography="France",
        Gender="Male",
        Age=35,
        Tenure=5,
        Balance=75000.0,
        NumOfProducts=2,
        HasCrCard=1,
        IsActiveMember=1,
        EstimatedSalary=50000.0
    )
    result = predict_new(test_data)
    assert "prediction" in result
```

## 📊 API Endpoints

### Authentication
All prediction endpoints require API key in header:
```
X-API-Key: your-secret-key
```

### Endpoints
1. **Home**
   - `GET /`
   - Welcome message and version info

2. **Random Forest Prediction**
   - `POST /predict/forest`
   - Requires customer data in request body

3. **XGBoost Prediction**
   - `POST /predict/XGoost`
   - Requires customer data in request body

## 📈 Data Model
```python
class CustmerData(BaseModel):
    CreditScore: int
    Geography: Literal["France", "Spain", "Germany"]
    Gender: Literal["Male", "Female"]
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: Literal[0, 1]
    IsActiveMember: Literal[0, 1]
    EstimatedSalary: float
```

## 🔒 Security
- API key authentication
- Environment variable protection
- Docker container isolation

## 🚀 Deployment
1. **Build Docker image:**
```bash
docker build -t churn-predictor .
```

2. **Run container:**
```bash
docker run -p 8000:8000 -p 8501:8501 churn-predictor
```

## ⚠️ Troubleshooting

### Common Issues
1. **Import Errors:**
   - Check Python version (3.12 required)
   - Verify virtual environment activation
   - Confirm all dependencies installed

2. **Model Loading Errors:**
   - Verify model files in `models/` directory
   - Check file permissions
   - Confirm pickle version compatibility

3. **API Key Issues:**
   - Check `.env` file exists
   - Verify SECRET_KEY_TOKEN setting
   - Confirm header format in requests

## 📝 Contributing
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Submit pull request

## 📄 License
[Add your license information]

## 📞 Support
- Open an issue
- Contact: [your-contact-information]

## 🙏 Acknowledgments
- FastAPI
- Streamlit
- scikit-learn
- XGBoost
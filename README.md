# Bank Customer Prediction System

## 📁 Project Structure
```
project_root/
│   .env                    # Environment variables (private)
│   .env.example           # Example environment variables template
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
│       Churn_Modelling.csv    # Training dataset
│
├───models/
│       forest_tuned.pkl       # Trained Random Forest model
│       Preprocessor.pkl       # Data preprocessing pipeline
│       XGoost.pkl            # Trained XGBoost model
│
├───Notebooks/
│       main.ipynb            # Model development notebook
│
└───utils/
    │   config.py            # Configuration settings
    │   CustumerData.py      # Data model definitions
    │   inference.py         # Prediction logic
    │   __init__.py          # Package initialization
```

## 🚀 Features
- Dual interface support:
  - FastAPI backend (`mainroot.py`)
  - Streamlit web interface (`Sttr_app.py`)
- Multiple ML models:
  - Random Forest (tuned)
  - XGBoost
- Containerized development environment
- Environment variable management
- Comprehensive data preprocessing pipeline

## 📋 Prerequisites
- Python 3.12
- Docker (for development container)
- Git

## 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Using Development Container
1. Install Docker and VS Code with Remote-Containers extension
2. Open project in VS Code
3. Click "Reopen in Container" when prompted

### Running FastAPI Application
```bash
python mainroot.py
```
Access the API documentation at `http://localhost:8000/docs`

### Running Streamlit Interface
```bash
streamlit run Sttr_app.py
```
Access the web interface at `http://localhost:8501`

## 🔑 Environment Variables
Create `.env` file based on `.env.example`:
```env
SECRET_KEY_TOKEN=your_secret_key
APP_NAME=your_app_name
VERSION=your_version
```

## 📊 Models

### Random Forest (`forest_tuned.pkl`)
- Tuned for optimal performance
- Used for primary predictions

### XGBoost (`XGoost.pkl`)
- Alternative model
- Optimized for specific use cases

### Preprocessor (`Preprocessor.pkl`)
- Handles data transformation
- Feature scaling and encoding

## 📈 Dataset
The `Churn_Modelling.csv` dataset includes:
- Customer demographic information
- Banking behavior data
- Churn status

## 🛠️ Development

### Model Training
1. Open `Notebooks/main.ipynb`
2. Follow the training pipeline
3. Export models to `models/` directory

### API Development
Modify `mainroot.py` for API changes:
```python
@app.post('/predict/forest', tags=['Models'])
async def predict_forest(data: CustmerData, api_key: str = Depends(verify_api_key)) -> dict:
    # Implementation
```

### Streamlit Interface Development
Modify `Sttr_app.py` for UI changes.

## 🧪 Testing
1. API testing:
```bash
# Add your testing commands
```

2. Model testing:
```bash
# Add your testing commands
```

## 🔒 Security
- API key authentication implemented
- Environment variable protection
- Docker container isolation

## 🤝 Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Submit pull request

## 📝 License
[Add your license information]

## ⚠️ Troubleshooting

### Common Issues
1. Model Loading Errors:
   - Verify model files in `models/` directory
   - Check Python version compatibility

2. Environment Variables:
   - Ensure `.env` file exists
   - Check variable names match `.env.example`

3. Container Issues:
   - Verify Docker installation
   - Check devcontainer.json configuration

## 📞 Support
For support:
- Open an issue
- Contact [your-contact-information]

## 🔄 Version History
- Current Version: [Your Version]
- [Add version history]

## 🙏 Acknowledgments
- FastAPI
- Streamlit
- scikit-learn
- XGBoost

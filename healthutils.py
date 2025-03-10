
from models import User, HealthData, DiabetesData
from app import db

def get_user_health_data(user_id):
    """
    Get all health data entries for a specific user
    Returns a list of HealthData objects
    """
    return HealthData.query.filter_by(user_id=user_id).order_by(HealthData.timestamp.desc()).all()

def get_latest_health_data(user_id):
    """
    Get the most recent health data entry for a specific user
    Returns a single HealthData object or None
    """
    return HealthData.query.filter_by(user_id=user_id).order_by(HealthData.timestamp.desc()).first()

def get_health_data_summary(user_id): # return the health data based on user id

    data = get_user_health_data(user_id)
    if not data:
        return None
    
    latest = data[0]
    return {
        'latest': {
            'blood_pressure': latest.blood_pressure,
            'heart_rate': latest.heart_rate,
            'temperature': latest.temperature,
            'weight': latest.weight,
            'risk_score': latest.risk_score,
            'timestamp': latest.timestamp,
            'cholesterol': latest.cholesterol
        },
        'count': len(data)
    }

def get_user_diabetes_data(user_id):
    """
    Get all health data entries for a specific user
    Returns a list of HealthData objects
    """
    return DiabetesData.query.filter_by(user_id=user_id).order_by(DiabetesData.timestamp.desc()).all()

def get_diabetes_data_summary(user_id):

    data = get_user_diabetes_data(user_id)
    if not data:
        return None
    
    latest = data[0]
    return {
        'latest': {
            'gender': latest.gender,
            'age': latest.age,
            'hypertension': latest.hypertension,
            'heart_disease': latest.heart_disease,
            'smoking_history': latest.smoking_history,
            'bmi': latest.bmi,
            'hba1c_level': latest.hba1c_level,
            'blood_glucose_level': latest.blood_glucose_level,
            'risk_score': latest.risk_score,
            'timestamp': latest.timestamp
        },
        'count': len(data)
    }
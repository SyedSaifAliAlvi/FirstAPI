import joblib
import numpy as np
import pandas as pd

model = joblib.load('weights_model.pkl')

def userData(arrayData):
  data = np.array(arrayData)
  user_df = pd.DataFrame(data,['age', 'resting_blood_pressure', 'cholesterol', 'max_heart_rate_achieved', 'st_depression', 'num_major_vessels', 'st_slope_downsloping', 'st_slope_flat', 'st_slope_upsloping', 'sex_male', 'chest_pain_type_atypical angina', 'chest_pain_type_non-anginal pain', 'chest_pain_type_typical angina', 'fasting_blood_sugar_lower than 120mg/ml', 'rest_ecg_left ventricular hypertrophy', 'rest_ecg_normal', 'exercise_induced_angina_yes', 'thalassemia_fixed defect', 'thalassemia_normal','thalassemia_reversable defect']).transpose()
  predict = model.predict(user_df)
  res = predict[0]
  return res
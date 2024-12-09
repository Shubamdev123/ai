import pandas as pd
data=pd.read_csv("heartdisease.csv")
heart_disease=pd.DataFrame(data)
print(heart_disease)

from pgmpy.models import BayesianModel
model=BayesianModel([
('age','Lifestyle'),
('Gender','Lifestyle'),
('Family','heartdisease'),
('diet','cholestrol'),
('Lifestyle','diet'),
('cholestrol','heartdisease'),
('diet','cholestrol')
])

from pgmpy.estimators import MaximumLikelihoodEstimator
model.fit(heart_disease, estimator=MaximumLikelihoodEstimator)

from pgmpy.inference import VariableElimination
HeartDisease_infer = VariableElimination(model)

print('For age Enter { SuperSeniorCitizen:0, SeniorCitizen:1, MiddleAged:2, Youth:3, Teen:4 }')
print('For Gender Enter { Male:0, Female:1 }')
print('For Family History Enter { yes:1, No:0 }')
print('For diet Enter { High:0, Medium:1 }')
print('For lifeStyle Enter { Athlete:0, Active:1, Moderate:2, Sedentary:3 }')
print('For cholesterol Enter { High:0, BorderLine:1, Normal:2 }')

# Taking inputs for the evidence
age = int(input('Enter age: '))
gender = int(input('Enter Gender: '))
family = int(input('Enter Family history: '))
diet = int(input('Enter diet: '))
lifestyle = int(input('Enter Lifestyle: '))
cholesterol = int(input('Enter cholesterol: '))

# Perform inference on the model
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={
    'age': age,
    'Gender': gender,
    'Family': family,
    'diet': diet,
    'Lifestyle': lifestyle,
    'cholestrol': cholesterol
})

# Print the probability distribution for 'heartdisease'
print("Probability distribution for 'heartdisease':")
print(q)
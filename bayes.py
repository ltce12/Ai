!pip install pgmpy
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define the structure of the Bayesian Network
model = BayesianNetwork([('Cold', 'Cough'), ('Cold', 'Fever')])

# Step 2: Define the Conditional Probability Distributions (CPDs)

# Prior probability for Cold
cpd_cold = TabularCPD(variable='Cold', variable_card=2, values=[[0.7], [0.3]])
# Probability of Cough given Cold
cpd_cough = TabularCPD(variable='Cough', variable_card=2,
                       values=[[0.8, 0.1], [0.2, 0.9]],
                       evidence=['Cold'], evidence_card=[2])
# Probability of Fever given Cold
cpd_fever = TabularCPD(variable='Fever', variable_card=2,
                       values=[[0.9, 0.2], [0.1, 0.8]],
                       evidence=['Cold'], evidence_card=[2])

# Step 3: Add the CPDs to the model
model.add_cpds(cpd_cold, cpd_cough, cpd_fever)

# Step 4: Validate the model
assert model.check_model(), "Model is incorrect"

# Step 5: Perform inference
inference = VariableElimination(model)

# Query: What is the probability of Cold given that the person has a cough and fever?
result = inference.query(variables=['Cold'], evidence={'Cough': 1, 'Fever': 1})
print(result)

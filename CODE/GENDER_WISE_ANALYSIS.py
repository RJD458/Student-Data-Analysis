import mysql.connector as mc;
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;




# Connect to MySQL
con = mc.connect(
    host="localhost",
    user="root",
    password="ami bangali",
    database="STUDENT"
)




# Collect data with the help of pandas
query = "SELECT * FROM STUDENT_INFORMATION"
data = pd.read_sql(query, con)
con.close()




# Calculate average score
data["average_score"] = data[["MATH_SCORE", "PHYSICS_SCORE", "CHEMISTRY_SCORE"]].mean(axis=1)
# Compare gender performance
print("\n\n\n================ GENDER-WISE ANALYSIS ================")
avg_gender = data.groupby("GENDER")["average_score"].mean()
print("\n\n========== Average Score by Gender ==========\n", avg_gender)




# Correlation between subjects
corr_matrix = data[["MATH_SCORE", "PHYSICS_SCORE", "CHEMISTRY_SCORE"]].corr()
print("\n\n========== Correlation Matrix ==========\n", corr_matrix)




# Subject-wise analysis

## Math score analysis
math_scores = data["MATH_SCORE"].to_numpy()
print("\n\n==========Math Score Analysis==========")
print("\nMath Variance : ", np.var(math_scores))
print("Math Std Dev : ", np.std(math_scores))

AVG_MATH = data.groupby("GENDER")["MATH_SCORE"].mean()
print("\nMath score analysis according to gender ::==")
print(AVG_MATH)

## Physics score analysis
phy_scores = data["PHYSICS_SCORE"].to_numpy()
print("\n\n==========Physics Score Analysis==========")
print("\nPhysics Variance : ", np.var(phy_scores))
print("Physics Std Dev : ", np.std(phy_scores))

AVG_PHYSIC = data.groupby("GENDER")["PHYSICS_SCORE"].mean()
print("\nPhysics score analysis according to gender ::==")
print(AVG_PHYSIC)

## Chemistry score analysis
chem_scores = data["CHEMISTRY_SCORE"].to_numpy()
print("\n\n==========Chemistry Score Analysis==========")
print("\nChemistry Variance : ", np.var(chem_scores))
print("Chemistry Std Dev : ", np.std(chem_scores))

AVG_CHEMISTRY = data.groupby("GENDER")["CHEMISTRY_SCORE"].mean()
print("\nChemistry score analysis according to gender ::==")
print(AVG_CHEMISTRY)

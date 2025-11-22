import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import mysql.connector as mc;

# CONNECT WITH MYSQL
con = mc.connect(
    host = "localhost",
    user = "root",
    password = "ami bangali",
    database = "STUDENT"
)

# LOAD DATA WITH THE HELP OF PANDAS
query = "SELECT * FROM STUDENT_INFORMATION";
data = pd.read_sql(query, con);
con.close();



# TOTAL AVG SCORE ANALYSIS ACCORDING TO PARENTAL_LEVEL_OF_EDUCATION
data["AVG_SCORE"] = data[["MATH_SCORE", "PHYSICS_SCORE", "CHEMISTRY_SCORE"]].mean(axis=1)
AVG_TEST = data.groupby("PARENTAL_LEVEL_OF_EDUCATION")["AVG_SCORE"].mean().sort_values(ascending=False)
print("\n\n\n============= PARENTAL_LEVEL_OF_EDUCATION-WISE ANALYSIS =============")
print("\n\n========== Average Score by PARENTAL_LEVEL_OF_EDUCATION ==========\n", AVG_TEST)



# Subject-wise analysis

## Math score analysis
AVG_MATH = data.groupby("PARENTAL_LEVEL_OF_EDUCATION")["MATH_SCORE"].mean().sort_values(ascending=False)
print("\nMath score analysis according to PARENTAL_LEVEL_OF_EDUCATION ::==")
print(AVG_MATH)

## Physics score analysis
AVG_PHYSIC = data.groupby("PARENTAL_LEVEL_OF_EDUCATION")["PHYSICS_SCORE"].mean().sort_values(ascending=False)
print("\nPhysics score analysis according to PARENTAL_LEVEL_OF_EDUCATION ::==")
print(AVG_PHYSIC)

## Chemistry score analysis
AVG_CHEMISTRY = data.groupby("PARENTAL_LEVEL_OF_EDUCATION")["CHEMISTRY_SCORE"].mean().sort_values(ascending=False)
print("\nChemistry score analysis according to PARENTAL_LEVEL_OF_EDUCATION ::==")
print(AVG_CHEMISTRY)

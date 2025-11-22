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



# TOTAL AVG SCORE ANALYSIS ACCORDING TO TEST PREPARETION
data["AVG_SCORE"] = data[["MATH_SCORE", "PHYSICS_SCORE", "CHEMISTRY_SCORE"]].mean(axis=1)
AVG_TEST = data.groupby("TEST_PREPARETION")["AVG_SCORE"].mean()
print("\n\n\n============= TEST PREPARETION-WISE ANALYSIS =============")
print("\n\n========== Average Score by TEST PREPARETION ==========\n", AVG_TEST)



# Subject-wise analysis

## Math score analysis
AVG_MATH = data.groupby("TEST_PREPARETION")["MATH_SCORE"].mean()
print("\nMath score analysis according to TEST PREPARETION ::==")
print(AVG_MATH)

## Physics score analysis
AVG_PHYSIC = data.groupby("TEST_PREPARETION")["PHYSICS_SCORE"].mean()
print("\nPhysics score analysis according to TEST PREPARETION ::==")
print(AVG_PHYSIC)

## Chemistry score analysis
AVG_CHEMISTRY = data.groupby("TEST_PREPARETION")["CHEMISTRY_SCORE"].mean()
print("\nChemistry score analysis according to TEST PREPARETION ::==")
print(AVG_CHEMISTRY)

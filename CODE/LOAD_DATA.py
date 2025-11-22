import pandas as pd;
import mysql.connector as mc;

data = pd.read_csv("C:\\Users\\RAJDEEP SADHU\\OneDrive\\Desktop\\Student Data Analysis Project\\DATA\\STUDENT_dATA.csv");
data.columns = ["GENDER", "RACE", "PARENTAL_LEVEL_OF_EDUCATION", "LUNCH", "TEST_PREPARETION", "MATH_SCORE", "PHYSICS_SCORE", "CHEMISTRY_SCORE"];


con = mc.connect(
    host="localhost",
    user="root",
    password="ami bangali",  # Replace with your MySQL password
    database="STUDENT"
);
cursor = con.cursor();


for _, row in data.iterrows():
    cursor.execute("""
        INSERT INTO STUDENT_INFORMATION
        (GENDER, RACE, PARENTAL_LEVEL_OF_EDUCATION, LUNCH, TEST_PREPARETION, MATH_SCORE, PHYSICS_SCORE, CHEMISTRY_SCORE)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))
con.commit();
print("Data Successfully inserted in mysql database!!");

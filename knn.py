import streamlit as st
import mysql.connector
import tomllib
import math
import time
st.header("Implementation of K Nearest Neighbour")
st.divider()
with open("config.toml","rb") as file:
    config=tomllib.load(file)
connection=mysql.connector.connect(
    host=config["mysql"]["host"],
    user=config["mysql"]["user"],
    password=config["mysql"]["password"],
    database=config["mysql"]["database"],
    port=config["mysql"]["port"]
)
cursor=connection.cursor(dictionary=True)
sql="""
    SELECT * FROM knn
"""
cursor.execute(sql)
result=cursor.fetchall()
st.dataframe(result)
if "data_filled " not in st.session_state:
    st.session_state.data_filled=False
x1=st.text_input("Enter the value of Height : ")
y1=st.text_input("Enter the value of Weight : ")
k=st.text_input("Enter the value of k : ")
if(st.button("Entered",type="primary")):
    st.session_state.data_filled=True
if(st.session_state.data_filled):
    distance=[]
    extracted_data={}
    try:
        k=int(k)
        if(k>=1 and k<=5):
            x1=int(x1)
            y1=int(y1)
            for i in range(1,6):
                sql="""
                SELECT Height, Weight FROM knn
                WHERE `Ex.`=%s
            """
                cursor.execute(sql,(i,))
                results=cursor.fetchall()
                for result in results:
                    x2=result["Height"]
                    y2=result["Weight"]
                    dist=math.sqrt((x2-x1)**2+(y2-y1)**2)
                    distance.append({"Distance":dist,"Ex.":i})
                    distance.sort(key=lambda x: x["Distance"])
            for j in range(k):
                sql="""
                SELECT Prediction ,COUNT(*) AS Count,`Ex.` 
                FROM knn
                WHERE `Ex.` IN (%s)
            """
                cursor.execute(sql,(distance[j]["Ex."],))
                results=cursor.fetchall()
                for item in results:
                    prediction=item["Prediction"]
                    count=item["Count"]
                    extracted_data[prediction]=extracted_data.get(prediction,0)+1
            final_prediction=max(extracted_data,key=extracted_data.get)
            st.write_stream(
                time.sleep(0.05) or char for char in f"Prediction for x1={x1} and y1={y1} is  {final_prediction}."
            )
        else:
            st.error("Value of k is not valid!")

    except ValueError:
        st.error("Check the values of Height and Weight")
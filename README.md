# sakila_lab_alicia_gezelius

This document will contain some hightlight from this labb.

Step 1: Load sakila data using DLT. 
  - created ingest script with all the paths
  - created the pipline

Step 2: Query sakila data
  - First created a funktion that returns a dataframe and in order to not keep having to open and close the connection with duckdb all the time. 
  - Used the funktion to do the quereis in SQL and then putputing the data in a dataframe 
  - I did use LLM to genrate questions form f-i in the eda-part. 

Step 3: Graphs 
  -  For the graphs i did use LLM to figure out how to scale the graphs and how to rotare the names for it to become more clear. 
  - for the first graph i used concat to make the customer name one colum for and limit the answer for top five before puting it in the graph. 
  - Lastly i saved both graphs in a sepreate png.file so they can be put in presentaions if needed. 

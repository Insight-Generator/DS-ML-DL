# Corrected format

{x: gender, y: count, filter: [], data: [{gender: male, count: 500}, {gender: female, count: 500}]} {x: gender, y: avg_test, data: [gender: "ethnicity A female", avg_test: 100]} {x: {ref: gender, full_name: "Gender"}, y: {ref: avg_score, full_name: "Average score per gender and race"}, data: []}

# Corrected format without data

[{x: column1, y: column2, filter: [], data: [{WILL BE SENT TO D3}], source: "WHAT ALGORITHM IT CAME FROM"}, same but for similarity?]

# Separations between tasks

Backend gets request for data, reads csv or database, and then send to d3
Machine learning gets a celery tasks, download data, process solutions/compile, outputs summary statistics (column names, percentages, etc) to send to backend & d3

# Overall format for outputs

[

{x: columna, y:columnb, type: basic}, # Basics graph to give. When user opens graph, backend opens csv and parses just 2 columns and sends it to D3. Possible count of column a & column b. Typically for ML outputs

{x:columnc, y:columnd, data:[{data}], type: with_data}, # User opens graphs, backend accesses db and sends just data. 

{x: columne, y:columnf, filter: [columnz, columny]}, # Other columns of interest. Filter can be for additional columns of comparison

]
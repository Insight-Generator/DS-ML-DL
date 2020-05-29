
count of string
- male, female
- OUTPUT
       X             Y
- - [[male, 500], [female, 500]]
- - [{male: 500}, {female: 500}]
- - [{gender: male, count: 500}, {gender: female, count: 500}], [{x: gender, y: count}]
{x: gender, y: count, filter: [], data: [{gender: male, count: 500}, {gender: female, count: 500}]}
{x: gender, y: avg_test, data: [gender: "ethnicity A female", avg_test: 100]}
{x: {ref: gender, full_name: "Gender"}, y: {ref: avg_score, full_name: "Average score per gender and race"}, data: []}

- Possibility that D3 graphing library can already do some of these
{file_based_graphs: {similarity: [[x,y], [z,x]], correlation:[]}, custom_data_graphs: [{x:{}, y:{}, filter:[], data: []}]}
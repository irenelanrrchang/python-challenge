

```python
import csv
import pandas as pd
import numpy as np

```


```python
schools = "generated_data/schools_complete.csv"
students = "generated_data/students_complete.csv"
```


```python
schools_pd = pd.read_csv(schools, encoding="iso-8859-1", low_memory=False)
schools_pd.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>school_name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Miller High School</td>
      <td>Charter</td>
      <td>2424</td>
      <td>1418040</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Sherman High School</td>
      <td>District</td>
      <td>3213</td>
      <td>2152710</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Galloway High School</td>
      <td>Charter</td>
      <td>2471</td>
      <td>1445535</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Smith High School</td>
      <td>District</td>
      <td>4954</td>
      <td>3210192</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Kelly High School</td>
      <td>District</td>
      <td>3307</td>
      <td>2225611</td>
    </tr>
  </tbody>
</table>
</div>




```python
students_pd = pd.read_csv(students, encoding="iso-8859-1", low_memory=False)
students_pd.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>student_name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school_name</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>April Miller</td>
      <td>F</td>
      <td>9th</td>
      <td>Miller High School</td>
      <td>99</td>
      <td>92</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Robert Martinez</td>
      <td>M</td>
      <td>9th</td>
      <td>Miller High School</td>
      <td>99</td>
      <td>71</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Brandon Perkins</td>
      <td>M</td>
      <td>9th</td>
      <td>Miller High School</td>
      <td>93</td>
      <td>89</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Sierra Hernandez</td>
      <td>F</td>
      <td>10th</td>
      <td>Miller High School</td>
      <td>89</td>
      <td>94</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Nicole Johnson</td>
      <td>F</td>
      <td>10th</td>
      <td>Miller High School</td>
      <td>89</td>
      <td>77</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a high level snapshot (in table form) of the district's key metrics, including:
total_schools = []
total_students = []
total_budget = []
avg_math_score = []
avg_reading_score = []
percent_passing_math = []
percent_passing_reading = []
overall_passing_rate = []
```


```python
# Total Students: .count
total_students = students_pd["student_name"].count()
print(total_students)
```

    29376



```python
# Total Schools: .value_counts
school_list = students_pd["school_name"].value_counts()
total_schools = school_list.count()
print(total_schools)
```

    11



```python
# Total Budget: sum
df = schools_pd["budget"]
total_budget = df.sum(axis=0)
print(total_budget)
```

    18648468



```python
# Average Math Score: sum of math score/ Total Stutents OR avg_math_score = students_pd["math_score"].mean()
avg_math_score = round(students_pd["math_score"].mean(),2)
print(avg_math_score)
```

    82.27



```python
# Average Reading Score: sum of reading score/ Total Students OR avg_reading_score = students_pd["reading_score"].mean()
avg_reading_score = round(students_pd["reading_score"].mean(),2)
print(avg_reading_score)
```

    82.87



```python
# % Passing Math
# % Passing Reading
# Adding two columns for passing math & reading 
students_pd["passing_math"] = np.where(students_pd["math_score"] >= 60, 1, 0)
students_pd["passing_reading"] = np.where(students_pd["reading_score"] >= 60, 1, 0)
```


```python
# Calculate for %
percent_passing_math = round(students_pd["passing_math"].sum()/total_students*100, 2)
percent_passing_reading = round(students_pd["passing_reading"].sum()/total_students*100, 2)
```


```python
# Overall Passing Rate (Average of the above two): "% of Passing Math" + "% of Passing reading"/ 2
percent_overall_passing = round((percent_passing_math + percent_passing_reading)/2,2)
```


```python
# Create a new table to summarize above calculations
district_summary = pd.DataFrame({"Total Schools": [total_schools],
                                   "Total Students": [total_students],
                                   "Total Budget": [total_budget],
                                   "Average Math Score": [avg_math_score],
                                   "Average Reading Score": [avg_reading_score],
                                   "% Passing Math":[percent_passing_math],
                                   "% Passing Reading":[percent_passing_reading],
                                   "Overall Passing Rate": [percent_overall_passing],
})
district_summary = district_summary[["Total Schools", 
                                     "Total Students", 
                                     "Total Budget", 
                                     "Average Math Score", 
                                     "Average Reading Score", 
                                     "% Passing Math", 
                                     "% Passing Reading",
                                      "Overall Passing Rate"]]

district_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11</td>
      <td>29376</td>
      <td>18648468</td>
      <td>82.27</td>
      <td>82.87</td>
      <td>100.0</td>
      <td>92.77</td>
      <td>96.38</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Export to Excel
district_summary.to_excel("generated_data/DistrictSummary.xlsx", index=False)
```


```python
# Create a dataframe with school_name, Total Student, Avg Math & Reading Score
student_school = students_pd.groupby("school_name")
students1 = student_school.agg({"Student ID":"count" , "math_score" :"mean" , "reading_score" : "mean"})
students1.rename(columns = {"Student ID": "Total Student", "math_score":"Avg Math Score", "reading_score":"Avg Reading Score"}, inplace = True)
students1["Avg Math Score"]= round(students1["Avg Math Score"], 2)
students1["Avg Reading Score"]= round(students1["Avg Reading Score"], 2)
students1.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Student</th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
    </tr>
    <tr>
      <th>school_name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Campbell High School</th>
      <td>271</td>
      <td>83.59</td>
      <td>93.77</td>
    </tr>
    <tr>
      <th>Galloway High School</th>
      <td>2471</td>
      <td>83.57</td>
      <td>94.03</td>
    </tr>
    <tr>
      <th>Glass High School</th>
      <td>3271</td>
      <td>81.29</td>
      <td>76.89</td>
    </tr>
    <tr>
      <th>Gomez High School</th>
      <td>2154</td>
      <td>83.84</td>
      <td>94.03</td>
    </tr>
    <tr>
      <th>Gonzalez High School</th>
      <td>1855</td>
      <td>83.44</td>
      <td>94.14</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Add student count of math & reading test passing
## grab the score >= 60
mathpass = students_pd["math_score"] >= 60
student_math = students_pd[mathpass]
readpass = students_pd["reading_score"]>=60
student_read = students_pd[readpass]
## groupby school and count no.
group_math = student_math.groupby("school_name").agg({"math_score":"count"}).rename(columns ={"math_score" :"mathP_count"} )
group_read = student_read.groupby("school_name").agg({"reading_score":"count"}).rename(columns = {"reading_score": "readingP_count"})
group_math_read = group_math.merge(group_read, how = "left", left_index = True, right_index = True)

## Create a dataframe with school_name,  Passing Math, passing Reading no. and total amount of math & reading score
total_score_no = student_school.agg({"math_score": "count", "reading_score":"count" })
df1 = group_math_read.merge(total_score_no, how = "left", right_index = True, left_index = True)

## Count % of passing
df1["% Math Passing"] = round(df1["mathP_count"]/df1["math_score"]*100,2)
df1["% Reading Passing"] = round(df1["readingP_count"]/df1["reading_score"]*100,2)
df1["% Overall Passing"] = round((df1["% Math Passing"] + df1["% Reading Passing"])/2,2)
final_df1 = df1.drop(df1.columns[[0,1,2,3]], axis=1)
final_df1

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Math Passing</th>
      <th>% Reading Passing</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>school_name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Campbell High School</th>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Galloway High School</th>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Glass High School</th>
      <td>100.0</td>
      <td>88.72</td>
      <td>94.36</td>
    </tr>
    <tr>
      <th>Gomez High School</th>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Gonzalez High School</th>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Hawkins High School</th>
      <td>100.0</td>
      <td>88.72</td>
      <td>94.36</td>
    </tr>
    <tr>
      <th>Kelly High School</th>
      <td>100.0</td>
      <td>88.75</td>
      <td>94.38</td>
    </tr>
    <tr>
      <th>Macdonald High School</th>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Miller High School</th>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Sherman High School</th>
      <td>100.0</td>
      <td>89.45</td>
      <td>94.72</td>
    </tr>
    <tr>
      <th>Smith High School</th>
      <td>100.0</td>
      <td>89.28</td>
      <td>94.64</td>
    </tr>
  </tbody>
</table>
</div>




```python
# schools_pd.columns = ["name", "type", "size", "budget" ]
df2 = schools_pd[["school_name", "type", "size", "budget"]]
df2 = df2.sort_values("school_name").set_index('school_name')


#Per Student Budget: budget/ size
df2["per student budget" ] = df2["budget"]/ df2["size"]
df3 = df2.merge(students1, how = 'left', left_index=True, right_index = True)
df4 = df3.merge(final_df1, how = 'left', left_index=True, right_index = True)
df4
df4.head()
#df4["budget"] = df4["budget"].map("$ {:,.2f}".format) to add $ sign in budget column if required
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>per student budget</th>
      <th>Total Student</th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
      <th>% Math Passing</th>
      <th>% Reading Passing</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>school_name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Campbell High School</th>
      <td>Charter</td>
      <td>271</td>
      <td>157993</td>
      <td>583.0</td>
      <td>271</td>
      <td>83.59</td>
      <td>93.77</td>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Galloway High School</th>
      <td>Charter</td>
      <td>2471</td>
      <td>1445535</td>
      <td>585.0</td>
      <td>2471</td>
      <td>83.57</td>
      <td>94.03</td>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Glass High School</th>
      <td>District</td>
      <td>3271</td>
      <td>2155589</td>
      <td>659.0</td>
      <td>3271</td>
      <td>81.29</td>
      <td>76.89</td>
      <td>100.0</td>
      <td>88.72</td>
      <td>94.36</td>
    </tr>
    <tr>
      <th>Gomez High School</th>
      <td>Charter</td>
      <td>2154</td>
      <td>1288092</td>
      <td>598.0</td>
      <td>2154</td>
      <td>83.84</td>
      <td>94.03</td>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Gonzalez High School</th>
      <td>Charter</td>
      <td>1855</td>
      <td>1192765</td>
      <td>643.0</td>
      <td>1855</td>
      <td>83.44</td>
      <td>94.14</td>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df4.columns
df4.columns = ["School Type",
                      "Total Size",
                      "Total Budget",
                      "Per Student Budget",
                      "Total Student",
                      "Average Math Score",
                      "Average Reading Score",
                      "% Passing Math",
                      "% Passing Reading",
                      "% Overall Passing"]
df4
# school_summary = df4[["School Type",
#                       "Total Student",
#                       "Total Budget",
#                       "Per Student Budget",
#                       "Total Student",
#                       "Average Math Score",
#                       "Average Reading Score",
#                       "% Passing Math",
#                       "% Passing Reading",
#                       "Overall Passing Rate"]] doesn't work

# school_summary = pd.DataFrame({ "School Name": [school_name],
#                                  "School Type": [type],
#                                  "Total Student": [size],
#                                  "Total Budget" : [budget],
#                                  "Per Student Budget": [per student budget],
#                                  "Average Math Score": [Avg Math Score],
#                                  "Average Reading Score": [Avg Reading Score],
#                                  "% Passing Math":[% Math Passing],
#                                  "% Passing Reading":[% Reading Passing],
#                                  "Overall Passing Rate": [% Overall Passing]
#                                }) doesn't work
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Size</th>
      <th>Total Budget</th>
      <th>Per Student Budget</th>
      <th>Total Student</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>school_name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Campbell High School</th>
      <td>Charter</td>
      <td>271</td>
      <td>157993</td>
      <td>583.0</td>
      <td>271</td>
      <td>83.59</td>
      <td>93.77</td>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Galloway High School</th>
      <td>Charter</td>
      <td>2471</td>
      <td>1445535</td>
      <td>585.0</td>
      <td>2471</td>
      <td>83.57</td>
      <td>94.03</td>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Glass High School</th>
      <td>District</td>
      <td>3271</td>
      <td>2155589</td>
      <td>659.0</td>
      <td>3271</td>
      <td>81.29</td>
      <td>76.89</td>
      <td>100.0</td>
      <td>88.72</td>
      <td>94.36</td>
    </tr>
    <tr>
      <th>Gomez High School</th>
      <td>Charter</td>
      <td>2154</td>
      <td>1288092</td>
      <td>598.0</td>
      <td>2154</td>
      <td>83.84</td>
      <td>94.03</td>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Gonzalez High School</th>
      <td>Charter</td>
      <td>1855</td>
      <td>1192765</td>
      <td>643.0</td>
      <td>1855</td>
      <td>83.44</td>
      <td>94.14</td>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Hawkins High School</th>
      <td>District</td>
      <td>4555</td>
      <td>2851430</td>
      <td>626.0</td>
      <td>4555</td>
      <td>81.72</td>
      <td>77.01</td>
      <td>100.0</td>
      <td>88.72</td>
      <td>94.36</td>
    </tr>
    <tr>
      <th>Kelly High School</th>
      <td>District</td>
      <td>3307</td>
      <td>2225611</td>
      <td>673.0</td>
      <td>3307</td>
      <td>81.68</td>
      <td>76.83</td>
      <td>100.0</td>
      <td>88.75</td>
      <td>94.38</td>
    </tr>
    <tr>
      <th>Macdonald High School</th>
      <td>Charter</td>
      <td>901</td>
      <td>550511</td>
      <td>611.0</td>
      <td>901</td>
      <td>83.78</td>
      <td>93.93</td>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Miller High School</th>
      <td>Charter</td>
      <td>2424</td>
      <td>1418040</td>
      <td>585.0</td>
      <td>2424</td>
      <td>83.61</td>
      <td>94.00</td>
      <td>100.0</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Sherman High School</th>
      <td>District</td>
      <td>3213</td>
      <td>2152710</td>
      <td>670.0</td>
      <td>3213</td>
      <td>81.50</td>
      <td>77.29</td>
      <td>100.0</td>
      <td>89.45</td>
      <td>94.72</td>
    </tr>
    <tr>
      <th>Smith High School</th>
      <td>District</td>
      <td>4954</td>
      <td>3210192</td>
      <td>648.0</td>
      <td>4954</td>
      <td>81.54</td>
      <td>77.15</td>
      <td>100.0</td>
      <td>89.28</td>
      <td>94.64</td>
    </tr>
  </tbody>
</table>
</div>




```python
# #Top 5 Performing Schools (By Passing Rate)
Top = df4.sort_values("% Overall Passing", ascending = False)
Top.head(5)

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Size</th>
      <th>Total Budget</th>
      <th>Per Student Budget</th>
      <th>Total Student</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>school_name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Campbell High School</th>
      <td>Charter</td>
      <td>271</td>
      <td>157993</td>
      <td>583.0</td>
      <td>271</td>
      <td>83.59</td>
      <td>93.77</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>Galloway High School</th>
      <td>Charter</td>
      <td>2471</td>
      <td>1445535</td>
      <td>585.0</td>
      <td>2471</td>
      <td>83.57</td>
      <td>94.03</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>Gomez High School</th>
      <td>Charter</td>
      <td>2154</td>
      <td>1288092</td>
      <td>598.0</td>
      <td>2154</td>
      <td>83.84</td>
      <td>94.03</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>Gonzalez High School</th>
      <td>Charter</td>
      <td>1855</td>
      <td>1192765</td>
      <td>643.0</td>
      <td>1855</td>
      <td>83.44</td>
      <td>94.14</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>Macdonald High School</th>
      <td>Charter</td>
      <td>901</td>
      <td>550511</td>
      <td>611.0</td>
      <td>901</td>
      <td>83.78</td>
      <td>93.93</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Bottom 5 Performing Schools (By Passing Rate)
Bottom = df4.sort_values("% Overall Passing", ascending = False)
Bottom.tail(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Size</th>
      <th>Total Budget</th>
      <th>Per Student Budget</th>
      <th>Total Student</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>school_name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Sherman High School</th>
      <td>District</td>
      <td>3213</td>
      <td>2152710</td>
      <td>670.0</td>
      <td>3213</td>
      <td>81.50</td>
      <td>77.29</td>
      <td>100.0</td>
      <td>89.45</td>
      <td>94.72</td>
    </tr>
    <tr>
      <th>Smith High School</th>
      <td>District</td>
      <td>4954</td>
      <td>3210192</td>
      <td>648.0</td>
      <td>4954</td>
      <td>81.54</td>
      <td>77.15</td>
      <td>100.0</td>
      <td>89.28</td>
      <td>94.64</td>
    </tr>
    <tr>
      <th>Kelly High School</th>
      <td>District</td>
      <td>3307</td>
      <td>2225611</td>
      <td>673.0</td>
      <td>3307</td>
      <td>81.68</td>
      <td>76.83</td>
      <td>100.0</td>
      <td>88.75</td>
      <td>94.38</td>
    </tr>
    <tr>
      <th>Glass High School</th>
      <td>District</td>
      <td>3271</td>
      <td>2155589</td>
      <td>659.0</td>
      <td>3271</td>
      <td>81.29</td>
      <td>76.89</td>
      <td>100.0</td>
      <td>88.72</td>
      <td>94.36</td>
    </tr>
    <tr>
      <th>Hawkins High School</th>
      <td>District</td>
      <td>4555</td>
      <td>2851430</td>
      <td>626.0</td>
      <td>4555</td>
      <td>81.72</td>
      <td>77.01</td>
      <td>100.0</td>
      <td>88.72</td>
      <td>94.36</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Math Score by grade at each school
x = students_pd.groupby(["school_name", "grade"]).agg({"math_score":"mean"})
x["math_score"]= round(x["math_score"], 2)
x
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>math_score</th>
    </tr>
    <tr>
      <th>school_name</th>
      <th>grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Campbell High School</th>
      <th>10th</th>
      <td>84.27</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.94</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>82.06</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.84</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Galloway High School</th>
      <th>10th</th>
      <td>83.55</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.98</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.20</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.53</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Glass High School</th>
      <th>10th</th>
      <td>81.04</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>81.39</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.82</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.87</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Gomez High School</th>
      <th>10th</th>
      <td>83.97</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.87</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.83</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.68</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Gonzalez High School</th>
      <th>10th</th>
      <td>83.95</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.20</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>82.84</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.55</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Hawkins High School</th>
      <th>10th</th>
      <td>81.48</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>81.89</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>81.94</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.67</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Kelly High School</th>
      <th>10th</th>
      <td>81.88</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>81.50</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>81.45</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.79</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Macdonald High School</th>
      <th>10th</th>
      <td>83.81</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.48</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.52</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>84.26</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Miller High School</th>
      <th>10th</th>
      <td>83.62</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.64</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.30</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.82</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Sherman High School</th>
      <th>10th</th>
      <td>81.53</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>81.23</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>81.74</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.50</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Smith High School</th>
      <th>10th</th>
      <td>81.00</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>81.83</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>81.55</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.91</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Reading Score by grade at each school
y = students_pd.groupby(["school_name", "grade"]).agg({"reading_score":"mean"})
y["reading_score"]= round(y["reading_score"], 2)
y
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>reading_score</th>
    </tr>
    <tr>
      <th>school_name</th>
      <th>grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Campbell High School</th>
      <th>10th</th>
      <td>93.88</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>94.08</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>93.71</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>93.47</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Galloway High School</th>
      <th>10th</th>
      <td>93.96</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>93.98</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>94.13</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>94.07</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Glass High School</th>
      <th>10th</th>
      <td>77.32</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.13</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>76.62</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>76.44</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Gomez High School</th>
      <th>10th</th>
      <td>93.97</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>93.81</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>94.13</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>94.19</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Gonzalez High School</th>
      <th>10th</th>
      <td>94.10</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>94.42</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>94.04</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>94.04</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Hawkins High School</th>
      <th>10th</th>
      <td>77.17</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.53</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>76.85</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>76.52</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Kelly High School</th>
      <th>10th</th>
      <td>77.27</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.64</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>76.97</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>76.37</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Macdonald High School</th>
      <th>10th</th>
      <td>94.14</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>93.80</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>93.67</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>94.05</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Miller High School</th>
      <th>10th</th>
      <td>94.04</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>94.24</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>93.82</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>93.90</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Sherman High School</th>
      <th>10th</th>
      <td>77.11</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.31</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.50</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.29</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Smith High School</th>
      <th>10th</th>
      <td>76.81</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.34</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.75</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>76.86</td>
    </tr>
  </tbody>
</table>
</div>




```python
# **Scores by School Spending**
# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
# use .bin() & groupby (per student budget) 
# Create the names for the four bins
bins = [570, 595, 620, 645, 670]
group_names = ['570-595', '595-620', '620-645', '645-670']
pd.cut(df4["Per Student Budget"], bins, labels=group_names)
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#  * Overall Passing Rate (Average of the above two)
df5 = df4.drop(df4.columns[[0,1,2,4]], axis=1)
df5["Per Student Budget"] = pd.cut(df5["Per Student Budget"], bins, labels=group_names)
df5["% Overall Passing"] = (df5["% Overall Passing"]).map("%{:.2f}".format)
df5["% Passing Reading"] = (df5["% Passing Reading"]).map("%{:.2f}".format)
df5["% Passing Math"] = (df5["% Passing Math"]).map("%{:.2f}".format)
budget_grouping = df5.groupby("Per Student Budget")
budget_grouping.max()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>Per Student Budget</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>570-595</th>
      <td>83.61</td>
      <td>94.03</td>
      <td>%100.00</td>
      <td>%100.00</td>
      <td>%100.00</td>
    </tr>
    <tr>
      <th>595-620</th>
      <td>83.84</td>
      <td>94.03</td>
      <td>%100.00</td>
      <td>%100.00</td>
      <td>%100.00</td>
    </tr>
    <tr>
      <th>620-645</th>
      <td>83.44</td>
      <td>94.14</td>
      <td>%100.00</td>
      <td>%88.72</td>
      <td>%94.36</td>
    </tr>
    <tr>
      <th>645-670</th>
      <td>81.54</td>
      <td>77.29</td>
      <td>%100.00</td>
      <td>%89.45</td>
      <td>%94.72</td>
    </tr>
  </tbody>
</table>
</div>




```python
# **Scores by School Size**

# * Repeat the above breakdown, but this time group schools based on a reasonable approximation of school size (Small, Medium, Large).
bins = [0, 2000, 3500, 5000]
group_names = ['Small', 'Medium', 'Large']
df6 = df4.drop(df4.columns[[0,1,2,3]], axis=1)
df6["School Size Level"]= pd.cut(df6["Total Student"], bins, labels= group_names)
df6["% Overall Passing"] = (df6["% Overall Passing"]).map("%{:.2f}".format)
df6["% Passing Reading"] = (df6["% Passing Reading"]).map("%{:.2f}".format)
df6["% Passing Math"] = (df6["% Passing Math"]).map("%{:.2f}".format)
size_grouping = df6.groupby("School Size Level")
size_grouping.max()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Student</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>School Size Level</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small</th>
      <td>1855</td>
      <td>83.78</td>
      <td>94.14</td>
      <td>%100.00</td>
      <td>%100.00</td>
      <td>%100.00</td>
    </tr>
    <tr>
      <th>Medium</th>
      <td>3307</td>
      <td>83.84</td>
      <td>94.03</td>
      <td>%100.00</td>
      <td>%89.45</td>
      <td>%94.72</td>
    </tr>
    <tr>
      <th>Large</th>
      <td>4954</td>
      <td>81.72</td>
      <td>77.15</td>
      <td>%100.00</td>
      <td>%89.28</td>
      <td>%94.64</td>
    </tr>
  </tbody>
</table>
</div>




```python
# **Scores by School Type**

# * Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).
df7 = df4.drop(df4.columns[[1,2,3,4]], axis=1)
type_grouping = df7.groupby("School Type").mean()
type_grouping.reset_index(inplace=True)

type_grouping.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Charter</td>
      <td>83.638333</td>
      <td>93.983333</td>
      <td>100.0</td>
      <td>100.000</td>
      <td>100.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>District</td>
      <td>81.546000</td>
      <td>77.034000</td>
      <td>100.0</td>
      <td>88.984</td>
      <td>94.492</td>
    </tr>
  </tbody>
</table>
</div>



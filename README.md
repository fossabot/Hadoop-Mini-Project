# Hadoop-Mini-Project


Testing without Hadoop

```head -n 5 h1b_kaggle.csv | python group_by_mapper.py 5 6 | sort -k1,1 | python reducer.py```


**group_by_mapper** 

- Take 1 column as key and other column as value

Command Line arguments for ```group_by_mapper``` are ```key_column``` and ```aggregate_column```

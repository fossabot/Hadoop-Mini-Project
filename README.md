# Hadoop-Mini-Project
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fitssuyog96%2FHadoop-Mini-Project.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fitssuyog96%2FHadoop-Mini-Project?ref=badge_shield)


Dataset: [H-1B Visa Petitions 2011-2016](https://www.kaggle.com/nsharan/h-1b-visa/data)

Testing without Hadoop

$ ```head -n 5 h1b_kaggle.csv | python group_by_mapper.py 5 6 | sort -k1,1 | python value_summation_reducer.py```

*Requires python 3+*


**group_by_mapper** 

- Take 1 column as key and other column as value

Command Line arguments for ```group_by_mapper``` are ```key_column``` and ```aggregate_column```

$ ```python run.py group_by 5 6 h1b_kaggle.csv```

## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fitssuyog96%2FHadoop-Mini-Project.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fitssuyog96%2FHadoop-Mini-Project?ref=badge_large)
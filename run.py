import hadoop

"""
data = file in hadoop

mapper arguments in case of group_by_mapper in bellow example is 
groupby = 5th column
aggretate = 6th column
"""

result = hadoop.execute(data='test.csv',
                mapper='group_by_mapper.py', mapper_arguments=[5,6],
                reducer='value_summation_reducer.py',
                hadoop_path='bin/hadoop', streaming_path='/usr/local/hadoop-2.7.0/share/hadoop/tools/lib/hadoop-streaming-2.7.0.jar',
                )

print('output is',result)
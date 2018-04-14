import hadoop


result = hadoop.execute(data='h1b_kaggle.csv',
                mapper='group_by_mapper.py', mapper_arguments=[6,5],
                reducer='value_summation_reducer.py',
                hadoop_path='hadoop', streaming_path='/usr/local/hadoop-2.7.0/share/hadoop/tools/lib/hadoop-streaming-2.7.0.jar',
                )

print(result)
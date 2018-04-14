import os

# os.popen: returns terminal output after execution

def output_fetch(output_dir, output_file='part-r-00000'):
    """
    :param output: name of the output directory in hadoop
    :return: returns the data as dict
    """

    data_fetch_command = """
        hadoop fs -cat {output_dir}/{output_file}
    """.format(output_dir=output_dir,output_file=output_file)

    data = os.popen(data_fetch_command).read().split('\n')

    result = {}
    for key, value in [i.split('\t') for i in data]:
        result[key] = value
    return result

def directory_exists(dir_name):
    """
    :param dir_name: name of directory on hdfs
    :return: True if directory exists
    """

    command = "hadoop fs -ls | grep '{name}'".format(name = dir_name)

    output = os.popen(command).read()

    return True if len(output) else False

count = 0

def find_unique_output_dir(desired_name='output'):
    global count
    name = desired_name

    while True:
        name = desired_name + str(count)
        if not directory_exists(directory_exists):
            return desired_name
        count +=1

def execute(data, mapper, reducer, hadoop_path = 'bin/hadoop', streaming_path = 'contrib/streaming/hadoop-*streaming*.jar' ,mapper_arguments=None, reducer_arguments=None, output = 'output'):
    """
    :param data: location of data on hdfs
    :param mapper:  mapper file
    :param reducer: reducer file
    :param mapper_arguments: any arguments to pass to mapper
    :param reducer_arguments: any arguments to pass to reducer
    :param output:  optional desired output file
    :return:
    """

    if directory_exists(output):
        output = find_unique_output_dir(output)

    if mapper_arguments:
        mapper_arguments = [str(i) for i in mapper_arguments]
        mapper_arguments = "'"+mapper +' '+' '.join(mapper_arguments) + "'"
    else:
        mapper_arguments = mapper

    if reducer_arguments:
        reducer_arguments = [str(i) for i in reducer_arguments]

        reducer_arguments = "'" + mapper +' '+ ' '.join(reducer_arguments) + "'"
    else:
        reducer_arguments = reducer

    command = """{hadoop_path} jar {streaming_path} \
         -mapper {mapper_arguments}    -file {mapper}  \
         -reducer {reducer_arguments}    -file {reducer}  \
        -input {input}  -output {output}
    """.format(hadoop_path=hadoop_path,mapper=mapper, mapper_arguments = mapper_arguments, reducer_arguments = reducer_arguments, reducer=reducer, input=data, output=output, streaming_path=streaming_path)

    print(command)

    os.popen(command)

    return output_fetch(output)


"""
bin/hadoop jar /usr/local/hadoop-2.7.0/share/hadoop/tools/lib/hadoop-streaming-2.7.0.jar \
 -mapper 'group_by_mapper.py 7 6' -file group_by_mapper.py \
 -reducer value_summation_reducer.py -file value_summation_reducer.py \
 -input test.csv -output output_dir1 \
"""
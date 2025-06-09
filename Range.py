from pyspark import SparkContext

def main():
  
    sc = SparkContext(appName = 'VisibilityRangeByStation')
    
    input_rdd = sc.textFile('/home/13student13/input_Project/Project_Data')
   
    filtered_rdd = input_rdd.filter(lambda line: line[78:84] != "999999" and int(line[84:85]) in [0, 1, 4, 5, 9])
    
    station_visibility_rdd = filtered_rdd.map(lambda line: (line[4:10], int(line[78:84])))

    station_max_visibility_rdd = station_visibility_rdd.reduceByKey(lambda v1, v2: max(v1, v2))

    station_min_visibility_rdd = station_visibility_rdd.reduceByKey(lambda v1, v2: min(v1, v2))

    station_visibility_min_max_rdd = station_max_visibility_rdd.join(station_min_visibility_rdd)

    station_visibility_range_rdd = station_visibility_min_max_rdd.mapValues(lambda min_max: min_max[0] - min_max[1])

    station_visibility_output_rdd = station_visibility_range_rdd.map(lambda x: (x[0], x[1]))

    station_visibility_output_rdd.saveAsTextFile('/home/13student13/outputProjectPart25')

    sc.stop()

if __name__ == "__main__":
    main()



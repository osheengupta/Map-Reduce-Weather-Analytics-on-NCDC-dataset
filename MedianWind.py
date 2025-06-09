from mrjob.job import MRJob

import re
import sys

class MRMedianWind (MRJob):
    def mapper (self, _, line):
        val = line.strip()
        (year_mnth, dir, q) = (val[15:21], val[60:63], val[63:64])
        if (dir != "999" and re.match("[01459]", q)):
            yield year_mnth, int(dir)

    def reducer (self, year_mnth, dir):
        wind_dir_list = list(dir)
        wind_dir_list.sort()
        
        n = len(wind_dir_list)
        if n % 2 == 0:
            median = (wind_dir_list[n // 2 - 1] + wind_dir_list[n // 2]) / 2
        else:
            median = wind_dir_list[n // 2]
        
        yield year_mnth, median 

if __name__ == '__main__':
    MRMedianWind.run()
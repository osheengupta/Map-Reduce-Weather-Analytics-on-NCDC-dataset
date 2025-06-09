from mrjob.job import MRJob

import re
import sys

class MRWeatherStationVisibility(MRJob):
    def mapper (self, _, line):
        val = line.strip()
        (usaf_id, visibility, q) = (val[4:10], val[78:84], val[84:85])
        if visibility != "999999" and re.match("[01459]", q):
            yield usaf_id, int(visibility)

    def reducer(self, usaf_id, visibilities):
        for visibility in visibilities:
            yield usaf_id, visibility

if __name__ == '__main__':
    MRWeatherStationVisibility.run()
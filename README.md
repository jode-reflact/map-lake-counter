# Lake counter on a given 2D-map

A small script to count lakes in a 2D-map. The map is represented through a matrix of 0 and 1.
1 stands for the presence of a lake, while 0 represents land.
Lakes can be connected to each other vertically and horizontally, which means that they should be counted as 1 lake.

Example map:
[\
  [0,1,1,0,0,1,1,0],\
  [0,0,0,0,1,1,0,0],\
  [0,1,1,1,1,1,1,1]\
]\
In this example the correct lake count would be 2.

The script outputs the lake count for the given map. I have also added 4 test cases to further test the function.

#Given area coverage of one can, height and width of the wall, output the number of cans required to paint the entire wall\
import math
def calculate(coverage, height, width):
    num = (height*width)/coverage;
    num = math.ceil(num);
    print("Number of cans required to paint the wall:",num);

calculate(5, 10 , 10.3);
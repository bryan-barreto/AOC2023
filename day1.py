import re
import math

sample = open("sample/day1.txt").read()
sampletwo = open("sample/day1part2.txt").read()
input = open("input/day1.txt").read()

value_list = ["1","2","3","4","5","6","7","8","9","one","two","three","four","five","six","seven","eight","nine"]
names_to_value = { "one":"1",
         "two":"2",
         "three":"3",
         "four":"4",
         "five":"5",
         "six":"6",
         "seven":"7",
         "eight":"8",
         "nine":"9"
    }


def calibrate(input):
    to_cal = input.split("\n")
    value = 0
    for x in to_cal:
        first = None
        second = None
        numbers = re.findall("(\d)", x)
        for y in numbers:
            if first == None:
                first = y
            else:
                second = y
        if second == None:
            second = first
        toAdd = int(first+second)
        value += toAdd
    return value
            
def cal_with_words(input):
    to_cal = input.split("\n")
    total = 0
    for x in to_cal:
        first = None
        first_pos = math.inf
        
        second = None
        second_pos = 0
        
        for test_value in value_list:
            find_first = x.find(test_value)
            last_pos = x.rfind(test_value)
            if find_first != -1 and find_first < first_pos:
                first = test_value
                first_pos = find_first
            if last_pos != -1 and last_pos > second_pos:
                second = test_value
                second_pos = last_pos
        try:
            first = int(first)
        except:
            first = names_to_value[first]
        
        if second == None:
            second = first
        try:
            second = int(second)
        except:
            second = names_to_value[second]
        
        total += int(str(first) + str(second))
    return total
        
        
        
        
    

# print(calibrate(input))
print(cal_with_words(sampletwo))
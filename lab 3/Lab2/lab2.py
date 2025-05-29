print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu(): 
 print("display_main_menu ")

def calc_average(): 
 print("calc_average")


def get_user_input() :
    print("Enter temp values")
    temp_values = input("Enter temperature values separated by spaces: ")
    temp_values = temp_values.split()
    temp_values = [float(value) for value in temp_values]
    return temp_values

def calc_average_temperature(temp_values) :
    average_temp = sum(temp_values) / len(temp_values)
    return average_temp

def calc_min_max_temperature(temp_values) :
    min_temp = min(temp_values)
    max_temp = max(temp_values)
    return min_temp, max_temp

def sort_temperatures(temp_values) :
    sorted_temp = sorted(temp_values)
    return sorted_temp

def calc_median_temperature(temp_values):
    sorted_temp = sorted(temp_values)
    n = len(sorted_temp)
    if n % 2 == 0:
        median_temp = (sorted_temp[n//2 - 1] + sorted_temp[n//2]) / 2
    else:
        median_temp = sorted_temp[n//2]
    return median_temp

def main():
      temp_values=get_user_input()
      avg_temp=calc_average_temperature(temp_values)
      print("Average temperature:" + str(avg_temp))
      min_temp,max_temp=calc_min_max_temperature(temp_values)
      print("Minimum temperature:" + str(min_temp))
      print("Maximum temperature:" + str(max_temp))
      sorted_temp=sort_temperatures(temp_values)
      print("Sorted temperatures:" + str(sorted_temp))
      median_temp=calc_median_temperature(temp_values)
      print("Median temperature:" + str(median_temp))

if __name__ == "__main__": 
 main() 
        
    
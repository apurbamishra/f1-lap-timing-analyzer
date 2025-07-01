import sys

def input_file(file_name):
    """Reads the file and returns its contents as a list of lines."""
    with open(file_name, "r") as lap_times_file:
        file_lines = lap_times_file.readlines()
        return file_lines

def race_name(file_lines):
    """Returns the race location from the first line of the file."""
    race_location = file_lines[0]
    return race_location

def driver_data(file_lines):
    """Extracts driver names and lap times from the file."""
    driver_name = []
    lap_times = []
    for line in file_lines[1:]:
        driver_name.append(line[:3])  # Driver code
        lap_times.append(float(line[3:]))  # Lap time
    return driver_name, lap_times

def fastest_driver(driver_name, lap_times):
    """Finds and returns the fastest driver and their time."""
    fastest_driver = driver_name[0]
    fastest_time = lap_times[0]
    for i in range(1, len(driver_name)):
        if lap_times[i] < fastest_time:
            fastest_driver = driver_name[i]
            fastest_time = lap_times[i]
    return fastest_driver, fastest_time

def average_time(lap_times):
    """Calculates and returns the average lap time."""
    sum_of_times_value = sum(lap_times)
    number_of_times_value = len(lap_times)
    average_time = sum_of_times_value / number_of_times_value
    return average_time

def main_function(file_name):
    """Processes the file and returns race location, fastest driver, fastest time, and average time."""
    file_contents = input_file(file_name)
    race_location = race_name(file_contents)
    driver_code, times_data = driver_data(file_contents)
    fastest_driver_name, fastest_time_value = fastest_driver(driver_code, times_data)
    avg_time = average_time(times_data)
    
    return race_location, fastest_driver_name, fastest_time_value, avg_time  

def print_contents():
    """Checks for the file argument and processes it to display the results."""
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        race_location, fastest_driver_name, fastest_time_value, avg_time = main_function(file_name)
        print(f"\nThe location of the race is: {race_location}")
        print(f"The three-letter code of the driver with the current fastest time is {fastest_driver_name} : {fastest_time_value} seconds.")
        print(f"\nThe overall average time is {avg_time:.3f} seconds.")
    else:
        print("Error: File is missing. Please input the file name.")

# calling function to print the contents 
print_contents()

# 🏎️ Formula 1 Timings Board

This Python program analyzes lap time data from Formula 1 practice sessions to provide insights into driver performance.

## ✨ Features

- 📂 Reads an input file containing the Grand Prix location and lap times recorded by multiple drivers.  
- 🏁 Displays the location of the race.  
- 🥇 Identifies the driver with the fastest lap time (three-letter code) and the corresponding time.  
- 📊 Calculates and displays the overall average lap time across all recorded laps.  

## 📄 Input File Format

- The **first line** contains the location of the Grand Prix (a string).  
- Each **subsequent line** contains a driver’s three-letter code immediately followed by their lap time (a floating-point number with three decimal places).  

### 📝 Example input file (`lap_times_sample.txt`):
Dewsbury
SAI111.875 <br>
STR103.844 <br>
MAG117.792 <br>
NOR100.211 <br>
SAI105.628 <br>
GAS108.142 <br>
...

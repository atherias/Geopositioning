import csv
import os

def parse_files(input_file):
    #Converts .txt file output by Homedale app into .csv for analysis
    fout = "parsed_{0}.csv".format(input_file[:-4])
    with open(input_file,"r") as fin:
        with open(fout, "w", newline='') as csvfile:
            text_writer = csv.writer(csvfile, delimiter=",")
            header = ["date", "mac", "provider", "access_point", "signal_strength", "quality,unknown2", "frequency",
                      "stations", "device", "station_count"]
            text_writer.writerow(header)
            all_lines = fin.readlines()
            split_lines = []
            for line in all_lines:
                if "eduroam" in line:
                    split_line = line.split("\t")
                    split_lines.append(split_line)
                    text_writer.writerow(split_line)
                else:
                    continue

#directly parses all files in a designated folder
for filename in os.listdir("C:/Users/Adele/Documents/TU-Delft/Q2/GEO1003 - Geopositioning/Lab 3 - Wifi Fingerprinting/Geopositioning"):
    if filename.startswith("measurement") and filename.endswith(".txt"):
        parse_files(filename)
    else:
        continue
import csv
import os

def parse_files(input_file):
    # create output file name from input file name
    fout = "parsed_{0}.csv".format(input_file[:12])
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


# parse_files("measurement10-group2.txt")

for filename in os.listdir("C:/Users/Adele/Documents/TU-Delft/Q2/GEO1003 - Geopositioning/Lab 3 - Wifi Fingerprinting"):
    if filename.startswith("room"):
         # print(os.path.join(directory, filename))
        parse_files(filename)
    else:
        continue
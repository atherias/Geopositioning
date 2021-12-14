import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

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

def identify_location(input_file):
    # read CSV file (note: first row considered the header, so it starts from row 2)
    mystery_location = pd.read_csv(input_file,sep=",",index_col = False, usecols=["mac","signal_strength"])
    mystery_mac_mean_signal = mystery_location.groupby('mac').mean().sort_values('mac')
    # ax1 = mystery_mac_mean_signal.plot(mystery_mac_mean_signal)
    # plt.show()

    # top_10_mac_mean = mac_mean_signal.sort_values('signal_strength').head(10)
    for filename in os.listdir("C:/Users/Adele/Documents/TU-Delft/Q2/GEO1003 - Geopositioning/Lab 3 - Wifi Fingerprinting/Geopositioning"):
        if filename.startswith("parsed") and filename.endswith(".csv"):
            reference_location = pd.read_csv(filename, sep=",", index_col=False, usecols=["mac", "signal_strength"])
            reference_mac_mean_signal = reference_location.groupby('mac').mean().sort_values('mac')
            plt_reference = ax2.plt.plot(reference_mac_mean_signal)
            fig,(ax1,ax2) = plt.subplots(2)
            ax1.plot(mystery_mac_mean_signal)
            ax2.plot(reference_mac_mean_signal)
            plt.show()
            # fig, (plt_mystery, plt_reference) = plt.subplots(2)
            # plt.show()
        else:
            continue

identify_location("parsed_measurement16-group4.csv")

# for filename in os.listdir("C:/Users/Adele/Documents/TU-Delft/Q2/GEO1003 - Geopositioning/Lab 3 - Wifi Fingerprinting/Geopositioning"):
#     if filename.startswith("parsed") and filename.endswith(".csv"):
#         identify_location(filename)
#     else:
#         continue
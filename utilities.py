import csv, datetime

def convertTimestamps(infile, outfile):
  with open(infile) as csv_file:
    with open(outfile, mode='w') as modified_file:
      reader = csv.reader(csv_file)
      writer = csv.writer(modified_file, delimiter=',')

      skip = True  # boolean flag to skip the first row
      for row in reader:
        if skip:
          skip = False
          writer.writerow(row)
          continue

        duplicate = row.copy()
        parsed = datetime.datetime.strptime(row[2], "%Y-%m-%dT%H:%M:%S")
        time = parsed.hour + (parsed.minute / 60)
        duplicate[2] = round(time, 2)
        writer.writerow(duplicate)

convertTimestamps('./data/ExplicitClasses.csv', './data/DataV1.csv')
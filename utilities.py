import csv, datetime, operator

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

def convertToOtherClasses(infile, outfile, numOther):

  counter = {}
  with open(infile) as csv_file:
    reader = csv.reader(csv_file)

    skip = True
    for row in reader:
      if skip:
        skip = False
        continue

      if row[20] not in counter.keys():
        counter[row[20]] = 1
      else:
        counter[row[20]] += 1

    sorted_counter = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
    keep = sorted_counter[0:numOther]
    keep_names = [tup[0] for tup in keep]

  with open(infile) as csv_file:
    with open(outfile, mode='w') as modified_file:
      reader = csv.reader(csv_file)
      writer = csv.writer(modified_file, delimiter=',')

      inner_skip = True
      for row in reader:
        if inner_skip:
          inner_skip = False
          writer.writerow(row)
          continue

        duplicate = row.copy()
        if duplicate[20] not in keep_names:
          duplicate[20] = 'Other'

        writer.writerow(duplicate)

#convertTimestamps('./data/ExplicitClasses.csv', './data/DataV1.csv')
convertToOtherClasses('./data/DataV1.csv', './data/DataV2.csv', 20)
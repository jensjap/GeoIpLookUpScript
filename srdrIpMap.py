#!/Users/jensjap/.virtualenvs/GeoIP/bin/python

# getopt code from: http://www.tutorialspoint.com/python/python_command_line_arguments.htm

import sys, getopt
import GeoIP

def main(argv):
  inputfile = ''
  outputfile = ''
  try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
    print('srdrIpMap.py -i <inputfile> -o <outputfile>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print('srdrIpMap.py -i <inputfile> -o <outputfile>')
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg
  print('Input file is "', inputfile)
  print('Output file is "', outputfile)
  if inputfile != '':
    if outputfile != '':
      processFile(inputfile, outputfile)
    else:
      processFile(inputfile)

def processFile(inputfile, outputfile=False):
  # Instantiate GeoIP object.
  gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

  # Output file is provided: we write to it.
  if outputfile:
    with open(inputfile, 'r', encoding='utf-8') as infile, open(outputfile, 'w') as outfile:
      for line in infile:
        line = line.strip()
        line = "%s,%s\n" % (line, gi.country_code_by_addr(line))
        outfile.write(line)

  # No output file is provided: we write to console.
  else:
    with open(inputfile, 'r', encoding='utf-8') as infile:
      for line in infile:
        line = line.strip()
        print("%s: %s" % (line, gi.country_code_by_addr(line)))



if __name__ == "__main__":
  main(sys.argv[1:])

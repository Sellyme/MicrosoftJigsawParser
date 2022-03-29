import csv
import sys
import xml.etree.ElementTree as ET

#grab whatever XML file is passed in from the CLI
filename = sys.argv[1]

#load the XML tree
f = open(filename, encoding='utf-8')
tree = ET.parse(f)
root = tree.getroot()

#pull out the group metadata + puzzles list
group = root.find("./Groups/Group")
puzzles = root.findall("./Groups/Group/Puzzle")

#and turn these into strings
group_name = group.attrib["title"]
for i in range(0, len(puzzles)):
	print(group_name, "–", puzzles[i].attrib["title"])
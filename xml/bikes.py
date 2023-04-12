import re
import zipfile

from lxml import etree

z5 = zipfile.ZipFile("/stat129/download990xml_2020_1.zip")

fnames = z5.namelist()


# Let's look at one of the files
f0 = z5.open(fnames[0])
tree = etree.parse(f0)

# https://stackoverflow.com/questions/4255277/lxml-etree-xmlparser-remove-unwanted-namespace
nodes = tree.xpath("//*[local-name() = 'DescriptionProgramSrvcAccomTxt']")

desc = [n.text for n in nodes]

pattern = re.compile(r'vision challenge|visually handicap', re.IGNORECASE)

matches = [d for d in desc if pattern.search(d)]

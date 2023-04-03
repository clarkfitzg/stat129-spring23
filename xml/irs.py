import zipfile
from lxml import etree

# 65,551 tax returns in one file
zf = "/Users/fitzgerald/Downloads/download990xml_2020_1.zip"
z = zipfile.ZipFile(zf)

n = 5
fnames = z.namelist()[:n]

with zipfile.ZipFile("first-5-tax-returns.zip", "w") as znew:
    for fn in fnames:
        zipdata = z.read(fn)
        znew.writestr(fn, zipdata)


# For class

z5 = zipfile.ZipFile("first-5-tax-returns.zip")

fnames = z5.namelist()

# Let's look at one of the files
f0 = z5.open(fnames[0])
tree = etree.parse(f0)

tree.write("return.xml", pretty_print=True)


tree.xpath("//ProgramSrvcAccomplishmentGrp")

# https://stackoverflow.com/questions/4255277/lxml-etree-xmlparser-remove-unwanted-namespace
nodes = tree.xpath("//*[local-name() = 'DescriptionProgramSrvcAccomTxt']")

text = [n.text for n in nodes]


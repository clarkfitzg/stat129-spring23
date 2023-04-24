import zipfile
from multiprocessing import Pool
import glob

from lxml import etree

# Start with an empty function

def extract1(fname, zf):
    """
    Extract elements of interest
    fname: IRS 990 XML file
    zf: ZipFile where fname is stored
    """
    f = zf.open(fname)
    tree = etree.parse(f)
    ns = {'irs':'http://www.irs.gov/efile'}

    # Holds everything we're interested in.
    result = {}

    #result["description"] = tree.xpath('//irs:DescriptionProgramSrvcAccomTxt/text()', namespaces = ns)


    result["BusinessName"] = tree.xpath('//irs:Filer/irs:BusinessName/irs:BusinessNameLine1Txt/text()', namespaces = ns)[0]

    result["Year"] = int(tree.xpath('//irs:TaxYr/text()', namespaces = ns)[0])

    # If we're not sure if we'll find anything we can try
    try:
        result["EIN"] = tree.xpath('//irs:Filer/irs:EIN/text()', namespaces = ns)[0]
    except:
        pass

    return result


def extract(zname):
    """
    Extract elements of interest
    zname: zipfile
    """
    zf = zipfile.ZipFile(zname)
    f = lambda x: extract1(x, zf)
    result = map(f, zf.namelist())
    return list(result)


x5 = extract("first-5-tax-returns.zip")


# Now we want to do this to a bunch of zip files in parallel
zipfiles = ["first-5-tax-returns.zip", "first-5-tax-returns.zip"]

# Use 4 parallel processes
with Pool(4) as p:
    result0 = p.map(extract, zipfiles)


# Moving on to the whole data set:
allzipfiles = glob.glob("/stat129/*.zip")

with Pool(4) as p:
    result = p.map(extract, allzipfiles)




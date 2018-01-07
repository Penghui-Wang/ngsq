import sys
import os
import json

dirname = os.path.dirname(os.path.abspath(__file__))
dirname = os.path.join(dirname,"../")
sys.path.append(dirname)
from ngsqc.fastqc.FastQC import FastQC
from ngsqc.arranger.arranger import arranger


def main(fqjson,prefix):
    # load input files
    fqs = []
    indict = json.loads(open(fqjson).read())
    for prex,pair in indict.items():
        for item in pair:
            fqs.append(item)

    # start pipeline 
    qcer = FastQC(fqs,prefix)
    qcer.byfastqc()
    qcer.byfastp()

    # arranger out file to attachment
    arr = arranger(prefix)
    arr.arrange()



if __name__ == "__main__":
    usage = '''
Usage:
    fastQc.py -i <json> -o <prefix>
    fastQc.py -h | --help
    fastQc.py -v | --version

Options:
    -h --help                         print usage
    -v --version                      print version information
    -i <json> --input <json>           json generated by smartFqs
    -o <prefix> --outprefix <prefix>  output prefix
    
    '''   

    from docopt import docopt
    args = docopt(usage) 
    ijson = args["--json"]
    prex = args["--outprefix"]
    main(ijson,prex) 




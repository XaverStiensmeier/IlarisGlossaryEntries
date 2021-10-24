#!/usr/bin/env python3
import argparse
import computeFunctions as CF
import xml.etree.ElementTree as ET

tagIdent = {
    "Rüstung" : CF.computeRuestung,
    "Vorteil" : CF.computeVorteil,
    "Manöver" : CF.computeManoever,
    "Talent" : CF.computeTalent,
    "Fertigkeit" : CF.computeFertigkeit,
    "Übernatürliche-Fertigkeit" : CF.computeUFertigkeit,
    "Waffe" : CF.computeWaffe,
    "Waffeneigenschaft" : CF.computeWaffeneigenschaft,
    "FreieFertigkeit" : CF.computeFreieFertigkeit
}

parser = argparse.ArgumentParser(description='Creates an ilaris-glossary for LaTeX from a datenbank.xml file')
parser.add_argument('-d','--database', default='datenbank.xml',
                    help='path to database')

args = parser.parse_args()
tree = ET.parse(args.database)
root = tree.getroot()

for child in root:
    tagIdent[child.tag](child)
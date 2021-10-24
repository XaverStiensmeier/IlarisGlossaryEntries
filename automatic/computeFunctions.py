#!/usr/bin/env python3
base = """
\\newglossaryentry{{{id}}}
{{
    name={{{name}}},
    description={{{description}}}
}}
"""
def uncapitalize(s):
  if len(s) > 0:
    s = s[0].lower() + s[1:]
  return s

def firstCap(s):
  if len(s) > 0:
    s = s[0].upper() + s[1:]
  return s

def getInfoDesc(content, allRemove):
    desc = content.text.strip("\n").replace("\n\n","\\newline ").replace("\n","\\newline ").replace("&","\&") if content.text else ""
    keys = content.keys()
    info = ""
    for elem in allRemove:
        if elem in keys: keys.remove(elem)
    for key in keys:
        if(content.attrib[key]):
            info += "\\textbf{{{name}}}: {value} ".format(name=firstCap(key), value=firstCap(content.attrib[key]))
    info = info[:-1] + "\\newline "
    print(base.format(id=(uncapitalize(content.attrib["name"])+"_"+content.tag).replace(" ", ""), name=firstCap(content.attrib["name"]), 
        description=info.replace("\n","")+desc))

rstyp = ["Stoffrüstung", "Lederrüstung", "Holz- oder Knochenrüstung", "Ketten- oder Schuppenrüstung", "Plattenrüstung"]

def computeRuestung(content):
    allRemove = ["name", "system", "typ"]
    getInfoDesc(content, allRemove)
def computeVorteil(content):
    allRemove = ["name", "typ", "variable", "kommentar", "script", "csBeschreibung", "linkKategorie", "linkElement", "csAuflisten"]
    getInfoDesc(content, allRemove)
def computeManoever(content):
    allSame(content)
def computeTalent(content):
    allSame(content)
def computeFertigkeit(content):
    allSame(content)
def computeUFertigkeit(content):
    allSame(content)
def computeWaffe(content):
    print()
    desc = content.text.strip("\n").replace("\n\n","\\newline ").replace("\n","\\newline ").replace("&","\&") if content.text else ""
    keys = content.keys()
    chosen=""
    if "wm" in keys:
        chosen = "\\textbf{{WM}}: {wm}".format(wm=content.attrib["wm"])
    else:
        chosen = "\\textbf{{LZ}}: {lz}".format(lz=content.attrib["lz"])
    info = """\\textbf{{TP}}: {w}W6+{b} \\textbf{{RW}}: {rw} {wmlz} \\textbf{{Härte}}: {haerte}
        \\textbf{{Fertigkeit}}: {fertigkeit} \\textbf{{Talent}}: {talent}""".format(w=content.attrib["W6"], b=content.attrib["plus"], haerte=content.attrib["haerte"], 
        fertigkeit=content.attrib["fertigkeit"], talent=content.attrib["talent"], rw=content.attrib["rw"], wmlz=chosen)
    print(base.format(id=(uncapitalize(content.attrib["name"])+"_"+content.tag).replace(" ", ""), name=firstCap(content.attrib["name"]), 
        description=info.replace("\n","")+" \\textbf{{Eigenschaften}}: " + str(desc)))
def computeWaffeneigenschaft(content):
    allSame(content)
def computeFreieFertigkeit(content):
    print(base.format(id=uncapitalize(content.text).replace(" ", ""), name=firstCap(content.text), description="Sprache"))

def allSame(content):
    print(base.format(id=(uncapitalize(content.attrib["name"])+"_"+content.tag).replace(" ", ""), name=firstCap(content.attrib["name"]), 
        description=content.text.strip("\n").replace("\n\n","\\newline ").replace("\n","\\newline ").replace("&","\&") if content.text else ""))
# IlarisGlossaryEntries
Glossary entries for the ilaris rpg

## Contribute
Ihr könnt gerne einfach selbst Glossary-Einträge schreiben und zur Einbindung vorschlagen. Dafür benötigt man kein Berufsgeheimnis ;)

```
\newglossaryentry{einzigartigeid}
{
    name={wunderschönerAnzeigeName},
    description={Beschreibung aus dem offiziellen Regelwerk mit sinnvollen Kürzungen/Umformulierungen, wo nötig oder angebracht.}
}
```

Dabei sollten Begriffe, die in der Beschreibung vorkommen auch schon verlinkt werden:
`\gls{begriff}` verlinkt den Begriff mit dem wunderschönerAnzeigeName. Manchmal ist die deutsche Grammatik da aber ein Hindernis und man muss den Fall anpassen. In dem Fall benutzt man `\glslink{begriff}{NeuerWunderschönerAnzeigenameFürDiesenFall}`

Eine Abkürzung kann über:
```
\newacronym{einzigartigeid}{Abkürzungsname}{\gls{iddeseigentlichenBegriffsmitErklärung}}
```

Beispiel:
```
\newglossaryentry{erfahrungspunkte}
{
    name={Erfahrungspunkte},
    description={Erfahrungspunkte sind die Währung, mit der du die Werte deines Charakters weiterentwickelst, sodass dein Charakter immer größere Herausforderungen bestehen kann.}}
    
\newacronym{ep}{EP}{\gls{erfahrungspunkte}}
```

## Use
1. https://ctan.org/pkg/glossaries?lang=en
2. https://en.wikibooks.org/wiki/LaTeX/Glossary

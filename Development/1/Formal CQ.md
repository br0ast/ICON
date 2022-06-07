# Formal Competency Questions

## CQ 1.1
What level 1 objects are represented in the artwork?

### CQ 1.1.1

Retrieve all the artistic motifs of `ART1004`.

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?am WHERE {
?icrec icon:aboutWorkOfArt d:ART1004; 
     {?icrec icon:recognizedArtisticMotif ?am} UNION {?icrec icon:recognizedComposition ?comp. ?comp icon:hasPart ?am }

} 

```
### CQ 1.1.2

Retrieve all the compositions of `ART1004`.
```
PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?comp WHERE {
?icrec icon:aboutWorkOfArt d:ART1004; 
  icon:recognizedComposition ?comp. 

}
```

### CQ 1.1.3

Retrieve all the pre-iconographical descriptions of `ART1201` along with the person responsible of the interpretation.

```SPARQL
PREFIX d: <http://icondataset.org/> 
prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?desc ?person WHERE {
?rec icon:aboutWorkOfArt d:ART1201; # ART1196 . ART1201 ha errore di conversione: non risulta preicdesc1!
    icon:isListedIn ?desc; 
    crm:P14_carried_out_by ?person. 
?desc a icon:PreiconographicalDescription.

} LIMIT 100
```

## CQ 1.2
Which objects are natural elements, expressive characteristics or actions?

### CQ1.2.1

Retrieve all the natural, expressional meanings and actions recognized in the artistic motifs of `ART1195`.

```SPARQL
PREFIX ex: <https://example.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

SELECT DISTINCT ?natural ?expressional?action WHERE {
?icrec icon:aboutWorkOfArt ex:artwork1; 
     {?icrec icon:recognizedArtisticMotif ?am} UNION {?icrec icon:recognizedComposition ?comp. ?comp icon:hasPart ?am }
{?am icon:hasExpressionalMeaning ?expressional} UNION {?am icon:hasFactualMeaning ?natural. ?natural a icon:NaturalElement}
UNION {?am icon:hasFactualMeaning ?action. ?action a icon:Action}
}
```

### CQ 1.2.2 

Which are the natural elements identified in the Preiconographical Description `ART1310-PREICDESC`?

```SPARQL
PREFIX d: <http://icondataset.org/> 
prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

SELECT DISTINCT ?factual WHERE {
?rec icon:isListedIn d:ART1310-PREICDESC. 
?desc a icon:PreiconographicalDescription.
{?rec icon:recognizedArtisticMotif ?am} UNION {?rec icon:recognizedComposition ?comp. ?comp icon:hasPart ?am }
?am icon:hasFactualMeaning ?factual. 
?factual a icon:NaturalElement.
} LIMIT 100
```

### CQ 1.2.3

Retrieve the artistic motifs of Expressional Meaning `smiling`.

```SPARQL
PREFIX d: <http://icondataset.org/> 
prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?am WHERE {

?am icon:hasExpressionalMeaning d:smiling. 

} LIMIT 100
```


## CQ 1.3 
What level 1 subjects are formally derived or copied from other artworks level 1 subjects?



### CQ 1.3.1
What are the level 1 subjects (i.e. copied subjects) copied by `ART1284` from `ART1285`, including the ones identified by a composition? What are the corresponding original subjects in `ART1285` (i.e. subjects)?

```SPARQL
PREFIX d: <http://icondataset.org/> 
prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?subject ?copiedSubject WHERE {
?rec a icon:FormalMotifRecognition; 
    icon:aboutWorkOfArt d:ART1284, d:ART1285. 
{?rec icon:hasPrototypicalMotif ?am. ?am a icon:ArtisticMotif} UNION {?rec icon:hasPrototypicalMotif ?comp. ?comp icon:hasPart ?am}
?am icon:hasFactualMeaning | icon:hasExpressionalQuality ?subject.
{?rec icon:hasCopiedMotif ?copied. ?copied a icon:ArtisticMotif} UNION {?rec icon:hasCopiedlMotif ?comp. ?comp icon:hasPart ?copied}
?copied icon:hasFactualMeaning | icon:hasExpressionalQuality ?copiedSubject
} LIMIT 100
```



### CQ 1.3.2
Retrieve the prototypical Artistic Motif of the Formal Motif Recognition `ART1285ART1284-MOTIFREC2`

```SPARQL
PREFIX d: <http://icondataset.org/> 
prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?am WHERE {
d:ART1285ART1284-MOTIFREC2 icon:hasPrototypicalMotif ?am.
?am a icon:ArtisticMotif.
} LIMIT 100
```

### CQ 1.3.3
Retrieve the copied Artistic Motif of the Formal Motif Recognition `ART1285ART1284-MOTIFREC2`

```SPARQL
PREFIX d: <http://icondataset.org/> 
prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?am WHERE {
d:ART1285ART1284-MOTIFREC2 icon:hasCopiedMotif ?am.
?am a icon:ArtisticMotif.

} LIMIT 100
```

## CQ 1.4

In What compositional structure are the objects organized (e.g. pyramidal arrangement)?

### CQ 1.4.1

What is the compositional structure of the first level subjects in `ART1384`?

```SPARQL
PREFIX d: <http://icondataset.org/> 
prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?compStructure WHERE {
?rec icon:aboutWorkOfArt d:ART1384; 
    icon:recognizedComposition ?comp. 
?comp icon:hasCompositionalStructure ?compStructure. 

} LIMIT 100
```
### CQ 1.4.2

What are the level 1 subjects included in the composition having the compositional structure `vertical-arrangement` in `ART1384`?

```SPARQL
PREFIX d: <http://icondataset.org/> 
prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?lev1 WHERE {
?rec icon:aboutWorkOfArt d:ART1384; 
    icon:recognizedComposition ?comp. 
?comp icon:hasCompositionalStructure d:vertical-arrangement. 
?comp icon:hasPart ?am. 
?am icon:hasFactualMeaning | icon:hasExpressionalMeaning ?lev1.
} LIMIT 100
```
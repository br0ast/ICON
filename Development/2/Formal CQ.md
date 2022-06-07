# Formal Competency Questions

## CQ 2.1
What level 2 subjects are identified in each artwork?

## CQ2.1.1

Retrieve the iconographical descriptions that have been made on `ART1195`.

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?desc WHERE {
?rec icon:isListedIn ?desc; 
    icon:aboutWorkOfArt d:ART1195.
?desc a icon:IconographicalDescription. 

}
```

## CQ2.2 (new code: 2.1.2 - changed)

Retrieve the compositions that appear in ART1195.

```SPARQL

PREFIX ex: <https://example.org/> 
PREFIX symb: <http://www.semanticweb.org/bruno/ontologies/2021/0/symbont#> 
PREFIX symb2: <http://www.semanticweb.org/bruno/ontologies/2021/0/symbont2#> 

SELECT ?composition WHERE {
  ex:workofart2 symb:iscomposedBy ?composition .
  ?composition a symb2:Composition
}

```
changed in: 

Retrieve the compositions that are recognized as a level 2 subject in `workofart2`.

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

SELECT DISTINCT ?comp WHERE {
{?rec icon:recognizedImage ?img} UNION {?rec icon:recognizedInvenzione ?img}
?rec icon:refersToArtisticMotif ?comp; 
    icon:aboutWorkOfArt d:ART1195;
    a icon:IconographicalRecognition.
?comp a icon:Composition. 
}
```
### CQ 2.1.3 (new)

What are the level 2 subjects depicted in ART1195?
```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

SELECT DISTINCT ?lev2 WHERE {
VALUES ?rel {icon:hasCharacter icon:hasPlace icon:hasNamedObject icon:hasPersonification icon:hasEvent}
{?rec icon:recognizedImage ?img} UNION {?rec icon:recognizedInvenzione ?img}
?rec icon:aboutWorkOfArt d:ART1195;
    a icon:IconographicalRecognition.
?img ?rel ?lev2. 
}
```

## CQ 2.2 (new)
Retrieve respectively all the characters, events, personifications, named objects, and places recognised at level 2.

## CQ2.4 (new data: 2.2.1)

Retrieve, from all the iconographical descriptions made on ART1290, all the personifications associated with an artistic motif through an image.

```SPARQL


PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

SELECT DISTINCT ?subject WHERE {
?rec a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt d:ART1290;  
    icon:recognizedImage ?img. 
?img icon:hasPersonification ?subject.  
{?rec icon:refersToArtisticMotif ?am. 
?am a icon:ArtisticMotif} 
UNION 
{?rec icon:refersToArtisticMotif ?comp.
?comp icon:hasPart ?am} 

}

```
## CQ2.6 (new: 2.2.2)

Retrieve all the compositions and their artistic motifs linked by an image to a character in all the iconographical descriptions of ART1195.

```SPARQL


PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

SELECT DISTINCT ?comp ?am WHERE {
?rec a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt d:ART1195;
    icon:recognizedImage ?img; 
    icon:refersToArtisticMotif ?comp.
?comp icon:hasPart ?am.
} 

```

## CQ2.7 (new: 2.2.3)

Retrieve all the places that are recognized to be in ART1195 according to an image. 

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?place WHERE {
?rec a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt d:ART1195;
    icon:recognizedImage ?img. 
?img icon:hasPlace ?place. 

}

```


## CQ2.10 (new: 2.2.4)

Retrieve all the works of art that have an artistic motif or composition associated with the Character "Venus" through the recognition of an image

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?art WHERE {
?rec a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt ?art;
    icon:refersToArtisticMotif ?am;
    icon:recognizedImage ?img. 
?img icon:hasCharacter d:venus. 
}
```


## CQ 2.3 (new) 
In which story or allegory are involved the depicted subjects?


## 2.3.1

Retrieve all the conventional meanings associated to a story in `workofart2`.

changed in: 

Retrieve all the images associated to a second level subject which is part of a story in in ART1197.

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

SELECT DISTINCT ?img WHERE {
VALUES ?rel {icon:hasCharacter icon:hasPlace icon:hasNamedObject icon:hasPersonification icon:hasEvent}
?rec icon:recognizedImage ?img; 
    icon:aboutWorkOfArt d:ART1197;
    a icon:IconographicalRecognition.
?img ?rel ?lev2. 
?rec2 icon:recognizedInvenzione ?story;
        icon:aboutWorkOfArt d:ART1197.
?lev2 icon:partOf ?story.
?story a icon:Story.
}

```

### CQ 2.3.2  (new)
Retrieve all the second level subjects associated to a story in ART1195.</br>


```SPARQL

PREFIX ex: <https://example.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

SELECT DISTINCT ?subject WHERE {
?rec a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt d:ART1195; 
    icon:recognizedImage ?img. 
?img ?rel ?subject. 
?subject icon:partOf ?story. 
?story a icon:Story. 
?rec2 a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt d:ART1195; 
    icon:recognizedInvenzione ?story. 
}

```



## CQ 2.3.3

Retrieve all the iconographical descriptions on ART1379 that contain at least one one second level subject that refers to a story and at least a one second level subject that refers to an allegory.

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

SELECT DISTINCT ?desc WHERE {
?rec a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt d:ART1379; 
    icon:recognizedImage ?img; 
    icon:isListedIn ?desc. 
?img ?rel ?subject. 
{?subject icon:partOf ?story. ?story a icon:Story.} UNION {?subject icon:partOf ?allegory. ?allegory a icon:Allegory.}
}

```

## CQ 2.4 Do the level 2 subjects have a symbolic meaning?

## 2.4.1 

Retrieve all artistic motifs associated to a symbol through the recognition of an image in ART1254

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?am WHERE {
?rec a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt d:ART1254;
    icon:refersToArtisticMotif ?am;
    icon:recognizedImage ?img. 
?img icon:hasSymbol ?symbol. 
?am a icon:ArtisticMotif. 
}

```

## CQ 2.4.2

Retrieve all the iconographical descriptions in which the symbol "Phaeton symbol of the presumptuous" is associated to an artistic motif or a composition in a work of art.

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?desc WHERE {
?rec a icon:IconographicalRecognition; 
    icon:isListedIn ?desc;
    icon:recognizedImage ?img. 
?img icon:hasSymbol d:phaeton-the-presumptuous. 
?am a icon:ArtisticMotif. 
{?rec icon:refersToArtisticMotif ?am. 
?am a icon:ArtisticMotif} 
UNION 
{?rec icon:refersToArtisticMotif ?comp.
?comp icon:hasPart ?am} 
}

```
### CQ 2.4.3 (new)
Retrieve all the characters that share are linked to symbol by means of a common artistic motif or composition in ART1329. 

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?char WHERE {
?rec a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt d:ART1329;
    icon:refersToArtisticMotif ?amOrComp;
    icon:recognizedImage ?img. 
?img icon:hasSymbol ?symbol. 
?rec2 a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt d:ART1329;
    icon:refersToArtisticMotif ?amOrComp;
    icon:recognizedImage ?img2. 
?img2 icon:hasCharacter ?char. 
}

```

## CQ 2.5
which is the object that allows the character recognition at level 2, i.e. the character’s attribute?



### CQ 2.5.1 
Which are the attributes that allows the recognition of Cupid in ART1123? 


```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?lev1 WHERE {
?rec a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt d:ART1123;
    icon:recognizedImage ?img. 
?img icon:hasCharacter d:cupid; 
    icon:hasRecAttribute ?am.
?am icon:hasFactualMeaning | icon:hasExpressionalMeaning ?lev1. 



}

```



### CQ 2.5.2 

What are the level 1 objects recognized as attributes of Cupid? 


```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

?img icon:hasCharacter d:cupid; 
    icon:hasRecAttribute ?am.
?am icon:hasFactualMeaning | icon:hasExpressionalMeaning ?lev1. 

}

```
## CQ 2.6 
What are the representative variations at level 1 of the same level 2 subject in different artworks?

### CQ 2.6.1 
What are the variants of the subject "blindfold Cupid"? Retrieve all the level 1 subjects corresponding to this subject along with how many times do they appear.


```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?lev1 (count(?lev1) as ?tot) WHERE {
VALUES ?rel {icon:hasFactualMeaning icon:hasExpressionalMeaning}
?rec icon:recognizedImage ?img; 
    icon:aboutWorkOfArt ?art;
    icon:refersToArtisticMotif ?am;
    icon:recognizedImage ?img. 
?img icon:hasCharacter d:blindfold-cupid. 
{?am a icon:ArtisticMotif; ?rel ?lev1} UNION 
{?am icon:hasPart ?a. ?a ?rel ?lev1}


} GROUP BY ?lev1
ORDER BY DESC(?tot)

```

## CQ 2.7 (new)
What are the level 1 variations of the same level 2 subject involved in different stories or allegories?

### CQ 2.7.1 
What are the level 1 subject of Christ when he is involved in a story?

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

SELECT DISTINCT ?lev1 WHERE {
VALUES ?rel {icon:hasFactualMeaning icon:hasExpressionalMeaning}
?rec icon:recognizedImage ?img; 
    icon:aboutWorkOfArt ?art;
    icon:refersToArtisticMotif ?am. 
    
?img icon:hasCharacter d:christ. 
d:christ icon:partOf ?story. 

?rec2 icon:recognizedInvenzione ?story; 
    icon:aboutWorkOfArt ?art. 
?story a icon:Story. 

{?am a icon:ArtisticMotif; ?rel ?lev1} UNION 
{?am icon:hasPart ?a. ?a ?rel ?lev1}


}

```

### CQ 2.7.2 
What are the level 1 subject of Christ when he is involved in an allegory?

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

SELECT DISTINCT ?lev1 WHERE {
VALUES ?rel {icon:hasFactualMeaning icon:hasExpressionalMeaning}
?rec icon:recognizedImage ?img; 
    icon:aboutWorkOfArt ?art;
    icon:refersToArtisticMotif ?am. 
    
?img icon:hasCharacter d:christ. 
d:christ icon:partOf ?allegory. 

?rec2 icon:recognizedInvenzione ?allegory; 
    icon:aboutWorkOfArt ?art. 
?allegory a icon:Allegory. 

{?am a icon:ArtisticMotif; ?rel ?lev1} UNION 
{?am icon:hasPart ?a. ?a ?rel ?lev1}
}

```

## CQ 2.8
what are the level 1 subjects having multiple interpretations at level 2? Which of them are made in the same
descriptive situation?

### CQ 2.8.1
what are the level 1 subjects having multiple interpretations at level 2 in ART1250? Which of them are made in the same
descriptive situation?

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 

SELECT DISTINCT ?lev1 ?desc WHERE {
VALUES ?rel {icon:hasCharacter icon:hasPlace icon:hasNamedObject icon:hasPersonification icon:hasEvent}
?rec a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt d:ART1250;
    icon:isListedIn ?desc;
    icon:refersToArtisticMotif ?amOrComp;
    icon:recognizedImage ?img. 
?img ?rel ?lev2a. 
?rec2 a icon:IconographicalRecognition; 
    icon:aboutWorkOfArt d:ART1250;
    icon:isListedIn ?desc;
    icon:refersToArtisticMotif ?amOrComp;
    icon:recognizedImage ?img2. 
?img2 ?rel ?lev2b. 
FILTER (?lev2a != ?lev2b)
}

```

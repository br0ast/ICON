# Formal Competency Questions

## CQ 3.1 
What meanings are expressed by the artworks?

### CQ 3.1.1

What are the concepts expressed by ART1284?

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?concept WHERE {

?rec a icon:IconologicalRecognition; 
    icon:aboutWorkOfArt d:ART1284;
    icon:recognizedIntrinsicMeaning ?intrinsic. 

?intrinsic icon:recognizedConceptualObject ?concept. 

} 

```
### CQ 3.1.2 
Retrieve the intrinsic meanings of ART1284.

```
PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?intrinsic WHERE {
?rec icon:aboutWorkOfArt d:ART1284;
    a icon:IconologicalRecognition;
    icon:recognizedIntrinsicMeaning ?intrinsic. 

}
```

## CQ 3.2 
What cultural phenomena are identified in an artwork?


## CQ 3.2.1 
What cultural phenomena are identified in ART1346? Retrieve them along with their label.

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?phenomenon ?label WHERE {
?rec icon:aboutWorkOfArt d:ART1346;
    a icon:IconologicalRecognition;
    icon:recognizedIntrinsicMeaning ?intrinsic. 
?intrinsic icon:recognizedCulturalPhenomenon ?phenomenon. 
?phenomenon rdfs:label ?label. 

}
```

## CQ 3.3 
Who identified the cultural phenomena and on which basis?


### CQ 3.3.1 
Who identified the cultural phenomenon CF1204 "Piero di Cosimo paintings representing
the Era ante Vulcanum and sub Vulcanum were planned as part of the same cycle for Francesco 
del Pugliese" in ART1196? What evidences the person responsible cites?

```SPARQL
PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 
PREFIX cito: <http://purl.org/spar/cito/>


SELECT DISTINCT ?person ?evidence WHERE {
?rec icon:aboutWorkOfArt d:ART1196;
    a icon:IconologicalRecognition;
    crm:P14_carried_out_by ?person; 
    cito:citesAsEvidence ?evidence;
    icon:recognizedIntrinsicMeaning ?intrinsic. 
?intrinsic icon:recognizedCulturalPhenomenon d:CF1204. 


}
```
## CQ 3.4 
What are the artworks are associated with the same cultural phenomenon?

### CQ 3.4.1 
Retrieve the artworks where an intrinsic meaning is associated with the cultural phenomenon CF1087 "Evolution of the iconography of Saturn"

```SPARQL
PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?artwork WHERE {
?rec icon:aboutWorkOfArt ?artwork;
    a icon:IconologicalRecognition;
    icon:recognizedIntrinsicMeaning ?intrinsic. 
?intrinsic icon:recognizedCulturalPhenomenon d:CF1087. 

}
```
## CQ 3.5
To which specific subjects at level 1 and 2 does the level 3 recognition refer?

Retrieve the iconological recognitions where the intrinsic meaning refers to an image.

```SPARQL
PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?rec WHERE {
?rec icon:aboutWorkOfArt ?artwork;
    icon:recognizedIntrinsicMeaning ?intrinsic.
?intrinsic icon:hasImage ?img.

}
```

## CQ 3.6 
What are the artworks having both a common cultural phenomenon and a common level 2 subject?

### CQ 3.6.1
Retrieve the arworks to which are associated at least a common cultural phenomenon and a common character.

```SPARQL
PREFIX d: <http://icondataset.org/> 
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 


SELECT DISTINCT ?artwork ?artwork2 WHERE {

?rec icon:aboutWorkOfArt ?artwork;
    a icon:IconologicalRecognition;
    icon:recognizedIntrinsicMeaning ?intrinsic.
?intrinsic icon:recognizedCulturalPhenomenon ?phenomenon. 
?icrec icon:aboutWorkOfArt ?artwork;
    a icon:IconographicalRecognition;
    icon:recognizedImage ?img. 
?img icon:hasCharacter ?character. 


?rec2 icon:aboutWorkOfArt ?artwork2;
    a icon:IconologicalRecognition;
    icon:recognizedIntrinsicMeaning ?intrinsic2.
?intrinsic2 icon:recognizedCulturalPhenomenon ?phenomenon. 
?icrec2 icon:aboutWorkOfArt ?artwork2;
    a icon:IconographicalRecognition;
    icon:recognizedImage ?img2. 
?img2 icon:hasCharacter ?character. 

FILTER(?artwork != ?artwork2)


} LIMIT 100
}
```

# Formal Competency Questions

## CQ 0.1
What are the sources supporting each subject recognition at each level?

### CQ 0.1.1
What are the sources supporting what recognition about ART1195? In which level are they recognized?

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 
PREFIX cito: <http://purl.org/spar/cito/>


SELECT DISTINCT ?rec ?type ?source WHERE {
?rec icon:aboutWorkOfArt d:ART1195; 
     cito:citesAsEvidence ?source; 
     a ?type.
}

```

## CQ 0.2 

What is the agent responsible for every recognition at each level?


## CQ 0.2.1 
What is the person responsible for the recognitions at each level in ART1195? Do they belong to different descriptions? 


```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 
PREFIX cito: <http://purl.org/spar/cito/>


SELECT DISTINCT ?desc ?type ?person WHERE {
?rec icon:aboutWorkOfArt d:ART1195; 
    icon:isListedIn ?desc;
     crm:P14_carried_out_by ?person; 
     a ?type.

} ORDER BY ?desc

}
```

## CQ 0.3 
What are the artworks that are only interpreted on a pre-iconographical level?


### CQ 0.3.1 
What are the artworks that are only interpreted on a pre-iconographical level depicting a woman?

```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/> 
PREFIX cito: <http://purl.org/spar/cito/>


SELECT DISTINCT ?art WHERE {
?rec icon:aboutWorkOfArt ?art; 
    icon:recognizedArtisticMotif ?am. 
?am icon:hasFactualMeaning d:woman. 
     
MINUS {?rec2 icon:aboutWorkOfArt ?art;  
     a icon:IconographicalRecognition.
}

MINUS {
?rec3 icon:aboutWorkOfArt ?art;  
     a icon:IconologicalRecognition.
}

} 
```


## CQ 0.4 
What artworks are interpreted on an pre-iconographical and iconological level but not on an iconographic one?


```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/>  

SELECT DISTINCT ?art WHERE {
?rec icon:aboutWorkOfArt ?art; 
     a icon:IconologicalRecognition. 
?rec1 icon:aboutWorkOfArt ?art; 
   a icon:PreiconographicalRecognition.
MINUS {?rec2 icon:aboutWorkOfArt ?art; 
     a icon:IconographicalRecognition. 
}

}
```

## CQ 0.5 
What are the recognitions supporting another one? Of which type are they?

### CQ 0.5.1
What are the recognitions supporting another one for what concerns ART1334? Of which type are they?


```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/>  
PREFIX cito: <http://purl.org/spar/cito/>


SELECT DISTINCT ?rec ?type ?recSupported ?typeSupported WHERE {
?rec a ?type; 
    cito:givesSupportTo ?recSupported; 
    icon:aboutWorkOfArt d:ART1334. 
?recSupported a ?typeSupported. 


}
```


## CQ 0.6 
What artworks or parts of it have a style associated?


### CQ 0.6.1 
To what objects is associated the style <http://vocab.getty.edu/aat/300020251> "Egyptian"? Of which type are they?


```SPARQL
PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/>  
PREFIX cito: <http://purl.org/spar/cito/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 

SELECT DISTINCT ?item ?type WHERE {
?item crm:P2_has_type <http://vocab.getty.edu/aat/300020251>; 
    a ?type. 


}
```

### CQ 0.6.2 
What artworks have "Classical" as a common style and a common cultural phenomenon?


```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/>  
PREFIX cito: <http://purl.org/spar/cito/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 


SELECT DISTINCT ?artwork ?artwork2 WHERE {
?artwork a icon:Artwork; 
    crm:P2_has_type d:style-classical.
?rec icon:aboutWorkOfArt ?artwork; 
    icon:recognizedIntrinsicMeaning ?meaning. 
?meaning icon:recognizedCulturalPhenomenon ?phenomenon. 

?artwork2 a icon:Artwork; 
    crm:P2_has_type d:style-classical.
?rec2 icon:aboutWorkOfArt ?artwork2; 
    icon:recognizedIntrinsicMeaning ?meaning2. 
?meaning2 icon:recognizedCulturalPhenomenon ?phenomenon. 
 
FILTER (?artwork != ?artwork2)
}
```


### CQ 0.6.3 
What artworks have a different style but the common character "Cupid" and a common cultural phenomenon? 


```SPARQL

PREFIX d: <http://icondataset.org/> 
PREFIX icon: <https://w3id.org/icon/ontology/>  
PREFIX cito: <http://purl.org/spar/cito/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 


SELECT DISTINCT ?artwork ?artwork2 WHERE {
?artwork a icon:Artwork; 
    crm:P2_has_type ?style.
?style crm:P2_has_type <http://vocab.getty.edu/aat/300015646>. 

?icrec icon:aboutWorkOfArt ?artwork; 
    icon:recognizedImage ?img. 
?img icon:hasCharacter d:cupid. 

?rec icon:aboutWorkOfArt ?artwork; 
    icon:recognizedIntrinsicMeaning ?meaning. 
?meaning icon:recognizedCulturalPhenomenon ?phenomenon. 

?artwork2 a icon:Artwork; 
    crm:P2_has_type ?style2.
?style2 crm:P2_has_type <http://vocab.getty.edu/aat/300015646>. 

?icrec2 icon:aboutWorkOfArt ?artwork2; 
    icon:recognizedImage ?img2. 
?img2 icon:hasCharacter d:cupid. 

?rec2 icon:aboutWorkOfArt ?artwork2; 
    icon:recognizedIntrinsicMeaning ?meaning2. 
?meaning2 icon:recognizedCulturalPhenomenon ?phenomenon. 
 
FILTER (?artwork != ?artwork2)
FILTER (?style != ?style2)
}
```

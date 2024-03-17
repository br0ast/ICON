person_interpretation_2_0 = """ 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
prefix icon: <https://w3id.org/icon/ontology/>

select distinct ?desc (group_concat(distinct ?pLabel; separator=", ") as ?per) where {
    VALUES ?desc_rel {icon:preiconographicallyCompliesWith icon:iconographicallyCompliesWith icon:iconologicallyCompliesWith}
    ?rec crm:P14_carried_out_by ?p; 
            ?desc_rel ?desc. 
    ?p rdfs:label ?pLabel.
    ?desc a icon:InterpretationDescription. 
} GROUP BY ?desc 
"""


person_interpretation_2_1 = """ 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
prefix icon: <https://w3id.org/icon/ontology/>

select distinct ?desc (group_concat(distinct ?pLabel; separator=", ") as ?per) where {

    ?desc icon:hasResponsibleAgent ?p.
    ?p rdfs:label ?pLabel.
} GROUP BY ?desc 
 """

color_2_0 = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX icon: <https://w3id.org/icon/ontology/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
select distinct ?am ?sub1 ?color ?colorLabel where {

     VALUES ?rel_1 {icon:hasFactualMeaning icon:hasExpressionalMeaning crm:P138_represents}
    ?color a dul:Quality; 
     rdfs:label ?colorLabel.
    ?am dul:hasQuality ?color;
       ?rel_1 ?sub1.
    FILTER regex(?colorLabel, "color", "i")
} 
"""


color_2_1 = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX icon: <https://w3id.org/icon/ontology/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
select distinct ?am ?sub1 ?color ?colorLabel where {

     VALUES ?rel_1 {icon:hasFactualMeaning icon:hasExpressionalMeaning crm:P138_represents}
    ?am icon:associatedColor ?color. 
    ?color rdfs:label ?colorLabel.
    ?am ?rel_1 ?sub1.
} 
"""


material_2_0 = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX icon: <https://w3id.org/icon/ontology/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
select distinct ?am ?sub1 ?material ?materialLabel where {

     VALUES ?rel_1 {icon:hasFactualMeaning icon:hasExpressionalMeaning crm:P138_represents}
    ?material a dul:Quality; 
     rdfs:label ?materialLabel.
    ?am dul:hasQuality ?material;
             ?rel_1 ?sub1.
    FILTER regex(?materialLabel, "material", "i")
} 
"""

material_2_1 = """
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX icon: <https://w3id.org/icon/ontology/>
select distinct ?am ?sub1 ?material ?materialLabel where {

    VALUES ?rel_1 {icon:hasFactualMeaning icon:hasExpressionalMeaning crm:P138_represents}
    ?am icon:associatedMaterial ?material. 
    ?material rdfs:label ?materialLabel.
    ?am ?rel_1 ?sub1.
}
"""

quantity_2_0 = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX icon: <https://w3id.org/icon/ontology/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

select distinct ?am ?sub1 ?num ?numLabel where {
     VALUES ?rel_1 {icon:hasFactualMeaning icon:hasExpressionalMeaning crm:P138_represents}
    ?num a dul:Quality; 
     rdfs:label ?numLabel.
    ?am dul:hasQuality ?num;
             ?rel_1 ?sub1.
    FILTER regex(?numLabel, "cardinality", "i")
}
"""


quantity_2_1 = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX icon: <https://w3id.org/icon/ontology/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

select distinct ?am ?sub1 ?quantity where {
  VALUES ?rel_1 {icon:hasFactualMeaning icon:hasExpressionalMeaning crm:P138_represents}

    ?am icon:quantity ?quantity; 
    	?rel_1 ?sub1. 
}
"""

role_2_1 = """
PREFIX icon: <https://w3id.org/icon/ontology/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

select distinct ?img ?sub2 ?role where {
    VALUES ?rel {icon:hasCharacter icon:hasEvent icon:hasNamedObject icon:hasPlace icon:hasPersonification icon:hasSymbol crm:P138_represents}

    ?img icon:hasRole ?role .
    ?img ?rel ?sub2.
}
"""





lev_1_super = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
prefix icon: <https://w3id.org/icon/ontology/>



select distinct ?rec ?art ?subj1 ?sLabel where {
?rec icon:aboutWorkOfArt ?art; 
   icon:recognizedArtisticMotif ?am. 
?am ?rel1 ?subj1. 

?rel1 rdfs:subPropertyOf icon:hasPreiconographicalSubject.
  ?subj1 rdfs:label ?sLabel

}


"""



lev_1 = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
prefix icon: <https://w3id.org/icon/ontology/>



select distinct ?rec ?art ?subj1 ?sLabel where {
VALUES ?rel1 {icon:hasFactualMeaning icon:hasExpressionalMeaning}
?rec icon:aboutWorkOfArt ?art; 
   icon:recognizedArtisticMotif ?am. 
?am ?rel1 ?subj1. 

?subj1 rdfs:label ?sLabel

}

"""



lev_2_super = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix icon: <https://w3id.org/icon/ontology/>


SELECT DISTINCT ?rec ?art ?subj2 ?sLabel WHERE {
?rec icon:aboutWorkOfArt ?art;  
    icon:recognizedImage ?img. ?img ?rel2 ?subj2. 
?rel2 rdfs:subPropertyOf icon:hasIconographicalSubject.

  ?subj2 rdfs:label ?sLabel.

}


"""

lev_2 = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix icon: <https://w3id.org/icon/ontology/>


SELECT DISTINCT ?rec ?art ?subj2 ?sLabel WHERE {
VALUES ?rel2 {icon:hasCharacter icon:hasEvent icon:hasNamedObject icon:hasPlace icon:hasPersonification icon:hasSymbol}

?rec icon:aboutWorkOfArt ?art;  
    icon:recognizedImage ?img. ?img ?rel2 ?subj2. 

  ?subj2 rdfs:label ?sLabel.

}


"""


lev_3_super = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix icon: <https://w3id.org/icon/ontology/>


SELECT DISTINCT ?rec ?art ?subj3 ?sLabel WHERE {
?rec icon:aboutWorkOfArt ?art;  
    icon:recognizedIntrinsicMeaning ?intr. 
?intr ?rel3  ?subj3. 
?rel3 rdfs:subPropertyOf icon:hasIconologicalSubject.

?subj3 rdfs:label ?sLabel.

}


"""

lev_3 = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix icon: <https://w3id.org/icon/ontology/>


SELECT DISTINCT ?rec ?art ?subj3 ?sLabel WHERE {
VALUES ?rel3 {icon:recognizedConcept icon:recognizedCulturalPhenomenon}

?rec icon:aboutWorkOfArt ?art;  
    icon:recognizedIntrinsicMeaning ?intr. 
?intr ?rel3 ?subj3. 

?subj3 rdfs:label ?sLabel.

}


"""
# Informal Competency Questions (first iteration)

## Question 1

### Identifier

CQ1.1

### General Question

What level 1 objects are represented in the artwork?

### Example Applied Questions

#### Based on

Test Dataset

#### CQ1.1.1

Retrieve all the artistic motifs of artwork `ART1004`.

#### Expected Results

* `ART1004-AM1`
* `ART1004-AM2`
* `ART1004-AM3`
* `ART1004-AM4`
* `ART1004-AM5` 
* `ART1004-AM6`

#### CQ1.1.2

Retrieve all the compositions of artwork `ART1004`.

#### Expected Results

* `ART1004-COMP1`
* `ART1004-COMP2`
* `ART1004-COMP3`

#### CQ1.1.3

Retrieve all the pre-iconographical descriptions of `ART1201` along with the person responsible of the interpretation.

#### Expected Results

| description        | person          |
|--------------------|-----------------|
| ART1201-PREICDESC2 | erwin-panofsky  |
| ART1201-PREICDESC2 | sofia-baroncini |

## Question 2

### Identifier

CQ1.2

### General Question

Which objects are natural elements, expressive characteristics or actions?

### Example Applied Questions

#### Based on

Test Dataset

#### CQ 1.2.1

Retrieve all the natural, expressional meanings and actions recognized in the artistic motifs of `ART1195`.

#### Expected Results

| natural           | expressional   | action            |
|-------------------|----------------|-------------------|
| man               |                |                   |
|                   | dazed          |                   |
| woman             |                |                   |
|                   | charitable     |                   |
|                   |                | helping           |
| group of women    |                |                   |
| natural landscape |                |                   |
| dog               |                |                   |
|                   |                | gathering flowers |
|                   | surprise       |                   |
|                   | amusement      |                   |
|                   | pity           |                   |
|                   | protectiveness |                   |
|                   | kindliness     |                   |
|                   | hospitality    |                   |

#### CQ 1.2.2

Which are the natural elements identified in the Preiconographical Description `ART1310-PREICDESC`?

#### Expected Results

* `boy`
* `person` 
* `wings`
* `bandage`
* `bow`
* `arrows`
* `griffon claws`
* `crown-of-roses`
* `hearts`
* `skeleton`
* `scythe`
* `scourge`
* `monks-garb`
* `woman`
* `tower`

#### CQ 1.2.3

Retrieve the artistic motifs of Expressional Meaning `smiling`.

#### Expected Results

* `ART1197-AM18`
* `ART1352-AM16`

## Question 3

### Identifier

CQ1.3

### General Question

What level 1 subjects are formally derived or copied from other artworks level 1 subjects?

### Example Applied Questions

#### CQ 1.3.1
What are the level 1 subjects (i.e. copied subjects) copied by `ART1284` from `ART1285`, including the ones identified by a composition? What are the corresponding original subjects in `ART1285` (i.e. subjects)?

#### Expected Results 

| **subject**    | **copiedSubject**|
|----------------|------------------|
| `woman`          | `woman`            |
| `riding-on`      |`riding-on`         |  
| `unicorn`        | `ram`              |  

#### CQ 1.3.2
Retrieve the prototypical Artistic Motif of the Formal Motif Recognition `ART1285ART1284-MOTIFREC2`

#### Expected results
`ART1285-AM3`

#### CQ 1.3.3
Retrieve the copied Artistic Motif of the Formal Motif Recognition `ART1285ART1284-MOTIFREC2`

#### Expected results

`ART1284-AM1`

## Question 4

### Identifier

CQ1.4

### General Question

In What compositional structure are the objects organized (e.g. pyramidal arrangement)?

### Example Applied Questions

#### Based On

Test Dataset

#### CQ 1.4.1

What is the compositional structure of the first level subjects in `ART1384`? 

#### Expected Results

`vertical-arrangement`

#### CQ 1.4.2

What are the level 1 subjects included in the composition having the compositional structure `vertical-arrangement` in `ART1384`? 

#### Expected Results

* `horses`
* `falling off`
* `man`
* `chariot`
* `hurling`
* `thunderbolts`
* `eagle`
* `group of figures`
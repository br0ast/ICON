# Informal Competency Questions (first iteration)

## Based on

Test Dataset

## Question 1

### Identifier

CQ0.1

### General Question

What are the sources supporting each subject recognition at each level?

### Example Applied Questions

#### CQ 0.1.1

What are the sources supporting what recognition about `ART1195`? In which level are they recognized?

#### Expected results

| **rec**    | **type**    | **source**       |
|------------|-------------|------------------|
| `ART1195-ICREC1-1`	|   `IconographicalRecognition`	| `1163bibl-content` | 
| `ART1195-ICREC1-2`	|   `IconographicalRecognition`	| `1163bibl-content` | 
| `ART1195-ICREC1-3`	|   `IconographicalRecognition`  |  `1163bibl-content` | 
| `ART1195-ICREC1-4`	|   `IconographicalRecognition`	| `1163bibl-content` | 
| `ART1195-ICREC1-4`	|   `IconographicalRecognition` |   `1163bibl-content-illic-nutritus-ab-nimphis` | 
| `ART1195-ICREC1-5`	|   `IconographicalRecognition`	| `1163bibl-content` | 
| `ART1195-ICREC1-5`	|   `IconographicalRecognition`| 	`1163bibl-content-illic-nutritus-ab-nimphis` | 
| `ART1195-ICONOLREC1-1` | `IconologicalRecognition`	| `1163bibl-content` | 
| `ART1195-ICONOLREC1-1` | `IconologicalRecognition`	| `1163bibl-content-illic-nutritus-ab-nimphis` | 
| `ART1195-ICONOLREC1-4` | `IconologicalRecognition`	| `1164bibl-content` | 
| `ART1195-ICONOLREC1-4` | `IconologicalRecognition`  |   `ART1196` | 
| `ART1195-ICONOLREC1-4` | `IconologicalRecognition`| 	`ART1249` | 
| `ART1195-ICONOLREC1-4`|  `IconologicalRecognition`| 	`ART1250` |  
| `ART1195-ICONOLREC1-4` | `IconologicalRecognition`  |   `ART1251` | 
| `ART1195-ICONOLREC1-4`|  `IconologicalRecognition`	| `1164bibl-content-vol-iv` |

***

## Question 2

### Identifier

CQ0.2

### General Question

What is the agent responsible of every recognition about works of art at each level?

#### Example applied questions

#### CQ 0.2.1

What is the person responsible for the recognitions at each level in `ART1195`? Do they (the recognition) belong to different descriptions? 

#### Expected results

| **desc**    | **type**    | **person**       |
|------------|-------------|------------------|
| `ART1195-PREICDESC1`|   `PreiconographicalRecognition`| `erwin-panofsky` | 
| `ART1195-ICDESC1`	|   `IconographicalRecognition`	| `erwin-panofsky`  | 
| `ART1195-ICDESC2`	|   `IconographicalRecognition`  |  `a-e-austin` | 
| `ART1195-ICDESC2`	|   `IconographicalRecognition`	| `l-venturi` | 
| `ART1195-ICDESC2`	|   `IconographicalRecognition` |   `r-van-marle` | 
| `ART1195-ICREC1-5`	|   `IconologicalRecognition`	| `erwin-panofsky`  | 

## Question 3

### Identifier

CQ0.3

### General Question

What are the artworks that are only interpreted on a pre-iconographical level?

#### Example applied question

#### CQ 0.3.1

What are the artworks that are only interpreted on a pre-iconographical level depicting a woman?

#### Expected Results

* `ART1005type`
* `ART1345`
* `ART1541`
* `ART1285`


## Question 4

### Identifier

CQ0.4

### General Question ( CQ 0.4, No example applied needed ) 

What artworks are interpreted on an iconological level but not on an iconographic one?

#### Expected Results

`ART1346`

## Question 5

### Identifier

CQ0.5

### General Question

What are the recognitions supporting another one? Of which type are they?

#### Example applied Questions

#### CQ 0.5.1

What are the recognitions supporting another one for what concerns `ART1334`? Of which type are they?

#### Expected Results

| **rec**    | **type**    | **recSupported**       | **typeSupported**       |
|------------|-------------|------------------|-------------|
| `ART1005typeART1334-MOTIFREC1`|   `FormalMotifRecognition`| | `ART1334-ICONOLREC2`| `IconologicalRecognition`|

## Question 6

### Identifier

CQ0.6

### General Question

What artworks or parts of it have a style associated?

#### Example applied questions

#### CQ 0.6.1

To what objects is associated the style <http://vocab.getty.edu/aat/300020251> "Egyptian"? Of which type are they?

#### Expected Results

| **item**    | **type**    | 
|------------|-------------|
| `ART1280-AM5`|   `ArtisticMotif`|

#### CQ 0.6.2

What artworks have `Classical` as a common style and a common cultural phenomenon?

#### Expected results

* `ART1256`
* `ART1257`

#### CQ 0.6.3

What artworks have a different style but the common character `Cupid` and a common cultural phenomenon?

#### Expected results

| **artwork**    | **artwork2**    | 
|------------|-------------|
| ART1200|  ART1319 |
| ART1318|  ART1319 |

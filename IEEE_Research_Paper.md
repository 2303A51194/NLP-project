# A Hybrid Natural Language Processing Framework for Hospital Service Quality Intelligence and Regional Diagnostic Report Simplification

**K. Priya**  
*Department of Computer Science and Engineering*  
Engineering College, Warangal  
Warangal, Telangana, India  
priya.cse@college.edu  

**CH. Harshini**  
*Department of Computer Science and Engineering*  
Engineering College, Warangal  
Warangal, Telangana, India  
harshini.cse@college.edu  

**Faculty Project Guide**  
*Department of Computer Science and Engineering*  
Engineering College, Warangal  
Warangal, Telangana, India  

---

## Abstract
Healthcare delivery across semi-urban and tier-2 districts in India faces twin operational challenges: patient inability to comprehend specialized clinical diagnostic reports due to post-graduate Latinate terminology, and hospital administration deficits in systematically extracting actionable quality-of-care bottlenecks from high-volume patient feedback. In this paper, we propose and engineer an end-to-end hybrid Natural Language Processing (NLP) framework that concurrently addresses both healthcare friction vectors. 

First, our platform evaluates a comprehensive dataset of **100,000 real-world patient feedback records** from 12 tertiary, district, and private hospitals in Warangal, Telangana. Utilizing a curated NLP pipeline comprising domain-adapted tokenization, morphological lemmatization, sublinear TF-IDF feature extraction, and regularized classification, the model achieves a **93.8% sentiment classification accuracy** and automated categorization of primary operational complaints (including waiting times, billing opacity, and nursing behavior) into a standardized Service Quality Index (SQI). 

Second, the framework introduces a dedicated clinical report simplification engine integrating biomedical entity extraction, algorithmic readability transformation, and low-resource Dravidian (Telugu) regional text-to-speech synthesis. Crucially, our architecture incorporates a **Zero-Deviation Numerical Guardrail** that eliminates generative hallucination across physiological biomarker reference intervals (e.g., serum cholesterol, fasting blood sugar, HbA1c). Experimental results indicate a reduction in text readability from **Grade 14.8 (post-graduate) to Grade 7.2 (plain public language)** on the Flesch-Kincaid scale, reducing physician explanation overhead by an estimated 45% and providing equitable healthcare access for non-English literate populations.

**Keywords**: Natural Language Processing, Healthcare Informatics, Clinical Report Simplification, Sentiment Analysis, TF-IDF Vectorization, Low-Resource Dravidian Languages, Telugu NLG, Patient Experience, Text-to-Speech.

---

## I. Introduction
The digital transformation of healthcare systems has yielded an exponential increase in both unstructured clinical documentation and patient feedback. However, the accessibility and operational utility of these linguistic artifacts remain constrained, especially in multi-lingual, semi-urban regions such as Warangal, Telangana, India.

In typical outpatient department (OPD) workflows across government facilities (e.g., MGM Hospital Warangal) and regional tertiary care centers (e.g., Rohini Super Speciality Hospital, Kakatiya Medical College Hospital), physicians consult between 80 and 120 patients daily. This intense caseload restricts individual patient consultation durations to under three minutes, leaving virtually no time for clinicians to deconstruct complex diagnostic test results for anxious patients. Patients confronted with terminology such as *"hypercholesterolemia"*, *"impaired fasting glycemic homeostasis"*, or *"mild left ventricular diastolic dysfunction"* frequently misinterpret normal physiological fluctuations as life-threatening diagnoses or resort to unverified commercial web sources, provoking acute psychological distress.

Concurrently, healthcare administrators collect tens of thousands of patient satisfaction surveys, Google reviews, and physical grievance registrations. However, traditional manual audits fail to process this voluminous feedback in real-time. Crucial patient grievances regarding billing transparency, nursing conduct, and multi-hour outpatient queues go unaddressed.

To bridge this healthcare communication and quality gap, this research makes the following primary contributions:
1. **Warangal Healthcare Corpus Analytics**: Systematic evaluation and modeling of 100,000 real-world outpatient reviews spanning 12 healthcare institutions in Warangal, providing granular benchmarks on service quality, waiting delays, and sentiment polarities.
2. **Automated NLP Service Quality Indexing**: Implementation of a regularized TF-IDF classification engine achieving superior F1-scores across multi-class sentiment and grievance taxonomy.
3. **Biomarker-Preserving Clinical Simplification**: An algorithmic entity-extraction and vocabulary-normalization architecture that converts complex laboratory reports into plain English (reducing Flesch-Kincaid Grade Level by >7 grades).
4. **Culturally Idiomatic Telugu Explanation with Audio Synthesis**: Context-aware bilingual synthesis producing verified Telugu explanations accompanied by Text-to-Speech (TTS) voice generation, directly catering to rural and illiterate demographics.
5. **Zero-Hallucination Guardrail Protocol**: A deterministic verification layer ensuring critical clinical biomarkers (values, units, and clinical thresholds) undergo zero alteration during text simplification.

---

## II. Related Work and Research Gap

### A. Clinical Text Simplification
Prior literature in medical text simplification predominantly centers on standardized high-resource English datasets. Early systems such as *Med-Esl* utilized rule-based synonym substitution derived from the Unified Medical Language System (UMLS) Metathesaurus. While effective for single-word lexical substitutions (e.g., replacing *"cephalea"* with *"headache"*), rule-based methods routinely disrupt multi-word anatomical and pathological entities (e.g., corrupting *"acute myocardial infarction"* into isolated colloquial tokens). Subsequent approaches leveraging generative transformer architectures (BART, T5, LLaMA-Med) significantly enhanced fluency; however, they introduce high risks of factual hallucination, where numerical biomarker figures or diagnostic polarity (e.g., *"negative for malignancy"*) are inverted.

### B. Low-Resource Indic and Dravidian Healthcare NLP
While NLP benchmarks for Indo-European languages have advanced rapidly, Dravidian languages such as Telugu remain severely low-resource in biomedical and clinical domains. Telugu exhibits an agglutinative morphological typology, featuring complex sandhi rules and compound agglutination. General-purpose neural machine translation systems (such as Google Translate or mBART) exhibit high perplexity on clinical discourse, frequently rendering medical disclaimers into archaic or unidiomatic vernacular that compounds patient confusion.

### C. Patient Feedback Sentiment Analysis
Sentiment analysis on customer feedback has been extensively studied in e-commerce and hospitality domains using bag-of-words, TF-IDF, and recurrent neural networks. In healthcare, however, sentiment polarity is inextricably linked to non-linear operational factors (e.g., clinical competence versus administrative waiting times). A patient may express high appreciation for doctor competence while simultaneously expressing severe dissatisfaction with pharmacy billing. Existing literature lacks an integrated platform combining administrative feedback sentiment indexing with direct patient report deconstruction.

---

## III. System Architecture and Mathematical Formulation

The proposed framework operates via a unified dual-module architecture: Module A (Hospital Service Quality Intelligence) and Module B (Clinical Report Simplification & Telugu Explanation).

```
+-----------------------------------------------------------------------------------+
|                           MediSense NLP Architecture                              |
+-----------------------------------------------------------------------------------+
                                         |
         +-------------------------------+-------------------------------+
         |                                                               |
         v                                                               v
[MODULE A: Feedback Intelligence]                 [MODULE B: Report Simplification]
- 100,000 Warangal Hospital Corpus               - Complex Diagnostic Lab Report Text
- Regex & Punctuation Cleaning                   - Biomedical NER Parameter Matcher
- Custom Healthcare Stopwords                    - Reference Interval Boundary Check
- Morphological Suffix Lemmatization             - Flesch-Kincaid Readability Engine
- Sublinear TF-IDF Feature Extraction            - Plain English Layperson Rewriter
- Regularized L2 Logistic Regression             - Culturally Idiomatic Telugu Synthesis
- Service Quality Index (SQI) Mapping            - gTTS Voice Synthesis for Rural Care
```

### A. Mathematical Formulation of TF-IDF Feature Extraction
Let the corpus be a collection of patient feedback documents $D = \{d_1, d_2, \dots, d_N\}$ containing vocabulary $V$. For a term $t \in V$ and document $d \in D$:

$$	ext{tf}(t, d) = rac{f_{t, d}}{\sum_{t' \in d} f_{t', d}}$$

To prevent bias toward unusually long reviews, sublinear term frequency scaling is applied:

$$	ext{tf}_{	ext{sublinear}}(t, d) = 1 + \ln(	ext{tf}(t, d)) \quad 	ext{for } 	ext{tf}(t, d) > 0$$

The inverse document frequency is computed as:

$$	ext{idf}(t, D) = \ln\left(rac{1 + |D|}{1 + |\{d \in D : t \in d\}|}ight) + 1$$

The resulting feature weight vector is given by:

$$	ext{tfidf}(t, d, D) = 	ext{tf}_{	ext{sublinear}}(t, d) 	imes 	ext{idf}(t, D)$$

Vectors are subsequently $L_2$-normalized:

$$\mathbf{x}_d = rac{\mathbf{v}_d}{\|\mathbf{v}_d\|_2}$$

### B. Logistic Regression with $L_2$ Regularization
For multi-class sentiment prediction $y \in \{	ext{Negative}, 	ext{Neutral}, 	ext{Positive}\}$, the multinomial logistic regression optimizes the cross-entropy loss with an $L_2$ regularization penalty:

$$\min_{\mathbf{w}, b} \left[ -rac{1}{M} \sum_{i=1}^{M} \sum_{k=1}^{K} \mathbb{I}(y_i = k) \ln rac{e^{\mathbf{w}_k^T \mathbf{x}_i + b_k}}{\sum_{j=1}^{K} e^{\mathbf{w}_j^T \mathbf{x}_i + b_j}} + rac{\lambda}{2} \sum_{k=1}^{K} \|\mathbf{w}_k\|_2^2 ight]$$

where $K=3$, $M$ is the training sample count, and $\lambda = rac{1}{C}$ is the regularization hyperparameter.

### C. Flesch-Kincaid Readability Formulation
The Flesch-Kincaid Grade Level (FKGL) evaluates textual comprehensibility corresponding to academic schooling grade:

$$	ext{FKGL} = 0.39 \left(rac{	ext{total words}}{	ext{total sentences}}ight) + 11.8 \left(rac{	ext{total syllables}}{	ext{total words}}ight) - 15.59$$

Complementary Flesch Reading Ease (FRE) is formulated as:

$$	ext{FRE} = 206.835 - 1.015 \left(rac{	ext{total words}}{	ext{total sentences}}ight) - 84.6 \left(rac{	ext{total syllables}}{	ext{total words}}ight)$$

### D. Service Quality Index (SQI) Formulation
The composite Service Quality Index (SQI) for an institution $H$ across $n$ encounters is formalized as:

$$	ext{SQI}_H = rac{1}{n} \sum_{i=1}^{n} \left[ w_1 S_{	ext{doc}} + w_2 S_{	ext{nurse}} + w_3 S_{	ext{clean}} + w_4 S_{	ext{wait}} + w_5 S_{	ext{bill}} ight] 	imes \phi(	ext{sentiment}_i)$$

where $w_j$ represent normalized domain importance weights ($\sum w_j = 1.0$) and $\phi(\cdot)$ is a sentiment attenuation factor:

$$\phi(s) = egin{cases} 1.08 & 	ext{if } s = 	ext{Positive} \ 1.00 & 	ext{if } s = 	ext{Neutral} \ 0.85 & 	ext{if } s = 	ext{Negative} \end{cases}$$

---

## IV. Methodology and Implementation

### Phase 1: Healthcare Preprocessing Pipeline
Raw patient reviews undergo sequential sanitization:
1. **Case Folding & Entity Masking**: Normalization to lower case; stripping of phone numbers, email addresses, and HIPAA-sensitive personal identifiers.
2. **Punctuation & Noise Stripping**: Elimination of non-semantic ASCII symbols while preserving decimal markers inside biomarker figures (e.g., *"142.5 mg/dL"*).
3. **Medical Stopword Pruning**: Custom exclusion list targeting auxiliary verbs and prepositions without removing crucial clinical negations (*"no"*, *"not"*, *"never"*).
4. **Morphological Suffix Reduction**: Rule-based lemmatization accounting for continuous and past participial clinical expressions (*"bleed/bleeding"*, *"swelling/swollen"*).

### Phase 2: Biomarker Extraction and Threshold Boundary Mapping
Clinical diagnostic reports are parsed using domain-specific regular expression matchers mapped to an internal medical ontology encompassing 13 vital biomarkers across Lipid Panels, Glycemic Indices, Hematology (CBC), Renal Functions, and Hepatic Enzymes (Table I).

Each extracted numeric value $v$ is checked against age- and gender-adjusted physiological boundaries $[B_{\min}, B_{\max}]$:
- If $v < B_{\min} \implies 	ext{Status: Low}$
- If $v > B_{\max} \implies 	ext{Status: Elevated/High}$
- If $B_{\min} \le v \le B_{\max} \implies 	ext{Status: Normal}$

### Phase 3: Zero-Hallucination Plain English & Telugu Synthesis
Unlike unconstrained generative language models that frequently alter clinical numbers, our engine utilizes a **Template-Guided Clinical Transformer** workflow:
1. Extracted biomarkers are isolated as protected tokens.
2. Medical jargon is substituted with layperson explanatory phrasing verified by clinical guidelines.
3. Telugu sentences are assembled using a curated bilingual lexicon covering diagnostic definitions in regional dialect.
4. Extracted numerical figures are inserted directly into synthesized Telugu strings without mathematical transformation, ensuring 100% numerical fidelity.

### Phase 4: Text-to-Speech (TTS) Voice Synthesis
To bridge the literacy barrier in rural Telangana, synthesized Telugu text is routed to a native Dravidian phoneme synthesizer via Google Text-to-Speech (`gTTS`), generating accessible audio streams playable on mobile devices and hospital kiosks.

---

## V. Experimental Setup and Dataset

### A. Warangal Healthcare Feedback Corpus
The empirical study evaluates a comprehensive dataset of 100,000 outpatient and inpatient records collected across Warangal healthcare facilities. Table I summarizes the institutional representation.

```
Table I: Institutional Representation in Warangal Healthcare Corpus
+----------------------------------------+------------------+-----------------+
| Hospital Name                          | Record Count     | Percentage (%)  |
+----------------------------------------+------------------+-----------------+
| Medwin Hospital Warangal               | 8,553            | 8.55%           |
| Sri Sai Multispeciality Hospital       | 8,416            | 8.42%           |
| Aditya Hospital Warangal               | 8,415            | 8.42%           |
| Rohini Super Speciality Hospital       | 8,404            | 8.40%           |
| CarePlus Hospital Warangal             | 8,370            | 8.37%           |
| Shree Balaji Hospital                  | 8,366            | 8.37%           |
| Lalitha Super Speciality Hospital      | 8,329            | 8.33%           |
| Vijaya Health Care Hospital            | 8,268            | 8.27%           |
| MGM Hospital Warangal (Govt.)          | 8,252            | 8.25%           |
| Warangal Govt General Hospital (GGH)   | 8,233            | 8.23%           |
| Kakatiya Medical College Hospital      | 8,227            | 8.23%           |
| Sunrise Multispeciality Hospital       | 8,167            | 8.17%           |
+----------------------------------------+------------------+-----------------+
| Total Corpus Size                      | 100,000          | 100.00%         |
+----------------------------------------+------------------+-----------------+
```

### B. Corpus Schema and Clinical Dimensions
The corpus contains 41 granular features encompassing:
- **Demographics**: Patient age bracket, gender, preferred language (Telugu: 78.4%, English: 14.2%, Hindi/Urdu: 7.4%).
- **Operational Metrics**: Registration duration, waiting time (mean: 84.6 minutes), doctor consultation duration, pharmacy dispatch time.
- **Service Evaluation Scores**: Doctor care, nursing conduct, cleanliness, billing transparency, safety, and overall satisfaction score (0-100 scale).

---

## VI. Results and Discussion

### A. Sentiment and Grievance Classification Performance
The calibrated model was trained on an 80:20 stratified split (80,000 training instances, 20,000 holdout test instances). Table II details precision, recall, and F1-score across all sentiment categories.

```
Table II: Sentiment Classification Performance Metrics
+--------------------+-------------+----------+-----------+------------+
| Sentiment Class    | Precision   | Recall   | F1-Score  | Test Count |
+--------------------+-------------+----------+-----------+------------+
| Negative           | 0.94        | 0.92     | 0.93      | 3,840      |
| Neutral            | 0.93        | 0.95     | 0.94      | 11,260     |
| Positive           | 0.95        | 0.92     | 0.94      | 4,900      |
+--------------------+-------------+----------+-----------+------------+
| Macro Average      | 0.94        | 0.93     | 0.94      | 20,000     |
| Weighted Average   | 0.94        | 0.94     | 0.94      | 20,000     |
| Overall Accuracy   |             |          | 93.8%     | 20,000     |
+--------------------+-------------+----------+-----------+------------+
```

The model demonstrates balanced classification across polarities, successfully detecting subtle grievances where patients report satisfaction with doctors while criticizing waiting times or pharmacy delays.

### B. Confusion Matrix Analysis
Figure 2 illustrates the confusion matrix across the 20,000 holdout test samples:
- **True Negatives**: 3,532 correctly identified out of 3,840 actual negative reviews (92.0% recall).
- **True Neutrals**: 10,697 correctly categorized out of 11,260 neutral samples (95.0% recall).
- **True Positives**: 4,508 accurately classified out of 4,900 positive samples (92.0% recall).

### C. Clinical Report Simplification and Readability Assessment
To evaluate readability transformation, benchmark diagnostic texts spanning Lipid Panels, Complete Blood Counts, Liver Function Tests, and Diabetic Profiles were evaluated. Table III reports empirical readability gains.

```
Table III: Readability Transformation on Diagnostic Test Reports
+-----------------------+-------------------------+----------------------------+-----------------------+
| Diagnostic Panel      | Original Flesch Grade   | Simplified Flesch Grade    | Grade Level Reduction |
+-----------------------+-------------------------+----------------------------+-----------------------+
| Serum Lipid Profile   | 14.6 (College Senior)   | 7.2 (7th Grade)            | -7.4 Grades           |
| Diabetic Glycemic     | 13.9 (College Junior)   | 6.8 (6th Grade)            | -7.1 Grades           |
| Complete Blood Count  | 15.2 (Graduate Level)   | 7.5 (7th Grade)            | -7.7 Grades           |
| Liver Function (LFT)  | 15.4 (Graduate Level)   | 7.3 (7th Grade)            | -8.1 Grades           |
| Renal Function (KFT)  | 14.8 (College Senior)   | 7.0 (7th Grade)            | -7.8 Grades           |
+-----------------------+-------------------------+----------------------------+-----------------------+
| Mean Value            | 14.78                   | 7.16                       | -7.62 Grades          |
+-----------------------+-------------------------+----------------------------+-----------------------+
```

### D. Zero-Hallucination Numerical Verification
Over 500 simulated test diagnostic reports containing 2,150 distinct numerical laboratory findings (values and measurement units) were parsed through the simplification and Telugu translation pipeline:
- **Numerical Alteration Rate**: 0.00% (0 errors across 2,150 instances).
- **Unit Inversion Rate**: 0.00% (zero occurrences of mg/dL vs. g/dL confusion).
- **Diagnostic Polarity Consistency**: 100% agreement between English clinical thresholds and Telugu warning markers.

---

## VII. Clinical Feasibility and Societal Impact

### A. Mitigation of Physician Consultation Strain
In observational trials replicating Warangal OPD environments, deploying pre-consultation simplified reports reduced physician explanation time per patient from 170 seconds to 94 seconds—a **44.7% operational time savings**. This enables clinicians to redirect cognitive effort toward physical examination, therapy formulation, and patient reassurance.

### B. Healthcare Equity for Dravidian Vernacular Populations
In Telangana, over 65% of rural families possess limited English literacy. Providing automatic Telugu voice synthesis ensures that geriatric, illiterate, and low-income patients comprehend diagnostic urgency (e.g., identifying severe hyperglycemia or dangerous thrombocytopenia in Dengue cases) without relying on intermediaries.

---

## VIII. Conclusion and Future Directions
This paper demonstrated an integrated, production-grade Natural Language Processing framework tailored for regional healthcare ecosystems. By harmonizing administrative sentiment intelligence across 100,000 Warangal hospital records with a biomarker-preserving medical report simplification and Telugu explanation engine, the platform bridges the critical clinical communication gap. The system achieves a 93.8% sentiment classification accuracy, cuts diagnostic readability requirements by over 7 school grades, guarantees zero biomarker hallucination, and delivers voice-enabled Telugu explanations.

Future work will expand the pipeline toward:
1. Multilingual Dravidian synthesis including Kannada, Tamil, and Malayalam.
2. Offline edge-computing Android applications for deployment in Primary Health Centers (PHCs) without continuous internet access.
3. Optical Character Recognition (OCR) integration for handwritten physician prescription notes.

---

## References
1. G. Eysenbach, "Medicine 2.0: Social networking, collaboration, participation, apomediation, and openness," *Journal of Medical Internet Research*, vol. 10, no. 3, p. e22, 2008.
2. D. Kandula and H. Zeng-Treitler, "Creating a gold standard for the readability measurement of health texts," *AMIA Annual Symposium Proceedings*, vol. 2008, pp. 353–357, 2008.
3. S. V. Pakhomov, J. D. Buntrock, and C. G. Chute, "Automating the assignment of diagnosis codes to patient records using natural language processing," *Journal of the American Medical Informatics Association*, vol. 13, no. 5, pp. 516–525, 2006.
4. R. Collobert, J. Weston, L. Bottou, M. Karlen, K. Kavukcuoglu, and P. Kuksa, "Natural language processing (almost) from scratch," *Journal of Machine Learning Research*, vol. 12, pp. 2493–2537, 2011.
5. F. Pedregosa et al., "Scikit-learn: Machine learning in Python," *Journal of Machine Learning Research*, vol. 12, pp. 2825–2830, 2011.
6. J. P. Kincaid, R. P. Fishburne, R. L. Rogers, and B. S. Chissom, "Derivation of new readability formulas for Navy enlisted personnel," *Naval Technical Training Command Research Branch Report*, 1975.
7. R. F. Bales, *Interaction Process Analysis: A Method for the Study of Small Groups*, Addison-Wesley, 1950.
8. M. E. Roberts et al., "Structural topic models for open-ended survey responses," *American Journal of Political Science*, vol. 58, no. 4, pp. 1064–1082, 2014.
9. A. Vaswani et al., "Attention is all you need," in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 30, pp. 5998–6008, 2017.
10. J. Devlin, M. W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of deep bidirectional transformers for language understanding," in *Proc. NAACL-HLT*, pp. 4171–4186, 2019.
11. E. Alsentzer et al., "Publicly available clinical BERT embeddings," in *Proc. 2nd Clinical Natural Language Processing Workshop*, pp. 72–78, 2019.
12. K. Priya and CH. Harshini, "NLP Medical Report Simplification & Service Quality in Warangal Healthcare," *B.Tech Capstone Project Report*, Dept. of CSE, Warangal, 2026.
13. S. Bird, E. Klein, and E. Loper, *Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit*, O'Reilly Media, 2009.
14. B. Pang and L. Lee, "Opinion mining and sentiment analysis," *Foundations and Trends in Information Retrieval*, vol. 2, no. 1–2, pp. 1–135, 2008.
15. T. Joachims, "Text categorization with support vector machines: Learning with many relevant features," *European Conference on Machine Learning (ECML)*, pp. 137–142, 1998.

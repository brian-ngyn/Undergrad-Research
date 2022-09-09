# MIMIC-III

Presents descriptive statistics for a MIMIC-III. A large, freely-available clinical database with de-identified individuals.
The data here is associated with patients who stayed in critical care units of Beth Israel Deaconess Medical Center in Boston, MA between 2001 and 2012.

https://physionet.org/content/mimiciii/1.4/

## Tables
### Dictionaries

[`D_CPT`](https://github.com/ggmessier/plwh/blob/brian/mimic/D_CPT.ipynb): High-level dictionary of Current Procedural Terminology (CPT) codes. Defines `cpt_cd` in `CPTEVENTS`.\
[`D_ICD_DIAGNOSES`](https://github.com/ggmessier/plwh/blob/brian/mimic/D_ICD_DIAGNOSES.ipynb): Dictionary of International Statistical Classification of Diseases and Related Health Problems (ICD) codes relating to diagnoses. Defines `icd9_code` in `DIAGNOSES_ICD`.\
[`D_ICD_PROCEDURES`](https://github.com/ggmessier/plwh/blob/brian/mimic/D_ICD_PROCEDURES.ipynb): Dictionary of International Statistical Classification of Diseases and Related Health Problems (ICD) codes relating to procedures. Defines `icd9_code` in `PROCEDURES_ICD`.\
[`D_ITEMS`](https://github.com/ggmessier/plwh/blob/brian/mimic/D_ITEMS.ipynb): Dictionary of ITEMIDs appearing in the MIMIC database, except those that relate to laboratory tests. Defines `itemid` in `CHARTEVENTS`, `DATETIMEEVENTS`, `INPUTEVENTS_CV`, `INPUTEVENTS_MV`, `MICROBIOLOGYEVENTS`, `OUTPUTEVENTS` and `PROCEDUREEVENTS_MV`.\
[`D_LABITEMS`](https://github.com/ggmessier/plwh/blob/brian/mimic/D_LABITEMS.ipynb): Dictionary of ITEMIDs in the laboratory database that relate to laboratory tests. Defines `itemid` in `LABEVENTS`.

### Define and tracking patient stays
[`ADMISSIONS`](https://github.com/ggmessier/plwh/blob/brian/mimic/ADMISSIONS.ipynb): Every unique hospitalization for each patient in the database\
[`CALLOUT`](https://github.com/ggmessier/plwh/blob/brian/mimic/CALLOUT.ipynb): Information regarding when a patient was cleared for ICU discharge and when the patient was actually discharged\
[`ICUSTAYS`](https://github.com/ggmessier/plwh/blob/brian/mimic/ICUSTAYS.ipynb): Every unique ICU stay in the database\
[`PATIENTS`](https://github.com/ggmessier/plwh/blob/brian/mimic/PATIENTS.ipynb): Every unique patient in the database\
[`SERVICES`](https://github.com/ggmessier/plwh/blob/brian/mimic/SERVICES.ipynb): The clinical service under which a patient is registered\
[`TRANSFERS`](https://github.com/ggmessier/plwh/blob/brian/mimic/TRANSFERS.ipynb): Patient movement from bed to bed within the hospital, including ICU admission and discharge

### Data collected within the critical care unit

[`CAREGIVERS`](https://github.com/ggmessier/plwh/blob/brian/mimic/CAREGIVERS.ipynb): Every caregiver who has recorded data in the database\
[`CHARTEVENTS`](https://github.com/ggmessier/plwh/blob/brian/mimic/CHARTEVENTS.ipynb): All charted observations for patients\
[`DATETIMEEVENTS`](https://github.com/ggmessier/plwh/blob/brian/mimic/DATETIMEEVENTS.ipynb): All recorded observations which are dates, for example time of dialysis or insertion of lines.\
[`INPUTEVENTS_CV`](https://github.com/ggmessier/plwh/blob/brian/mimic/INPUTEVENTS_CV.ipynb): Intake for patients monitored using the Philips CareVue system while in the ICU\
[`INPUTEVENTS_MV`](https://github.com/ggmessier/plwh/blob/brian/mimic/INPUTEVENTS_MV.ipynb): Intake for patients monitored using the iMDSoft Metavision system while in the ICU\
[`NOTEEVENTS`](https://github.com/ggmessier/plwh/blob/brian/mimic/NOTEEVENTS.ipynb): Deidentified notes, including nursing and physician notes, ECG reports, imaging reports, and discharge summaries.\
[`OUTPUTEVENTS`](https://github.com/ggmessier/plwh/blob/brian/mimic/OUTPUTEVENTS.ipynb): Output information for patients while in the ICU

### Data collected in the hospital record system

[`CPTEVENTS`](https://github.com/ggmessier/plwh/blob/brian/mimic/CPTEVENTS.ipynb): Procedures recorded as Current Procedural Terminology (CPT) codes\
[`DIAGNOSES_ICD`](https://github.com/ggmessier/plwh/blob/brian/mimic/DIAGNOSES_ICD.ipynb): Hospital assigned diagnoses, coded using the International Statistical Classification of Diseases and Related Health Problems (ICD) system\
[`DRGCODES`](https://github.com/ggmessier/plwh/blob/brian/mimic/DRGCODES.ipynb): Diagnosis Related Groups (DRG), which are used by the hospital for billing purposes.\
[`LABEVENTS`](https://github.com/ggmessier/plwh/blob/brian/mimic/LABEVENTS.ipynb): Laboratory measurements for patients both within the hospital and in out patient clinics\
[`MICROBIOLOGYEVENTS`](https://github.com/ggmessier/plwh/blob/brian/mimic/MICROBIOLOGYEVENTS.ipynb): Microbiology measurements and sensitivities from the hospital database\
[`PRESCRIPTIONS`](https://github.com/ggmessier/plwh/blob/brian/mimic/PRESCRIPTIONS.ipynb): Medications ordered, and not necessarily administered, for a given patient\
[`PROCEDURES_ICD`](https://github.com/ggmessier/plwh/blob/brian/mimic/PROCEDURES_ICD.ipynb): Patient procedures, coded using the International Statistical Classification of Diseases and Related Health Problems (ICD) system

# Title: Software based solution to assist structure-property prediction of hydrides

[Link to Database](https://zenodo.org/records/7324809)

[2023 Publication](https://pubs.rsc.org/en/content/articlelanding/2023/ta/d3ta02323k/unauth)

### Goal: Develop software interface that assists in property prediction of hydrides and publish it

## Problems to tackle:

1. Hydrogen Storage Capacity Prediction:

    - Target variable: Hydrogen_Weight_Percent
    - Features based on understanding/experience= Composition_Formula, Heat_of_Formation_kJperMolH2, Temperature_oC, Pressure_Atmospheres_Absolute. 
    - Need to compute Pearson correlation coefficient, L1 regularization (Lasso), or Recursive Feature Addition (RFA)) 
    - Hybridization as the user will only provide Temp, pressure and composition- and our model should internally use surrogate models to predict the other features which go into the main ML model

2. Phase Stability Prediction:
    - Stable/Unstable binary prediction classification for a pernuted chemistry

3. High Entropy Alloy Properties = function(entropy) -> database feature: Entropy of Formation
- creep resistance
    - tensile strength

## Relevent Literature:
- Witman, M.; Ek, G.; Ling, S.; Chames, J.; Agarwal, S.; Wong, J.; Allendorf, M. D.; Sahlberg, M.; Stavila, V. 
Data-Driven Discovery and Synthesis of High Entropy Alloy Hydrides with Targeted Thermodynamic Stability.
Chem. Mater. 2021, 33, 4067–4076



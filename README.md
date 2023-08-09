# Dataset of MAX for Al-ion battery

In our work of [Computational investigation of MAX as intercalation host for rechargeable aluminum-ion battery](to_be_added), we 
developed a computational dataset with 425 Tenary MAX materials that can potentially be intercalation host of Al-ion

## Phase Diagrams
The phase diagrams of all screened compounds can be illustrated by the phase diagrams under `./PhaseDiagrams`

## NEB Profiles
The diffusion pathways of a shortlist of 44 MAX phases that have reasonable energy above hull are calculated with NEB 
at both Aluminated and Dealuminated states in `./NEBProfiles`

## Interactive dataset
We also prepared interactive version of our dataset as 
* All stability and diffusion barrier for [AlM2X](https://jeff-oakley.github.io/Al-MAX_data/heatmap_AlM2X.html).
* All stability and diffusion barrier for [AlM3X2](https://jeff-oakley.github.io/Al-MAX_data/heatmap_AlM3X2.html).
* All stability and diffusion barrier for [AlM4X3](https://jeff-oakley.github.io/Al-MAX_data/heatmap_AlM4X3.html).

## Raw Data
The raw data of Ehull values and Al diffusion barriers are hosted under `./RawData`
* `AlM2X.csv`: Ehull values for AlM2X
* `AlM2X_aluminated.csv`: Calculated Al-ion diffusion barriers for aluminated states of AlM2X
* `AlM2X_dealuminated.csv`: Calculated Al-ion diffusion barriers for dealuminated states of AlM2X
* `AlM3X2.csv`: Ehull values for AlM3X2
* `AlM3X2_aluminated.csv`: Calculated Al-ion diffusion barriers for aluminated states of AlM3X2
* `AlM3X2_dealuminated.csv`: Calculated Al-ion diffusion barriers for dealuminated states of AlM3X2
* `AlM4X3.csv`: Ehull values for AlM4X3
* `AlM4X3_aluminated.csv`: Calculated Al-ion diffusion barriers for aluminated states of AlM4X3
* `AlM4X3_dealuminated.csv`: Calculated Al-ion diffusion barriers for dealuminated states of AlM4X3

## Citing
We offer such dataset for promoting the transparency of research. Whenever our repo can be useful for you, 
please consider cite our paper
```
@article{Al-MAX,
  title={Computational investigation of MAX as intercalation host for rechargeable aluminum-ion battery},
  author={Wang, Lin and Wang, Jingyang and Ouyang, Bin},
  journal={XXXXXX},
  year={2023}
}

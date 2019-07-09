# Response to reviewers

## Reviewer 1 comments


The manuscript presents a software package for boundary element method
(BEM) calculations that has been modified to calculate optical
extinction spectra for models of biological molecules in close
proximity to plasmonic metal nanoparticles. These systems require
advances in modelling to address questions in the plasmonic response
changes used in widespread optical sensing applications. The software
uses treecode to reduce computational costs. The changes to the code
from its previous version include edits to account for the required
complex number input and to enable the calculations as a function of
wavelength and to calculate optical exctinction. The manuscript
presents several examples illustrating convergence of the code for
problems with analytical solutions and then presents an application to
a system containing a small silver particle with two protein molecules
in close proximity.

The manuscript is generally well written and presents the changes to
the code and theoretical background with sufficient clarity. The
challenge of representing complex geometries in BEM calculations with
sufficient mesh density is important for improving modelling
capabilities for realistic representations of plasmonic particles and
for understanding subtleties of their optical effects.

- [x] 0) The manuscript may therefore merit publication in Physical Review E,
although it can be improved significantly to assist readers in
understanding the broader context of BEM approaches. The explanation
of how the mesh is used to model biological proteins also requires
revision to clarify the physical constraints or interpretation of the
resulting calculations.

I have identified several key questions and comments below:

- [x] 1) The manuscript would be significantly improved if the BEM
formulation could be compared with alternative implementations in more
detail. This would assist with comparisons between implementations
which is ultimately linked to aspirations for checks on
reproducibility and validation of the calculations beyond analytical
models. The question of validation between codes is beyond the scope
of the manuscript, but pointing readers to key similarities or key
differences in BEM implementations would provide a more complete
introduction and background framework on the use of BEM in solving
quasi-static as well as full Maxwell’s equations.

- [x] 2) The relaxation of some parameters for calculations shown in Figure
6 is not inherently a problem, but I would have thought that a figure
showing the wavelength dependence for the silver sphere with
decreasing meshes and for directly comparable sets of treecode
parameters used in Figure 5 would provide another important consistent
comparison.

- [x] 3) For BSA and other proteins, is it physical to represent them as an
unconstrained mesh? What I mean is, there are presumably regions that
are (chemically) motivated to be charged in particular ways which
would seem to possibly contribute dipoles at relevant length scales?
It is not clear to me in this manuscript how the dielectric function
value and its local or total dipole moment is represented on the mesh
used for the protein molecules. This may be discussed in other work,
but should be explained within this manuscript as it is central to the
calculations reported here.

- [x] 4) Is a classical treatment appropriate for distances of 1 nm (or less
than 1 nm)? How do results compare with 5 nm away? And how would the
calculations change for a gold particle rather than a silver one?

- [x] 5) Why have the authors elected to show calculations for two BSA
proteins not just one? Are the positions of the two particles opposite
each other selected because this relative positioning enhances the
reported effects?

- [x] 6) What are the relevant distances and concentrations for experimental
comparisons? Can this code handle those? (THE REPLY NEEDS SOME MORE WORK)

- [x] 7) Why do the authors report only the extinction cross section Cext?
Are there easy ways to calculate other optical properties from the
solved system (e.g. Cabs, Csca, near fields, scattering matrix)?
Perhaps a comment on the feasibility or computational obstacles to
these alternative outputs could be offered.

A few minor points:

- [x] 8) In the introduction of extinction, it is unclear if ‘a.k.a.’ is
referring to both scattering and absorption or just to the second part
of sentence (scattering).

- [x] 9) Is Gamma defined at its first appearance on p. 2?


### Comment 0 
> The manuscript may therefore merit publication in Physical Review E,
although it can be improved significantly to assist readers in
understanding the broader context of BEM approaches. The explanation
of how the mesh is used to model biological proteins also requires
revision to clarify the physical constraints or interpretation of the
resulting calculations.

#### Reply
The way biomolecules are modeled with the boundary element method was not detailed in the original manuscript, which led to this comment by the reviewer. This is not the main effort of the paper, and has been done previously with our code in reference [26]—Cooper, Bardhan, Barba (2014). Nonetheless, we should clarify for completeness. We have added a subsection under Methods called 'Protein mesh preparation', where we explain how we start from a molecular structure from the Protein Data Bank, and represent it as a surface mesh, clarifying the physical meaning of the molecular surface,and how the biomolecule is parameterized in terms of van der Waals parameters and charges.  

#### Modifications

We added a subsection called 'Protein mesh preparation' in commits [fb1785c](https://github.com/barbagroup/pygbe_lspr_paper/commit/fb1785c1744b0ef318128f167a95ff25f0e737fb) and [ab38e80](https://github.com/barbagroup/pygbe_lspr_paper/commit/ab38e80996577fa273a2fbdde17fd6f6b4af01d0).

### Comment 1
> 1) The manuscript would be significantly improved if the BEM
formulation could be compared with alternative implementations in more
detail. This would assist with comparisons between implementations
which is ultimately linked to aspirations for checks on
reproducibility and validation of the calculations beyond analytical
models. The question of validation between codes is beyond the scope
of the manuscript, but pointing readers to key similarities or key
differences in BEM implementations would provide a more complete
introduction and background framework on the use of BEM in solving
quasi-static as well as full Maxwell’s equations.


#### Reply
There are two research software codes that could be used in this setting: BEM++ and MNPBEM. They can solve either full Maxwell's equations or the quasi-static electrostatic approximation. However, they haven't been used in the context of biomolecules, and are not able to model with in the order of hundred-thousand boundary elements, which is required to represent molecular surfaces accurately. 

Part of this discussion was present in the conclusion of the original manuscript—we've now moved it to the introduction, and expanded it. This way, the reader will have a clearer idea of differences with similar available software.

The reviewer is not requesting that we run additional computations using these other software packages, acknowledging that is beyond the scope of our manuscript. Thank you!
The request is for explaining differences and similarities with other BEM implementations in this field. We have now added new text on this topic at the end of the Discussion section.

#### Modifications
- We have added mention of similar software (BEM++ and MNPBEM) in the introduction via commit [d44c84e](https://github.com/barbagroup/pygbe_lspr_paper/commit/d44c84e11520d81d6d6b4224587c2f1aaf921212).
- We have added a paragraph to the Discussion addresing similarities and differences with other BEM implementations, via commits [11a93e8](https://github.com/barbagroup/pygbe_lspr_paper/commit/11a93e82391a8f7b982f99f83680ab4a6e200a88) and [53e3db8](https://github.com/barbagroup/pygbe_lspr_paper/commit/53e3db86e96b63d9da4afaa60b9fadd043484fb0).


### Comment 2
>2) The relaxation of some parameters for calculations shown in Figure
6 is not inherently a problem, but I would have thought that a figure
showing the wavelength dependence for the silver sphere with
decreasing meshes and for directly comparable sets of treecode
parameters used in Figure 5 would provide another important consistent
comparison.


#### Reply
Figure 6 shows a visually undetectable error compared with the analytical solution. Repeating these calculations with a finer mesh or tighter parameters for the treecode will decrease the errors, but the figure will look the same. Currently, errors are everywhere smaller than 1%. These finer mesh and parameters, however, increase the time to solution by 12X. 
This justifies their use: undetectable difference in the results, with a considerable savings in compute time.

#### Modifications
- We have added the runtime advantage of relaxed parameters in [91e73b5](https://github.com/barbagroup/pygbe_lspr_paper/commit/91e73b5cc3926c1fbc653f79364b4ddfb6382923).


### Comment 3
>  3) For BSA and other proteins, is it physical to represent them as an
unconstrained mesh? What I mean is, there are presumably regions that
are (chemically) motivated to be charged in particular ways which
would seem to possibly contribute dipoles at relevant length scales?
It is not clear to me in this manuscript how the dielectric function
value and its local or total dipole moment is represented on the mesh
used for the protein molecules. This may be discussed in other work,
but should be explained within this manuscript as it is central to the
calculations reported here.


#### Reply

The molecular charges that appear in the last term of Eq. (17) are considered explicitly, and their effect does not need to be transferred to the mesh in the model. The effect of these charges on the boundary (mesh) is captured by this term in the mathematical formulation. The dielectric function is a uniform complex value inside the protein, and appears as `\epsilon_3` in Eq. (17). Its value depends on the wavelength.
Perhaps this was not clear as we didn't explain the physical meaning of the `q_k` variable in the original manuscript. This was fixed in the revised version.

#### Modifications
- To explain how the BSA molecules is modeled, we added a subsection called 'Protein mesh preparation' in commits [fb1785c](https://github.com/barbagroup/pygbe_lspr_paper/commit/fb1785c1744b0ef318128f167a95ff25f0e737fb) and [ab38e80](https://github.com/barbagroup/pygbe_lspr_paper/commit/ab38e80996577fa273a2fbdde17fd6f6b4af01d0). We also added an explanation of the meaning of `q_k` in commit [f648cd1](https://github.com/barbagroup/pygbe_lspr_paper/commit/f648cd1d25625b41b99887d1bd7def136e63404e). The molecule contains point charges at the local partial charges from applying `pdb2pqr` with an Amber force field. This model is broadly used to represent biomolecules.

### Comment 4
>4) Is a classical treatment appropriate for distances of 1 nm (or less
than 1 nm)? How do results compare with 5 nm away? And how would the
calculations change for a gold particle rather than a silver one?

#### Reply
1. Classical treatment is adequate for these small distances. A point of comparison is this study of coarse-grained MD (classic limit) where metallic nanoparticles are at similar distances from a membrane under an electric field: Shimizu, K., Nakamura, H. and Watano, S., 2016. MD simulation study of direct permeation of a nanoparticle across the cell membrane under an external electric field. Nanoscale, 8(23), pp.11897-11906, doi:[10.1039/C6NR02051H](http://doi.org/10.1039/C6NR02051H).
  - "The electrostatic interactions were calculated using the particle mesh Ewald (PME) method with a real space cut off length of 1.2 nm and a  fast Fourier-transform grid spacing of 0.24 nm." Fig. 5 shows distances between nanoparticle and membrane and they have values smaller than 1nm. 
2. At 5 nm the shift will be negligible and we won't see the effect of the proteins on the nanoparticle. At 2 nm we already see a smaller shift, reported in section Results-Sensitivity calculations (Fig 12).  
3. In order to answer fully this question we would need to perform multiple calculations using gold, which is out of the scope of this paper. However, we can say that the shift magnitude would be smaller due to gold's Figure of Merit, FOM (how a nanoparticle's sensing capability is characterized). The reason we chose silver instead of gold is because the FOM  of silver is better, according to [FarooqAraujo2018](https://file.scirp.org/pdf/OJAppS_2018032115143480.pdf). 

#### Modifications
- No modifications needed.


### Comment 5
>  5) Why have the authors elected to show calculations for two BSA
proteins not just one? Are the positions of the two particles opposite
each other selected because this relative positioning enhances the
reported effects?

####  Reply
Simulations were performed using two BSA dimers, hence, effectively, there are four BSA molecules. The choice is supported by experimental studies (Teichroeb et al 2008, reference [41] in the paper, see Comment 6). Using fewer analytes, the red shift would indeed be smaller, and we would need to examine a finer range of wavelengths to see a shift.

#### Modifications
- No modifications needed.


### Comment 6
> 6) What are the relevant distances and concentrations for experimental
comparisons? Can this code handle those?


#### Reply
Our simulations were performed under realistic conditions. Similar to our model with BSAs placed very close to the nanoparticle, there is experimental work where BSA is directly adsorbed on the metallic surface (without a layer of ligand in between), and the distance between them is effectively zero ([Tang et al 2010](https://pubs.acs.org/doi/abs/10.1021/jp1056336) and [Nghiem et al 2012](https://iopscience.iop.org/article/10.1088/2043-6262/3/1/015002/meta)). This has also been modeled computationally by other researchers ([Phan et al 2013](https://aip.scitation.org/doi/abs/10.1063/1.4826514) and [Dan and Hu 2014](https://avs.scitation.org/doi/abs/10.1116/1.4895964)).

In our simulations, we looked at the resonance shift of two BSA dimers near a 16nm-diameter nanoparticle, which agrees with [Teichroeb et al 2008](https://link.springer.com/article/10.1140/epje/i2007-10342-9). This work reports nanoparticles of 15nm diameter, with a concentration per surface area of 3.2x10^12 molecules /cm^2 (0.032 molecules/ nm^2). This gives approximately 4 to 6 molecules ( BSA-monomers) per nanoparticle.

#### Modifications
- Added more details regarding the experimental work of Teichroeb et al., 2008. Relevant commits to the manuscript: [0eb2637](https://github.com/barbagroup/pygbe_lspr_paper/commit/0eb2637a57f6c6096d76418a070e1db88156135c), [aaa9e79](https://github.com/barbagroup/pygbe_lspr_paper/commit/aaa9e79244de721909d15da720f9aaec599e6e68), fixed wording and typos in [eef190d3](https://github.com/barbagroup/pygbe_lspr_paper/commit/eef190d32e04dbab6b3e7f16aab46da712b3b003) and [14a5e06](https://github.com/barbagroup/pygbe_lspr_paper/commit/14a5e0661f02ea23fe21116d9af1eeb51069554f). 

### Comment 7
> 7) Why do the authors report only the extinction cross section Cext?
Are there easy ways to calculate other optical properties from the
solved system (e.g. Cabs, Csca, near fields, scattering matrix)?
Perhaps a comment on the feasibility or computational obstacles to
these alternative outputs could be offered.


#### Reply

The extinction cross section is the sum of the absorption and scattering cross sections. The reason why we report the extinction cross section only is that with our model, it is not possible to separate these two components. However, for such nanoparticles smaller than 20 nm, absorption dominates over the scattering (as detailed in [Petryayeva, E., & Krull, U. J. (2011).](https://www.sciencedirect.com/science/article/pii/S0003267011011196). and [Olson et al 2015](https://pubs.rsc.org/en/content/articlehtml/2015/cs/c4cs00131a)), making Cext approximately equal to Cabs. We will mention this fact in the manuscript.

By default, the code returns a file with the values of the potential and its derivative on the surface of the scatterer. This could be used to compute the field anywhere in the domain, including the region close to the nanoparticle. However, it would require some modifications to the code.

Also, in the computation of the extinction cross-section, we use the forward scattering amplitude, as detailed in Equation 5. This is one entry of the scattering matrix, and can be back-calculated from Equation 5. With the current status of the code, it is not possible to compute other entries of the scattering matrix.


#### Modifications 
- We mention that absorption dominates when nanoparticles are smaller than 20 nm; added on commits [252807e](https://github.com/barbagroup/pygbe_lspr_paper/commit/252807efdb12ec616f9dacc2367c9682a2592f31) and [c7ee588](https://github.com/barbagroup/pygbe_lspr_paper/commit/c7ee588d94f347154585a4d143fde4d4b4ed205a).

### Comment 8

> 8) In the introduction of extinction, it is unclear if ‘a.k.a.’ is
referring to both scattering and absorption or just to the second part
of sentence (scattering).


#### Reply
The "a.k.a., extinction" refers to the "shadow," produced by the combination of absorption and scattering. 


#### Modifications
- We rewrite as: "When this happens, most of the incoming energy is either absorbed by the nanoparticle, or scattered in different directions, both effects creating a shadow behind the scatterer (a.k.a., extinction)" on commit [ae87a75](https://github.com/barbagroup/pygbe_lspr_paper/commit/ae87a752fa38d56f3ae7b113ab696baf5d38f2be) and [c7ee588](https://github.com/barbagroup/pygbe_lspr_paper/commit/c7ee588d94f347154585a4d143fde4d4b4ed205a).


### Comment 9

> 9) Is Gamma defined at its first appearance on p. 2?


#### Reply
Yes, the first appearance is on page two. We added an explanation after it is first introduced saying that it is a boundary between regions `\Omega_1` and `\Omega_2` .

#### Modifications
- Fixed on commit [75c74a0](https://github.com/barbagroup/pygbe_lspr_paper/commit/75c74a05f61e7eab661d30f4235ea7c88fe54219).




##Reviewer 2 comments


In manuscript EC12092, Clementi et al. describe a boundary element method at the electrostatic limit to simplify the numerical calculation/analysis for bio-sensing using nanoplasmonics. Due to the conductive electrons of the metallic nano-particles (NP), the electric field/density of states will be significantly magnified at the hot spots, which in turn make the effective mode volume much smaller than the relatively more traditional optical cavities. As a result the light matter interaction is strongly enhanced when the target/matter is put around the NP, and this is the physical basis of most applications of nanoplamonics and the biosensing studied in the current manuscript. As a specific application of nanoplasmonic, the latest development in the field should be well referenced such as single molecule imaging Ref.[Nature 498, 82 (2013)] and the modal theory developed in the past few years Refs.[Phys. Rev. Lett. 110 237401 (2013); New J Phys. 16, 113048 (2014)]. With their own software (PyGBe) they could reduce the computational complexity as O(NlogN). Over all the manuscript is well presented with respect to its technical
details. 

- [x] However, the manuscript is made redundant at several places such as Subsection F in Section II and Subsection C in Section III; most of them could be moved the the documented files then make a reference to them at the reference list in order to make the manuscript more compact and readable. 

And the following are a number of issues/comments which need to be addressed:

- [x] 1. At the end of the manuscript, the authors claimed that for a distance (between the NP and the analytes ) of d = 0.5 nm the redshift of the peak 0.75 nm; but it seems at this regime the nonlocal effect could kick in Ref.[Nature Commun. 5, 3809 (2014)].

- [x] 2. The superindex in the definition of V and K in Eqs. (8-9) should be corrected.

- [x] 3. The bold fonts for pi between eq.(22) and eq.(24) should be changed into plain.

- [x] 4. Should the “location” in ”To study the effect of location of the analytes, ... Figure 13” (on page 9) be orientation?

- [x] 5. Figures (1) and (2) are basically the same which make the manuscript redundant. The same happens to Figs (3) and (7), and Figs (9) and (13)

- [x] 6. Is it possible to give more physical description of the bovine serum albumin proteins such as the distribution of the charge as implied in Eq.(12)? This I think may be useful to understand the effect of orientation of the molecule.

- [x] 7. On page 11 the authors wrote ”Figure 10 shows a red shift of the plasmon resonance frequency peak in presence of the BSA proteins. This result agrees with experimental observations [42,43] ...”. In fact the red shift is easy to understand from a two-mode model and assume the mode provided by the BSA proteins is a lower energy mode with respect to the pamonic mode. So it is hard to say the experiment support the numerical calculation here. Maybe it is better to add in new calculation with well established software/technique to support the numerics here; this is just a very personal suggestion, and I would leave it to the author to decide.

To summarize, the current manuscript is treating some interesting problem, but there are some questions need to be addressed. So I would not recommend any form of publication until the questions/comments are fully addressed.

### Comment -1
> As a specific application of nanoplasmonic, the latest development in the field should be well referenced such as single molecule imaging Ref.[Nature 498, 82 (2013)] and the modal theory developed in the past few years Refs.[Phys. Rev. Lett. 110 237401 (2013); New J Phys. 16, 113048 (2014)].


#### Reply
The reviewer points out interesting references. The first one is related to our work, as it is regarding efforts towards single-molecule detection. We added this reference in the discussion section, where the issue of experimental evidence of low-analyte concentration is discussed.

We believe the other two references are out of the scope to our work. These focus on the modal theory of quantum effects in nanoplasmonics, without referencing biosensing applications. In our work, we focus on nanoplasmonics for biosensing and use a classical approach.

#### Modifications
- We added reference to Nature 498, 82 (2013) in commit [58228689](https://github.com/barbagroup/pygbe_lspr_paper/commit/582286896d96b0933244e927e2cfabe613c15d9a).


### Comment 0
>  However, the manuscript is made redundant at several places such as Subsection F in Section II and Subsection C in Section III; most of them could be moved the the documented files then make a reference to them at the reference list in order to make the manuscript more compact and readable.

#### Reply
§II.F. lists the code modifications and enhancements needed to produce the results in this paper, and we feel is necessary to include in the Methods portion of the paper. §III.C. is our standard statement on reproducibility of the results, which our group has made a pledge to always include. The sum of these two sub-sections is about one column of text, which hardly impacts the overall length. 

#### Modifications
- No modifications needed



### Comment 1
> 1. At the end of the manuscript, the authors claimed that for a distance (between the NP and the analytes ) of d = 0.5 nm the redshift of the peak 0.75 nm; but it seems at this regime the nonlocal effect could kick in Ref.[Nature Commun. 5, 3809 (2014)].

#### Reply
According to the reference cited by the referee, the model presented by the authors has a validity domain. For the case of metallic Ag and Au nanoparticles, the authors say: "We point out that our diffusive model is valid for structural dimensions exceeding the mean-free path that in pure single crystals can be of the order of 100 nm for Ag and Au... " In our case the nanoparticles are of 8nm of radius and the interactions are between a metallic nanoparticle and a protein that doesn't generate plasmons. 


#### Modifications
- no modifications needed

### Comment 2
> 2. The superindex in the definition of V and K in Eqs. (8-9) should be corrected.

#### Reply
The inconsistency in the superindices from Eq 8-9 was fixed by replacing `\mathbf{r}_\Gamma` for `\Gamma` .
 
#### Modifications
- Fixed in commit [70757e3](https://github.com/barbagroup/pygbe_lspr_paper/commit/70757e38d910f2d25e81100bb3c46942127c0112).


### Comment 3
>  3. The bold fonts for pi between eq.(22) and eq.(24) should be changed into plain.

#### Reply
The bold fonts for p_i were removed. 

#### Modifications
- Fixed in commit [9b620d7](https://github.com/barbagroup/pygbe_lspr_paper/commit/9b620d756fce1670503f8912e6423b2278f76ea3).


### Comment 4
> 4. Should the “location” in ”To study the effect of location of the analytes, ... Figure 13” (on page 9) be orientation?


#### Reply
We are referring to the location not the orientation. We refer to the position on the x, y or z axis. The x and y configurations were obtained by performing a solid rotation of the z-configuration of 90 degrees along the x- and y-axis respectively. This statement was added in the text to clarify the point. 

#### Modifications
- Added note on how we obtained these configurations in commit [8180cb0](https://github.com/barbagroup/pygbe_lspr_paper/commit/8180cb005d737a6276bb3f78a613d4af17d2dbec).


### Comment 5
> 5. Figures (1) and (2) are basically the same which make the manuscript redundant. The same happens to Figs (3) and (7), and Figs (9) and (13)


#### Reply
- With respect to Figures 1 and 2, we believe that Figure 1 represent more the physics while Figure 2 aims to explaining the model. Therefore we prefer to leave them. 
- Regarding Figures 3 and 7, we agree with the reviewer. We removed Figure 7 and adapted Figure 3. 
- Figures 9 and 13 do not represent the same arrangement of the proteins; to make this point clear we adapted the figures by adding the direction of the electric field. 

#### Modifications
- We adapt Fig 3 and remove Fig 7. Changes made in commit [e525375](https://github.com/barbagroup/pygbe_lspr_paper/commit/e525375ae77105930f16eae96669f66052f3f227).
- We add electric field direction on display figures (old 9 and 13). Changes made in [8de6810](https://github.com/barbagroup/pygbe_lspr_paper/commit/8de6810a815605e708353273abad023a49c08843).


### Comment 6
>  6. Is it possible to give more physical description of the bovine serum albumin proteins such as the distribution of the charge as implied in Eq.(12)? This I think may be useful to understand the effect of orientation of the molecule.


#### Reply
This is related to Comment 0 of the first reviewer. In the original manuscript, it wasn't clear how the biomolecule is modeled with boundary integrals. This has been done previously with our code (citation [24]), however, we've added a section under Methods called 'Protein mesh preparation' explaining how the biomolecule is prepared, starting from its molecular structure in the Protein Data Bank, to the parameterization and physical meaning of the molecular surface definition. We also found a mistake in  the charge representation of Equation (12), which may have led to the confusion of the Reviewer, and the charge `q_k` was not being introduced accordingly.

#### Modifications
- Added a subsection called 'Protein mesh preparation' in commits [fb1785c](https://github.com/barbagroup/pygbe_lspr_paper/commit/fb1785c1744b0ef318128f167a95ff25f0e737fb) and [ab38e80](https://github.com/barbagroup/pygbe_lspr_paper/commit/ab38e80996577fa273a2fbdde17fd6f6b4af01d0).
- Added introduction of `q_k` variable in commit [f648cd1d](https://github.com/barbagroup/pygbe_lspr_paper/commit/f648cd1d25625b41b99887d1bd7def136e63404e). 
- Fixed Equation (12) in commit [4aa36fb](https://github.com/barbagroup/pygbe_lspr_paper/commit/4aa36fb5c6f53f49d172f199942355568b08d728).


### Comment 7
> 7. On page 11 the authors wrote ”Figure 10 shows a red shift of the plasmon resonance frequency peak in presence of the BSA proteins. This result agrees with experimental observations [42,43] ...”. In fact the red shift is easy to understand from a two-mode model and assume the mode provided by the BSA proteins is a lower energy mode with respect to the pamonic mode. So it is hard to say the experiment support the numerical calculation here. Maybe it is better to add in new calculation with well established software/technique to support the numerics here; this is just a very personal suggestion, and I would leave it to the author to decide.


#### Reply
The reviewer asserts that the red shift we observe can be explained from the point of view of a two-mode model. We are not familiar with this theory, but if this relates to the references cited by the reviewer at the beginning of the report, it appears to be in a quantum-mechanics setting, which is outside the scope of our paper. The issue at hand, though, is how much the experimental results support our computational results. We removed the claim that the experimental results "agree" and simply state what they report and leave the reader to decide if they find the correspondence convincing enough.

Regarding adding other calculations with well-established software: 1) We provide evidence that our software solves correctly the mathematical model via grid convergence tests. 2) We are unable to run simulations with another open-source software because they cannot handle the amount of boundary elements we are using. 3) The options of running with commercial software is not something we can do because we don't have access to such paid software.

#### Modifications

- We delete the language "This result agrees with experimental observations" and state only what the experimental papers report. Changes in [1556a72](https://github.com/barbagroup/pygbe_lspr_paper/commit/1556a72913b312f3817343fd68371038540f5a04), [df3c348](https://github.com/barbagroup/pygbe_lspr_paper/commit/df3c3489d25a49705126ccdf80da0b4858d9673c) and [b8a6e28](https://github.com/barbagroup/pygbe_lspr_paper/commit/b8a6e28f29202f71463df662cd8431318f83522f).

# Response to reviewers - round two

## Reviewer 1 comments

The authors have provided thorough responses to all comments raised in review and in the majority of cases have provided satisfactory explanations or modifications to the text to improve the quality of the manuscript.

I am pleased to recommend the manuscript for publication in Physical Review E subject to minor changes to address a few remaining points identified below. I have also included notes below on a few items that do not require changes but where comments seemed appropriate (within an itemized list of the comments and responses).


- [x] Comment 1: The authors have added a good discussion of BEM++ and MNPBE and how these differ in terms of implementation and how PyGBe is better suited to address the problems presented in the manuscript.

- [x] Comment 2: There are two possible ways to come at consistency between parameters used in Fig. 5 and Fig. 6. I appreciate that the parameters used for Fig. 5 would be prohibitively expensive. Instead, could the grid convergence be run with the ‘relaxed’ parameters? This is a minor point and could add unnecessarily complexity to figures and verification tests.

- [x] Comment 4: I am not yet convinced by the reply here. The authors refer to a molecular dynamics simulation (classic limit) paper with an electrostatic field. The question in Comment 4 was centered on whether there are quantum mechanical or relativistic/retardation effects which might need to be accounted for given the size regimes discussed. The MD paper would not appear to account for either of these factors. Dispersion effects may become more prominent in gold and require an electrodynamic treatment. Additionally, quantum tunneling effects might occur even in systems that are not two metal nanoparticles interacting (although the quantum regime may be for gaps closer to 0.5 nm and for very small particles the quasi-static approximations may certainly still be valid). It may be worth noting in the manuscript that there may be limitations due to the choice of classical treatment for very small distances and systems which are not well-described in quasi-static terms.

- [x] Comment 5: I am not entirely satisfied by the reply here as the authors have not made any comment on the particular configuration of two particles opposite each other raised in the question. This appears to be a high symmetry arrangement and therefore may represent a
‘special’ geometry with either enhanced or damped effects relative to a more randomly distributed arrangement of particles of BSA dimer around the surface of the sphere. Would the authors be able to clarify this point in the text? I would also suggest that the authors clearly
identify the BSA particles as dimers in the relevant figure captions (e.g. Fig. 8).

- [x] Comment 6: I would suggest that the changes made in response to this comment be qualified and presented with a bit more care. The Teichroeb reference uses gold particles of 15 nm diameter. This raises questions about the utility of the comparison given that gold and silver
particles of comparable size will have very different wavelength dependent responses arising from the differences in the metal dielectric functions. The comparison of concentrations also deserves some attention due to seeming differences between monomer concentrations and dimer concentrations (number of particles per unit volume). The authors suggest that the Teichroeb paper would be equivalent to modeling 4 to 6 BSA-monomers around the nanoparticle. Why have the authors opted to model the BSA as dimers? The concentration of “\Omega_3” particles (to abuse the notation in Fig. 3 somewhat, to capture the number of particles/closed surfaces of BSA per unit volume) would also seem to be different by a factor of 2-3 if the concentration in Teichroeb is strictly 4 to 6 separate monomers (integer counting of separate particles/molecules) suggesting 4 to 6 “\Omega_3” particles arranged, possibly asymmetrically, around the gold particle. Here, there are 2 “\Omega_3” particles arranged symmetrically around a silver particle. Broadly, the Teichroeb values may serve as a suitable motivation, but I would hesitate to say that these parameters are directly comparable values – perhaps in the same ballpark. The authors’ work would potentially appear to be at lower concentrations which is a positive in one regard – that the shift in the peak of the extinction is detectable at lower numbers of particles around the metal nanoparticle. But this comparison can also be viewed more pessimistically – that the modeling of 4 to 6 molecular surfaces might become prohibitively costly in terms of computations. I think some further comment on all of this may be warranted with a more judicious treatment in the final text.

- [x] Comment 7: I would suggest the authors note the limitations discussed in their reply in the main text. That is, explicit discussion of the fact that changes would be required to calculate the fields or other elements of the scattering matrix should be added (and could be done
very briefly). Given the manuscript's focus on presenting the new code, identifying where further modifications to the code could be made would not go amiss.


### Comment 2 :
>There are two possible ways to come at consistency between parameters used in Fig. 5 and Fig. 6. I appreciate that the parameters used for Fig. 5 would be prohibitively expensive. Instead, could the grid convergence be run with the ‘relaxed’ parameters? This is a minor point and could add unnecessarily complexity to figures and verification tests.


**Reply**

The goal of the grid-convergence analysis in Fig. 5 is to find a mesh density that correctly resolves all the features of the problem. All the other parameters need to be set as fine as possible such that the errors associated with them do not contaminate the error from the mesh, and we can see the expected 1/N convergence. Using 'relaxed' parameters for this purpose would contaminate the error and prevent us to see the 1/N convergence.


## Comment 4:
>I am not yet convinced by the reply here. The authors refer to a molecular dynamics simulation (classic limit) paper with an electrostatic field. The question in Comment 4 was centered on whether there are quantum mechanical or relativistic/retardation effects which might need to be accounted for given the size regimes discussed. The MD paper would not appear to account for either of these factors. Dispersion effects may become more prominent in gold and require an electrodynamic treatment. Additionally, quantum tunneling effects might occur even in systems that are not two metal nanoparticles interacting (although the quantum regime may be for gaps closer to 0.5 nm and for very small particles the quasi-static approximations may certainly still be valid). It may be worth noting in the manuscript that there may be limitations due to the choice of classical treatment for very small distances and systems which are not well-described in quasi-static terms.

**Reply**
This was also noted by reviewer 2. We are aware of the possibilities of quantum effects, although according to the literature it is not fully clear is they are present in our case. In response to the reviewers, we decided to mention this in the manuscript, both in the caption of Fig 11 as well as in the Discussion section, with references.


## Comment 5 
>I am not entirely satisfied by the reply here as the authors have not made any comment on the particular configuration of two particles opposite each other raised in the question. This appears to be a high symmetry arrangement and therefore may represent a
‘special’ geometry with either enhanced or damped effects relative to a more randomly distributed arrangement of particles of BSA dimer around the surface of the sphere. Would the authors be able to clarify this point in the text? I would also suggest that the authors clearly
identify the BSA particles as dimers in the relevant figure captions (e.g. Fig. 8).

**Reply**
- Regarding the placement of the two proteins (dimers) opposite each other on an axis, the reason for this arrangement is that—at this proof-of-concept stage—we decided to methodically vary two conditions: distance to the nanoparticle, and principal axis alignment with the electric field. The electric field is aligned with the z-direction. We thus position the proteins in axes aligned with x, y and z. If the proteins were not opposite each other, the definition of "aligned" w.r.t. the electric field becomes vague. In essence, we would have infinite possibilities of arrangement, which resists a methodical treatment.
- Following the reviewer's suggestion, we changed 'protein' to 'dimer'  in the captions of all the relevant figures.

**Modifications** 
- In Fig 7,8,9,10,11 and 12 I specify that BSA where dimers. Number of commit 23ceae1


## Comment 6: 
>I would suggest that the changes made in response to this comment be qualified and presented with a bit more care. The Teichroeb reference uses gold particles of 15 nm diameter. This raises questions about the utility of the comparison given that gold and silver particles of comparable size will have very different wavelength dependent responses arising from the differences in the metal dielectric functions. The comparison of concentrations also deserves some attention due to seeming differences between monomer concentrations and dimer concentrations (number of particles per unit volume). The authors suggest that the Teichroeb paper would be equivalent to modeling 4 to 6 BSA-monomers around the nanoparticle. Why have the authors opted to model the BSA as dimers? The concentration of “\Omega_3” particles (to abuse the notation in Fig. 3 somewhat, to capture the number of particles/closed surfaces of BSA per unit volume) would also seem to be different by a factor of 2-3 if the concentration in Teichroeb is strictly 4 to 6 separate monomers (integer counting of separate particles/molecules) suggesting 4 to 6 “\Omega_3” particles arranged, possibly asymmetrically, around the gold particle. Here, there are 2 “\Omega_3” particles arranged symmetrically around a silver particle. Broadly, the Teichroeb values may serve as a suitable motivation, but I would hesitate to say that these parameters are directly comparable values – perhaps in the same ballpark. The authors’ work would potentially appear to be at lower concentrations which is a positive in one regard – that the shift in the peak of the extinction is detectable at lower numbers of particles around the metal nanoparticle. But this comparison can also be viewed more pessimistically – that the modeling of 4 to 6 molecular surfaces might become prohibitively costly in terms of computations. I think some further comment on all of this may be warranted with a more judicious treatment in the final text.


**Reply**
The reviewer made a good point that our reference to the experimental work of Teichroeb et al. was a little sloppy, mixing concentration with comparison of particle size. Also, the characterization as "similar" sounded stranger than we intended. In fact, we simply want to say (like the reviewer suggests) that our choices are in the ballpark with published experimental work. We revised the passage carefully, and more precisely refer to comparable volume fractions (rather than concentration).
Regarding the capacity of the code to compute problems with more proteins around the nanoparticle, we report on the paper that it can handle half a million boundary elements. The cases with two dimers have around 120k, so there is ample room for bigger problems.

**Modifications**
- Modified text. Commit number 3a0a712


## Comment 7: 
>I would suggest the authors note the limitations discussed in their reply in the main text. That is, explicit discussion of the fact that changes would be required to calculate the fields or other elements of the scattering matrix should be added (and could be done very briefly). Given the manuscript's focus on presenting the new code, identifying where further modifications to the code could be made would not go amiss.

**Ideas**
The reviewer suggests we should add things we said in the reply to the text. In comment 7, our reply was:
- We are not able to separate scattering and absorption cross sections, even though absorption dominates for small nanoparticles.
- Currently, the code only computes potential and its derivative on the surface, which allows to calculate the electric field if desired. 
- We cannot compute other terms of the scattering S-matrix currently, only the forward scattering amplitude (which is one term of the matrix)

**[Naty's attempt to reply]**

We added in the text (methods section) that we not only compute the potential on the surfaces but we also compute the normal derivative of the potential. The normal derivative of the potential allows the direct calculation of the electric field on the surface if desired.  This was included in commit number 272285e
Regarding the other elements of the scattering matrix, we disagree with the reviewer on including on the text what modifications of the code we would need to do to include this, since it doesn't not add value to our main result.

**[Chris]**
The reviewer makes a fair point that we are not being explicit about everything that is an output of our code. The solution of the linear system we are solving is the potential and its normal derivative (electric field in the normal direction) evaluated at the surface of the molecules and nanoparticle, which may be important information to, for example, detect potential hot spots on the scatterer. We added this information in the methods section. Commit 272285e.

Even though it may be desirable to output other terms of the scattering matrix, the code in its current state cannot calculate them. However, considering they are not required to compute the parameters we are presenting, we feel that including such discussion on the main text does not add more information to the paper.

------------------------------------------------------------------------------------------------------

## Reviewer 2 comments

> It is fair the authors thought that some of the references are not quite related to their current study. But it does not make sense to say that the quantum effect is beyond the scope of the research so they do not care about it. To be more specific the authors should justify why their full classical calculation at distance $d=0.5~$nm makes any sense --- namely why we should believe it is right. This is extremely important and relevant here: the authors should make it clear when their prediction is reliable since the whole research here is about an in-house numerical soft-ware/method. And I strongly doubt that at $d=0.5~$nm there will be (quantum) tunneling of electrons between the metallic particle and the molecules; if this is the case then the quantitative analysis at such a small distance does not make much sense. So there are two choices: 1) the authors could argue that the quantum effect is negligible so their result is correct; or 2) the authors delete the relevant result to make their conclusion scientifically sound.

As a result I would not recommend the acceptance of current manuscript for publication until the authors address the above comment properly.


**Comment**
The reviewer is concerned that the case with smallest distance (d=0.5 nm) could be incorrect, due to the fact that our model does not include quantum effects. The question of whether quantum effects, e.g., quantum tunneling of electrons between the nanoparticle and the protein, are applicable in this case is not straightforward to answer. We reviewed the literature more carefully to answer the reviewer's question, and found the following:


**Reply**
The reviewer raises an important point in this comment. It is true that our model cannot handle quantum effects, such as tunneling, which may be present at small distances between the analyte and the nanoparticle. In particular, this may be a problem for our last test case, when that distance is 0.5nm.

The literature gives some evidence that 0.5nm is within the validity domain of a classical approach:
-  [Savage et al 2012](https://www.nature.com/articles/nature11653.pdf) studied tunneling effects in plasmonic systems. In particular, they consider two nanostructures, and look at tunneling as a function of the inter particle distance. In this paper, the authors claim that plasmon interactions are consistent with the classical approach when `d>~0.4nm`. Moreover, their results show that the quantum and classical predictions start diverging at `d=0.31nm`. 
- [Esteban et al 2012](https://www.nature.com/articles/ncomms1806.pdf) presents a "quantum corrected model", that incorporates quantum-mechanical effects in the classical electrodynamics approach. Their results show the tunnelling transmission probability  as a function of separation between two metallic nanospheres, and state that the tunnelling regime happens between `0.1 nm < d <~0.5 nm`. However, the probability of transmission at 0.5 nm is almost zero.  

These two articles support that, in systems that are similar to ours, quantum effects can be ignored for the one case we include with `d=0.5nm`. However, it is close to the limit. We are aware of articles that consider such distances inside the quantum regime, for example, [Garcia de Abajo 2008](https://pubs.acs.org/doi/pdf/10.1021/jp807345h?rand=q4g7gkca) and [Ciraci et al 2012](https://science.sciencemag.org/content/sci/337/6098/1072.full.pdf)

In conclusion, we understand the reviewer's concern, however, from the literature it is not clear that for the distance `d=0.5 nm` quantum effects are significant. In response to the reviewer's concern, we added a disclaimer stating that the model does not consider quantum effects, even though they might be present in our last test case. We mention it both in the caption of Fig 11 as well as in the Discussion section, with references.

**Modifications:**
- Add note in caption of Fig 11: commit number 13878d3 and 6965bbd 
- Add comment on discussion section: commit number 178e02f, 6998713 and 567a395




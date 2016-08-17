# HPatches

This is the first release of the *HPatches* (Homography patches) dataset and benchmark for local descriptor matching. This dataset will be used as the basis for the descriptor matching challenge that will be presented in the
[Local Features: State of the Art, Open Problems and Performance Evaluation](http://www.iis.ee.ic.ac.uk/ComputerVision/DescrWorkshop/index.html)
workshop at ECCV 2016. There is a companion [*HBench*](https://github.com/featw/hbench) toolbox which implements the *HPatches* evaluation protocol and allows to produce the result files required to enter the challenge.

> **Note:** Currently we are releasing *only the development (Training) subset* of the data. The test set will be released a few week before the challenge at the ECCV 2016 workshop .

To download the HPatches dataset (training data), download and untar the following file:

* [HPatches training set](http://www.iis.ee.ic.ac.uk/ComputerVision/DescrWorkshop/hpatches-train.tar.gz) [1.5GB].
* HPatches test set (coming soon).

## Dataset description

* i_X: sequences with illumination changes
* v_X: sequences with viewpoint changes

For each sequence, we provide a set of reference patches `ref.png` extracted from a reference image. 
`eX.png` and `hX.png` contain the same patches found in `ref.png` with less significant (e-easy) and 
more significant deformations (h-hard). 

Note that each patch is `65x65` pixels.

Code for reading the patches in several languages is provided on the `code` folder.

For more information contact:

[Karel Lenc](mailto:karel@robots.ox.ac.uk)

[Vassileios Balntas](mailto:v.balntas@imperial.ac.uk)

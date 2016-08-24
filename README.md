# hpatches: Homography-patches dataset
A dataset with patches extracted from a large set of planar
sequences. 

For more information, please check the website for the
[Local Features: State of the art, open problems and performance evaluation](http://www.iis.ee.ic.ac.uk/ComputerVision/DescrWorkshop/)
workshop which will take place together with ECCV 2016.

Currently we are releasing only the training set for the ECCV-2016 workshop. 
The test set with the evaluation methods will be released soon. 

To download the hpatches dataset (training data), download and untar the following file

`wget www.iis.ee.ic.ac.uk/ComputerVision/DescrWorkshop/hpatches-train.tar.gz`

## Training set description
* i_X: sequences with illumination changes
* v_X: sequences with viewpoint changes

For each sequence, we provide a set of reference patches `ref.png` extracted from a reference image. 
`eX.png` and `hX.png` contain the same patches found in `ref.png` with less significant (e-easy) and 
more significant deformations (h-hard). Note that each patch is `65x65` pixels.

Sample code for reading the patches in python is provided on the
`code` folder. 

For information about relevant citations concerning patches extracted from sequences
that were not originally introduced in this dataset, please check [references.txt](references.txt)

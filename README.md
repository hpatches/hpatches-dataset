# hpatches

First release of the homography patches dataset. 

Currently we are releasing only the training set for the ECCV-2016 workshop. 
The test set with the evaluation methods will be released soon. 

To download the hpatches dataset (training data), download and untar the following file

`wget www.iis.ee.ic.ac.uk/ComputerVision/DescrWorkshop/hpatches-train.tar.gz`

## Training set description
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

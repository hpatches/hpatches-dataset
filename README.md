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

Sample code for reading the patches in python is provided on the
`code` folder.

For information about relevant citations concerning patches extracted from sequences
that were not originally introduced in this dataset, please check [references.txt](references.txt)

## Dataset Description
Patches are organized in sequences which correspond to folders:
* i_X: patches from image sequences with illumination changes
* v_X: patches from image sequences with viewpoint changes

For each sequence, we provide a set of reference patches `ref.png` extracted from a reference image.
`eX.png` and `hX.png` contain the same patches found in `ref.png` with less significant (e-easy) and
more significant (h-hard) artificial affine jitters. Note that each patch is `65x65` pixels and multiple patches are concatenated along the rows.

## Training Set Description
In training set, patches are ordered by their location. This means that `i`th patch in the file `ref.png` (located at rows `(i-1)*65+1 ... i*65` for one-indexed rows) is extracted from the same location in the image (plus some jitter) as the `i`th patch from the `eX.png` or `hX.png`.

## Patch Extraction Method
Each image sequence contains a reference image and 5 target images with different illumination and/or different viewpoint for a planar scene. For all images we have the estimated ground truth homography `H` (stored in CSV files `H_ref_X` where `X=1..5`).

![Example sequence](img/images.png)
*Image 1: Example sequence. First image is the reference image followed by 5 images with a different viewpoint.*

Patches are sampled in the reference image using combination of local feature extractors (Hessian, Harris and DoG detector). Patch orinetation is estimated using a single major orientation from Lowe's method. No affine adaptation is used, therefore all patches are square regions in the reference image.

Patches are extracted from regions with a scale magnified by a factor of 5 compared to the original detected feature scale. Only patches which measurement region is are present fully in all images of a sequence are kept.

In order to prevent multiple detections on the same location, only single feature is selected by random from a cluster of patches with an ellipse overlap higher than 50%. A subset of the detected patches with their measurement regions is shown in the following image:

<center>![Example detections](img/detections.png)</center>

*Image 2: Example detections on the reference image. Patches locations are visualized as ellipses. The scale of the detected patches (orange) is magnified by factor 5 to obtain the patch measurement region (yellow).*

In order to extract the patches from a target image, at first an affine jitter is applied. The goal of the affine jitter is to simulate the mistakes of local features detector.

For easy jitter, the median ellipse overlap with the original patches is ~0.85, for hard jitter it is ~0.72. Then, the frames are reprojected to the target image using the ground truth homography.

The following images show the reprojected easy/hard patches in the target image together with extracted patches.

![Reprojected easy patches](img/images_easy.png)
*Image 3: Visualization of the easy patches locations in the target images.*

![Extracted easy patches](img/patches_easy.png)
*Image 4: Extracted easy patches from the example sequence.*

![Reprojected hard patches](img/images_hard.png)
*Image 5: Visualization of the hard patches locations in the target images.*

![Extracted hard patches](img/patches_hard.png)
*Image 6: Extracted hard patches from the example sequence.*

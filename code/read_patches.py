from scipy import misc
import numpy as np

# all available patch types 
p_itr = ['ref','e1','e2','e3','e4','e5','h1','h2','h3','h4','h5']

# simple loading interface for sequences - makes the patches accesible 
# directly e.g. -> sequence.patches['ref'][0] accesses the first reference
# patch from the sequence 

class featw_sequence:
    """A simple class that loads a featw sequence"""
    def __init__(self,name,base):
        self.name = name
        self.base = base
        self.patches = {}

        for i in p_itr:
            im = misc.imread(self.base+self.name+'/'+i+'.png')
            self.n_feats = im.shape[0]/65
            self.patches[i] = np.split(im, self.n_feats)  

# download the hpathces-train dataset and extract in root repo folder
# more info - https://github.com/featw/hpatches
# adjust accordingly if you download hpatches-train on a different folder
seq = featw_sequence('v_calder','../hpatches-train/')

#show all patches idx-th feature frame
idx = 100
pt = np.array([])
for i in p_itr:
    p_buf = seq.patches[i][idx]
    pt = np.hstack([pt,p_buf]) if pt.size else p_buf
misc.imshow(pt)

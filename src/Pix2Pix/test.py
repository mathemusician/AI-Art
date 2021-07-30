#%%

from getpaths import getpath
from skimage import io as io
# make splicer

# get images
image_path = getpath('/Users/mosaicchurchhtx/Desktop/ScriptReader/MSS_Borg.ind.28', custom=True)

file_names = [i for i in image_path.ls() if i[-3:] == 'jpg'][0]


# splice images
io.concatenate_images(ic)

# put images back together

# %%

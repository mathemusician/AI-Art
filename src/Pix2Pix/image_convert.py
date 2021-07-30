#%%
from Pix2Pix_PL import *

# load the latest checkpoint
checkpoint_path = getpath('/Users/mosaicchurchhtx/Downloads/last.ckpt', custom=True)
image_path = getpath('/Users/mosaicchurchhtx/Desktop/test_output', custom=True)
output_image_path = getpath()/'test_images'

# make sure output image path exists
if not os.path.exists(output_image_path):
    os.makedirs(output_image_path)

print('Using checkpoint path: ', checkpoint_path)

model = Pix2Pix.load_from_checkpoint(checkpoint_path = checkpoint_path)
model.freeze()

# put the datamodule in test model
datamodule.setup("test", pathA=image_path, pathB=None)
test_data = datamodule.test_dataloader()

trainer = pl.Trainer(gpus = 0, profiler = 'simple')
trainer.test(model, test_dataloaders = test_data)

#%%
for index, image in enumerate(datamodule.test):
    T.functional.to_pil_image(model.forward(image['A'].unsqueeze(0)).squeeze(0)).save(output_image_path/f'{index}.png')

# T.functional.to_pil_image(model.forward(datamodule.train[0]['A'].unsqueeze(0)).squeeze(0)).save('new.jpg')
# %%

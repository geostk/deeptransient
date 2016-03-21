import caffe
import numpy as np

#
# load the trained net (default: TransientNet-H) 
#

MODEL = './transientnet_models/deploy.net'
PRETRAINED = './transientnet_models/transientneth.caffemodel'
MEAN = './data/transient_mean.binaryproto'

#
# load the mean image 
#

blob=caffe.io.caffe_pb2.BlobProto()
file=open(MEAN,'rb')
blob.ParseFromString(file.read())
means = caffe.io.blobproto_to_array(blob)
means = means[0]

caffe.set_mode_cpu()
net = caffe.Net(MODEL, PRETRAINED, caffe.TEST)

#
# load and process the image
#

image = 'data/example_webcam.jpg'

im = caffe.io.load_image(image)
im = caffe.io.resize_image(im, (256,256))
im = im[:,:,[2,1,0]]
im = im.swapaxes(0,2).swapaxes(1,2)
im = (255*im).astype(np.uint8, copy=False)

caffe_input = im - means
caffe_input = caffe_input.transpose((1,2,0))
caffe_input = caffe.io.resize_image(caffe_input, (227,227))
caffe_input = caffe_input.transpose((2,0,1))
caffe_input = caffe_input.reshape((1,)+caffe_input.shape)

#
# push through the network
#

out = net.forward_all(data=caffe_input)
pred = out['fc8-t'].squeeze()

#
# output the results
# clean this up to include attribute labels
#

print pred

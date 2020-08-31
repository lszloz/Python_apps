
with open("VGG_ILSVRC_16_layers_fc_reduced.caffemodel", 'ab') as f:
    for i in range(4):
        with open(str(i), 'rb') as seg:
            f.write(seg.read())

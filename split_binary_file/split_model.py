
with open("VGG_ILSVRC_16_layers_fc_reduced.caffemodel", 'rb') as f:
    byte_list = []
    while True:
        single_r = f.read(25165824)
        if single_r:
            byte_list.append(single_r)
        else:
            break

for i in range(len(byte_list)):
    with open(str(i), 'wb+') as f:
        f.write(byte_list[i])


'''
    checkpoint_path = getpath(os.getcwd(), custom=True)/'logs/Pix2Pix'
    checkpoint_path_list = sorted([int(x[8:]) for x in checkpoint_path.ls() if x[0] == 'v'])
    latest_folder = 'version_' + str(checkpoint_path_list[-1])
    checkpoint_path = checkpoint_path/latest_folder/'checkpoints'
    checkpoint_path_list = sorted(checkpoint_path.ls())
    latest_file = checkpoint_path_list[-1]
    checkpoint_path = checkpoint_path/latest_file
    '''
import os
import pandas as pd
import random
from glob import glob


def split_dataset(image_list, image_folder, landmark_file_folder, landmark_mask_folder, output_folder):
    """
    Generate dataset
    """
    seed = 0
    random.Random(seed).shuffle(image_list)

    num_training_images = int(len(image_list) * 4 // 5)
    training_images = image_list[:num_training_images]
    test_images = image_list[num_training_images:]

    # generate dataset for the training set
    content = []
    training_images.sort()
    print('Generating training set ...')
    for name in training_images:
        print(name)
        image_path = os.path.join(image_folder, name, 'org.nii.gz')
        landmark_file_path = os.path.join(landmark_file_folder, '{}.csv'.format(name))
        #landmark_mask_path = os.path.join(landmark_mask_folder, name, '{}.nii.gz'.format(name))
        landmark_mask_path = os.path.join(landmark_mask_folder, '{}.nii.gz'.format(name))
        content.append([name, image_path, landmark_file_path, landmark_mask_path])

    csv_file_path = os.path.join(output_folder, 'train.csv')
    columns = ['image_name', 'image_path', 'landmark_file_path', 'landmark_mask_path']
    df = pd.DataFrame(data=content, columns=columns)
    df.to_csv(csv_file_path, index=False)

    # generate dataset for the test set
    content = []
    test_images.sort()
    print('Generating training set ...')
    for name in test_images:
        print(name)
        image_path = os.path.join(image_folder, name, 'org.nii.gz')
        landmark_file_path = os.path.join(landmark_file_folder, '{}.csv'.format(name))
        landmark_mask_path = os.path.join(landmark_mask_folder, name, '{}.nii.gz'.format(name))
        content.append([name, image_path, landmark_file_path, landmark_mask_path])

    csv_file_path = os.path.join(output_folder, 'test.csv')
    columns = ['image_name', 'image_path', 'landmark_file_path', 'landmark_mask_path']
    df = pd.DataFrame(data=content, columns=columns)
    df.to_csv(csv_file_path, index=False)

def split_dataset(data_list_folder, output_folder):
    """
    Generate dataset
    """
    seed = 0
    random.Random(seed).shuffle(data_list_folder)

    num_training_images = int(len(data_list_folder) * 4 // 5)
    training_data = data_list_folder[:num_training_images]
    test_data = data_list_folder[num_training_images:]

    # generate dataset for the training set
    content = []
    sorted(training_data, key=lambda x:x['img'])
    print('Generating training set ...')
    for data in training_data:
        print(data['img'])
        print(data['mask'])
        print(data['csv'])
        basename = os.path.basename(data['csv'])[:-4]
        content.append([basename, data['img'], data['csv'],data['mask']])
    csv_file_path = os.path.join(output_folder, 'train.csv')
    columns = ['image_name', 'image_path', 'landmark_file_path', 'landmark_mask_path']
    df = pd.DataFrame(data=content, columns=columns)
    df.to_csv(csv_file_path, index=False)

   # generate dataset for the test set
    content = []
    sorted(test_data, key=lambda x:x['img'])
    print('Generating test set ...')
    for data in test_data:
        print(data['img'])
        print(data['mask'])
        print(data['csv'])
        basename = os.path.basename(data['csv'])[:-4]
        content.append([basename, data['img'], data['csv'],data['mask']])

    csv_file_path = os.path.join(output_folder, 'test.csv')
    columns = ['image_name', 'image_path', 'landmark_file_path', 'landmark_mask_path']
    df = pd.DataFrame(data=content, columns=columns)
    df.to_csv(csv_file_path, index=False)
        


def get_image_list(image_folder):
    """
    Get image list from the image folder
    """
    image_list = []

    images = os.listdir(image_folder)
    for image in images:
        if image.startswith('case'):
            image_list.append(image)

    return image_list

def get_data_list(image_foler,mask_folder):
    images = sorted(glob(os.path.join(image_foler, "case*.nii.gz")))
    landmarks = sorted(glob(os.path.join(image_foler, "case*.csv")))
    masks = sorted(glob(os.path.join(mask_folder, "case*.nii.gz")))

    #print(images)
    print(f"image size:{len(images)}")
    #print(segs)
    print(f"mask size:{len(masks)}")
    data_list = [{"img": img, "mask": mask,"csv":csv} for img, mask, csv in zip(images, masks,landmarks)]
    print(data_list[0]['img'])
    print(data_list[0]['mask'])
    print(data_list[0]['csv'])
    return data_list



if __name__ == '__main__':

    #image_list = get_image_list('/mnt/projects/CT_Dental/data_v2')
    # split_dataset(image_list,
    #               '/shenlab/lab_stor6/projects/CT_Dental/data_v2',
    #               '/shenlab/lab_stor6/projects/CT_Dental/landmark_v2',
    #               '/shenlab/lab_stor6/projects/CT_Dental/landmark_mask_v2',
    #               '/mnt/projects/CT_Dental/dataset/landmark_detection/face')

    # image_list = get_image_list('C:/project/Model-Zoo/Dental/detection/landmark/test_data-2-data/data_v2')
    # split_dataset(image_list,
    #               'C:/project/Model-Zoo/Dental/detection/landmark/test_data-2-data/data_v2',
    #               'C:/project/Model-Zoo/Dental/detection/landmark/test_data-2-data/landmark_v2',
    #               'C:/project/Model-Zoo/Dental/detection/landmark/test_data-2-data/landmark_mask_v2',
    #               'C:/project/Model-Zoo/Dental/detection/landmark/test_data-2-data/dataset')

    # image_list = get_image_list('C:/project/Model-Zoo/Dental/detection/landmark/pelvicBone/CT_data')
    # split_dataset(image_list,
    #               'C:/project/Model-Zoo/Dental/detection/landmark/pelvicBone/CT_data',
    #               'C:/project/Model-Zoo/Dental/detection/landmark/pelvicBone/landmark_csv',
    #               'C:/project/Model-Zoo/Dental/detection/landmark/pelvicBone/landmark_mask',
    #               'C:/project/Model-Zoo/Dental/detection/landmark/pelvicBone/dataset')

    # image_list = get_image_list('C:/project/Model-Zoo/Dental/detection/landmark/spine_data/CT_data')
    # split_dataset(image_list,
    #               'C:/project/Model-Zoo/Dental/detection/landmark/spine_data/CT_data',
    #               'C:/project/Model-Zoo/Dental/detection/landmark/spine_data/landmark_csv',
    #               'C:/project/Model-Zoo/Dental/detection/landmark/spine_data/landmark_mask',
    #               'C:/project/Model-Zoo/Dental/detection/landmark/spine_data/dataset')
    data_list = get_data_list("C:\project\Medical-Detection3d-Toolkit\data\spine",
    "C:\project\Medical-Detection3d-Toolkit\data\landmark_mask")
    split_dataset(data_list,'C:\project\Medical-Detection3d-Toolkit\data\dataset')


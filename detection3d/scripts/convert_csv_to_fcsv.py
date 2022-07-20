import sys
import csv
import os
import os.path



def write_lands_map_to_fcsv(lands,dst_fcsv_path,lps_to_ras=False):
    with open(dst_fcsv_path, 'w') as f:
        f.write('# Markups fiducial file version = 4.11\n')
        f.write('# CoordinateSystem = LPS\n')
        f.write('# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID\n')

        i = 1
        for (land_name, land_pt) in lands.items():
            x = land_pt[0]
            y = land_pt[1]
            z = land_pt[2]

            if lps_to_ras:
                x *= -1
                y *= -1

            f.write('{},{:.8f},{:.8f},{:.8f},0,0,0,1,1,1,0,{},,vtkMRMLScalarVolumeNode1\n'.format(i,x,y,z,land_name))
            i = i + 1

        f.flush()

def extract_lands_map_for_csv(src_csv_path):
    kLAND_NAMES = [ 'LLentry',   'LLtarget',
                    'LRentry',  'LRtarget']

    lands_map = { }

    with open(src_csv_path) as f:
        csv_reader = csv.DictReader(f)
        
        for csv_row in csv_reader:
            print(csv_row['name'])
            print(csv_row['x'])
            print(csv_row['y'])
            print(csv_row['z'])
            x = float(csv_row['x'])
            y = float(csv_row['y'])
            z = float(csv_row['z'])
            # if (int(csv_row['pat']) == pat_idx) and (int(csv_row['proj']) == proj_idx):
            #     r = int(csv_row['row'])
            #     c = int(csv_row['col'])

            lands_map[csv_row['name']] = (x,y,z)

    return lands_map


def csv_fscv_batch(csv_dir):
    filenames = os.listdir(csv_dir)
    for f in filenames:
        if f.endswith(".csv"):
            csv_file = os.path.join(csv_dir,f)
            fcsv_file = csv_file.replace(".csv",".fcsv")
            lands = extract_lands_map_for_csv(csv_file)
            write_lands_map_to_fcsv(lands,fcsv_file)




if __name__ == '__main__':
    #csv_fscv_batch('C:/Users/Bxd/Desktop/testData/badData/landmark/1/')
    #csv_fscv_batch("C:/Users/Bxd/Documents/VisualSpine/SpineLandmark/output/")
    #csv_fscv_batch("C:\project\Medical-Detection3d-Toolkit\data\pelvic")
    csv_fscv_batch("C:\\project\\Medical-Detection3d-Toolkit\\data\PelvicBone\\17-1882")
    # filename = 'C:/project/Medical-Detection3d-Toolkit/data/spine/case_0001_patient.csv'
    # target_name = 'C:/project/Medical-Detection3d-Toolkit/data/spine/case_0001_patient.fcsv'
    # lands = extract_lands_map_for_csv(filename)
    # write_lands_map_to_fcsv(lands,target_name)

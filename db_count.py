import pymysql
import sys
import os
import platform

#crossplatform - add for Windows
conn = pymysql.connect(host='mysql-new.home.jungo.com', port=3306, user='videouser', passwd='videouser', db='videodb')
cur = conn.cursor()

def select(query, ):
    cur = conn.cursor()
    cur.execute(query)
    myresult = cur.fetchall()

    for x in myresult:
        # x = x[:-1]  # delete last ','
        print(x)

def synthetic():
    cur = conn.cursor()
    cur.execute("select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID")

#rewrite!
    synthetic_col_nums = cur.fetchall()
    synthetic_col_nums_edited = str(synthetic_col_nums).replace('(', '').replace(',)', '').replace(')', '')
    print(synthetic_col_nums_edited)
    synthetic_col_nums_edited_again = 'and CollectionID not in (' + synthetic_col_nums_edited + ')'
    print(synthetic_col_nums_edited_again)


if __name__ == '__main__':
    synthetic()

#prints

confidence = ('HIGH', 'MEDIUM', 'INVALID', 'NONE')
object_type = (
'face', 'hand', 'cigarette', 'cup', 'bottle', 'chair', 'book', 'laptop', 'cell phone', 'tie', 'bus', 'car', 'person',
'head top', 'child seat')
landmarks = ('Landmarks', 'Eye landmarks Left', 'Eye landmarks Right', 'Mouth landmarks', 'Synthetic landmarks',
             'Eye landmarks Left Synthetic', 'Eye landmarks Right Synthetic', 'Synthetic Mouth landmarks ')
head_pose = ('Head Pose Yaw', 'Head Pose Pitch', 'Head Pose Roll')
eyes = ('Eyes state', 'Eyes gaze', 'Eyes gaze lid', 'Eyes Iris Marks', 'Eyes wear')

# creating file with results
#match to the file

home_linux = os.getenv('HOME')
home_windows = os.path.expandvars("%userprofile%")
results_file_linux = os.path.join(home_linux, 'Desktop', 'db_count_results.txt')
results_file_windows = os.path.join(home_windows, '', 'Desktop', '', 'db_count_results.txt')

def saving_results():
    saving_results
    current_os = platform.system().lower()

    if current_os.lower() == "windows":
        db_count_reults = open("%s" % results_file_windows, "w")
        sys.stdout = db_count_reults
        db_count_reults.close
        if os.path.exists(results_file_windows):
            print('File already exists and will be overwrite')
        elif os.path.exists(results_file_windows) == False:
           print("File created")
           
    elif current_os.lower() == "linux":
        db_count_reults = open("%s" % results_file_linux, "w")
        sys.stdout = db_count_reults
        db_count_reults.close
        if os.path.exists(results_file_linux):
            print('File already exists and will be overwrite')
        elif os.path.exists(results_file_linux) == False:
           print("File created")

if __name__ == '__main__':
    saving_results()

#sys.stdout = open("/home/katerynad/Desktop/test.txt", "w")  # add by OS


#Eye Alignment (landmarks) – pinpoint interest points on the eyes. Output is provided as a vector of 53 points.  
#SELECT count(*) FROM videodb.objects where EyeLandmarksL is not NULL;


# Face rect HIGH
print('ObjectType:', object_type[0], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'face'")

sys.stdout.close()
cur.close()
conn.close()


#select("select count(*) from videodb.main_view where ObjectRectConfidence=", confidence [0], "and ObjectType =", object_type[0])

'''
# Face rect MEDIUM
print('ObjectType:', object_type[0], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'face'")

# Face rect INVALID
print('ObjectType:', object_type[0], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'face'")

# Face rect NONE
print('ObjectType:', object_type[0], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'face'")

# Face rect synthetic HIGH
print('ObjectTypeSynthetic:', object_type[0], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'face' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Face rect synthetic MEDIUM
print('ObjectTypeSynthetic:', object_type[0], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'face' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Face rect synthetic INVALID
print('ObjectTypeSynthetic:', object_type[0], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'face' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Face rect synthetic NONE
print('ObjectTypeSynthetic:', object_type[0], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'face' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Face landmarks HIGH
print('Face', landmarks[0], 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where LandmarksConfidence = 'HIGH'")

# Face landmarks MEDIUM
print('Face', landmarks[0], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where LandmarksConfidence = 'MEDIUM'")

# Face landmarks INVALID
print('Face', landmarks[0], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where LandmarksConfidence = 'INVALID'")

# Face landmarks NONE
print('Face', landmarks[0], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where LandmarksConfidence = 'NONE'")

# Face landmarks synthetic HIGH
print('Face', landmarks[4], 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where LandmarksConfidence = 'HIGH' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Face landmarks synthetic MEDIUM
print('Face', landmarks[4], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where LandmarksConfidence = 'MEDIUM' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Face landmarks synthetic INVALID
print('Face', landmarks[4], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where LandmarksConfidence = 'INVALID' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Face landmarks synthetic NONE
print('Face', landmarks[4], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where LandmarksConfidence = 'NONE' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Left eye landmark HIGH
print(landmarks[1], 'Confidence', confidence[0])
select("select count(*) from videodb.main_view where EyeLandmarksLConfidence = 'HIGH'")

# Left eye landmark MEDIUM
print(landmarks[1], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where EyeLandmarksLConfidence = 'MEDIUM'")

# Left eye landmark INVALID
print(landmarks[1], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where EyeLandmarksLConfidence = 'INVALID'")

# Left eye landmark NONE
print(landmarks[1], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where EyeLandmarksLConfidence = 'NONE'")

# Left eye landmark synthetic HIGH
print(landmarks[5], 'Confidence', confidence[0])
select("select count(*) from videodb.main_view where EyeLandmarksLConfidence = 'HIGH' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Left eye landmark synthetic MEDIUM
print(landmarks[5], 'Confidence', confidence[1])
select(
    "select count(*) from videodb.main_view where EyeLandmarksLConfidence = 'MEDIUM' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Left eye landmark synthetic INVALID
print(landmarks[5], 'Confidence', confidence[2])
select("select count(*) from videodb.main_view where EyeLandmarksLConfidence = 'INVALID' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Left eye landmark synthetic NONE
print(landmarks[5], 'Confidence', confidence[3])
select("select count(*) from videodb.main_view where EyeLandmarksLConfidence = 'NONE' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Right eye landmark HIGH
print(landmarks[2], 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where EyeLandmarksRConfidence = 'HIGH'")

# Right eye landmark MEDIUM
print(landmarks[2], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where EyeLandmarksRConfidence = 'MEDIUM'")

# Right eye landmark INVALID
print(landmarks[2], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where EyeLandmarksRConfidence = 'INVALID'")

# Right eye landmark NONE
print(landmarks[2], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where EyeLandmarksRConfidence = 'NONE'")

# Right eye landmark synthetic HIGH
print(landmarks[6], 'Confidence:', confidence[0])
select(
    "select count(*) from videodb.main_view where EyeLandmarksRConfidence = 'HIGH' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Right eye landmark synthetic MEDIUM
print(landmarks[6], 'Confidence:', confidence[1])
select(
    "select count(*) from videodb.main_view where EyeLandmarksRConfidence = 'MEDIUM' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Right eye landmark synthetic INVALID
print(landmarks[6], 'Confidence:', confidence[2])
select(
    "select count(*) from videodb.main_view where EyeLandmarksRConfidence = 'INVALID' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Right eye landmark synthetic NONE
print(landmarks[6], 'Confidence:', confidence[3])
select(
    "select count(*) from videodb.main_view where EyeLandmarksRConfidence = 'NONE' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Mouth landmarks HIGH
print(landmarks[3], 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where MouthLandmarksConfidence = 'HIGH'")

# Mouth landmarks MEDIUM
print(landmarks[3], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where MouthLandmarksConfidence = 'MEDIUM'")

# Mouth landmarks INVALID
print(landmarks[3], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where MouthLandmarksConfidence = 'INVALID'")

# Mouth landmarks NONE
print(landmarks[3], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where MouthLandmarksConfidence = 'NONE'")

# Mouth landmarks synthetic HIGH
print(landmarks[7], 'Confidence:', confidence[0])
select(
    "select count(*) from videodb.main_view where MouthLandmarksConfidence = 'HIGH' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Mouth landmarks synthetic MEDIUM
print(landmarks[7], 'Confidence:', confidence[1])
select(
    "select count(*) from videodb.main_view where MouthLandmarksConfidence = 'MEDIUM' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Mouth landmarks synthetic INVALID
print(landmarks[7], 'Confidence:', confidence[2])
select(
    "select count(*) from videodb.main_view where MouthLandmarksConfidence = 'INVALID' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Mouth landmarks synthetic NONE
print(landmarks[7], 'Confidence:', confidence[3])
select(
    "select count(*) from videodb.main_view where MouthLandmarksConfidence = 'NONE' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Head Pose Yaw HIGH
print(head_pose[0], 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where HeadPoseYawConfidence = 'HIGH'")

# Head Pose Yaw MEDIUM
print(head_pose[0], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where HeadPoseYawConfidence = 'MEDIUM'")

# Head Pose Yaw INVALID
print(head_pose[0], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where HeadPoseYawConfidence = 'INVALID'")

# Head Pose Yaw NONE
print(head_pose[0], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where HeadPoseYawConfidence = 'NONE'")

# Head Pose Yaw HIGH synthetic
print('Synthetic ', head_pose[0], 'Confidence:', confidence[0])
cur.execute(
    "SELECT count(*) from videodb.main_view where HeadPoseYawConfidence = 'HIGH' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")
head_pose_synt = cur.fetchall()
print(head_pose_synt)

# Head Pose Yaw MEDIUM synthetic
print('Synthetic ', head_pose[0], 'Confidence:', confidence[1])
cur.execute(
    "SELECT count(*) from videodb.main_view where HeadPoseYawConfidence = 'MEDIUM' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")
head_pose_synt = cur.fetchall()
print(head_pose_synt)

# Head Pose Yaw INVALID synthetic
print('Synthetic ', head_pose[0], 'Confidence:', confidence[2])
cur.execute(
    "SELECT count(*) from videodb.main_view where HeadPoseYawConfidence = 'INVALID' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")
head_pose_synt = cur.fetchall()
print(head_pose_synt)

# Head Pose Yaw NONE synthetic
print('Synthetic ', head_pose[0], 'Confidence:', confidence[3])
cur.execute(
    "SELECT count(*) from videodb.main_view where HeadPoseYawConfidence = 'NONE' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")
head_pose_synt = cur.fetchall()
print(head_pose_synt)

# Head Pose Pitch HIGH
print(head_pose[1], 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where HeadPosePitchConfidence = 'HIGH'")

# Head Pose Pitch MEDIUM
print(head_pose[1], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where HeadPosePitchConfidence = 'MEDIUM'")

# Head Pose Pitch INVALID
print(head_pose[1], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where HeadPosePitchConfidence = 'INVALID'")

# Head Pose Pitch NONE
print(head_pose[1], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where HeadPosePitchConfidence = 'NONE'")

# Head Pose Pitch HIGH synthetic
print('Synthetic ', head_pose[1], 'Confidence:', confidence[0])
cur.execute(
    "SELECT count(*) from videodb.main_view where HeadPosePitchConfidence = 'HIGH' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")
head_pose_synt = cur.fetchall()
print(head_pose_synt)

# Head Pose Pitch MEDIUM synthetic
print('Synthetic ', head_pose[1], 'Confidence:', confidence[1])
cur.execute(
    "SELECT count(*) from videodb.main_view where HeadPosePitchConfidence = 'MEDIUM' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")
head_pose_synt = cur.fetchall()
print(head_pose_synt)

# Head Pose Pitch INVALID synthetic
print('Synthetic ', head_pose[1], 'Confidence:', confidence[2])
cur.execute(
    "SELECT count(*) from videodb.main_view where HeadPosePitchConfidence = 'INVALID' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")
head_pose_synt = cur.fetchall()
print(head_pose_synt)

# Head Pose Pitch NONE synthetic
print('Synthetic ', head_pose[1], 'Confidence:', confidence[3])
cur.execute(
    "SELECT count(*) from videodb.main_view where HeadPosePitchConfidence = 'NONE' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")
head_pose_synt = cur.fetchall()
print(head_pose_synt)

# Head Pose Roll HIGH
print(head_pose[2], 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where HeadPoseRollConfidence = 'HIGH'")

# Head Pose Roll MEDIUM
print(head_pose[2], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where HeadPoseRollConfidence = 'MEDIUM'")

# Head Pose Roll INVALID
print(head_pose[2], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where HeadPoseRollConfidence = 'INVALID'")

# Head Pose Roll NONE
print(head_pose[2], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where HeadPoseRollConfidence = 'NONE'")

# Head Pose Roll HIGH synthetic
print('Synthetic ', head_pose[2], 'Confidence:', confidence[0])
cur.execute(
    "SELECT count(*) from videodb.main_view where HeadPosePitchConfidence = 'HIGH' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")
head_pose_synt = cur.fetchall()
print(head_pose_synt)

# Head Pose Roll MEDIUM synthetic
print('Synthetic ', head_pose[2], 'Confidence:', confidence[1])
cur.execute(
    "SELECT count(*) from videodb.main_view where HeadPosePitchConfidence = 'MEDIUM' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")
head_pose_synt = cur.fetchall()
print(head_pose_synt)

# Head Pose Roll INVALID synthetic
print('Synthetic ', head_pose[2], 'Confidence:', confidence[2])
cur.execute(
    "SELECT count(*) from videodb.main_view where HeadPosePitchConfidence = 'INVALID' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")
head_pose_synt = cur.fetchall()
print(head_pose_synt)

# Head Pose Roll NONE synthetic
print('Synthetic ', head_pose[2], 'Confidence:', confidence[3])
cur.execute(
    "SELECT count(*) from videodb.main_view where HeadPosePitchConfidence = 'NONE' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")
head_pose_synt = cur.fetchall()
print(head_pose_synt)

# Eyes state HIGH
print(eyes[0], 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where EyesStateConfidence = 'HIGH'")

# Eyes state MEDIUM
print(eyes[0], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where EyesStateConfidence = 'MEDIUM'")

# Eyes state INVALID
print(eyes[0], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where EyesStateConfidence = 'INVALID'")

# Eyes state NONE
print(eyes[0], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where EyesStateConfidence = 'NONE'")

# Eyes state synthetic HIGH
print('Synthetic ', eyes[0], 'Confidence:', confidence[0])
select(
    "select count(*) from videodb.main_view where EyesStateConfidence = 'HIGH' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes state synthetic MEDIUM
print('Synthetic ', eyes[0], 'Confidence:', confidence[1])
select(
    "select count(*) from videodb.main_view where EyesStateConfidence = 'MEDIUM' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes state synthetic INVALID
print('Synthetic ', eyes[0], 'Confidence:', confidence[2])
select(
    "select count(*) from videodb.main_view where EyesStateConfidence = 'INVALID' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes state synthetic NONE
print('Synthetic ', eyes[0], 'Confidence:', confidence[3])
select(
    "select count(*) from videodb.main_view where EyesStateConfidence = 'NONE' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes gaze HIGH
print(eyes[1], 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where EyeGazeConfidence  = 'HIGH'")

# Eyes gaze MEDIUM
print(eyes[1], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where EyeGazeConfidence = 'MEDIUM'")

# Eyes gaze INVALID
print(eyes[1], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where EyeGazeConfidence = 'INVALID'")

# Eyes gaze NONE
print(eyes[1], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where EyeGazeConfidence = 'NONE'")

# Eyes gaze synthetic HIGH
print('Synthetic ', eyes[1], 'Confidence:', confidence[0])
select(
    "select count(*) from videodb.main_view where EyeGazeConfidence = 'HIGH' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes gaze synthetic MEDIUM
print('Synthetic ', eyes[1], 'Confidence:', confidence[1])
select(
    "select count(*) from videodb.main_view where EyeGazeConfidence  = 'MEDIUM' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes gaze synthetic INVALID
print('Synthetic ', eyes[1], 'Confidence:', confidence[2])
select(
    "select count(*) from videodb.main_view where EyeGazeConfidence  = 'INVALID' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes gaze synthetic NONE
print('Synthetic ', eyes[1], 'Confidence:', confidence[3])
select(
    "select count(*) from videodb.main_view where EyeGazeConfidence = 'NONE' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes gaze lid HIGH
print(eyes[2], 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where EyeGazeLidConfidence = 'HIGH'")

# Eyes gaze lid MEDIUM
print(eyes[2], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where EyeGazeLidConfidence = 'MEDIUM'")

# Eyes gaze lid INVALID
print(eyes[2], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where EyeGazeLidConfidence = 'INVALID'")

# Eyes gaze lid NONE
print(eyes[2], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where EyeGazeLidConfidence = 'NONE'")

# Eyes gaze lid synthetic HIGH
print('Synthetic ', eyes[2], 'Confidence:', confidence[0])
select(
    "select count(*) from videodb.main_view where EyeGazeLidConfidence = 'HIGH' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes gaze lid synthetic MEDIUM
print('Synthetic ', eyes[2], 'Confidence:', confidence[1])
select(
    "select count(*) from videodb.main_view where EyeGazeLidConfidence = 'MEDIUM' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes gaze lid synthetic INVALID
print('Synthetic ', eyes[2], 'Confidence:', confidence[2])
select(
    "select count(*) from videodb.main_view where EyeGazeLidConfidence = 'INVALID' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes gaze lid synthetic NONE
print('Synthetic ', eyes[2], 'Confidence:', confidence[3])
select(
    "select count(*) from videodb.main_view where EyeGazeLidConfidence = 'NONE' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes iris marks HIGH
print(eyes[3], 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where IrisMarksConfidence = 'HIGH'")

# Eyes iris marks MEDIUM
print(eyes[3], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where IrisMarksConfidence = ' MEDIUM'")

# Eyes iris marks INVALID
print(eyes[3], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where IrisMarksConfidence = 'INVALID'")

# Eyes iris marks NONE
print(eyes[3], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where IrisMarksConfidence = 'NONE'")

# Eyes iris marks synthetic HIGH
print('Synthetic ', eyes[3], 'Confidence:', confidence[0])
select(
    "select count(*) from videodb.main_view where IrisMarksConfidence = 'HIGH' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes iris marks synthetic MEDIUM
print('Synthetic ', eyes[3], 'Confidence:', confidence[1])
select(
    "select count(*) from videodb.main_view where IrisMarksConfidence = 'MEDIUM' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes iris marks synthetic INVALID
print('Synthetic ', eyes[3], 'Confidence:', confidence[2])
select(
    "select count(*) from videodb.main_view where IrisMarksConfidence = 'INVALID' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyes iris marks synthetic NONE
print('Synthetic ', eyes[3], 'Confidence:', confidence[3])
select(
    "select count(*) from videodb.main_view where IrisMarksConfidence = 'NONE' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyewear HIGH
print(eyes[4], 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where EyeWearConfidence = 'HIGH'")

# Eyewear MEDIUM
print(eyes[4], 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where EyeWearConfidence = 'MEDIUM'")

# Eyewear INVALID
print(eyes[4], 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where EyeWearConfidence = 'INVALID'")

# Eyewear NONE
print(eyes[4], 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where EyeWearConfidence = 'NONE'")

# Eyewear synthetic HIGH
print('Synthetic ', eyes[4], 'Confidence:', confidence[0])
select(
    "select count(*) from videodb.main_view where EyeWearConfidence = 'HIGH' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyewear synthetic MEDIUM
print('Synthetic ', eyes[4], 'Confidence:', confidence[1])
select(
    "select count(*) from videodb.main_view where EyeWearConfidence = 'MEDIUM' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyewear synthetic INVALID
print('Synthetic ', eyes[4], 'Confidence:', confidence[2])
select(
    "select count(*) from videodb.main_view where EyeWearConfidence = 'INVALID' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Eyewear synthetic NONE
print('Synthetic ', eyes[4], 'Confidence:', confidence[3])
select(
    "select count(*) from videodb.main_view where EyeWearConfidence = 'NONE' and CollectionID in (select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID)")

# Seatbelt HIGH
print('Seatbelt ', 'Confidence:', confidence[0])
select("select count(*) from videodb.main_view where SeatBeltMarksConfidence = 'HIGH'")

# Seatbelt MEDIUM
print('Seatbelt ', 'Confidence:', confidence[1])
select("select count(*) from videodb.main_view where SeatBeltMarksConfidence = 'MEDIUM'")

# Seatbelt INVALID
print('Seatbelt ', 'Confidence:', confidence[2])
select("select count(*) from videodb.main_view where SeatBeltMarksConfidence = 'INVALID'")

# Seatbelt NONE
print('Seatbelt ', 'Confidence:', confidence[3])
select("select count(*) from videodb.main_view where SeatBeltMarksConfidence = 'NONE'")


# Age HIGH
print('Age Confidence:', confidence[0])
select("select count(*) from videodb.main_view where AgeConfidence = 'HIGH'")

# Age MEDIUM
print('Age Confidence:', confidence[1])
select("select count(*) from videodb.main_view where AgeConfidence = 'MEDIUM'")

# Age INVALID
print('Age Confidence:', confidence[2])
select("select count(*) from videodb.main_view where AgeConfidence = 'INVALID'")

# Age NONE
print('Age Confidence:', confidence[3])
select("select count(*) from videodb.main_view where AgeConfidence = 'NONE'")

# Gender HIGH
print('Gender Confidence:', confidence[0])
select("select count(*) from videodb.main_view where GenderConfidence = 'HIGH'")

# Gender MEDIUM
print('Gender Confidence:', confidence[1])
select("select count(*) from videodb.main_view where GenderConfidence = 'MEDIUM'")

# Age INVALID
print('Gender Confidence:', confidence[2])
select("select count(*) from videodb.main_view where GenderConfidence = 'INVALID'")

# Age NONE
print('Gender Confidence:', confidence[3])
select("select count(*) from videodb.main_view where GenderConfidence = 'NONE'")

# Hand HIGH
print('ObjectType:', object_type[1], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'hand'")

# Hand MEDIUM
print('ObjectType:', object_type[1], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'hand'")

# Hand INVALID
print('ObjectType:', object_type[1], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'hand'")

# Hand NONE
print('ObjectType:', object_type[1], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'hand'")


# Child seat HIGH
print('ObjectType:', object_type[14], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'child seat'")

# Child seat MEDIUM
print('ObjectType:', object_type[14], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'child seat'")

# Child seat INVALID
print('ObjectType:', object_type[14], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'child seat'")

# Child seat NONE
print('ObjectType:', object_type[14], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'child seat'")

# Cigarette HIGH
print('ObjectType:', object_type[2], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'cigarette'")

# Cigarette MEDIUM
print('ObjectType:', object_type[2], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'cigarette'")

# Cigarette INVALID
print('ObjectType:', object_type[2], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'cigarette'")

# Cigarette NONE
print('ObjectType:', object_type[2], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'cigarette'")

# Cup HIGH
print('ObjectType:', object_type[3], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'cup'")

# Cup MEDIUM
print('ObjectType:', object_type[3], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'cup'")

# Cup INVALID
print('ObjectType:', object_type[3], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'cup'")

# Cup NONE
print('ObjectType:', object_type[3], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'cup'")

# Bottle HIGH
print('ObjectType:', object_type[4], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'bottle'")

# Bottle MEDIUM
print('ObjectType:', object_type[4], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'bottle'")

# Bottle INVALID
print('ObjectType:', object_type[4], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'bottle'")

# Bottle NONE
print('ObjectType:', object_type[4], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'bottle'")

# Chair HIGH
print('ObjectType:', object_type[5], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'chair'")

# Chair MEDIUM
print('ObjectType:', object_type[5], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'chair'")

# Chair INVALID
print('ObjectType:', object_type[5], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'chair'")

# Chair NONE
print('ObjectType:', object_type[5], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'chair'")

# Book HIGH
print('ObjectType:', object_type[6], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'book'")

# Book MEDIUM
print('ObjectType:', object_type[6], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'book'")

# Book INVALID
print('ObjectType:', object_type[6], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'book'")

# Book NONE
print('ObjectType:', object_type[6], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'book'")

# Laptop HIGH
print('ObjectType:', object_type[7], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'laptop'")

# Laptop MEDIUM
print('ObjectType:', object_type[7], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'laptop'")

# Laptop INVALID
print('ObjectType:', object_type[7], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'laptop'")

# Laptop NONE
print('ObjectType:', object_type[7], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'laptop'")

# Cell phone HIGH
print('ObjectType:', object_type[8], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'cell phone'")

# Cell phone MEDIUM
print('ObjectType:', object_type[8], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'cell phone'")

# Cell phone INVALID
print('ObjectType:', object_type[8], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'cell phone'")

# Cell phone NONE
print('ObjectType:', object_type[8], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'cell phone'")

# Tie HIGH
print('ObjectType:', object_type[9], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'tie'")

# Tie MEDIUM
print('ObjectType:', object_type[9], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'tie'")

# Tie INVALID
print('ObjectType:', object_type[9], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'tie'")

# Tie NONE
print('ObjectType:', object_type[9], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'tie'")

# Bus HIGH
print('ObjectType:', object_type[10], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'bus'")

# Bus MEDIUM
print('ObjectType:', object_type[10], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'bus'")

# Bus INVALID
print('ObjectType:', object_type[10], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'bus'")

# Bus NONE
print('ObjectType:', object_type[10], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'bus'")

# Car HIGH
print('ObjectType:', object_type[11], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'car'")

# Car MEDIUM
print('ObjectType:', object_type[11], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'car'")

# Car INVALID
print('ObjectType:', object_type[11], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'car'")

# Car NONE
print('ObjectType:', object_type[11], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'car'")

# Person HIGH
print('ObjectType:', object_type[12], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'person'")

# Person MEDIUM
print('ObjectType:', object_type[12], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'person'")

# Person INVALID
print('ObjectType:', object_type[12], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'person'")

# Person NONE
print('ObjectType:', object_type[12], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'person'")

# Head top HIGH
print('ObjectType:', object_type[13], 'ObjectRectConf:', confidence[0])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'HIGH' and ObjectType = 'head top'")

# Head top MEDIUM
print('ObjectType:', object_type[13], 'ObjectRectConf:', confidence[1])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'MEDIUM' and ObjectType = 'head top'")

# Head top INVALID
print('ObjectType:', object_type[13], 'ObjectRectConf:', confidence[2])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'INVALID' and ObjectType = 'head top'")

# Head top NONE
print('ObjectType:', object_type[13], 'ObjectRectConf:', confidence[3])
select("select count(*) from videodb.main_view where ObjectRectConfidence = 'NONE' and ObjectType = 'head top'")

'''



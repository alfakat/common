import pymysql
import sys
import os
import platform

# sql connection
try:
    conn = pymysql.connect(host='mysql-new.home.jungo.com', port=3306, user='videouser', passwd='videouser',
                           db='videodb')
    cur = conn.cursor()
except pymysql.Error as e:
    print("Error reading data ", e)


# creating file with results
def saving_results():
    current_os = platform.system().lower()

    if current_os.lower() == "windows":
        home_windows = os.path.expandvars("%userprofile%")
        results_file_windows = os.path.join(home_windows, '', 'Desktop', '', 'db_count_results.txt')
        db_count_results = open("%s" % results_file_windows, "w")
        sys.stdout = db_count_results
        db_count_results.close

    elif current_os.lower() == "linux":
        home_linux = os.getenv('HOME')
        results_file_linux = os.path.join(home_linux, 'Desktop', "db_count_results.txt")
        db_count_results = open("%s" % results_file_linux, "w")
        sys.stdout = db_count_results
        db_count_results.close


if __name__ == '__main__':
    saving_results()

# queries
select_query = "SELECT count(*) FROM videodb.main_view "
obj_conf = "WHERE ObjectRectConfidence = "
obj_type = " and ObjectType = "
hp_yaw = "WHERE HeadPoseYawConfidence = "
hp_pitch = "WHERE HeadPosePitchConfidence = "
hp_roll = "WHERE HeadPoseRollConfidence = "
landm = "WHERE LandmarksConfidence = "
eyes = "WHERE EyesStateConfidence = "
eyel_landm = "WHERE EyeLandmarksLConfidence = "
eyer_landm = "WHERE EyeLandmarksRConfidence = "
gaze = "WHERE EyeGazeConfidence = "
eye_wear = "WHERE EyeWearConfidence = "
mask_yes = "WHERE Mask = 'YES'"
mask_no = "WHERE Mask = 'NO'"
age = "WHERE AgeConfidence = "
gender = "WHERE GenderConfidence = "
seat_belt = "WHERE SeatBeltMarksConfidence = "
mouth_land = "WHERE MouthLandmarksConfidence = "
gaze_lid = "WHERE EyeGazeLidConfidence = "
iris = "WHERE IrisMarksConfidence = "

# rows
confidence = ["'HIGH'", "'MEDIUM'", "'INVALID'", "'NONE'"]
object_type = ["'face'", "'cigarette'", "'cup'", "'bottle'", "'chair'", "'book'", "'laptop'", "'cell phone'", "'tie'",
               "'bus'", "'car'", "'person'", "'child seat'",
               "'head top'", "'hand'"]

print('===== Total tagged images =====\n')

# Objects counting
for j in confidence:
    for i in object_type:
        cur.execute(select_query + obj_conf + j + obj_type + i)
        print(cur._last_executed)
        print(cur.fetchone())

for j in confidence:
    cur.execute(select_query + hp_yaw + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + hp_pitch + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + hp_roll + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + landm + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + eyes + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + eyel_landm + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + eyer_landm + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + gaze + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + eye_wear + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + mask_yes)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + mask_no)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + age + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + gender + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + seat_belt + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + mouth_land + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + gaze_lid + j)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + iris + j)
    print(cur._last_executed)
    print(cur.fetchone())

print('\n===== Synthetic data =====\n')


def synthetic():
    cur = conn.cursor()
    global synth_query
    cur.execute("select CollectionID from collections where Origin='SYNTHETIC'")

    # rewrite!
    synth = cur.fetchall()
    synth_coll = str(synth).replace('(', '').replace(',)', '').replace(')', '')
    synth_query = ' and CollectionID in (' + synth_coll + ')'


if __name__ == '__main__':
    synthetic()

# Synthetic objects counting
for j in confidence:
    obj_type_face = " and ObjectType = 'face'"
    cur.execute(select_query + obj_conf + j + obj_type_face + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())

for j in confidence:
    cur.execute(select_query + hp_yaw + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + hp_pitch + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + hp_roll + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + landm + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + eyes + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + eyel_landm + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + eyer_landm + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + gaze + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + eye_wear + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + mask_yes + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + mask_no + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + age + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + gender + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + seat_belt + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + mouth_land + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + gaze_lid + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())
    cur.execute(select_query + iris + j + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())

sys.stdout.close()
cur.close()
conn.close()

'''
# to do
# initializing list
test_list = ['Landmarks', 'EyeLandmarksL']

# initializing append_str
pref_str = '"WHERE '
suf_str = 'Confidence = "'

# Append suffix / prefix to strings in list
for sub in test_list:
    result = pref_str + sub + suf_str
    print(result)
'''

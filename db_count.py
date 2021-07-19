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
pref_str = 'WHERE '
suf_str = 'Confidence = '
features = ['HeadPoseYaw', 'HeadPosePitch', 'HeadPoseRoll', 'Landmarks', 'EyesState', 'EyeLandmarksL', 'EyeLandmarksR', 'EyeGaze', 'EyeWear', 'Age', 'Gender',
             'SeatBeltMarks', 'MouthLandmarks', 'EyeGazeLid', 'IrisMarks']
features_synth = ['HeadPoseYaw', 'HeadPosePitch', 'HeadPoseRoll', 'Landmarks', 'EyesState', 'EyeLandmarksL', 'EyeLandmarksR', 'EyeGaze', 'EyeWear',
                  'MouthLandmarks', 'EyeGazeLid', 'IrisMarks']
mask_yes = "WHERE Mask = 'YES'"
mask_no = "WHERE Mask = 'NO'"

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
        cur.execute(select_query + mask_yes)
        print(cur._last_executed)
        print(cur.fetchone())
        cur.execute(select_query + mask_no)
        print(cur._last_executed)
        print(cur.fetchone())

for j in confidence:
    for f in features:
        cur.execute(select_query + pref_str + f + suf_str + j + synth_query)
        print(pref_str + sub + suf_str) #debug
        print(cur._last_executed)
        print(cur.fetchone())

print('\n===== Synthetic data =====\n')

# Synthetic objects counting

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

for j in confidence:
    obj_type_face = " and ObjectType = 'face'"
    cur.execute(select_query + obj_conf + j + obj_type_face + synth_query)
    print(cur._last_executed)
    print(cur.fetchone())

for j in confidence:
    for s in features_synth:
        cur.execute(select_query + pref_str + s + suf_str + j + synth_query)
        print(cur._last_executed)
        print(cur.fetchone())

sys.stdout.close()
cur.close()
conn.close()

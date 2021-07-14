import pymysql
import sys
import os
import platform

#https://cs50.stackexchange.com/questions/27873/final-project-sql-error-execute-takes-2-positional-arguments-but-3-were-given

# crossplatform - add for Windows
conn = pymysql.connect(host='mysql-new.home.jungo.com', port=3306, user='videouser', passwd='videouser', db='videodb')
cur = conn.cursor()


def select(query, confidence, query2, object_type):
    cur = conn.cursor()
    cur.execute(query, confidence, query2, object_type)
    myresult = cur.fetchall()

    for x in myresult:
        # x = x[:-1]  # delete last ','
        print(x)


def synthetic():
    cur = conn.cursor()
    cur.execute("select CollectionID from collections where Origin='SYNTHETIC' group by CollectionID")

    # rewrite!
    synthetic_col_nums = cur.fetchall()
    synthetic_col_nums_edited = str(synthetic_col_nums).replace('(', '').replace(',)', '').replace(')', '')
    print(synthetic_col_nums_edited)
    synthetic_col_nums_edited_again = 'and CollectionID not in (' + synthetic_col_nums_edited + ')'
    print(synthetic_col_nums_edited_again)


if __name__ == '__main__':
    synthetic()

# prints

confidence = ('HIGH', 'MEDIUM', 'INVALID', 'NONE')
object_type = (
    'face', 'hand', 'cigarette', 'cup', 'bottle', 'chair', 'book', 'laptop', 'cell phone', 'tie', 'bus', 'car',
    'person',
    'head top', 'child seat')
landmarks = ('Landmarks', 'Eye landmarks Left', 'Eye landmarks Right', 'Mouth landmarks', 'Synthetic landmarks',
             'Eye landmarks Left Synthetic', 'Eye landmarks Right Synthetic', 'Synthetic Mouth landmarks ')
head_pose = ('Head Pose Yaw', 'Head Pose Pitch', 'Head Pose Roll')
eyes = ('Eyes state', 'Eyes gaze', 'Eyes gaze lid', 'Eyes Iris Marks', 'Eyes wear')

# creating file with results
# match to the file

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

select("select count(*) from videodb.main_view where ObjectRectConfidence=", confidence[0], "and ObjectType =", object_type[0])

sys.stdout.close()
cur.close()
conn.close()


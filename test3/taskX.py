class SimpleBackup:
    def __init__(self) -> None:
        self.backup_dir = os.path.join('lab04_files', 'task_x', 'backups')
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
    
    def create(self,path:str):
        fd = open(path, 'r')
        #HVANI GO
        for line in fd:
            #hvani go 
            new_path = os.path.join(*line.split(' '))
            #tova sa moite repliki
        try:

            timest = time.strftime("%Y%m%d_%H%M%S")
            back_name = f"backup_{timest}"
            backup_path = os.path.join(self.backup_dir,back_name)
            os.makedirs(backup_path)
            backup_path = os.path.join(backup_path,back_name+".txt")
            shutil.copy(new_path,backup_path)
            
            return True
        except FileNotFoundError:
            return False


    # Връщане на сортиран списък с всички копия на данни, които са направени
    def show(self):
         return sorted(os.listdir(self.backup_dir))

    def delete(self, file_name:str):
        backup_path = os.path.join(self.backup_dir, file_name)
        if os.path.exists(backup_path):
            shutil.rmtree(backup_path)
            return True
        else:
            return False
    def restore(self,name,location):
        backup_path = os.path.join(self.backup_dir,name)
        if os.path.exists(backup_path):
            shutil.copy(backup_path, location)
            return True
        else:
            return False


import os
def get_folder_content(backup_dir: str) -> list[str]:
    result = []

    for content in os.listdir(backup_dir):
        with open(os.path.join(backup_dir, content), 'r') as f:
            result.append(f.read().strip())

    return result
import time
import shutil

backups = SimpleBackup()


# # Arrange 
default_listing = backups.show()

# Act 
backup1_result = backups.create(os.path.join('lab04_files', 'task_x', 'backup_1.txt'))
time.sleep(1)  # to ensure that the backups will have a different timestamp
backup2_result = backups.create(os.path.join('lab04_files', 'task_x', 'backup_2.txt'))

listing1_result = backups.show()

backup1_path = listing1_result[-2]
backup2_path = listing1_result[-1]

backup1_content = get_folder_content(os.path.join('lab04_files', 'task_x', 'backups', backup1_path))
backup2_content = get_folder_content(os.path.join('lab04_files', 'task_x', 'backups', backup2_path))

time.sleep(1)  # to ensure that the backups will have a different timestamp

backup3_result = backups.create(os.path.join('lab04_files', 'task_x', 'backup_3.txt'))
time.sleep(1)  # to ensure that the backups will have a different timestamp

backup4_result = backups.create(os.path.join('lab04_files', 'task_x', 'backup_4.txt'))
time.sleep(1)  # to ensure that the backups will have a different timestamp

backup5_result = backups.create(os.path.join('lab04_files', 'task_x', 'backup_5.txt'))
time.sleep(1)  # to ensure that the backups will have a different timestamp

listing2_result = backups.show()

backup3_path = listing2_result[-2]
backup4_path = listing2_result[-1]

backup3_content = get_folder_content(os.path.join('lab04_files', 'task_x', 'backups', backup3_path))
backup4_content = get_folder_content(os.path.join('lab04_files', 'task_x', 'backups', backup4_path))

# backup6_result = backups.create(os.path.join('lab04_files', 'task_x', 'backup_4.txt'))
# listing3_result = sorted(backups.show())
# time.sleep(1)  # to ensure that the backups will have a different timestamp

# removal1_result = backups.delete(listing3_result[-1])
# listing4_result = backups.show()

# restore_results = []
# restore_paths = [os.path.join('lab04_files', 'task_x', f'restored_{i}') for i in range(1, 5)]
# backups_to_restore = listing4_result[-4:]
# restore_contents = []

# for backup_to_restore, restore_path in zip(backups_to_restore, restore_paths):
#     os.makedirs(restore_path)
#     restore_results.append(backups.restore(backup_to_restore, restore_path))
#     restore_contents.append(get_folder_content(restore_path))
#     shutil.rmtree(restore_path)

# restore5_result = backups.restore('backup_20231225_144719', restore_paths[0])
# restore6_result = backups.restore('asd', restore_paths[0])

# for backup in backups.show():
#     backups.delete(backup)

# listing5_result = backups.show()

# Tests

# Create
assert backup1_result == True
assert backup2_result == True
assert backup3_result == True
assert backup4_result == True
assert backup5_result == False, 'Config file for backup_5 does not exist'

assert set(backup1_content) == set(['123'])
assert set(backup2_content) == set(['456'])
assert set(backup3_content) == set(['456', '4567'])
assert set(backup4_content) == set(['123', '456', 'Атака, чичо !', '4567'])

# # Show
# assert len(listing1_result) == len(default_listing) + 2
# assert len(listing2_result) == len(default_listing) + 4
# assert len(listing3_result) == len(default_listing) + 5
# assert len(listing4_result) == len(default_listing) + 4
# assert len(listing5_result) == len(default_listing)
# assert listing5_result == default_listing

# # Restore
# assert restore_results[0] == True
# assert restore_results[1] == True
# assert restore_results[2] == True
# assert restore_results[3] == True
# assert restore5_result == False, 'Restore of non-existing backup should fail'
# assert restore6_result == False, 'Restore of backup with invalid name should fail'


# assert set(restore_contents[0]) == set(['123'])
# assert set(restore_contents[1]) == set(['456'])
# assert set(restore_contents[2]) == set(['456', '4567'])
# assert set(restore_contents[3]) == set(['123', '456', 'Атака, чичо !', '4567'])

# # Delete
# for backup in listing3_result:
#     assert os.path.exists(os.path.join('lab04_files', 'task_x', 'backups', backup)) == False


# "✅ All OK! +Y points"
import os


def remove_right(s):
    parts = s.split('_', 1)
    return parts[0] if len(parts) > 1 else s

all = os.listdir()
for i in range(len(all)):
    is_mp4 = False
    if '.mp4' in all[i]:
        is_mp4 = True

    new_name = remove_right(all[i])
    if (new_name.find(".mp4") == -1) and (is_mp4 is True):
        new_name += ".mp4"
        os.rename(all[i], new_name)
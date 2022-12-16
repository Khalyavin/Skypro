import time


def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""
    start_time = time.time()
    try:
        fp = open(file, mode='rb')
    except:
        print(f'FileNotFoundError: [Errno 2] No such file or directory: "{file}"')
    else:
        fp.close()
    finally:
        print(f'Time required for {file} = {time.time() - start_time}')


video_data = read_file_timed('Lesson_35_1.py')
video_data_1 = read_file_timed('video.mp4')
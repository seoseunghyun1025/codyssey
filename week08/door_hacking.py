import zipfile
import time


def unlock_zip():
    zip_filename = 'week08/emergency_storage_key.zip'
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password_length = 6

    start_time = time.time()
    attempt_count = 0
    found_password = None

    def try_password(zip_file, password):
        try:
            file_name = zip_file.namelist()[0]
            with zip_file.open(file_name, pwd=password.encode()) as f:
                f.read(1)
            return True
        except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile):
            return False
        except Exception:
            return False

    def recurse(current):
        nonlocal attempt_count, found_password
        if found_password is not None:
            return
        if len(current) == password_length:
            attempt_count += 1
            if attempt_count % 10000 == 0:
                elapsed = time.time() - start_time
                print(
                    f'Attempts: {attempt_count}, Time elapsed: {elapsed:.2f} seconds'
                )
            if try_password(zf, current):
                found_password = current
                elapsed = time.time() - start_time
                print(f'Password found: {current}')
                print(f'Total attempts: {attempt_count}')
                print(f'Time elapsed: {elapsed:.2f} seconds')

                # 암호 찾았을 때 파일로 저장
                with open('password.txt', 'w') as f:
                    f.write(current)

            return

        for c in chars:
            if found_password is None:
                recurse(current + c)

    try:
        with zipfile.ZipFile(zip_filename) as zf:
            recurse('')
            if found_password is None:
                print('Password not found.')
                elapsed = time.time() - start_time
                print(f'Total attempts: {attempt_count}')
                print(f'Time elapsed: {elapsed:.2f} seconds')
            return found_password
    except FileNotFoundError:
        print('Error: File not found.')
    except zipfile.BadZipFile:
        print('Error: Bad zip file.')
    except Exception as e:
        print('Unexpected error:', e)


if __name__ == '__main__':
    unlock_zip()

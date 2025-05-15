import zipfile
import time
from itertools import product


def unlock_zip():
    zip_filename = 'week08/emergency_storage_key.zip'
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password_length = 6

    start_time = time.time()
    attempt_count = 0

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

    try:
        with zipfile.ZipFile(zip_filename) as zf:
            for pwd_tuple in product(chars, repeat=password_length):
                pwd = ''.join(pwd_tuple)
                attempt_count += 1
                if try_password(zf, pwd):
                    elapsed = time.time() - start_time
                    print(f'Password found: {pwd}')
                    print(f'Total attempts: {attempt_count}')
                    print(f'Time elapsed: {elapsed:.2f} seconds')
                    return pwd
                if attempt_count % 10000 == 0:
                    elapsed = time.time() - start_time
                    print(
                        f'Attempts: {attempt_count}, Time elapsed: {elapsed:.2f} seconds'
                    )

            print('Password not found.')
            elapsed = time.time() - start_time
            print(f'Total attempts: {attempt_count}')
            print(f'Time elapsed: {elapsed:.2f} seconds')
            return None

    except FileNotFoundError:
        print('Error: File not found.')
    except zipfile.BadZipFile:
        print('Error: Bad zip file.')
    except Exception as e:
        print('Unexpected error:', e)


if __name__ == '__main__':
    unlock_zip()

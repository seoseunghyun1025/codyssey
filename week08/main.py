import zipfile
import time
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
import itertools


def try_password(zip_filename, password):
    try:
        with zipfile.ZipFile(zip_filename) as zf:
            file_name = zf.namelist()[0]
            with zf.open(file_name, pwd=password.encode()) as f:
                f.read(1)
        return True
    except:
        return False


def generate_passwords(chars, length):
    return (''.join(p) for p in itertools.product(chars, repeat=length))


def unlock_zip_parallel(
    zip_filename, chars, password_length, max_workers=4, batch_size=100
):
    start_time = time.time()
    passwords = generate_passwords(chars, password_length)

    attempt_count = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = set()
        pwd_map = dict()

        while True:
            submitted = 0
            try:
                while submitted < batch_size:
                    pwd = next(passwords)
                    future = executor.submit(try_password, zip_filename, pwd)
                    futures.add(future)
                    pwd_map[future] = pwd
                    submitted += 1
                # print(f'Submitted batch of {submitted} tasks')
            except StopIteration:
                print('No more passwords to submit')
                pass

            if not futures:
                break

            done, futures = wait(futures, return_when=FIRST_COMPLETED)

            for future in done:
                attempt_count += 1
                pwd = pwd_map.pop(future)

                if attempt_count % 100 == 0:
                    elapsed = time.time() - start_time
                    print(
                        f'Attempts: {attempt_count}, Time elapsed: {elapsed:.2f}s'
                    )

                if future.result():
                    elapsed = time.time() - start_time
                    print(f'Password found: {pwd}')
                    print(f'Total attempts: {attempt_count}')
                    print(f'Time elapsed: {elapsed:.2f}s')
                    executor.shutdown(wait=False)
                    return pwd

    print('Password not found.')
    elapsed = time.time() - start_time
    print(f'Total attempts: {attempt_count}')
    print(f'Time elapsed: {elapsed:.2f}s')
    return None


if __name__ == '__main__':
    zip_filename = 'week08/emergency_storage_key.zip'
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password_length = 6
    unlock_zip_parallel(zip_filename, chars, password_length)

import zipfile


def unlock_zip():
    zip_filename = 'week08/emergency_storage_key.zip'
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password_length = 6

    def try_password(zip_file, password):
        try:
            file_name = zip_file.namelist()[0]
            with zip_file.open(file_name, pwd=password.encode()) as f:
                f.read(1)  # 일부만 읽기 시도
            return True
        except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile):
            return False
        except Exception:
            return False

    try:
        with zipfile.ZipFile(zip_filename) as zf:

            def recurse(current):
                if len(current) == password_length:
                    pwd = ''.join(current)
                    if try_password(zf, pwd):
                        print('Password found:', pwd)
                        return pwd
                    return None
                else:
                    for c in chars:
                        result = recurse(current + [c])
                        if result is not None:
                            return result
                    return None

            password = recurse([])
            if password is None:
                print('Password not found.')
            return password

    except FileNotFoundError:
        print('Error: File not found.')
    except zipfile.BadZipFile:
        print('Error: Bad zip file.')
    except Exception as e:
        print('Unexpected error:', e)

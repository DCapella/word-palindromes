def file_list(file):
    try:
        with open(file) as f:
            data = f.read().strip().split('\n')
            return data
    except Exception as e:
        raise

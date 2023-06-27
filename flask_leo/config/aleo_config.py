
is_debug = 0

def get_leo_bin():
    if is_debug:
        return "/Users/niefeian/.cargo/bin/leo"
    else:
        return "/root/.cargo/bin/leo"

def get_snarkos_bin():
    if is_debug:
        return "/Users/niefeian/.cargo/bin/snarkos"
    else:
        return "/root/.cargo/bin/snarkos"

def get_aleo_bin():
    if is_debug:
        return "/Users/niefeian/.cargo/bin/aleo"
    else:
        return "/root/.cargo/bin/aleo"

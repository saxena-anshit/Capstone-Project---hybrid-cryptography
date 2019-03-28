from Crypto.Util import number


def one_time_pad_password():
    return bin(number.getPrime(16))[2:]

if __name__ == '__main__':
    password = one_time_pad_password()
    print(password)

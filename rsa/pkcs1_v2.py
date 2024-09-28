"""Functions for PKCS#1 version 2 encryption and signing

This module implements certain functionality from PKCS#1 version 2. Main
documentation is RFC 2437: https://tools.ietf.org/html/rfc2437
"""
from rsa import common, pkcs1, transform

def mgf1(seed: bytes, length: int, hasher: str='SHA-1') -> bytes:
    """
    MGF1 is a Mask Generation Function based on a hash function.

    A mask generation function takes an octet string of variable length and a
    desired output length as input, and outputs an octet string of the desired
    length. The plaintext-awareness of RSAES-OAEP relies on the random nature of
    the output of the mask generation function, which in turn relies on the
    random nature of the underlying hash.

    :param bytes seed: seed from which mask is generated, an octet string
    :param int length: intended length in octets of the mask, at most 2^32(hLen)
    :param str hasher: hash function (hLen denotes the length in octets of the hash
        function output)

    :return: mask, an octet string of length `length`
    :rtype: bytes

    :raise OverflowError: when `length` is too large for the specified `hasher`
    :raise ValueError: when specified `hasher` is invalid
    """
    pass
__all__ = ['mgf1']
if __name__ == '__main__':
    print('Running doctests 1000x or until failure')
    import doctest
    for count in range(1000):
        failures, tests = doctest.testmod()
        if failures:
            break
        if count % 100 == 0 and count:
            print('%i times' % count)
    print('Doctests done')
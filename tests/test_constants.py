import hashlib

import cachedir_tag

def test_tag_signature():
    expected = 'Signature: %s' % hashlib.md5(b'.IsCacheDirectory').hexdigest()
    assert expected == cachedir_tag.CACHEDIR_TAG_SIGNATURE

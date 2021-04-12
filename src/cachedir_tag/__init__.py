import errno
import pathlib


__all__ = [
    'CACHEDIR_TAG_FILENAME',
    'CACHEDIR_TAG_SIGNATURE',
    'contains_tag'
    'is_tagged',
    'tag',
]

CACHEDIR_TAG_FILENAME = 'CACHEDIR.TAG'
CACHEDIR_TAG_SIGNATURE = 'Signature: 8a477f597d28d172789f06886806bc55'
CACHEDIR_TAG_TEMPLATE = '''
# This file is a cache directory tag created by ({application}).
# For information about cache directory tags, see:
#	http://www.brynosaurus.com/cachedir/
'''


def tag(directory, application=None, template=CACHEDIR_TAG_TEMPLATE):
    '''Indicate that `directory` contains cache data, by creating a
    CACHEDIR.TAG file.
    '''
    suffix = template.format(application=application) if application else '\n'
    path = pathlib.Path(directory) / CACHEDIR_TAG_FILENAME
    with path.open('w', encoding='ascii') as f:
        f.write(CACHEDIR_TAG_SIGNATURE)
        f.write(suffix)


def is_tagged(directory):
    '''Return True if `directory` is tagged as a cache directory, or False
    otherwise.
    '''
    if contains_tag(directory):
        return True
    path = pathlib.Path(directory)
    return any(contains_tag(directory) for directory in path.parents)


def contains_tag(directory):
    '''Return True if `directory` contains a valid CACHEDIR.TAG file,
    or False otherwise.
    '''
    path = pathlib.Path(directory) / CACHEDIR_TAG_FILENAME
    if path.is_symlink():
        return False
    if not path.exists():
        return False
    if not path.is_file():
        return False

    try:
        with path.open('r', encoding='ascii') as f:
            signature = f.read(len(CACHEDIR_TAG_SIGNATURE))
    except IOError as e:
        if e.errno == e.ENOENT:
            return False
        raise

    return True


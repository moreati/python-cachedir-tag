# CACHEDIR.TAG for Python

This library handles [CACHEDIR.TAG](https://bford.info/cachedir/) files.
Allowing any arbitrary directory to be marked as a cache directory.

A CACHEDIR.TAG file indicates a directory that contain cached data, e.g.

- downloads
- previews, and thumbnails
- build artefacts, and other intermediate results

Cached data is useful, but not essential - if necessary it can be regenerated,
or downloaded again. However backup programs, disk cleanup utilities, & other
software can't know if an arbitrary path is cached data, unless it is marked.

A directory (and all directories within it) can be marked as a cache by
writing a regular file named CACHEDIR.TAG, with the first 43 bytes being

```
Signature: 8a477f597d28d172789f06886806bc55
```

After this signature any other text can be included. The specification
suggests lines of text beginning with `#`, encoded as UTF-8. E.g.

```
# This file is a cache directory tag created by (application name).
# For information about cache directory tags, see:
#	http://www.brynosaurus.com/cachedir/
```

This library follows that suggestion.

## Installation

```
$ python -m pip install cachedir-tag
```

## Usage

Create your cache directory, if necessary

```python
>>> import os, cachedir_tag
>>> os.mkdir('/var/cache/yourapp')
```

Tag it, this creates a new CACHEDIR.TAG file

```python
>>> cachedir_tag.tag('/var/cache/yourapp')
```

Check whether the directory is tagged

```python
>>> cachedir_tag.is_tagged('/var/cache/yourapp')
True
```

Check whether a sub-directory (which may not exist yet) is tagged

```python
>>> cachedir_tag.is_tagged('/var/cache/yourapp/somedir')
True
```

## Alternatives

Operating systems and similar platforms usually have conventions about where
to place cached data. A CACHEDIR.TAG file isn't needed if you follow these
conventions, but it doesn't hurt either.

## More information

- [Cache Directory Tagging Specification](https://bford.info/cachedir/)
  by [Bryan Ford](https://bford.info/)

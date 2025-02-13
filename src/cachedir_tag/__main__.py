'''
Check or mark whether a path contains a cache, indicated by a CACHEDIR.TAG file
'''

import argparse
import pathlib
import sys

import cachedir_tag


def check(args):
    return int(cachedir_tag.is_tagged(args.dir))


def tag(args):
    cachedir_tag.tag(args.dir)
    return 0


parser = argparse.ArgumentParser(description=__doc__)
#parser.add_argument('--verbose', action='store_true')
subparsers = parser.add_subparsers(dest='command')

check_cmd = subparsers.add_parser(
    'check',
    help='Check whether a directory is tagged as a cache',
)
check_cmd.add_argument('dir', type=pathlib.Path, help="Directory to check")
check_cmd.set_defaults(func=check)

tag_cmd = subparsers.add_parser(
    'tag',
    help='Tag a directory as a cache',
)
tag_cmd.add_argument('dir', type=pathlib.Path, help="Directory to tag")
tag_cmd.set_defaults(func=tag)

args = parser.parse_args()
rc = args.func(args)
sys.exit(rc)

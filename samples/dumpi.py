#! /usr/bin/env python
""" Dump all links from all sitemaps found in a given index"""

import sys
sys.path.append('..')

import sitemap

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: dumpi.py index_url_or_path'
        sys.exit(1)

    index = sitemap.SitemapIndex.from_url(sys.argv[1])
    for set in index:
        for url in set:
            print url.loc


#!/usr/bin/env python
# encoding: utf-8

"""
    Copyright 2013 Jérémie BOUTOILLE

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import argparse
import re

HASHES = {"MD5": re.compile(r"^[A-Fa-f0-9]{32}$"),
          "SHA1 hexcoded": re.compile(r"^[A-Fa-f0-9]{40}$"),
          "SHA1 base64coded (LDAP SHA)": re.compile(r"^\{SHA\}[a-zA-Z0-9+/]{27}=$"),
          "SHA1 base64coded + salt (LDAP SSHA)": re.compile(r"^\{SSHA\}[a-zA-Z0-9+/]{28,}[=]{0,3}$"),
          "SHA224": re.compile(r"^[A-Fa-f0-9]{56}$"),
          "SHA256": re.compile(r"^[A-Fa-f0-9]{64}$"),
          "SHA384": re.compile(r"^[A-Fa-f0-9]{96}$"),
          "SHA512": re.compile(r"^[A-Fa-f0-9]{128}$"),
          "MySQL": re.compile(r"^[A-Fa-f0-9]{16}$"),
          "MD5-Crypt": re.compile(r"^\$1\$[a-zA-Z0-9./]{8}\$[a-zA-Z0-9./]{1,}$"),
          "MD5-Crypt Apache (MD5-Crypt with 1000 iterations)": re.compile(r"^\$apr1\$[a-zA-Z0-9./]{8}\$[a-zA-Z0-9./]{1,}$"),
          "Blowfish-Crypt": re.compile(r"^\$2[axy]{0,1}\$[a-zA-Z0-9./]{8}\$[a-zA-Z0-9./]{1,}$"),
          "NT-Crypt": re.compile(r"^\$3\$[a-zA-Z0-9./]{8}\$[a-zA-Z0-9./]{1,}$"),
          "SHA1-Crypt": re.compile(r"^\$4\$[a-zA-Z0-9./]{8}\$[a-zA-Z0-9./]{1,}$"),
          "SHA256-Crypt": re.compile(r"^\$5\$[a-zA-Z0-9./]{8}\$[a-zA-Z0-9./]{1,}$"),
          "SHA512-Crypt": re.compile(r"^\$6\$[a-zA-Z0-9./]{8}\$[a-zA-Z0-9./]{1,}$")}


def main():

    parser = argparse.ArgumentParser(description='Identify a hash')
    parser.add_argument('hash', help='hash to identify')
    args = parser.parse_args()
    hashe = args.hash

    results = []

    for hashName, hashRegexp in HASHES.items():
        if hashRegexp.match(hashe):
            results.append(hashName)

    if len(results) == 0:
        print "[-] Unabble to identify the hash : %s" % hashe
        return

    if len(results) == 1:
        print "[+] Result for '%s' :" % hashe
    else:
        print "[+] '%s' can be :" % hashe

    for result in results:
        print "\t - %s" % result

if __name__ == '__main__':
    main()

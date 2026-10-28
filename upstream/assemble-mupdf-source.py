#!/usr/bin/env python3
"""Reassemble the exact MuPDF source archive from this repository's parts."""
from pathlib import Path
import argparse,hashlib
PARTS = [{'name': 'mupdf-1.28.1-source.tar.gz.part01', 'bytes': 24000000, 'sha256': '767848f0ab74c76a6d1380cf5d35d23db216c8ff6663b527d8ace0a24599ded7'}, {'name': 'mupdf-1.28.1-source.tar.gz.part02', 'bytes': 24000000, 'sha256': '7c948d69e690c8fc0634ee84825a392095cf987a589ea3384a83c46a63c046a4'}, {'name': 'mupdf-1.28.1-source.tar.gz.part03', 'bytes': 20898834, 'sha256': 'b23721bbe739ee67042086292000c80522386740962e60f010a83add60adfeb0'}]
SIZE = 68898834
SHA256 = 'dc94c60b2537e2ac9a2d379dd3801545f84a3a302d15c9da358362a1270707c3'
root=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,default=root/'mupdf-1.28.1-source.tar.gz')
args=parser.parse_args();output=args.output.resolve()
def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for data in iter(lambda:stream.read(1048576),b''):h.update(data)
    return h.hexdigest()
if output.exists():
    if output.stat().st_size==SIZE and digest(output)==SHA256:
        print('Already assembled and verified:',output)
        raise SystemExit(0)
    raise SystemExit('Refusing to overwrite an existing file with different bytes: '+str(output))
output.parent.mkdir(parents=True,exist_ok=True)
temporary=output.with_name(output.name+'.assembling')
whole=hashlib.sha256();written=0;created=False
try:
    with temporary.open('xb') as destination:
        created=True
        for part in PARTS:
            path=root/part['name'];h=hashlib.sha256();size=0
            with path.open('rb') as source:
                for data in iter(lambda:source.read(1048576),b''):
                    h.update(data);whole.update(data);destination.write(data);size+=len(data);written+=len(data)
            if size!=part['bytes'] or h.hexdigest()!=part['sha256']:raise ValueError('Source part failed verification: '+part['name'])
    if written!=SIZE or whole.hexdigest()!=SHA256:raise ValueError('Assembled source archive failed verification')
    if output.exists():raise FileExistsError('Output appeared during assembly; no file was replaced')
    temporary.rename(output);created=False
    print('Assembled and verified:',output)
    print('SHA256:',SHA256)
finally:
    if created:temporary.unlink(missing_ok=True)

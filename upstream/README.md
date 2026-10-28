# MuPDF corresponding source

The complete MuPDF 1.28.1 source archive is stored in three parts to fit the upload transport limit. All bytes are retained.

Run from the repository root:

```sh
python upstream/assemble-mupdf-source.py
```

This creates `upstream/mupdf-1.28.1-source.tar.gz` after checking every part and the final archive. Existing correct output is verified and reused; different existing files are not overwritten.

- Assembled size: 68898834 bytes
- SHA256: `dc94c60b2537e2ac9a2d379dd3801545f84a3a302d15c9da358362a1270707c3`

The assembled archive is byte-for-byte identical to the upstream source included in the local PDFCreator release package. It includes its licences and build instructions. Copy it beside the app source kit's `build.mjs` before rebuilding.

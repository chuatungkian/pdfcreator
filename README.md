# PDFCreator

A single-file offline PDF workspace for editing, organising, annotating, filling forms, OCR, comparison, redaction and signing. `index.html`, `pdfcreator.html` and the legacy `pdfpro.html` contain identical current app bytes.

## Open

Open one of the HTML files in a current desktop browser. PDF tools, English OCR and the **In-browser docx and doc converter** work on this device without an account or network download. The optional Microsoft Word companion uses installed desktop Word on Windows. Built-in conversion substitutes embedded Arimo fonts and can change pagination; review its output.

## Generate forms from XLSX or CSV

1. Open a PDF containing editable form fields and choose **Forms > Generate from XLSX / CSV**. Flat/scanned forms need fields added first.
2. Choose a data file, worksheet and header row. Select formatted text to preserve displayed dates and leading zeroes, or raw values when needed. CSV text is preserved literally.
3. Match PDF fields to columns, retain template values or enter fixed values. Preview records and PDF pages; correct required fields, invalid choices and character limits.
4. Select record ranges and an output filename pattern. For example, `Letter_{B}_{row}` uses column B and the record number. Duplicate filenames receive suffixes.
5. Keep fields editable or flatten them, then generate and download the ZIP. It includes a UTF-8 CSV report with source row numbers and any skipped records.

Formulas use saved workbook results and are never recalculated. Missing cached results and spreadsheet errors block affected mapped fields. Multi-select values use semicolons; checkboxes accept yes/no, true/false or 1/0. Invalid records require correction or explicit skipping. Read-only fields retain their values. Pending redactions and digitally signed templates require resolving first.

Data is read by an embedded, cancellable worker; no upload or external spreadsheet service is used. Source data and mappings are transient. The open template, tabs and undo history are retained. Limits are 20 MB input, 10,000 records, 256 columns, 500,000 workbook cells and 250 MB of generated PDFs.

## Workspace update — 31 October 2026

- A persistent active-tool guide explains the next gesture and provides Done, tool search and a favourite star.
- Pin tools in function search. Favourites appear before recent tools; Home provides shortcuts. Preferences recover with this browser's local session.
- Selecting PDF text offers Copy, Highlight, Underline, Edit paragraph and Add link. The selection must stay on one page. Native PDF edits use existing signature checks, undo and recovery.
- Image properties provide Crop, Adjust, Replace image and Add link. Replacement keeps other occurrences of a shared image intact and is one undo step; its proportions fit inside the selected image's displayed bounds.
- Dialogues have consistent sticky actions, bounded keyboard focus and an inert background. Page-range inputs provide All pages, Current page and a selected-page count. Background blur is removed.
- All HTML copies, embedded app sources, the separate source ZIP, licences and checksums are aligned in this release.

## Existing capabilities

Create blank/ruled/squared PDFs; use reusable templates; open document tabs; edit native text and rich text boxes; edit images and supported objects; organise/merge/split pages; add links and page decorations; annotate and review comments; create/fill/flatten forms; recognise English text; compare documents; compress to a target size; redact/sanitise; encrypt/unlock; apply visual/certificate signatures; export PDFs/images/text/workspaces; batch process; maintain a local library, Bin, backups, history and checkpoints. See [the user guide](README.txt) and [feature audit](FEATURE-AUDIT.txt).

## Source and rebuilding

Extract `pdfcreator-3.0-app-source.zip` and enter `source`. The HTML's `window.PDFCreator.downloadSource()` exports the same paths and bytes. With Node.js and pnpm installed:

```powershell
pnpm install --frozen-lockfile
node build.mjs C:\path\to\release-folder
node workspace-ux-test.mjs
node form-generation-test.mjs
node form-generation-interactions-test.mjs
$env:PDFCREATOR_RELEASE_DIR = 'C:\path\to\release-folder'
node release-alignment-test.mjs
```

The current build recompiles preferred app sources and retains the exact distributed PDF/OCR/Word engine bytes under `vendor/`. Runtime engines, fonts, source notices and English OCR data are local. No conversion runtime is fetched by the built app. `build-full.mjs` retains the earlier complete engine packaging workflow; its prerequisites are documented in that file and README.txt.

`PDFCreator-Ream-Source.zip` retains the Word converter's MIT dependency sources. Extract alongside the main source ZIP when rebuilding that worker. The official MuPDF corresponding source remains under `upstream/`; reconstruct it with `python upstream/assemble-mupdf-source.py`. Preserve these sources and third-party notices when redistributing.

## Verification and boundaries

See `VALIDATION.txt` for this release's completed checks. Controlled-DOM tests exercise real PDF engines with synthetic files and simulated geometry; they do not establish live browser layout, file-origin storage, clipboard or native download/print behaviour.

OCR is English-only. Direct text reflow stays within the selected page. Some PDF fonts, image types and advanced structures are unsupported. Visual signatures are separate from certificate signatures. Signature integrity checks do not establish trusted identity. Cropping/deleting images and workspace visibility controls are not secure redaction. Local recovery retains earlier content; manage stored copies when working with sensitive documents. No PDF/A, PDF/X or PDF/UA certification is claimed.

AGPL-3.0-or-later; component licences are retained in `THIRD-PARTY-NOTICES.txt` and the source kits.

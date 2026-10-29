# PDFCreator

An offline PDF workspace packaged as one HTML file. The current `index.html` is **20.82 MB** and includes its PDF engines, English OCR model, Inter font and downloadable source bundle.

## Use

Download `pdfcreator.html` (or the identical `index.html`) and open it in a current desktop browser. Standalone PDF tools need no installation, account or network connection after download. PDFs are processed on your device. The optional Word import companion requires Windows and installed Microsoft Word desktop.

The workspace includes document tabs, local recovery, continuous page scrolling, annotations and freehand drawing, page organisation, added text/images, forms, OCR, comparison, encryption, redaction, signatures and exports. The page toolbar can float, minimise, or lock across the top or bottom of the working area. The old `pdfpro.html` path is retained as a byte-identical compatibility copy for local bookmarks and storage. New workspaces use `.pdfcreator`; older `.pdfpro` workspaces still import.

**Edit > Direct edit** offers **Paragraph** (default), **Line** and dragged **Text chunk** scopes. Paragraph and chunk edits rewrap at the chosen width, closing gaps inside the selection. Include several paragraphs in one chunk to pull them together. Original native font programmes, colours, opacity and sizes remain, with unchanged inline styles retained and replacement words inheriting source styles. The first baseline stays in place; following lines move as text rewraps. Width and editing scope are remembered, and applied edits recover locally. Reflow stays on one page and avoids unselected text.

Choose the editing scope in tool settings or the on-page editor. **Width (pt)** controls wrapping; Enter adds a hard break and Ctrl+Enter (Cmd+Enter on Mac) applies a paragraph/chunk edit. Compatible embedded fonts load locally for typing previews. New PDFCreator text boxes retain their device-font recipe for editing as a complete box. Missing font characters, overflow and unsupported encodings are refused; scanned, outlined and older image-backed text are excluded. The tool remains selected for repeated edits.

Edits and inserted items retain the current page and both scroll offsets. Visual signatures combine a typed name and drawing, with the name below the drawing. Processing uses a circular outline that traces the circumference for unknown progress and fills as progress is reported.

**Organise > Merge & split** combines current edited PDFs from open tabs, the local library or uploads. Reorder sources, add visual split points or grouped page ranges, preview filenames, download grouped PDFs as a ZIP, or create a merged working tab. Plans recover locally and detect changed or missing sources.

**Edit > Add link** supports websites, email addresses and pages in the same PDF. Click existing text, an image or a shape; draw an area; or place new visible linked text with a chosen font, size and colour. Text and its link form one undo step. Choose Done to follow links. The small arrow edits or removes a link. Native PDF links survive undo/redo, exports and local recovery. OCR phrase search and plain-text line grouping are also checked in this revision.

IndexedDB retains documents and edits when permitted by the browser. Its availability for local files depends on the browser; check the save indicator. Local recovery may include unlocked copies, originals and undo history. Download important work and use Library to remove closed stored copies when needed.

**Home project cards have a dustbin beside Resume.** A warning asks for confirmation before deleting a locally saved project, its original copy, edits and history. Confirming also closes that project if it is open; cancelling keeps it intact. Downloaded files and other projects are retained. Storage deletion completes before an open tab closes, and queued/stale autosaves cannot recreate a deleted project. This revision passes 50 deletion checks covering cancellation, failures, concurrent saves and recovery.

## Create and expanded editing tools

**Create** is the first entry in the left toolbar. It opens the same side tool pane as the other navigation functions, with **New PDF**, **Import from Word** and **Open PDF** actions. Clicking the same navigation group again closes its popup; another group switches the content. New documents support named files, standard/custom page sizes, orientation, margins, multiple pages and blank/ruled/squared paper. Existing PDFs open in separate tabs.

For Word import, download [PDFCreator-Word-Companion.zip](PDFCreator-Word-Companion.zip), extract it and run `start-word-companion.cmd`. Paste its pairing code into **Create > Import from Word**. The companion uses the installed Microsoft Word PDF exporter over an authenticated loopback connection. No cloud conversion service is used. Word renders formatting, pictures, tables, headers, footers and page layout; source fonts and document restrictions can affect fidelity. The same companion ZIP is downloadable from the standalone HTML.

Field popups stay inside the visible PDF page and workspace, move inward near edges and use a scrolling body with separate Close/Apply controls. Bounds update for resized content and narrow views; 32 geometry checks pass.

**Protect & sign > Remove digital signatures** confirms removal before making an unsigned working copy. Signed fields/widgets and their appearances, signing dictionaries, certification/usage-rights signature policies, obsolete validation data and old incremental signature revisions are removed. Ordinary fields, other page content, empty signature fields and separate visual signatures are retained. Undo restores exact signed bytes. This revision passes 25 native/cryptographic checks and 18 interaction checks; original signing tests also pass. Signatures flattened into text/images can be removed with Select objects or Edit images.

**Edit > Edit form fields** (also in Forms) makes standard AcroForm fields directly clickable. Enter multiline paragraphs, retain the original font or choose a standard PDF font, and adjust size, colour and alignment. Choices, checkboxes and radio/list selections stay interactive. Add text, Direct edit and Replace route field clicks to this editor. Shared widgets, canonical values/appearances, lock/max-length rules, undo/redo, page position and local recovery are retained. Bulk Fill form now uses multiline textareas where appropriate. This revision passes 38 synthetic native checks, six local supplied-form checks and 50 interaction checks. No user PDF is packaged or uploaded.

**Edit > Edit images** lets you click existing images directly and crop, move, resize, delete, or adjust opacity, brightness, contrast, saturation, hue and warm/cool tone. Add image opens the same compact inspector after placement. A crop preview and position fields support precise adjustments; undo/redo and local recovery retain them. Shared/nested image instances are isolated. Original pixels are retained for readjustment, so crop/delete are not secure redaction. Inline/stencil images and colour adjustments above 20 million pixels are excluded. Clicking grey space outside the PDF deactivates the selected function; controls remain usable. The image tools pass 40 native checks and 58 interaction checks. A further 10-check large-image regression fixes colour/alpha buffers invalidated by WASM memory growth while decoding transparency masks. For an affected previous edit, Reset appearance and Apply restores the retained source pixels.

**Edit > Select objects** moves, resizes, rotates, duplicates and removes supported text, image/signature, Form and annotation objects, with alignment and snapping. **Annotate > Erase drawing** removes touched ink strokes. Rich text supports mixed fonts, bold/italic, colour, bullets, spacing and live page preview. Text-aware highlight/underline/strikeout follows multiple lines.

**Comments** spans all pages, with editing, replies, resolved status, filters and an exportable printable summary. **Organise > Page organiser** stages visual multi-page rearrangement, rotation, duplication, deletion, insertion and replacement from other tabs/uploads. **Find and replace** offers case/whole-word/page-range controls and a selectable replacement preview for supported native paragraphs and tracked text boxes. New edits use the shared undo and local recovery workflows.

**Edit > Watermark** now centres the visible rotated text on each displayed page, including crop/rotation handling, with size, angle, opacity, font and colour controls. Batch watermarks use the same positioning. **Edit > Edit watermarks** identifies tracked and older PDFCreator layers, tagged imported layers and candidate native text watermarks. Preview/select layers, update their text/appearance, or remove them with undo support. Inferred candidates need review; watermarks baked into page images cannot be separated automatically. The watermark revision passes 115 native geometry/pixel and controlled-interaction checks, including preserving overlapping body text. Rotation accepts -360 to 360 degrees in 0.1 degree steps.

**Headers, footers and page/Bates numbers** support independent left/centre/right alignment. Each has centimetre controls for distance from the top or bottom edge and separate left/right margins. Centre alignment uses the area between those margins; distances follow visible cropped/rotated page edges. Position checks pass 84 native-pixel/UI assertions. Add full-width header/footer rules with adjustable thickness and static date/time stamps. Footer text and page numbers use separate rows and can appear together. Later updates replace the corresponding tracked decoration while retaining the other rows.

The bottom page previews support Ctrl/Cmd-click and Shift-click selection, group dragging, and a right-click menu for rotation, duplication, deletion, extraction, moving, blank insertion and importing/replacing from other PDFs. The full Page organiser also has a document dropdown listing every open tab, defaults to the active PDF and switches it with staged-change protection.

**Save PDF** offers unchanged bytes, lossless cleanup, High/Balanced/Small image compression, or a target maximum in MB/kB. Target mode tries progressively smaller image settings within chosen quality limits and shows actual byte counts and whether the target was reached before download. It retains PDF text, vectors, forms, links and annotations; unsupported/protected images keep their pixels. Target size is best effort, and lower image quality can soften detail. Compressed downloads leave the open PDF at its current quality; the Optimise tool applies compression in one undo step.

The header **magnifying glass** searches all 75 distinct tools and five app actions, including common aliases. Ctrl/Cmd+K opens it, arrow keys navigate, Enter opens a result and Escape closes it. Tools requiring a PDF are disabled on empty Home. The header **question mark** opens About & source, including authorship/contact and source/licence links.

## Documentation and verification

- [User guide and limitations](README.txt)
- [Validation results](VALIDATION.txt): the earlier functional baseline passed 1,270 counted assertions, followed by 576 Direct edit/view-retention checks. Later revisions add 188 paragraph/chunk checks, 30 branding checks, 80 completion-workflow checks and 57 Create checks. Later targeted revisions add 100 page-feature checks, 74 thumbnail-organiser checks, 75 compression checks, 63 navigation-toggle checks and 61 function-search checks. The Word companion passes 22 checks against actual Microsoft Word and loopback HTTP using a synthetic document. Both native Word PDF pages were rendered and visually inspected. Affected regressions, actual-package integrity and source export also pass.
- [Feature audit](FEATURE-AUDIT.txt): all 75 distinct tool actions mapped to regression workflows. Live browser layout, font loading, external navigation, downloads and print-dialogue behaviour remain unverified.
- [Checksums](SHA256SUMS.txt)

PDFCreator is an offline PDF toolkit. It does not claim complete Adobe Acrobat feature parity, PDF/A or PDF/UA certification, or certificate identity/trust validation.

## Development history

Earlier commits remain available in [the original pdfpro repository](https://github.com/chuatungkian/pdfpro). This repository publishes the PDFCreator release under its new name.

## Source and rebuild

The complete application source kit is available in [pdfcreator-3.0-app-source.zip](pdfcreator-3.0-app-source.zip). The same file contents remain embedded and can be exported offline with `window.PDFCreator.downloadSource()`. About links to this repository; the former source/notice download buttons have been removed.

Extract the source kit, enter its `source` folder and install the locked dependencies with `pnpm install --frozen-lockfile`. From the repository root, run `python upstream/assemble-mupdf-source.py` to reconstruct the [complete MuPDF source archive](upstream/README.md) from its three verified parts. Copy the resulting `upstream/mupdf-1.28.1-source.tar.gz` beside `build.mjs`, then run `node build.mjs`. See README.txt for the exact runtime versions, test dependencies and build details. No user PDFs, browser storage, credentials or signing keys are included in this repository.

## Licence

PDFCreator is distributed under [AGPL-3.0-or-later](LICENSE.txt). Components retain their own licences; see [third-party notices](THIRD-PARTY-NOTICES.txt). The full MuPDF corresponding source is retained under `upstream/` in losslessly reassembled parts.

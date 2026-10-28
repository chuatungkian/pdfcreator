PDFCreator 3.0.0 — offline PDF workspace
==================================

OPEN
Open pdfcreator.html (or index.html from the GitHub package) in current desktop
Chrome, Edge, Firefox, or Safari. No installation, accounts, or network access
are needed by the application. Chrome and Edge are the browsers tested here.
The app may take a few seconds to unpack its embedded engines on first launch.
The current link/functionality revision was checked with native PDF processing and a
controlled test DOM; a fresh live-browser layout check was not available.

NAME AND COMPATIBILITY
PDFCreator was previously named pdfpro. The legacy pdfpro.html path is supplied
as an identical compatibility copy, so existing local-file bookmarks and document
storage can continue using that path. New workspaces use .pdfcreator; older
.pdfpro workspaces remain importable. The existing local database is retained.

COMPACT SINGLE-FILE PACKAGE
The build enforces a strict limit of 25,000,000 bytes for the HTML. PDF/OCR
engines, English recognition data, Inter and source files are retained locally.
Identical files share their stored bytes; source copies of runtime assets refer
to the existing embedded assets. No CDN or first-run download is required.
About & source > Download source bundle assembles the complete source ZIP on
demand. Its paths and file contents match the separate app-source ZIP. When
browser compression is unavailable, a valid larger ZIP preserves the same files.
This changes packaging only; PDF operations, OCR and local recovery are retained.

INTERFACE
White, maroon, navy and black palette. Inter4.1 is embedded in the HTML and
licensed under SIL Open Font License1.1. Interface copy uses British English.
The single header keeps Open files and Save PDF close at hand. The three-dot
menu contains New document, Local library and Print document. Page controls
float above a soft navy-tinted canvas. Tool panes use white surfaces and subtle
shadows; maroon highlights primary actions and selections. Dark theme remains
available at the top right. Reduced-motion preferences are respected.
The page/zoom toolbar can float, minimise, or lock across the full width of the
PDF working area at its top or bottom. Drag the dotted handle in Floating mode;
the position button offers Floating, Lock to top, Lock to bottom and a reset.
Use the minus button to minimise; restore with the plus button or page summary.
On the move handle, arrow keys move the floating toolbar and Shift moves further.
Floating positions remain inside the working area as its size changes. Layout,
position and minimisation are remembered locally when local storage is available.
Fullscreen includes both the document and its page controls.
Processing uses a circular outline in place of the horizontal bar. Unknown progress
traces around the circumference; reported progress fills the ring and shows its
percentage. Task details and Cancel remain available. Reduced-motion preferences
disable the tracing animation, and native progress semantics remain accessible.

QUICK START
Choose Edit > Direct edit. Paragraph is the default: click an outlined paragraph,
edit its text and choose Apply. Its lines rewrap at the selected width, so removing
words pulls the following text up instead of leaving gaps. Enter inserts a hard
line break; Ctrl+Enter (Cmd+Enter on Mac) applies. Cancel/Escape dismisses the edit.

Choose Edit as in tool settings or the on-page editor:
- Paragraph: edit a detected paragraph as continuous text, with automatic wrapping.
- Line: change a single visual line in place without reflowing its neighbours.
- Text chunk: drag around complete lines or several paragraphs, then edit/reflow
  them together. Removing old line/paragraph breaks closes gaps in that selection.

Width (pt) controls wrapping without reducing the font size. It defaults to the
original text width and is retained after an edit, even when the paragraph becomes
shorter. PDF paragraph boundaries are inferred from text geometry; use Text chunk
when automatic detection does not include the text you intend to change. A chunk
uses one text column and writing direction. Reflow stays on the current page;
unselected paragraphs, artwork and page elements do not move. To pull several
paragraphs together, include them in the same chunk. Growth that would overlap
unselected text or leave the page is refused; adjust width or select a larger chunk.

The saved PDF reuses original native font programmes, colours, opacity and sizes.
Unchanged mixed-style words retain their styles; replacement words inherit the
style of the source text they replace. New inserted words inherit a neighbouring
style. The first baseline stays in place; following lines move as text rewraps.
Compatible embedded TrueType/OpenType fonts load locally for the typing preview;
otherwise it uses a matching installed face or a fallback. A mixed-style paragraph
uses its first style in the typing preview; source styles are retained in the PDF.
The editing scope stays selected and is remembered locally. Applied edits, original
wrapping widths, undo/redo and reading position recover through IndexedDB.

Missing source-font characters and unsupported writing directions/encodings are
refused without changing the working PDF. Scanned images, outlined glyphs, invisible
OCR layers and older image-backed text boxes have no editable visible font data.
OCR makes scans searchable rather than directly editable. New PDFCreator text boxes
retain their font recipe and are edited as a complete box, preserving font settings
and fitting inside the original area. They use system fonts on this device;
unavailable fonts fall back. Annotations continue to use the comment tools.
Direct edit stays selected until another tool, Done or the same button is chosen.
Edits and inserted items keep the current page and scroll offset. Apply or cancel
before changing scope; changing page/tool or scrolling dismisses an unapplied edit.

Open PDFs with Open files or the + beside the document tabs. Each PDF opens in
its own tab. Click a tab to switch; edits, undo/redo, page position, zoom, search
and pending redactions stay with that document. Use the x on a tab to close it.
Unsaved edits or pending redactions prompt before closing. New, sample and
restored workspace documents also open new tabs. Images selected together become
one new PDF tab, separately from any selected PDFs.
PDF pages now form one continuous vertical stack. Scroll with your mouse wheel,
trackpad, scrollbar or touch to move through the document. The page field, compact
toolbar summary and bottom preview selection follow the page you are reading.
Previous/next, page-number entry and bottom previews still jump to a page within
the stack. Nearby pages render on demand with a bounded canvas cache. Selecting
text, viewing a comment or starting an annotation on another visible page uses
that page. Scrolling cancels an unfinished pen/area gesture. Reading page, zoom
and scroll position stay with each tab and recover locally. Earlier saved views
are converted to the matching page in the continuous layout when resumed.
IndexedDB automatically retains working documents and edits in this browser.
Open tabs are restored at startup. Closed tabs remain in Library for reopening.
Home, beside the document tabs, shows up to six recent files with first-page
previews and Resume buttons. Resume switches to an existing tab or reopens the
latest saved working copy without duplicating it. Home retains open tabs,
edits, undo history and each document's page/zoom/scroll position. View library
opens the full list. Previews are generated locally and cached only in memory;
view-only changes reuse them, while PDF edits refresh the relevant preview.
Use the chevron above the left navigation to collapse it to an icon bar; icons
are present in the expanded navigation too, with tooltips in compact mode.
Choose a group in the upper-left navigation to open its tools in a left popup
pane. Click outside or press Escape to dismiss it. Use its pin button to dock
the tools as an icon bar on the right. Hover icons for tool names; the settings
button opens options for the selected tool. Text tools show font, colour and
text size; drawing tools show colour and stroke width; search shows its search
controls. Done exits the selected tool. Clicking outside dismisses those
settings while the pinned bar stays visible. Unpin returns to the left popup;
the close button hides the bar.
Text appearance settings use a shallow horizontal card with a small font sample
and a close button. Closing settings keeps the placement tool active.
Page previews stay along the bottom. Use Compact
beside Document pages to reduce previews to a thin strip of numbered page tiles;
use the arrow at its left to expand them. Every tile remains clickable.
Placement tools use a rectangle dragged on the page.
Draw under Annotate uses a freehand pen gesture instead: press, move along your
desired path and release. A live stroke preview follows the active pointer.
Each completed stroke becomes a native PDF Ink annotation; separate strokes stay
separate. Draw stays selected for the next stroke. Colour and stroke width apply
at the start of each stroke. A tap makes a small dot. Escape, pointer cancellation
or a page rerender cancels an unfinished stroke. Undo/redo handles complete strokes.
Sticky notes, text comments, page text, stamps, drawing tools, images, links,
form fields and visual signatures stay selected after placement so they can be
used repeatedly. Click the same feature again, choose another feature, or use
Done/Escape to finish. Browsing tool categories does not cancel the current tool.
Save PDF downloads a new copy. Undo/redo history is also kept in local recovery.
Save workspace includes the current PDF and pending redaction marks in a
portable .pdfcreator file. Download backups for important work or transfer to another browser.

LINKS
Choose Edit > Add link and drag over the text or area that should become clickable.
The dialogue accepts a website URL, email address or a page in the same PDF. A bare
website address such as example.com becomes an HTTPS URL. Invalid input stays in
the dialogue for correction. Link placement remains selected for repeated use.
Choose Done or click Add link again to follow links. Website/email links use the
browser's normal handler; websites open separately. Page links jump within the
continuous document. The small arrow beside a link opens its edit/remove dialogue.
Undo/redo and local recovery retain native PDF links. Links from existing PDFs also
appear in the viewer. Unsupported destination schemes are not opened.

FEATURE AUDIT
FEATURE-AUDIT.txt in the GitHub package (or pdfcreator-FEATURE-AUDIT.txt beside the
standalone HTML) maps all 65 distinct tool actions to the regression suites used.
The PDF worker, OCR core and English model are executed with real synthetic PDFs
and images in a controlled worker runtime. Tests inspect PDF/text/image/JSON/ZIP
outputs, including complete form and certificate-signing UI workflows. A fresh
live-browser layout/print/download/profile test remains unavailable. No user PDFs
or credentials are used by the tests. Existing limitations below still apply.
OCR output retains line grouping for phrase search and plain-text extraction.

MERGE & SPLIT
Open a PDF, choose Organise > Merge & split. The active edited PDF is the first
source. Add PDFs imports additional documents as inactive tabs; choose an open
tab or locally saved PDF in Sources & settings to add its current working copy.
Drag source files or use their up/down arrows to set merged page order. Removing
a source from the plan keeps its document tab and local copy.

Use Split after page N below a preview to add a split, or Remove split after page N
to remove it. Clicking the preview itself also toggles that split. The Split points
field stays visible above the preview grid even when Sources & settings is collapsed.
Enter 3,7 and choose Apply split points to split after pages 3 and 7. The selected
points, grouped ranges and output count update together. Maroon markers identify the cuts;
the final page always ends the last output. Markers belong to source pages and
follow them if files are reordered. Alternatively enter grouped ranges such as
1-3,4-7,8-10 and choose Apply ranges: these create three PDFs. Groups must cover
all pages exactly once, in order. Split every page and Reset splits are shortcuts.
Output names, page ranges and counts appear before generation. Edit the filename
prefix to name the outputs. Previews load on demand in batches of up to 60 pages;
use the arrow buttons above Page previews to browse subsequent batches.

Download ZIP produces the grouped PDFs and a README with source order/ranges.
Where supported, Save As opens at the start of the click; otherwise a normal
download starts after generation. Save generated ZIP remains available in the
workspace for retrying the download. Changing the plan or leaving the workspace
clears that generated link. Create merged tab opens all ordered pages as one new
working PDF, independently of the split markers. Source PDFs remain unchanged.

Plans save with their owner PDF in IndexedDB when local saving is available.
They are local plans, not part of the PDF or portable .pdfcreator workspace export.
Reopening Merge & split restores its source order, cuts and naming. Source edits
require Refresh sources & reset splits and a new review; missing sources must be
removed or restored. Pending redactions must be applied or cleared before export.
Documents with form widgets require Flatten form first, including certificate
signature widgets. New copied PDFs cannot retain original certificate validity.
Flattening creates a changed working copy and requires reviewing/resetting the plan.
Encrypted uploads ask for the password and add an unlocked working copy; use
Encrypt PDF separately to protect an exported PDF. Back to PDF returns to the
owner's page/zoom/scroll position. Up to 200 sources are supported in a plan.

LOCAL LIBRARY AND RECOVERY
Local autosave uses IndexedDB, with no server or account. PDF bytes, original
working bytes, undo/redo, selected images, pending redactions, search, page/zoom/
scroll positions and font choice are retained. Open tab ordering and active tab,
collapsed navigation, compact previews, right docking and theme are restored.
PDF edits are saved before their action finishes. Small view/preferences changes
are debounced; view-only changes do not rewrite PDF binaries. Each PDF snapshot,
its small view record, library metadata and open-tab manifest commit atomically.

The footer reports Saved on this device, Local save pending, Saving locally,
Not saved locally, or Local saving unavailable. Failure never clears the current
in-memory PDF. A failed save keeps the last complete stored copy. Export work
if storage fails. Closed copies can be removed from Library to free space.
A revision check prevents another PDFCreator window from silently overwriting a newer
workspace; export current work before reloading a window that reports a conflict.

Closing a saved tab retains its current edits in Library without a discard prompt.
To delete it from the browser, close the tab then choose Library > Remove and
confirm the named copy. Downloaded files are unaffected. Recovery copies may be
unlocked even when the uploaded source was encrypted. Originals and undo history
can include content removed from a redacted export. Remove the stored copy to
clear its recovery history; other copies and original files are separate.

Storage belongs to the browser profile and web origin. Clearing site/browser data,
private browsing, quota/eviction or browser restrictions can remove/prevent it.
file:// support is browser-dependent and is reported by the save indicator.
Changing browser, origin or hosting location does not transfer stored documents.
Download PDFs or .pdfcreator workspaces for backup or transfer. No passwords, PFX
credentials or signing keys are included in the saved workspace state.

FONTS
Tool settings offer 30 common system-font choices with a live sample. The chosen
font applies to added/replacement text, text comments, stamps, watermarks, page
and Bates numbers, headers/footers, batch decorations and typed visual signatures.
It stays with its PDF tab and is included when saving a .pdfcreator workspace.
The application interface continues to use embedded Inter. Existing PDF text,
form-field fonts and the invisible OCR font are not restyled by the selector.
Watermark, numbering, header/footer and batch dialogs include their own font and
colour choices. Typed visual signatures also have a font selector. Cancelling a
dialog does not change its appearance settings.

Choices: Arial, Arial Black, Arial Narrow, Aptos, Aptos Display, Calibri, Cambria,
Candara, Century Gothic, Comic Sans MS, Consolas, Constantia, Corbel, Courier New,
Franklin Gothic Medium, Gabriola, Garamond, Georgia, Helvetica, Impact, Lucida
Console, Lucida Sans Unicode, Microsoft Sans Serif, Palatino Linotype, Segoe UI,
Segoe Print, Segoe Script, Tahoma, Times New Roman and Verdana.

Font availability depends on the device/browser. Missing faces fall back to
Arial/sans-serif. System font files are not bundled, downloaded or redistributed.
To preserve the chosen device-font appearance, new visible font text is stored
as a transparent image at up to 288 DPI, with searchable Unicode ActualText for
page text. Text comments retain complete Contents and a native annotation subtype.
These appearances are not vector glyph outlines or editable embedded system fonts.
Select an entire added text box when replacing it; its image and search layer are
removed together. Replacing native PDF text preserves surrounding graphics and
does not reflow paragraphs or automatically match the original font.

INCLUDED
Viewing, selection/copy/search, page organisation, PDF/image merging, blank
pages, extraction/splitting, annotation/comments/drawing/stamps, added text and
images, links, bookmarks, watermarks, numbering/Bates/header/footer, metadata,
attachments, AcroForm fill/create/import/export/flatten, visual signatures,
English OCR with invisible searchable text, visual/text comparison and heatmaps,
lossless optimisation, page image/text exports, batch processing, AES-256
password encryption, permanent region removal, full raster sanitation,
bounded existing-text replacement, and RSA PKCS12 certificate signing/verification.

REDACTION
Marking a region is only a pending selection. Apply redactions must be run.
Secure rebuild (default) creates every page from rendered pixels, then masks
selected rectangles again after all overlays render. The new PDF contains no
original text, forms, comments, links, attachments, metadata, or earlier revisions.
It also loses searchable text, vector quality and accessibility tags.
Native removal preserves remaining text/vector content but is not an exhaustive
hidden-data scrubber. Review all exported pages and all potentially sensitive
occurrences before sharing. Undo and local recovery retain prior copies and original working bytes across
sessions. Close the tab and remove its stored copy from Library after sensitive
work. Only the rebuilt export is sanitised; original files and other copies remain.

SIGNATURES
Visual signatures are images, separate from certificate signatures.
Type your name, draw a signature, or combine both. A combined visual signature
keeps the drawing and places the typed name below it in the chosen font. Clear
drawing leaves the typed name intact. Importing PNG/JPEG uses that image by itself.
The combined image stays available for repeated placement and local recovery.
Certificate signing supports RSA >=2048-bit PKCS12/P12/PFX, detached CMS SHA-256,
and incremental approval signatures. Certificate signature widgets are invisible;
add a visual signature separately if desired. Current RSA detached signatures
are verified for byte integrity and coverage. CA trust, revocation, hardware
tokens, ECDSA, RSA-PSS, trusted timestamps and PAdES/LTV are unsupported.
An intact signature does not establish a trusted identity. Claimed local signing
time is not a trusted timestamp. Certification/DocMDP/XFA/encrypted signing
inputs are rejected. Existing signatures may be invalidated by PDF edits.
Signing has a 150 MB input limit and uses main-thread cryptography.

ENCRYPTION
AES-256 export creates a separate password-protected download. Open working
copies remain unlocked. Passwords with commas, NUL/newlines, or over127 UTF-8
bytes are rejected by the native save grammar. If no owner password is given,
the open password is used. Permission restrictions depend on PDF reader support.

LIMITS
This is an implemented offline toolkit, not complete Adobe Acrobat equivalence.
No Office round-trip conversion, live shared reviews/signature collection,
scanner/OS printer drivers, AI assistant, dynamic XFA, rich media/3D/CAD,
professional colour preflight or PDF/A, PDF/X, PDF/UA conformance certification.
Text replacement is bounded by a selected rectangle; it does not automatically
match original font subsets or reflow paragraphs. OCR includes English
only; confidence is approximate and recognition can be wrong. OCR search text
uses a Latin character set. Comparison aligns pages at the top-left and is
not semantic equivalence. Browser print creates a local raster print view.
Advanced PDF structures may not survive rewriting; always work from a copy.
Very large PDFs may exceed browser memory. Render size is capped; heavy native
engine work and OCR can be cancelled by terminating their background workers.
Smaller page edits and certificate signing can briefly block the interface.

GITHUB PAGES
Extract the GitHub ZIP into your repository. index.html is the single runtime file.
Publish the repository root using GitHub Pages. No backend or secret is required.
Keep LICENSE.txt, THIRD-PARTY-NOTICES.txt, app source ZIP, and upstream source
available with the release. Large source archives can be GitHub Release assets.
The application runs at the hosted URL while connected; for dependable offline
reopening download index.html and open it locally. There is no service worker.
User documents are processed locally and are not committed or uploaded.

SOURCE AND BUILD
The About dialogue exports the application source/build kit embedded in the HTML.
The GitHub ZIP additionally includes the complete official MuPDF1.28.1 source
tarball, including third-party sources. Its platform/wasm/BUILDING.md describes
the upstream engine build (Emscripten4.0.8 and Node22).
For app rebuilds: extract app source ZIP, cd source, install pinned dependencies
with pnpm install --frozen-lockfile, place mupdf-1.28.1-source.tar.gz beside
build.mjs, then run node build.mjs. The output directory is ../../outputs relative
to the source folder. The build downloads nothing after dependencies/model are
present. The included vendor artefacts retain exact distributed runtime bytes.

VERSIONS
MuPDF1.28.1 (AGPL-3.0-or-later), pdf-lib1.17.1 (MIT), node-forge1.4.0 (BSD),
Tesseract.js7.0.0 and core6.1.2 (Apache-2.0). English model: tessdata_fast/eng.
The application is AGPL-3.0-or-later. See included notices and licences.

TESTS
Source tests: node engine-test.mjs; node signing-test.mjs; node annotations-test.mjs;
node annotation-interactions-test.mjs; node tabs-interactions-test.mjs.
node fonts-previews-test.mjs checks compact preview controls and saved system-font text.
node local-store-test.mjs checks IndexedDB transactions, rollback, revision conflicts
and queued writes. node persistence-interactions-test.mjs checks fresh-app recovery
and navigation/library controls. node ui-refresh-test.mjs checks Home/Resume,
bounded native thumbnails, contextual settings and the action menu. These storage
tests use fake-indexeddb as a test-only dependency;
this does not establish browser-specific file:// storage compatibility. Optional
test dependencies can be installed alongside the source with pnpm add -D
jsdom@30.1.3 fake-indexeddb@6.0.1 @napi-rs/canvas, or provided through the
PDFPRO_DOM_MODULES/PDFPRO_IDB_MODULES environment variables.
The interaction tests use jsdom and @napi-rs/canvas as test-only dependencies.
They exercise real PDF processing in a controlled DOM, not a browser layout engine.
Historical browser scripts are included; browser verification status is in VALIDATION.txt.
node source-package-test.mjs verifies deduplicated ZIP reconstruction, integrity
checks, safe paths and the compression fallback. After building, node
packaging-release-test.mjs verifies the strict size cap, all source-file bytes,
runtime assets, both ZIP export paths, release archives and checksums.
node source-export-ui-test.mjs uses the actual release assets in a controlled DOM
to check About > Download source bundle, notices, duplicate clicks and error/retry
behaviour without changing the working PDF.
node placement-tools-test.mjs checks repeated placements, toggle-off controls,
compact text settings, preserved placement coordinates and per-document selection.
node freehand-test.mjs checks live pen samples, native Ink paths and rendered pixels,
coalesced events, pointer ownership/cancellation, taps, rotations/zoom, undo/redo
and fresh-instance recovery using synthetic PDFs in a controlled DOM.
node page-toolbar-test.mjs checks dragging, minimisation/restoration, top/bottom
docking, keyboard controls, resizing, fullscreen targeting and local preference
recovery with simulated geometry. It does not establish browser layout accuracy.
The browser harness uses Playwright and a local installed Chrome/Edge and blocks
HTTP/HTTPS requests during file:// runtime tests. See VALIDATION.txt in release
outputs for the actually completed checks and remaining coverage gaps.

ANNOTATIONS
Text comments have a transparent background. Stamps have a transparent text-and-border
appearance. Text wraps/shrinks to fit the selected area or reports an error; it is not
silently clipped. Click an annotation while no placement tool is active, or use its
small comment button, to open its full contents. Dragging text still selects it.

ANNOTATION REGRESSION CHECKS
node annotations-test.mjs checks saved annotation rendering with real PDF bytes.
node annotation-interactions-test.mjs checks comment popups and navigation in
a test DOM using jsdom and @napi-rs/canvas. These are test-only dependencies;
PDFPRO_DOM_MODULES can point at a jsdom installation. This DOM check is not
a browser layout or accessibility certification.

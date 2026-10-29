PDFCreator 3.0.0 — offline PDF workspace
==================================

OPEN
Open pdfcreator.html (or index.html from the GitHub package) in current desktop
Chrome, Edge, Firefox, or Safari. No installation, accounts, or network access
are needed for standalone PDF tools. The optional Word import companion requires
Windows and installed Microsoft Word desktop. Chrome and Edge were tested earlier.
The app may take a few seconds to unpack its embedded engines on first launch.
The current image-editing revision was checked with native PDF processing and a
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
The complete source/build ZIP accompanies the release. The embedded source is
also available through window.PDFCreator.downloadSource(), which assembles it
locally. Its paths and file contents match the separate app-source ZIP. When
browser compression is unavailable, a valid larger ZIP preserves the same files.
This changes packaging only; PDF operations, OCR and local recovery are retained.

INTERFACE
White, maroon, navy and black palette. Inter4.1 is embedded in the HTML and
licensed under SIL Open Font License1.1. Interface copy uses British English.
Create is the first entry in the left toolbar; Save PDF has a diskette icon in
the header. Tool popups are 260 px wide with compact 36 px minimum-height tiles,
15 px icons and content-sized height, scrolling within the available workspace.
Create offers New PDF,
Import from Word and Open PDF; the old top Open files button has been removed.
The three-dot menu contains Create, Local library and Print document. Page controls
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


CREATE A NEW DOCUMENT OR IMPORT WORD
Choose Create in the left toolbar, on Home, or beside the document tabs.
It opens the same compact side tool pane as the other navigation functions.
New PDF opens page settings; Import from Word opens companion controls; Open PDF
goes directly to the file picker. There is no central Create choice dialogue.
The pane supports outside-click dismissal, collapsed navigation and icon-only
docking. It is also available on Home before a PDF has been opened.
- New PDF: name your document, choose A4/A5/A3/Letter/Legal or a custom size,
  orientation, 1-200 pages, margins and blank/ruled/squared paper. Dimensions and
  margins are in millimetres. The PDF opens ready to add text in Edit; use Add image,
  shapes or form tools to build the document from scratch. Other tabs stay open.
- Open PDF: select one or more existing PDFs. Password entry and document tabs work
  as before. Images can still be dragged in to create PDFs or placed using Add image.
- Import from Word: download/extract PDFCreator-Word-Companion.zip, then run
  start-word-companion.cmd. In the import dialogue, paste the console's pairing
  code, choose a .docx/.doc file and select Convert and open. The companion is also
  included in the GitHub ZIP and downloadable directly from the HTML itself.

Word import uses Microsoft Word's native PDF export on Windows. The HTML does not
try to recreate Word documents as browser HTML. Visible formatting, pictures,
tables, headers, footers and page layouts follow Word's rendering; use the source
fonts and review complex documents. Missing fonts, linked content or unsupported
Word features can affect fidelity. There is no unconditional guarantee of every
possible Word layout. Protected files may require manual PDF export from Word.
No cloud conversion API or account is used by PDFCreator. The companion binds only
to 127.0.0.1 and requires a fresh pairing code; your browser may ask for local-network
access. Pairing credentials stay in session memory, not IndexedDB. New/existing
PDF tools remain usable with the HTML alone. See WORD-COMPANION-README.txt for
requirements, temporary files, cancellation and process handling details.

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

Open PDFs with Create > Open PDF, or use the + beside the document tabs to open
the Create choices. Each PDF opens in
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
removed together. The older Replace text rectangle tool preserves surrounding
graphics and uses the chosen replacement font. Direct edit and Find and replace
reuse native source fonts and support paragraph reflow within the selected flow.


COMPLETION WORKSPACES (28 OCTOBER 2026)

Edit > Edit form fields (also under Forms)
Standard AcroForm fields are clickable in the normal viewer. Click a text field to
edit directly, including multiline paragraphs, or use Edit > Edit form fields to
keep selecting fields. Add text, Direct edit and Replace text also route clicks or
regions inside a text field to this native editor; text is not painted underneath
the widget. Apply/Ctrl+Enter saves one undo step. Cancel/Escape or clicking grey
space cancels a draft. The current page and local recovery are retained.

Text fields offer Original font or standard PDF Helvetica/Times/Courier variants,
size (0 for automatic sizing), colour, left/centre/right alignment and multiline.
The original font is retained unless changed. Text wraps within the original
field; reduce the font size if long content is clipped. Checkboxes, radio options,
dropdowns and list selections have appropriate on-page controls. Read-only/locked
fields stay protected. Field names, maximum lengths, choice export values and
shared widgets are respected. Distinct fields with duplicate names are isolated.
The logical field values and visible appearances update together; fields remain
interactive after Save PDF. Forms > Fill form retains a bulk editor and now uses
multiline textareas instead of single-line boxes where appropriate.
XFA, push-button scripts, signature fields and document JavaScript/calculations
are not executed by this editor. Flat/scanned forms have no native fields: use
Add text or create text fields in the blank areas. Existing form boxes do not grow
or move other page content automatically. Lists use a local native appearance.

Edit > Edit images
Click an image directly in the normal viewer, or choose Edit > Edit images first.
The Image inspector provides a crop preview, edge percentages, position/size in
points, a keep-proportions option, opacity, brightness, contrast, saturation,
colour hue and warm/cool tone. Drag the selected image to move it; drag its corner
to resize it. Preview crop changes by dragging a box in the small image preview.
Apply changes commits the inspector settings as one undo step. Delete image
removes the selected occurrence. Arrow keys move it (Shift moves 10 pt), Delete
removes it, and Escape deselects. The inspector can minimise or close.
Add image opens the same inspector after placement. Select objects retains its
rotation, duplication, alignment and snapping controls, with Image adjustments
opening the new inspector. Edits retain page position, undo/redo and local recovery.
Shared image resources and images inside content groups are isolated so editing
one occurrence does not change its other uses. Original pixels are retained for
readjustment: cropping and deleting are not secure redaction. Use Redact for
permanent removal. Colour preview/adjustment supports images up to 20 million
pixels; larger images retain move, resize, crop and opacity controls. Inline binary
images and stencil masks are unsupported. A picture baked into a larger scan
cannot be selected separately, and original PDF clipping can constrain movement.

Large-image appearance fix: pixel views are acquired after native transparency
mask decoding, which can resize WASM memory. This prevents stale colour/alpha
buffers from turning adjusted images blank or discoloured. If an earlier edit
looks white, open Image properties, Reset appearance and Apply changes to restore
its retained source pixels, then adjust it again in this updated app.

Click the grey space around a PDF page or blank non-working workspace to deactivate
the selected function. Clicking within the page keeps the function ready for
repeated use; tool settings, image properties and navigation remain usable.

Edit > Select objects
Click visible PDF text, an image/signature, a content group, or an annotation.
Drag its selection outline to move it; drag the bottom-right handle to resize.
Shift keeps proportions. X/Y/W/H and rotation are in points/degrees. Apply commits
numeric changes; Duplicate offsets a copy; Delete removes the selected item.
Align positions against the page; Snap aligns edges/centres against the page and
other selectable items. Hold Alt while dragging to bypass snapping. Arrow keys
nudge the focused selection; Shift moves 10 pt. Escape closes the inspector.
Native text keeps its vector glyphs/source fonts. Images and Form XObjects stay
native; annotation geometry and appearance move together. Added text retains its
independent editing recipe through movement, resize, rotation and duplication.
Inline binary images, arbitrary painted vector paths and locked annotations are
not independently editable. A nested PDF Form is selected as a content group;
its text can also be selected as individual editable text lines. Source clipping
paths still constrain transformed objects. Unsupported text encodings are refused.
Annotate > Erase drawing removes complete ink strokes touched by the gesture;
other strokes in the same Ink annotation remain. It does not erase image pixels.

Rich text and live page preview
Add text, Text comment and Stamp open a compact horizontal editor on the page.
Enter or paste plain text, then select text to change its font, size, colour,
bold or italic style. With no text selection, formatting applies to all text.
Alignment and bullets apply to selected paragraphs; Line and Gap set line and
paragraph spacing. The selected PDF area shows a live appearance preview.
Fit to area scales styles together if needed, down to 4 pt. Uncheck it to require
the requested sizes exactly. Apply commits; Cancel/Escape leaves the PDF unchanged.
Ctrl/Cmd+Enter applies. Placement stays selected for the next item.
Direct edit reopens the rich editor for tracked rich text boxes. In Comments,
Format text opens it for a FreeText comment or stamp, preserving its reply thread.
Mixed formatting is retained in a run model, never executable HTML. As before,
device-font appearance is a transparent image with searchable Unicode page text;
fonts come from the device and can differ on other devices when re-editing.

Text-aware markup
Highlight, Underline and Strikeout follow the text between pointer endpoints,
including partial lines and multiple lines. The drag preview shows the selected
text bounds. The native PDF annotation stores the selection quads and selected
words. Scans require OCR; unrecognised page images have no selectable text.

All-page comments
Annotate > Comments lists annotations across the whole document. Search contents,
replies and authors; filter by type, open/resolved status or the current page.
Select a comment to edit its text/author, add a reply, resolve/reopen it, or delete
its thread. Delete requires a second click. Go to page closes the workspace and
navigates to the comment. Format text handles the appearance of FreeText/stamps.
Replies use native PDF IRT relationships; resolved status is saved in PDF metadata.
Other viewers can interpret review status differently. Export summary downloads
an escaped offline HTML summary with a Print button. It contains all annotations.
No online collaboration or external messaging is involved.

Visual page organiser
Organise > Page organiser replaces the old numeric reorder prompt. Tiles have
lazy native previews. Click selects, Ctrl/Cmd-click toggles, Shift-click selects a
range. Drag selected tiles before another tile or into empty grid space to move
them to the end. Earlier/Later provides a keyboard-accessible alternative.
The Document dropdown lists every open PDF, defaults to the active tab and switches
the active PDF and organiser together. If changes are staged, choose Apply and
switch, Discard and switch, or Stay here. Cancel also cancels a pending switch.
Stage bulk rotation, duplication, deletion and blank pages. Use the separate
Insert from selector to choose another tab or Upload PDF, enter source page
ranges, then Insert pages or Replace selected.
Insertions follow the last selected tile; replacement uses the first selected
position and removes all selected tiles. Extract downloads selected staged pages.
Apply saves the staged arrangement in one undo step; Cancel discards the preview.
The current original page is followed to its new position when it is retained.
Flatten live forms before copying/extracting/duplicating pages containing fields.
Existing page objects/internal destinations are retained when rearranging originals;
advanced outlines, destinations to deleted pages and imported cross-document links
may need review after restructuring. Imported certificate-signed sources are refused.

Document-wide Find and replace
Available in View and Edit, from the Find tool, or Ctrl/Cmd+H. Choose literal search
text, replacement text, case matching, whole words and page ranges. Preview lists
before/after paragraphs and occurrence counts. Select individual results or all
supported results, then Replace selected. Replacements are one atomic undo step.
Native paragraphs reuse their source styles/fonts and wrap at the original width;
tracked device-font/rich text boxes update both appearance and searchable content.
Missing glyphs, overflows and collisions with unrelated native text are refused;
a failure preserves the entire working PDF. Search is for editable page text,
not comment bodies, image pixels, field values or every possible legacy encoding.
OCR can add search text to scans, but invisible OCR text cannot be directly edited.
Only the selected paragraph/box reflows; unrelated content is not moved.

INCLUDED
Viewing, selection/copy/search, page organisation, PDF/image merging, blank
pages, extraction/splitting, annotation/comments/drawing/stamps, added text and
images, links, bookmarks, watermarks, numbering/Bates/header/footer, metadata,
attachments, AcroForm fill/create/import/export/flatten, visual signatures,
English OCR with invisible searchable text, visual/text comparison and heatmaps,
lossless and image-aware compression, page image/text exports, batch processing, AES-256
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
The older Replace text tool is bounded by a selected rectangle. Direct edit and
Find and replace reuse compatible native fonts and reflow within paragraph bounds;
they do not move unrelated paragraphs or flow onto another page. OCR includes English
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
About & source shows authorship/contact and links to source/build instructions
and component licences. The complete source/build kit remains embedded and can
be exported with window.PDFCreator.downloadSource().
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
to check the embedded source API, retained notices, concurrent requests and
error/retry behaviour without changing the working PDF.
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

WATERMARK CENTRING AND EDITING (28 OCTOBER 2026)
Edit > Watermark centres the visible rotated text on each displayed page, using
its actual painted bounds. Crop origins, page rotation and scale are accounted
for. Size, angle, opacity, font, colour and page ranges can be chosen. Batch text
watermarks use the same positioning and retain identification metadata.

Edit > Edit watermarks identifies layers across the document. It supports newly
tracked PDFCreator layers, older diagonal/translucent PDFCreator image/search
Forms, explicitly tagged watermark Forms/annotations, and inferred transparent
or diagonal native text objects. Inferred candidates are labelled for review;
ordinary body text is never automatically selected or changed.
Select a listed layer to inspect the outlined page preview and original settings.
Select matching chooses layers with the same text/source on other pages. Update
selected replaces each selected layer with the chosen text/font/colour/size/angle
and centres the result. Imported image/vector layers can be replaced with text;
Remove selected deletes the chosen layers after a second confirmation click.
Other page content is retained, including body text that overlaps a native text
watermark. Updates/removals use one undo step and the normal local recovery path.
Watermarks baked into scanned/page images, clipping text or complex nested content
without an identifiable separate layer may not be recognised. Use Select objects
for other independently selectable artwork. This is not automatic image inpainting.
The Open PDF tile description also includes the requested wording, “Classify
documents before loading”; this change adds descriptive text only.

PAGE DECORATIONS AND LINK PLACEMENT (29 October 2026)
Watermark rotation accepts -360 to 360 degrees in 0.1 degree steps; placement
remains centred on the displayed page, including rotation and crop offsets.
Headers and footers have independent Left/Centre/Right alignment and timestamp
choices: date, time, both or none. Optional full-width rules sit below the header
and above the footer, with independent 0.25–12 pt thickness. Timestamps capture
the device's local date/time once per operation, using British date formatting.
Page numbers and Bates numbers have their own alignment. Add them alongside
header/footer text, or add/update a footer from the numbering dialogue. Footer
and number rows are separate. Later updates replace the same tracked slot while
retaining the other slots. Text shrinks to fit its page band. These slots apply
to PDFCreator's new decorations; untracked imported headers/footers are unchanged.

Edit > Add link offers three placement modes: click existing text, image or shape;
draw a link area; or place new linked text. The dialogue can add visible display
text with a chosen installed font, size and colour, plus a website/email or
internal-page destination. New text and its link form one undo action. Choose
Done to follow links, or use the existing arrow badge to edit/remove a destination.
Click targets follow text lines and identifiable image/vector/annotation bounds;
flattened scans require an area selection because their text/shapes are pixels.

BOTTOM PAGE PREVIEW ORGANISATION
Click a preview to navigate and select. Ctrl/Cmd-click toggles individual pages;
Shift-click selects a range. Ctrl/Cmd+Shift extends an existing selection. Drag
selected tiles together before or after another tile; the insertion mark shows
the position. Dragging near the strip's edges scrolls it. Drop in empty space
to append. The viewed original page follows its new position; undo restores it.
Right-click a tile or the strip for Select all, Rotate, Duplicate, Delete, Extract,
Move earlier/later, Insert blank before/after, Insert pages from PDF, Replace
selected from PDF and Open Page organiser. Right-clicking a selected tile retains
the selection; an unselected tile becomes the selection. New blank pages match
the clicked page's displayed dimensions. Imports accept another open tab or a
local file, with source page ranges. Signed sources and pending redactions need
resolving before import. Live form pages must be flattened before copying.
Changes apply immediately as one undo action and use normal local autosave.
The full organiser continues to offer a staged preview before Apply.
These controls work with both compact and expanded bottom previews. With a tile
focused, Ctrl/Cmd+A selects all, Alt+Left/Right moves earlier/later, Delete asks
before deletion, and Shift+F10 opens the context menu. Escape/outside click closes
the menu. Page selection resets after unrelated PDF changes or tab switches.

node page-features-test.mjs checks page-band pixels on cropped/rotated pages,
tracked-slot replacement, timestamps, existing-object/new-text links, the About
changes, watermark controls, compact tool CSS and organiser document switching.
node page-strip-test.mjs checks multi-selection, drag/drop, context menu actions,
blank/imported pages, native destination retention, form-copy safeguards, undo and
local recovery. Both use synthetic PDFs and a controlled DOM, not live browser
layout or actual browser drag/download behaviour.

SIZE-AWARE SAVE AND BETTER PDF COMPRESSION (29 October 2026)
Save PDF now opens export settings. Current quality downloads the exact current
bytes; choose Lossless, High quality (220 dpi / 90% JPEG), Balanced (150 dpi /
78% JPEG), Small file (96 dpi / 58% JPEG), or Choose a target file size. Enter a
maximum in decimal MB or kB, or use 1/2/5/10 MB presets. You can change the filename.
Compressed exports show current/prepared byte counts and percentage reduction
before download. Target results explicitly state whether the maximum was reached.
Cancelling either dialogue or the processing task keeps the working PDF intact.
The current-quality option preserves existing certificate signatures byte for
byte. Rewriting a signed PDF requires confirmation because signatures are invalidated.

Target mode first tries lossless cleanup. It then tries image settings from
300 dpi / 92% JPEG down to the chosen floors (default 72 dpi / 45% JPEG). It stops
at the first result at or below the maximum, or offers the smallest available
result. Higher resolution floors still permit quality adjustment. No padding is
added to force an exact size, and no result larger than the input is chosen.
Text-heavy, already compressed or unsupported-image PDFs may not reach the target.
Quality choices can soften photographic detail or scanned text; inspect the result.

Eligible opaque 8-bit RGB/grey image streams are JPEG-recompressed and downsampled
using their largest actual display size across pages and nested Forms. Shared
images are processed once, never upsampled, and replaced only when smaller.
Transparent/soft-mask/colour-key images, monochrome images, small images, special
colour spaces, images over 20 million pixels, inline images and unknown uses are
retained. Page content is not rasterised. Native text, vector graphics, links,
annotations, forms, page geometry, metadata and attachments are retained.
Lossless cleanup keeps image pixels and font programmes, removes unused/duplicate
objects and compresses streams/object streams. Target trials start from the
original bytes so JPEG quality loss does not accumulate between attempts.

The Compress tool offers the same settings and an actual-size preview, then
applies the result to the working PDF in one undo step. Saving a compressed copy
keeps the open PDF bytes, view and undo history at their existing quality.
Pending redactions require the usual acknowledgement before an unredacted save;
apply or clear them before changing the working PDF with Compress.

node compression-test.mjs checks real image/target compression, lossless pixel
equality, form/link/attachment/text/geometry retention, protected masks, size
floors and cancellation. node compression-interactions-test.mjs uses the actual
embedded offline worker to check Save/Compress settings, result confirmation,
attainable/unattainable targets, filenames, undo, cancellation and signature/
redaction decisions. These use synthetic documents and a controlled DOM; native
browser save pickers and layout have not been checked in this revision.

FUNCTION NAVIGATION TOGGLES
Click a left navigation function to open its popup. Click the same function again
to close it; another function replaces the popup content. Create follows the same
behaviour, including on Home and with collapsed navigation. When tools are pinned
as a right-side icon bar, clicking the active group closes its floating settings
while keeping the pinned bar. Home/tab-bar Create entries open the Create pane.
node navigation-toggle-test.mjs checks group/Create toggles, accessible state,
collapsed/pinned modes and retention of PDF bytes, page, tab and undo history.

SEARCH APP FUNCTIONS
The magnifying glass beside the dark-mode switch opens an offline function
search. Ctrl/Cmd+K opens it from the keyboard. Search tool names or common terms
such as compress, hyperlink, circle, reorder and scan. Results show their tool
group; shared tools appear once. The catalogue contains all 72 distinct tools
plus Create, Home, Local library, theme and About actions.
Click a result to open the matching tool or its normal settings/confirmation.
Existing safety confirmations and undo behaviour remain. Document tools are
disabled until a PDF is open; Create and app actions work on Home. A result
requiring a PDF resumes the active document if Home is showing. Opening an
already-selected placement tool retains its selection.
Arrow keys navigate, Enter opens, and Escape closes and restores focus to the
magnifier. Clicking outside or focusing another control dismisses the popup.
The header question-mark button opens About & source, retaining its accessible
name, source/licence links and authorship/contact information.
node function-search-test.mjs checks catalogue coverage, aliases, disabled states,
keyboard/dismissal behaviour, actual PDF actions, confirmations and About/theme.
These are controlled DOM/native PDF checks; live browser layout is unverified.

DELETE A PROJECT FROM HOME
Each recent project card has a dustbin beside Resume. Click it to see a warning
and choose Delete project or Cancel. Escape also cancels. Confirmed deletion
removes the project's locally saved PDF, original copy, edits, undo/redo history
and catalogue/view data. An open project is closed only after storage deletion
succeeds. Other projects and downloaded files are kept. Deletion cannot be undone.
Deleting the last project returns Home to its empty state. Invalid archived PDFs
can also be deleted without opening them. Storage errors leave an open project
and its edits intact; existing conflicting-window protection remains in effect.
Autosave serialises deletion with pending saves and excludes deleted IDs from
later captures, so stale queued state cannot recreate an explicitly deleted copy.
node home-deletion-test.mjs uses synthetic PDFs and simulated IndexedDB to check
confirmation/cancellation, failure retention, open/closed/last-project deletion,
in-flight saves, stale captures, local recovery and invalid archived copies.

CENTIMETRE POSITIONING FOR PAGE DECORATIONS
Headers, footers, page numbers and Bates numbers each have independent position
controls. Choose Top edge or Bottom edge and enter the distance in centimetres.
The distance is measured to the nearest visible text edge. Left and Right margin
(cm) position left/right-aligned text; Centre uses the space between those margins.
Distances follow the visible cropped/rotated page, using 72 / 2.54 points per cm.
Header/footer rules follow the text while continuing across the full visible width.
Keep footer and page-number distances different to avoid placing them on the same
row. Negative distances, margins that leave no text area and off-page placements
are refused. Current documents keep their existing decorations until updated.

FIELD EDITOR BOUNDS
Form-field popups stay inside the intersection of the current PDF page and the
visible working area, with an inset from its edges. They move inward near the
bottom or right edge and shrink for narrow/short views. The middle section scrolls
internally while Close and Apply stay outside that scrolling region. Resizing the
textarea, window or workspace recalculates the bounds; draft text is retained.

REMOVE DIGITAL SIGNATURES
Protect & sign > Remove digital signatures asks for confirmation before creating
an unsigned working copy. It removes populated certificate-signature fields and
widgets, their appearances and signing dictionaries, certification/usage-rights
signature policies and obsolete validation data. Full rewriting discards the old
incremental signature revisions. Ordinary fields, other page content and separate
visual signatures remain. Empty signature fields are retained. Save PDF downloads
the unsigned result; undo restores the exact signed bytes, and local recovery
retains the edited copy. The source file is not overwritten. A signature flattened
into page text or a picture has no certificate field to clear; remove it using
Select objects or Edit images. This tool does not make a signed original editable
while preserving its digital signature or establish certificate identity/trust.

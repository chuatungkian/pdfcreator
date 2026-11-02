Page attachment icons - 2 November 2026

Attachments are embedded inside the PDF. Use View > Attachments, choose a file (up to 50 MB), choose location, then click a PDF page to place its standard Paperclip icon. Nothing is embedded until the icon is placed. Done or Escape cancels placement. Existing embedded files without a page icon have a Place icon action. Filenames are kept unique so adding another file does not replace an earlier attachment.

In Read & select, click an icon for a local text or raster-image preview, Open PDF in a separate document tab, or Download. HTML, SVG and scripts are displayed as plain text. Other formats can be downloaded to open in an application on the device. Text previews show up to 1 MB; downloads retain the complete original file. No attachment is opened automatically. Icons remain in saved PDFs; external PDF viewer support for opening attachments varies. Move or delete an icon using Edit > Select objects or Objects & layers. Deleting an icon retains the file in the PDF attachment list. Adding a file and icon is one Undo step.

# Direct edit character mapping fix — 31 October 2026

## Website update notifications — 1 November 2026

Hosted HTTP/HTTPS copies check a small same-origin version.json after startup and every 30 minutes while the tab is visible and online. Returning to an overdue tab or reconnecting can trigger a throttled check. Heavy operations defer checking until idle; failed requests time out after 8 seconds and retry with backoff. No PDF/document data is sent. Downloaded file:// copies make no update requests.

A new build shows Update now / Later. Later leaves an update badge and suppresses repeated banners for that build during this session. About & source (?) includes the embedded build ID and Check for updates. Only explicit Update now can reload. Apply your draft first through Keep editing, or confirm Discard draft and update. Running tasks and open merge/split workspaces must finish first. Applied PDFs, originals, retained history, open tabs and reading positions are saved locally before navigating to the same app path with a fresh build query. A failed local save keeps the app and draft open and offers a workspace ZIP backup; unapplied drafts are not included in that backup.

Deployment: use node build.mjs with the output directory. Every build embeds a unique release ID and emits a matching version.json. Deploy that manifest beside index.html, pdfcreator.html and pdfpro.html in one atomic release. Where hosting supports it, use Cache-Control: no-store for version.json and no-cache for HTML. The checker also bypasses browser caching and adds a fresh query to manifest requests and release reloads. Existing tabs that predate this checker need one initial refresh to install it. Downloaded offline copies require replacing their HTML file.

## Changes review scroll following — 1 November 2026

Changes review now follows the visible PDF page automatically while scrolling or using page navigation. Its page number, changed-page selection and Original/Current preview update together. Unchanged pages show Unchanged; Original mode follows each page without changing the working PDF. Opening review keeps the current reading position. Previous/Next still jumps between changed pages.

## Changes review — 1 November 2026

Open View > Changes review to compare the working PDF with its originally opened copy. Changed pages are marked in the page strip and page headings. Previous/Next and the page list navigate modified, added, removed and moved pages. Toggle Original/Current for read-only page previews or open the larger comparison. Retained edits have individual before/after views without restoring earlier versions. Save PDF > Export review also offers Review page changes before downloading; this returns to the panel without downloading until Save is chosen again.

Text-fit/reflow choices (feature 4) remain in Edit > Direct edit: Keep layout, Fit text into box, and Move following text in this column. Recognition buttons now use a pastel red background with visible hover/focus states.

Review is local and does not change document bytes or history. It checks rendered pages, text geometry, form values, comments and links; tiny visual differences and hidden PDF structures may need separate inspection. Page matching uses contents; repeated identical pages are paired by position. Undo history is bounded to 20 steps, and undone edits are excluded from retained edits. The original baseline survives local recovery.

## Editing workflow upgrade — 1 November 2026

Text boxes: in Edit > Select objects, resizing native text, added text and FreeText comments changes the container and wrapping without scaling font sizes. Boxes grow downward when needed, and Direct edit keeps the chosen width as words are added. Added text defaults to automatic growth; Fit text remains an explicit sizing choice. Mixed groups scale artwork while retaining text sizes. Growth that affects nearby content requires confirmation, and page-edge overflow requires moving or widening the box.

- **Live page preview:** typing, formatting, width and layout choices render a draft on the PDF page. Amber outlines mark nearby text/artwork affected; purple outlines show following text moving. Preview never writes document bytes or history. Cancel restores the original view; Apply uses the same preparation engine.
- **OCR correction:** expand **Review recognised words and source boxes**. Correct words individually, filter uncertain words, jump to the next uncertain word, and adjust source-lettering boxes by dragging/resizing or entering coordinates. **Match original appearance** compares the local Helvetica/Times/Courier families and emphasis against the source ink. Fonts/backgrounds remain estimates.
- **Object controls:** drag an empty page area to select fully enclosed objects; Shift/Ctrl/Cmd adds to the selection. Group/Ungroup persists PDFCreator group membership in the PDF without flattening members. Arrange objects relative to selection bounds, the first selected object or the page; distribute spacing and match widths/heights/sizes. Grouped copies remain grouped. Replacing a text member can make that member independent.
- **Text layout:** choose **Keep layout**, **Fit text into box**, or **Move following text in this column**. Fit reduces the requested sizes only as needed, with a 4 pt lower limit. Column reflow shifts following text on the same page, including pulling it up after deletion. It stops at artwork/table rules, another column and the page edge; rotated text can use Fit. Reflowing additional OCR regions requires confirmation because their words and formatting are reconstructed from recognition.

## Direct edit for outlined and scanned text — 1 November 2026

Choose **Edit → Direct edit**. A page with drawings or scans and no editable text is recognised automatically. On mixed pages or later pages, choose **Recognise text for editing** at the top right of the page. Recognition uses the embedded English engine and leaves the PDF unchanged.

Click a recognised region to review and change its words, font, size, colour and emphasis in the same editor. Applying replaces the selected visible lettering with editable, searchable PDF text. Other recognised regions remain selectable, and one Undo restores the exact previous PDF. The replacement supports normal Direct edit afterwards. Table columns are separated at large gaps; the surrounding page is retained.

Recognition can misread words. Fonts, spacing and solid background colours are estimates; complex backgrounds need careful visual review. This is region-based English editing, not reconstruction of an original Word document. Searchable OCR remains available separately and retains the original visible page.

## Confirm overlapping text edits — 1 November 2026

When Direct edit formatting or reflow would overlap nearby text, the app asks **Apply edit with overlapping text?** Choose **Apply anyway** to save the edit, or **Cancel** to keep your formatted draft open. Nearby text stays in place and can be obscured by the new layout. Each edit requires its own confirmation, and one Undo restores the original PDF.

## Multiple object selection and resizable panes — 1 November 2026

In **Edit → Select objects**, use Ctrl/Cmd-click or Shift-click to add or remove objects on the same page. The properties pane also offers **Click to add/remove objects**. Each selected object is outlined. Move, resize, rotate, align, duplicate or delete the selection together; each applied group operation is one undo step. Select a content group or its internal text separately to avoid changing the same content twice.

Object properties now starts at 260 px, with a compact two-column geometry grid and horizontal action buttons. Opening an object from **Objects & layers** provides a **← Back** button in the pane header. Back preserves unapplied changes until you choose to keep editing or discard them.

Drag the left edge of any right-hand properties pane or docked tool-settings popup to adjust its width. The divider also supports arrow keys (Shift for larger steps), Home/End, and double-click to reset. Width preferences are saved on this device.

## Inline editing and optional helper bar — 1 November 2026

Direct edit now shows fonts, sizes, colours and emphasis in the editable text box. Formatting controls appear first, and the separate formatting preview is removed. Text selection, plain-text paste, line breaks, composition input and draft undo/redo are retained. Apply still uses the verified native PDF writer and embedded-font Unicode fix.

Use the helper bar’s × button to hide it. Restore it from **⋯ → Show helper bar**. The preference is saved on this device and hiding the bar releases its reserved space.


Fixed edited text reopening as glyph codes or gibberish with embedded subset fonts. The PDF writer previously tried to reconstruct Unicode from the font program's cmap, which can be absent or differ from the source PDF's text encoding. Edited overlays now carry an explicit glyph-to-Unicode map derived from the actual text being written. The prepared overlay is saved, reopened and checked before removing any source text. Existing glyph mappings take priority over a font's fallback cmap.

The shared fix covers line, paragraph and chunk Direct edit, Find and replace, and native text move/duplicate. Original fonts, appearance, layout, colours and formatting are retained. Ambiguous glyph aliases or unsupported encodings fail before the source text is removed. Full Unicode destinations use UTF-16, including supplementary characters where the source font supports them.

Added exact-content regression checks for repeated edits, reopening the same editor, save/reopen, undo/redo and recovery. Original tests also exercise Add text/rich formatting, Replace text, selected-text editing, page decorations, annotations, search/extraction and OCR. The package retains the spreadsheet form generator and workspace improvements from repository commit db29be1.

This prevents new corruption. For a PDF already saved with broken character mappings, use Undo/History or reopen an unmodified original and reapply the edit. The app does not guess at lost characters or silently rewrite an already-corrupted PDF.

# Workspace and spreadsheet forms — 31 October 2026

Forms now includes **Generate from XLSX / CSV**. Choose the worksheet/header row, map columns or fixed values to native form fields, preview each record and generate named PDFs in a ZIP with a CSV report. Outputs can retain interactive fields or be flattened. Required values, choices, character limits, cached formula results and duplicate filenames are handled explicitly. Cancellation and generation preserve the open template and history. Spreadsheet processing stays offline in an embedded worker.

The editor now keeps the active tool and its next gesture visible above the document. Done returns to reading/selection. Pin frequently used tools with a star; function search places favourites and recently used tools first, and Home offers quick access. These preferences remain local to this browser.

Select text on one page to copy, highlight, underline, open the existing text editor or add a hyperlink. Image properties now provide quick Crop/Adjust actions, image replacement and links. Replacing an image preserves other uses of a shared resource and supports a single undo step.

Dialogues retain visible action buttons while scrolling, keep keyboard focus inside the dialogue and restore it on close. Page-range fields add All pages, Current page and a page count. The background is dimmed without blur.

All three runnable HTML names contain the same build. The embedded source export and accompanying source ZIP contain identical file contents. The Word dependency source archive, current guide, third-party notices and release checksums accompany the app.

Existing tools, local projects and the legacy `.pdfpro` workspace format remain supported. The change introduces no shared review service or document upload. See `VALIDATION.txt` for checks and browser-verification limits.

Typography consistency — 2 November 2026
Shared interface sizes: 12 px controls and body text, 11 px help/labels, 10 px metadata. Equivalent tool tiles, dialogue controls and inspector actions share these roles. Home help/recent metadata no longer inherit an oversized paragraph style. Heading/icon hierarchy and PDF text/field preview formatting remain independent. typography-test.mjs verifies 109 cascade assertions in a controlled DOM; live browser layout is not certified.

Home shortcuts — 2 November 2026
Each Your tools shortcut has a separate, labelled remove button. Removing clears its favourite and recent entries, works without a PDF and retains keyboard focus. Removal persists locally; function search can pin it again. home-tools-test.mjs verifies 30 preference/DOM/recovery assertions.

Automatic tools dock — 2 November 2026
Choosing a feature docks its category tools on the right. Closing the dock retains the selected feature; the left category remains highlighted and names the active feature. Browsing another category is distinguished from the active category. Selecting another feature, Done or same-feature deselection updates this state. Shared tools retain the category from which they were selected, including tab switches and local recovery. auto-dock-test.mjs checks 97 selection, navigation, dismissal and recovery assertions in source and compiled app.

On-page text editing — 2 November 2026
Direct edit and added text boxes are typed directly on the PDF page, with formatting/layout/Apply/Cancel controls in a workspace bar above it. Text comments and stamps use the same on-page rich editor. Source font/colour/size and selected-word formatting continue through the existing native writers. The editable surface follows PDF coordinates and zoom; the toolbar remains accessible while scrolling. Apply is one undo step; Cancel removes the editing surface without changing PDF bytes. on-page-text-test.mjs checks 52 geometry, keyboard, formatting, saved-PDF, rich-text and recovery assertions in source and compiled app. Native AcroForm field property editing keeps its existing dedicated controls. Tests use native engines and controlled DOM, not a live-browser layout certification.

PDFCreator 3.0.1 — 2 November 2026
The on-page text editing release is designated 3.0.1. Its standalone HTML, embedded release metadata and version.json share the same new build ID and version. Hosted tabs recognise the new build on their next visible/online check (normally every 30 minutes), or through About > Check for updates. Detection does not reload or discard work automatically. Downloaded file:// copies retain offline behaviour and must be replaced manually.

OCR action and popup placement — 2 November 2026

The pastel red Recognise text for editing button stays below workspace popup layers. When a function/settings popup covers its usual page position, the action moves into clear space within the page and visible viewport. Closing or resizing the popup restores the usual position where possible. A completely covered control is temporarily hidden until room returns. Placement reacts to scrolling, resizing and popup changes without polling or changing PDF bytes.

Form control deletion, signature styling and privacy — 2 November 2026

Radio buttons and other supported form fields are now selectable in Edit > Select objects and Objects & layers. Delete selected (or keyboard Delete) removes selected widget instances, retaining unselected radio options and shared fields. A radio selection also offers Delete radio group, with confirmation covering options on other pages. Edit form fields has the same individual/group deletion controls. Empty field branches and calculation references are cleaned up, retained radio values/export labels stay aligned, and each operation is one Undo step. Printed option labels are separate PDF text and can be selected/deleted separately. Read-only/locked fields are protected.

Protect & sign > Visual signature now offers Colour and Line thickness (0.5–16), which redraw existing strokes and the live preview. Bold typed name changes typed lettering weight. Typed and drawn signatures use the chosen colour, retain transparent PNG backgrounds and preserve normal placement/Undo. Imported PNG/JPEG signatures retain their original pixels and bypass styling.

The ? > About popup includes: All information is processed locally on your device. No files are stored or uploaded to any cloud server or database. Your information remains yours.

# Direct edit character mapping fix — 31 October 2026

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

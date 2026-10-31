# Direct edit character mapping fix — 31 October 2026

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

Move attachment icons - 2 November 2026

In Read & select, drag a placed paperclip icon to move it within its PDF page. A destination preview follows the pointer; release to save its new position. A short click still opens the attachment preview/download menu. Movement preserves icon size and the original embedded file, stays inside the page bounds, and is one Undo step. Escape, scrolling, zoom changes or a cancelled pointer discard the drag. Unlock icons in Objects & layers before moving them.

Page attachment icons - 2 November 2026

Attachments are embedded inside the PDF. Use View > Attachments, choose a file (up to 50 MB), choose location, then click a PDF page to place its standard Paperclip icon. Nothing is embedded until the icon is placed. Done or Escape cancels placement. Existing embedded files without a page icon have a Place icon action. Filenames are kept unique so adding another file does not replace an earlier attachment.

In Read & select, click an icon for a local text or raster-image preview, Open PDF in a separate document tab, or Download. HTML, SVG and scripts are displayed as plain text. Other formats can be downloaded to open in an application on the device. Text previews show up to 1 MB; downloads retain the complete original file. No attachment is opened automatically. Icons remain in saved PDFs; external PDF viewer support for opening attachments varies. Move or delete an icon using Edit > Select objects or Objects & layers. Deleting an icon retains the file in the PDF attachment list. Adding a file and icon is one Undo step.

# Direct edit character mapping fix — 31 October 2026

## Website update notifications — 1 November 2026

Hosted HTTP/HTTPS copies check a small same-origin version.json after startup and every five minutes when online, including inactive tabs. Downloaded file:// copies check the official repository manifest. No PDF/document data or credentials are sent. Browsers can throttle or suspend background pages; an overdue check runs when the page resumes, is restored, regains focus or reconnects. Heavy PDF jobs defer checking until idle; failed requests time out after eight seconds and retry with backoff. Checks do not open modal dialogues, steal focus, or reload automatically.

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
The on-page text editing release is designated 3.0.1. Its standalone HTML, embedded release metadata and version.json share the same new build ID and version. The original 3.0.1 checker used a visible-tab interval. The current checker runs in active and inactive tabs every five minutes when online, and ? > Check for updates remains available. Detection does not reload or discard work automatically. Downloaded file:// copies retain offline behaviour and must be replaced manually.

OCR action and popup placement — 2 November 2026

The pastel red Recognise text for editing button stays below workspace popup layers. When a function/settings popup covers its usual page position, the action moves into clear space within the page and visible viewport. Closing or resizing the popup restores the usual position where possible. A completely covered control is temporarily hidden until room returns. Placement reacts to scrolling, resizing and popup changes without polling or changing PDF bytes.

Form control deletion, signature styling and privacy — 2 November 2026

Radio buttons and other supported form fields are now selectable in Edit > Select objects and Objects & layers. Delete selected (or keyboard Delete) removes selected widget instances, retaining unselected radio options and shared fields. A radio selection also offers Delete radio group, with confirmation covering options on other pages. Edit form fields has the same individual/group deletion controls. Empty field branches and calculation references are cleaned up, retained radio values/export labels stay aligned, and each operation is one Undo step. Printed option labels are separate PDF text and can be selected/deleted separately. Read-only/locked fields are protected.

Protect & sign > Visual signature now offers Colour and Line thickness (0.5–16), which redraw existing strokes and the live preview. Bold typed name changes typed lettering weight. Typed and drawn signatures use the chosen colour, retain transparent PNG backgrounds and preserve normal placement/Undo. Imported PNG/JPEG signatures retain their original pixels and bypass styling.

The ? > About popup includes: All information is processed locally on your device. No files are stored or uploaded to any cloud server or database. Your information remains yours.

Workspace interface improvements — 3 November 2026
Selected images, shapes/objects, annotations and native form controls now have quick contextual properties in the same top-of-workspace location as text formatting. Controls delegate to the existing image/object/field editors and keep their Apply, Cancel, validation and Undo behaviour. More properties opens the complete inspector; Crop and Adjust reach the existing image controls.

Tool popups reserve canvas space beside the PDF on wider screens and below it on narrower screens. Duplicate tool settings hide while a contextual editor is active. Text/selection bars, the active-tool guide, page toolbar and inspector reserve their own space. Page content remains scrollable, and popup menus are bounded to the viewport.

Focus mode is the corner icon beside the header help/search controls. Ctrl+Alt+F toggles it; Escape restores the workspace after open menus/dialogues are dismissed. It temporarily hides navigation, tool docks and page previews while keeping document/page/context controls available. It does not alter saved navigation settings or PDF bytes. More properties restores the normal workspace. Focus mode is intentionally not restored after reopening the app.

More document actions (the ellipsis) includes Interface density: Compact (existing 12/11/10 px interface roles), Standard (13/12/11) and Comfortable (14/13/12). Density persists with workspace preferences and never changes PDF zoom or PDF text sizes.

Direct edit uses browser caret hit testing near the clicked word when available, and shows an original-box/page-edge overflow indicator on the document and in the formatting bar. Existing layout/fit choices and native writer validation remain authoritative. IME composition Enter does not apply a draft.

Document tabs can be dragged into order or moved with Alt+Shift+Left/Right. Right-click or Shift+F10 opens Rename, Close tab, Close other tabs and Close tabs to the right. Names and tab order persist locally. Closing retains locally saved projects in the library, with the existing failed-save confirmation. These actions do not rewrite PDF content.

Shared SVG header/tab controls, consistent radii/borders/shadows, maroon selection states, labelled keyboard hints and visible focus rings refine the interface. Buttons retain at least 24 px pointer targets in the affected control areas; resize handles use a 24 px target around a small mark. Reduced-motion preferences suppress decorative transitions.

Validation: workspace-polish-test.mjs passes 80 source and compiled assertions for contextual image/object/field edits, native annotation selection, Apply/Cancel/Undo, side/bottom reservations, Focus, density/PDF independence, caret/overflow/IME, drag and keyboard tab order, menus/renaming/closing, accessible hints and IndexedDB recovery. Affected image (58), field (52), object workspace (61), page toolbar (62), navigation (63), automatic dock (97), typography (109), text formatting (21), on-page text (52), workspace UX (49), update UI (48) and OCR Direct edit (51) checks pass. Controlled DOM/native-engine checks do not certify live-browser layout or screen-reader conformance. The historic tabs-interactions test predates automatic docking; current navigation is covered by auto-dock and workspace-polish tests.

OCR control placement also recognises the new selection bar and tab menus as obstacles. The source and compiled ocr-control-placement-test.mjs regression passes 28 checks, including clear-space restoration and unchanged PDF/history.

Automatic content selection — 4 November 2026
Automatic tool selection is enabled by default. A stationary click on supported native text, an added text box, a shape or an annotation selects its object and highlights Select objects. Clicking an image selects Edit images and opens its existing adjustment controls. Clicking a supported interactive field selects Edit form fields. Double-clicking supported native text, an added text box, a text comment or a stamp opens its corresponding on-page text editor and highlights Direct edit.

The double-click remembers the first clicked item and PDF position so opening/docking properties cannot move the intended target away from the second click. It also handles native click/dblclick sequences and the changed selection overlay without opening two editors. Fast object dragging still uses the normal move/resize workflow. Ctrl/Cmd-click and Shift-click retain object multi-selection; dragging words in Read & select retains text selection/copying. Existing link and attachment actions keep their normal controls.

Explicit drawing, markup, placement, redaction and manually chosen Direct edit modes retain their gestures. Locked/read-only objects and unapplied drafts are protected. Detection is local and cached per PDF revision/page; selecting changes no PDF bytes or Undo history. Applied edits keep the existing writers, signature consent, validation, Undo and autosave. Scanned/unsupported lettering still needs the existing OCR or replacement tools.

More document actions includes Automatic tool selection. Switch it off to restore manual tool routing; the preference persists locally. The Read & select helper describes the active click behaviour. No browser project database or user PDF was accessed while building this update.

Validation: context-selection-test.mjs passes 84 source/compiled assertions with actual PDFs and pointer sequences, covering text/image/shape/field selection, native and rich direct edits, a page moving after the first click, quick object dragging, normal word dragging, manual tools, multi-selection, drafts/locks, zoom/later pages, Undo, preference recovery and unchanged bytes/history. Existing affected image (58), object (61), form-field (52), on-page text (52), workspace (80 and 49), attachment (45) and attachment-drag (65) checks pass. The image regression now expects the requested automatic Edit images highlight. Controlled DOM/native-engine checks are not a live-browser visual certification.

Text width resizing and alignment — 4 November 2026
Selected text containers now have side handles for changing the writing width (left/right for horizontal text; top/bottom for quarter-turn text). Drag the side, not the body, to resize; dragging the body still moves the object. Widening brings wrapped words back onto earlier lines and contracts unused text height. Narrowing rewraps and grows the frame so all content remains present. Corner resizing retains its separate minimum-height behaviour. Text sizes, colours and native font programmes are retained.

Text alignment is a separate control in object properties and the contextual top bar: Keep original, Left, Centre and Right. It changes line alignment inside the box; Align to page still moves the whole selection. Native multiline alignment is inferred from shared line edges/centres and is retained in saved reflow metadata; added rich paragraphs retain their stored alignment. Imported FreeText annotations retain native Q alignment. The on-page Direct editor follows the resized paragraph's alignment.

The page preview now updates periodically while a resize is held. It uses the same preparation path as the committed edit, with the latest drag geometry retained independently of the auto-fitted preview frame. Native/rich rotated text keeps the intended writing edge, and the saved frame matches the preview. Pointer cancellation restores the prior geometry. Each completed drag is one normal Undo step; local recovery retains the edited PDF. Existing overlap confirmation and page-boundary checks remain in place.

Validation: resize-reflow-test.mjs passes 98 source/compiled assertions for live drag previews, wider/narrower native and rich text, Left/Centre/Right transitions, fixed font sizes/colour, native and rich rotations, imported comments, cancellation, saved alignment, on-page typing, recovery and exact Undo. Affected text-box sizing (68), native reflow/pixels (145), reflow interactions (43), selected text formatting (21), object workspace (61), contextual selection (84), workspace polish (80) and on-page text (52) checks pass. These are controlled DOM/native-engine checks, not live-browser visual certification. Existing unsupported/scanned text still needs the corresponding OCR or replacement workflow.


Versioned background updates and compact top toolbars — 4 November 2026
PDFCreator is now 3.0.2. The ? heading, version details, app API, embedded metadata and version.json use package.json as their single version source. Each published app commit reserves exactly one patch above the latest repository version through release-version.mjs; rebuilding that same release keeps the reserved version. See RELEASING.md in the source kit. Older manifests cannot offer a downgrade.

A small manifest is checked after startup and every five minutes online, without requiring the ? panel or an active/visible tab. Focus, resume, page restoration and reconnection schedule overdue checks without bypassing the cooldown. Browsers can throttle/suspend background pages; the checker catches up on waking instead of trying to prevent suspension. Failed checks remain non-blocking and retry with backoff. No PDF data or credentials are transmitted.

Hosted copies check their deployment's version.json. Downloaded file copies check only the official public repository manifest; Download update opens the official updated HTML download on explicit user action and never navigates the existing local workspace. Apply unfinished edits, replace the HTML at its existing location, then reload to retain access to the same browser projects. Hosted Update now retains verified local saving, draft consent and failure backups; neither form of detection forces a reload.

Top object/image/form and on-page text toolbars use smaller desktop controls and tighter padding/gaps. Action names and field labels remain visible with tooltips, accessible names, focus outlines and larger touch targets. Density preferences still offer larger controls; the PDF font size and zoom are unchanged.

Validation: update-checker-test.mjs passes 61 deterministic assertions, website-updates-ui-test.mjs passes 63 source/compiled assertions, and release-version-test.mjs passes 20 assertions. Existing workspace polish (80) and on-page editing (52) checks pass. These use bounded mocked update responses, controlled DOM and native PDF processing; they do not certify browser-specific background timer policies or live layout.


PDFCreator 3.0.3 — 4 November 2026
Removed duplicate labels beneath buttons on mouse/touch focus. Keyboard hints are limited to icon-only controls and clear immediately on pointer interaction. Labelled top-toolbar actions no longer receive generated duplicate tooltips. The properties shortcut is now labelled More; its existing behaviour is unchanged.
Validation: workspace-polish-test.mjs passes 86 source/compiled assertions, including pointer versus keyboard focus, labelled controls and hint dismissal. On-page text editing retains 52 passing source/compiled checks. These are controlled DOM/native-engine checks rather than live-browser visual certification.


PDFCreator 3.0.4 — 4 November 2026
Images, object/annotation selections and interactive form fields now have one canonical properties editor above the PDF. The former quick-toolbar clones and duplicate right-side properties view have been replaced with the original editor controls, organised into labelled groups. Common size, text and actions stay visible. More expands position, rotation, arrangement/grouping, selection settings, image crop/preview/appearance, replacement/link actions and help within the same top surface. Nothing opens a second right properties pane.

Image Crop and Adjust reveal and focus their existing controls. Form values, checkboxes/choices, typography, deletion and next/previous navigation remain available. Form editors detach from their old on-page popup positioning so scrolling the original field offscreen does not hide the top editor. Direct/native/rich text formatting is grouped into Text, Style and Paragraph controls, while editing stays on the PDF. No controls are cloned and no new PDF mutation path is introduced.

The top surface reserves document height rather than width, wraps its groups and limits expanded content height with scrolling. More retains drafts, remains usable in Focus mode, and never restores a side duplicate. Apply, Cancel, discard protection, Back to Objects & layers, atomic edits and Undo/recovery are retained. Nonduplicated panels such as History, Changes review, Forms assistant and Objects & layers keep their existing single side panel.

Validation: top-properties-test.mjs passes 118 source/compiled assertions for canonical control identity/counts, width recovery, More, image crop/adjustments, object transforms, field values and next navigation, scrolling, Focus, Back, native/rich grouping, draft guards and exact Undo. Affected source checks pass: image interactions 58; object workspace 61; form fields 52; field deletion 28; experience panels 59; Changes review 54; on-page text 52; selected formatting 21; contextual selection 84; text resize/reflow 98; workspace polish 86; safe update UI 63. Tests use synthetic PDFs, native processing and controlled DOM. No user browser storage was accessed; live-browser visual layout is not certified.


PDFCreator 3.0.5 — 4 November 2026
Corrected top toolbar alignment and horizontal use. Properties containers stretch across their available workspace instead of centring at intrinsic width. Each primary row separates a flexible controls area from a right-aligned action rail. Groups use shared caption, label and control tracks, so input borders, style controls and layout toggles align horizontally. Independent control groups use the available row width before wrapping; narrow spaces retain horizontal access rather than stacking action buttons.

Action order is consistent across original object, image, field, native text and rich text controls: Apply first, Duplicate when available, deletion actions, then Clear/Cancel. The original controls and form ownership are retained. Native and rich text footers now contain only action buttons; fit options remain with layout controls, and source-font details appear inside Layout options. Initial/ready boilerplate no longer occupies a permanent status row. Meaningful preview progress, affected-layout notices, errors and overflow guidance remain visible.

Validation: top-properties-test.mjs passes 162 source/compiled assertions, covering canonical control identity, action ownership/order/placement, stretched properties, inline options, native edits, crop/adjustments, navigation, drafts and exact Undo. Affected source checks pass for workspace polish 86, on-page editing 52, selected text formatting 21, contextual selection 84 and field deletion 28. Tests use synthetic PDFs, native engines and controlled DOM, not live-browser visual certification.


PDFCreator 3.0.6 — 5 November 2026
Implemented all twelve UI/workflow refinements: comment/reply draft ownership and safe close; staged organiser close protection and selection-aware commands; separate local-save/PDF-download indicators and full project backup; prepared-export continuity through Changes review and settings; shared Current/Selected/All/Custom scope; explicit signature sources with image preview; complete page-grouped OCR issue navigation; searchable/filterable form-data mapping; explicit Home actions and persistent library context; common placement diagrams, unit conversion and appearance-only presets; selected-page/resolution print and image export; compact consistent dialogs/tiles. Canvas priority defaults to compact navigation/previews and can be disabled.
Original controls, native PDF writers, Undo, local recovery and password safeguards remain. Presets exclude text, page ranges, passwords and document content. Pending redaction content is identified before print/image output. Export settings/results remain in memory only for the same document revision.
Checks: dialog drafts 85; scope/placement 44; library state 36; signature/OCR/form workflow helpers 55; integrated Home/canvas/export/selected-print/backup 19; signature pixel/style 28; form generation 42; top properties 162; on-page editing 52. Synthetic PDFs, native rendering and controlled DOM are used; no user browser projects accessed, no live-browser visual certification claimed.


PDFCreator 3.0.7 — 6 November 2026
Fixed Home → Open files incorrectly treating its own click as an operation in progress. The synchronous file-picker launcher is separate from the guarded asynchronous import. Existing PDFs do not need to be saved, closed or deselected before opening additional PDFs in independent tabs. Retains edited bytes, per-tab Undo, page position, selected tool and pending redactions. Actual in-flight writes and unapplied drafts retain their existing ownership safeguards.
Validation: open-files-ui-test.mjs passes 18 source/compiled assertions through the actual picker entry, multiple uploads, edited-tab preservation, independent editing, picker cancellation/retry, Create → Open PDF and in-flight write protection. ui-completion-test.mjs passes 19 source/compiled assertions. Controlled DOM and synthetic PDFs; no user documents or browser projects accessed.


PDFCreator 3.0.8 — 6 November 2026
Implemented UI refinements 1–7.
1. Native/rich text, image, object and form-field drafts remain with their owning document tabs. Switch tabs, open another PDF or return Home without applying/cancelling first; return to resume the draft. Draft badges distinguish unapplied work. Closing a Draft tab asks before discarding it. Drafts are session memory: apply them before browser reload/close to retain them in local recovery.
2. Bulk OCR and compressed PDF preparation run as document-owned background tasks. One heavy task runs at a time while other PDFs remain editable. Source tabs show progress/ready badges; click a badge or More → Tasks (also in function search) for cancellation and results. Review/apply results explicitly, or open result copies. New edits, drafts and pending redactions are never silently overwritten. Tasks/results stay in memory until used/dismissed; browser exit/update protection covers them. OCR has a separate local recogniser; no PDF content is uploaded.
3. The canonical top toolbar uses a steady horizontal controls row and a consistent right-hand action rail. Overflow controls scroll horizontally; advanced options open under More without increasing reserved canvas height. Original controls and form ownership are retained.
4. Automatic selection outlines/names the hovered Text, Image, Shape or Field. Alt-click cycles overlapping items; right-click overlapping content for the keyboard-accessible Select item menu. Locks, explicit drawing tools and text-selection gestures remain respected.
5. Image/object movement shows temporary page-centre, page-edge, 20 mm reference-margin and object-alignment guides. Snapping uses screen-scaled tolerance; Alt bypasses it. Arrow keys nudge 1 pt, Shift+Arrow 10 pt. Guides disappear on completion/cancellation.
6. Undo/Redo tooltips and accessible labels name their actual history operations.
7. Save named text, comment, shape and stamp appearance presets in tool settings or text toolbars. Recent colour swatches, named selection, replacement and deletion are compact. Up to 30 device-local presets contain appearance only, never document text/passwords. Native Direct edit maps shared fonts to its supported Helvetica/Times/Courier families.
Validation uses synthetic PDFs, native engines, embedded offline workers and controlled DOM. Checks: integrated seven refinements 48; real background OCR 14; queue/styles 16; top properties 162; contextual selection 84; on-page text 52; completion UI 19; open files 18; image interactions 58; object workspace 61; compression UI 42; OCR layer 5; safe updates 63. No user documents or browser project storage accessed; no live-browser visual certification claimed.


PDFCreator 3.0.9 — 7 November 2026
Implements requested refinements 1, 2, 5, 7 and 8.
1. Native/rich text, image, object and form-field drafts are saved locally with their owning PDF revision, including parked tabs. After restart, Resume edit / Discard draft / Later lets the user decide. Draft persistence never applies changes to PDF bytes. Storage failures stay visible and keep the editor open. Explicit discard on close/update clears stored recovery. Password inputs and file pickers are excluded; recovery requires working browser storage and does not retain background task results.
2. Canonical top toolbars prioritise text/font/size/colour and Apply. Secondary style, paragraph, image, navigation and named-style controls move to More below 820 px; duplicate/delete actions move there below 600 px. Controls are moved, never cloned, and return to their original positions when space grows.
5. The current-page footer reports Editable text, Recognised text, Image-only page, Limited text editing or No editable text, with an explanation and relevant edit/recognise/add action. Classification is cached by PDF revision/page and never starts OCR automatically. Font changes and OCR estimates explain possible layout differences.
7. Attachment menus support Open/preview, Download, Move icon, Remove this icon and Remove embedded file, with all page locations listed. Icon-only deletion retains the file. Full deletion removes its page icons, all matching name-tree aliases and ordinary PDF/page AF associations. Locked icons protect full removal. Each change supports Undo and preserves unrelated attachments. Right-click opens the same menu; arrow keys move icons, Shift uses 10 pt.
8. Escape closes an editor More panel before dismissing the editor and returns focus to its toggle. Attachment keyboard movement preserves focus. Image/object resize corners support arrow keys and Shift increments; pane-drag cancellation restores the initial width. Coarse-pointer controls and invisible handle/field hit areas are larger, with visible keyboard outlines in light/dark themes.
Validation: five-refinements-test.mjs, 65 assertions in source and compiled app for real local recovery/restart, active/parked draft ownership, local-save failure, apply/Undo, discard/close/update, canonical responsive controls, Escape/focus, page capability and attachment actions; attachment-removal-test.mjs, 17 real-engine checks for shared/hidden/locked icons, aliases, AF cleanup, stale targets, orphan retention and unchanged page text. Existing storage 52, persistence/navigation 64, prior seven refinements 48, top properties 162, on-page text 52, image interactions 58, object workspace 61, safe updates 63 and attachment movement 65 pass. Tests use synthetic PDFs, native engines and controlled DOM. No user PDF contents or browser project storage accessed; live browser visual layout is not certified.

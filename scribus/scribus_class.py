Help on module scribus:

NAME
   scribus - Scribus Python interface module

FILE
   (built-in)

DESCRIPTION
   This module is the Python interface for Scribus. It provides functions
    to control scribus and to manipulate objects on the canvas. Each
    function is documented individually below.

    A few things are common across most of the interface.

    Most functions operate on frames. Frames are identified by their name,
    a string - they are not real Python objects. Many functions take an
    optional(non-keyword) parameter, a frame name.
    Many exceptions are also common across most functions. These are
    not currently documented in the docstring for each function.
    - Many functions will raise a NoDocOpenError if you try to use them
    without a document to operate on.
    - If you do not pass a frame name to a function that requires one,
    the function will use the currently selected frame, if any, or
    raise a NoValidObjectError if it can't find anything to operate
    on.
    - Many functions will raise WrongFrameTypeError if you try to use them
    on a frame type that they do not make sense with. For example, setting
    the text color on a graphics frame doesn't make sense, and will result
    in this exception being raised.
    - Errors resulting from calls to the underlying Python API will be
    passed through unaltered. As such, the list of exceptions thrown by
    any function as provided here and in its docstring is incomplete.

    Details of what exceptions each function may throw are provided on the
    function's documentation, though as with most Python code this list
    is not exhaustive due to exceptions from called functions.

CLASSES
   __builtin__.object
       ImageExport
        PDFfile
        Printer
    exceptions.Exception(exceptions.BaseException)
       ScribusException
           NameExistsError
            NoDocOpenError
            NoValidObjectError
            NotFoundError
            WrongFrameTypeError

    class ImageExport(__builtin__.object)
    |  Image export
     |
     |  Class ImageExport() provides the bitmap graphics exporting
     | for Python scripting as you know it from Export/Save as Image
     |  menu. See related class PDFfile() and procedure savePageAsEPS().
     |  Example:
     |  i = ImageExport()
     |  i.type = 'PNG'  # select one from i.allTypes list
     |  i.scale = 200  # I want to have 200%
     |  i.name = '/home/subik/test.png'
     |  i.save()
     |
     |  two last lines should be replaced with:
     |  i.saveAs('/home/subik/test.png')
     |
     |  Methods defined here:
     |
     |  __init__(...)
     |      x.__init__(...) initializes x
     see help(type(x)) for signature
     |
     |  save(...)
     |      save() -> boolean
     |
     |      Saves image under previously set 'name'.
     |
     |  saveAs(...)
     |      saveAs('filename') -> boolean
     |
     |      Saves image as 'filename'.
     |
     | ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  allTypes
     |      Available image types. Read only list of strings.
     |
     |  dpi
     |      This value will be used for export as DPI. Read/write integer.
     |
     |  name
     |      Filename of the image. With or without path. Read/write string.
     |
     |  quality
     |      Quality/compression: minimum 1 (poor), maximum 100 (qaulity). Read/write integer.
     |
     |  scale
     |      This is the scaling of the image. 100 = 100 % etc. Read/write iteger.
     |
     |  transparentBkgnd
     |      Enable or disable transparent background.
     |
     |  type
     |      Bitmap type. See allTypes list for more info. Read/write string.
     |
     | ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __new__ = <built-in method __new__ of type object >
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T

    class NameExistsError(ScribusException)
    |  Method resolution order:
     |      NameExistsError
     |      ScribusException
     |      exceptions.Exception
     |      exceptions.BaseException
     |      __builtin__.object
     |
     |  Data descriptors inherited from ScribusException:
     |
     |  __weakref__
     |      list of weak references to the object(if defined)
     |
     | ----------------------------------------------------------------------
     |  Methods inherited from exceptions.Exception:
     |
     |  __init__(...)
     |      x.__init__(...) initializes x
     see help(type(x)) for signature
     |
     | ----------------------------------------------------------------------
     |  Data and other attributes inherited from exceptions.Exception:
     |
     |  __new__ = <built-in method __new__ of type object >
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |
     | ----------------------------------------------------------------------
     |  Methods inherited from exceptions.BaseException:
     |
     |  __delattr__(...)
     |      x.__delattr__('name') <= => del x.name
     |
     |  __getattribute__(...)
     |      x.__getattribute__('name') <= => x.name
     |
     |  __getitem__(...)
     |      x.__getitem__(y) <= => x[y]
     |
     |  __getslice__(...)
     |      x.__getslice__(i, j) <= => x[i:j]
     |
     |      Use of negative indices is not supported.
     |
     |  __reduce__(...)
     |
     |  __repr__(...)
     |      x.__repr__() <= => repr(x)
     |
     |  __setattr__(...)
     |      x.__setattr__('name', value) <= => x.name = value
     |
     |  __setstate__(...)
     |
     |  __str__(...)
     |      x.__str__() <= => str(x)
     |
     |  __unicode__(...)
     |
     | ----------------------------------------------------------------------
     |  Data descriptors inherited from exceptions.BaseException:
     |
     |  __dict__
     |
     |  args
     |
     |  message

    class NoDocOpenError(ScribusException)
    |  Method resolution order:
     |      NoDocOpenError
     |      ScribusException
     |      exceptions.Exception
     |      exceptions.BaseException
     |      __builtin__.object
     |
     |  Data descriptors inherited from ScribusException:
     |
     |  __weakref__
     |      list of weak references to the object(if defined)
     |
     | ----------------------------------------------------------------------
     |  Methods inherited from exceptions.Exception:
     |
     |  __init__(...)
     |      x.__init__(...) initializes x
     see help(type(x)) for signature
     |
     | ----------------------------------------------------------------------
     |  Data and other attributes inherited from exceptions.Exception:
     |
     |  __new__ = <built-in method __new__ of type object >
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |
     | ----------------------------------------------------------------------
     |  Methods inherited from exceptions.BaseException:
     |
     |  __delattr__(...)
     |      x.__delattr__('name') <= => del x.name
     |
     |  __getattribute__(...)
     |      x.__getattribute__('name') <= => x.name
     |
     |  __getitem__(...)
     |      x.__getitem__(y) <= => x[y]
     |
     |  __getslice__(...)
     |      x.__getslice__(i, j) <= => x[i:j]
     |
     |      Use of negative indices is not supported.
     |
     |  __reduce__(...)
     |
     |  __repr__(...)
     |      x.__repr__() <= => repr(x)
     |
     |  __setattr__(...)
     |      x.__setattr__('name', value) <= => x.name = value
     |
     |  __setstate__(...)
     |
     |  __str__(...)
     |      x.__str__() <= => str(x)
     |
     |  __unicode__(...)
     |
     | ----------------------------------------------------------------------
     |  Data descriptors inherited from exceptions.BaseException:
     |
     |  __dict__
     |
     |  args
     |
     |  message

    class NoValidObjectError(ScribusException)
    |  Method resolution order:
     |      NoValidObjectError
     |      ScribusException
     |      exceptions.Exception
     |      exceptions.BaseException
     |      __builtin__.object
     |
     |  Data descriptors inherited from ScribusException:
     |
     |  __weakref__
     |      list of weak references to the object(if defined)
     |
     | ----------------------------------------------------------------------
     |  Methods inherited from exceptions.Exception:
     |
     |  __init__(...)
     |      x.__init__(...) initializes x
     see help(type(x)) for signature
     |
     | ----------------------------------------------------------------------
     |  Data and other attributes inherited from exceptions.Exception:
     |
     |  __new__ = <built-in method __new__ of type object >
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |
     | ----------------------------------------------------------------------
     |  Methods inherited from exceptions.BaseException:
     |
     |  __delattr__(...)
     |      x.__delattr__('name') <= => del x.name
     |
     |  __getattribute__(...)
     |      x.__getattribute__('name') <= => x.name
     |
     |  __getitem__(...)
     |      x.__getitem__(y) <= => x[y]
     |
     |  __getslice__(...)
     |      x.__getslice__(i, j) <= => x[i:j]
     |
     |      Use of negative indices is not supported.
     |
     |  __reduce__(...)
     |
     |  __repr__(...)
     |      x.__repr__() <= => repr(x)
     |
     |  __setattr__(...)
     |      x.__setattr__('name', value) <= => x.name = value
     |
     |  __setstate__(...)
     |
     |  __str__(...)
     |      x.__str__() <= => str(x)
     |
     |  __unicode__(...)
     |
     | ----------------------------------------------------------------------
     |  Data descriptors inherited from exceptions.BaseException:
     |
     |  __dict__
     |
     |  args
     |
     |  message

    class NotFoundError(ScribusException)
    |  Method resolution order:
     |      NotFoundError
     |      ScribusException
     |      exceptions.Exception
     |      exceptions.BaseException
     |      __builtin__.object
     |
     |  Data descriptors inherited from ScribusException:
     |
     |  __weakref__
     |      list of weak references to the object(if defined)
     |
     | ----------------------------------------------------------------------
     |  Methods inherited from exceptions.Exception:
     |
     |  __init__(...)
     |      x.__init__(...) initializes x
     see help(type(x)) for signature
     |
     | ----------------------------------------------------------------------
     |  Data and other attributes inherited from exceptions.Exception:
     |
     |  __new__ = <built-in method __new__ of type object >
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |
     | ----------------------------------------------------------------------
     |  Methods inherited from exceptions.BaseException:
     |
     |  __delattr__(...)
     |      x.__delattr__('name') <= => del x.name
     |
     |  __getattribute__(...)
     |      x.__getattribute__('name') <= => x.name
     |
     |  __getitem__(...)
     |      x.__getitem__(y) <= => x[y]
     |
     |  __getslice__(...)
     |      x.__getslice__(i, j) <= => x[i:j]
     |
     |      Use of negative indices is not supported.
     |
     |  __reduce__(...)
     |
     |  __repr__(...)
     |      x.__repr__() <= => repr(x)
     |
     |  __setattr__(...)
     |      x.__setattr__('name', value) <= => x.name = value
     |
     |  __setstate__(...)
     |
     |  __str__(...)
     |      x.__str__() <= => str(x)
     |
     |  __unicode__(...)
     |
     | ----------------------------------------------------------------------
     |  Data descriptors inherited from exceptions.BaseException:
     |
     |  __dict__
     |
     |  args
     |
     |  message

    class PDFfile(__builtin__.object)
    |  Exporting PDF
     |
     |  Class PDFfile() provides the PDF exporting
     | for Python scripting as you know it from Save as PDF
     |  menu.
     |  Example:
     |  pdf = PDFfile()
     |  pdf.thumbnails = 1  # generate thumbnails too
     |  pdf.file = 'mypdf.pdf'
     |  pdf.save()
     |
     |  Methods defined here:
     |
     |  __init__(...)
     |      x.__init__(...) initializes x
     see help(type(x)) for signature
     |
     |  save(...)
     |      Save selected pages to pdf file
     |
     | ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  aanot
     |      Deprecated. Use 'allowAnnots' instead.
     |
     |  achange
     |      Deprecated. Use 'allowChange' instead.
     |
     |  acopy
     |      Deprecated. Use 'allowCopy' instead.
     |
     |  allowAnnots
     |      Allow Adding Annotations and Fields. Bool value
     |
     |  allowChange
     |      Allow Changing the Document. Bool value
     |
     |  allowCopy
     |      Allow Copying Text and Graphics. Bool value
     |
     |  allowPrinting
     |      Allow Printing the Document. Bool value
     |
     |  aprint
     |      Deprecated. Use 'allowPrinting' instead.
     |
     |  article
     |      Save Linked Text Frames as PDF Articles
     |      Bool value
     |
     |  binding
     |      Choose binding.
     |      0 - Left binding
     |      1 - Right binding
     |
     |  bleedMarks
     |      Create marks delimiting the bleed area.
     |
     |  bleedb
     |      Bleed Bottom
     |      Distance for bleed from the bottom of the physical page
     |
     |  bleedl
     |      Bleed Left
     |      Distance for bleed from the left of the physical page
     |
     |  bleedr
     |      Bleed Right
     |      Distance for bleed from the right of the physical page
     |
     |  bleedt
     |      Bleed Top
     |      Distance for bleed from the top of the physical page
     |
     |  bookmarks
     |      Embed the bookmarks you created in your document.
     |      These are useful for navigating long PDF documents.
     |      Bool value
     |
     |  colorMarks
     |      Add color calibration bars.
     |
     |  compress
     |      Compression switch. Bool value.
     |
     |  compressmtd
     |      Compression method.
     |      0 - Automatic
     |      1 - JPEG
     |      2 - zip
     |      3 - None.
     |
     |  cropMarks
     |      Create crop marks in the PDF indicating where the paper should be cut or trimmed after printing.
     |
     |  displayBookmarks
     |      Display the bookmarks upon opening
     |
     |  displayFullscreen
     |      Display the document in full screen mode upon opening.
     |
     |  displayLayers
     |      Display the layer list upon opening. Useful only for PDF 1.5+.
     |
     |  displayThumbs
     |      Display the page thumbnails upon opening
     |
     |  doClip
     |      Do not show objects outside the margins in the exported file
     |
     |  docInfoMarks
     |      Add document information which includes the document title and page numbers.
     |
     |  domulti
     |      Produce a PDF File for every Page. Bool value
     |
     |  downsample
     |      Downsample image resolusion to this value. Values from 35 to 4000
     |      Set 0 for not to downsample
     |
     |  effval
     |      List of effection values for each saved page.
     |      It is list of list of six integers. Those int has followin meaning:
     | - Length of time the page is shown before the presentation
     |              starts on the selected page. (1-3600)
     | - Length of time the effect runs. (1 - 3600)
     |                      A shorter time will speed up the effect,
     |                      a longer one will slow it down
     | - Type of the display effect
     |                      0 - No Effect
     |                      1 - Blinds
     |                      2 - Box
     |                      3 - Dissolve
     |                      4 - Glitter
     |                      5 - Split
     |                      6 - Wipe
     | - Direction of the effect of moving lines
     | for the split and blind effects.
     |                      0 - Horizontal
     |                      1 - Vertical
     | - Starting position for the box and split effects.
     |                      0 - Inside
     |                      1 - Outside
     | - Direction of the glitter or wipe effects.
     |                      0 - Left to Right
     |                      1 - Top to Bottom
     |                      2 - Bottom to Top
     |                      3 - Right to Left
     |                      4 - Top-left to Bottom-Right
     |
     |  embedPDF
     |      Export EPS and PDFs in image frames as embedded PDFs. This does * not* yet take care of colorspaces, so you should know what you are doing before setting this to 'true'.
     |
     |  encrypt
     |      Use Encription. Bool value
     |
     |  file
     |      Name of file to save into
     |
     |  fitWindow
     |      Fit the document page or pages to the available space in the viewer window.
     |
     |  fontEmbedding
     |      Font embedding mode.
     |      Value must be one of integers: 0 (Embed), 1 (Outline), 2 (No embedding).
     |
     |  fonts
     |      List of fonts to embed.
     |
     |  hideMenuBar
     |      Hide the viewer menu bar, the PDF will display in a plain window.
     |
     |  hideToolBar
     |      Hide the viewer toolbar. The toolbar has usually selection and other editing capabilities.
     |
     |  imagepr
     |      Color profile for images
     |
     |  info
     |      Mandatory string for PDF/X or the PDF will fail
     |      PDF/X conformance. We recommend you use the title of the document.
     |
     |  intenti
     |      Rendering intent for images
     |      0 - Perceptual
     |      1 - Relative Colorimetric
     |      2 - Saturation
     |      3 - Absolute Colorimetric
     |
     |  intents
     |      Rendering intent for solid colors
     |      0 - Perceptual
     |      1 - Relative Colorimetric
     |      2 - Saturation
     |      3 - Absolute Colorimetric
     |
     |  isGrayscale
     |      Export PDF in grayscale
     |
     |  lpival
     |      Rendering Settings for individual colors.
     |
     |      This is list of values for each color
     |      Color values have structure[siii] which stand for:
     |              s - Color name('Black', 'Cyan', 'Magenta', 'Yellow')
     |              i - Frequency(10 to 1000)
     |              i - Angle(-180 to 180)
     |              i - Spot Function
     |                      0 - Simple Dot
     |                      1 - Line
     |                      2 - Round
     |                      3 - Ellipse
     |      Be careful when supplying these values as they
     |      are not checked for validity.
     |
     |  markLength
     |      Indicate the length of crop and bleed marks.
     |
     |  markOffset
     |      Indicate the distance offset between mark and page area.
     |
     |  mirrorH
     |      Mirror Page(s) horizontally
     |
     |  mirrorV
     |      Mirror Page(s) vertically
     |
     |  noembicc
     |      Don't use embedded ICC profiles. Bool value
     |
     |  openAction
     |      Javascript to be executed when PDF document is opened.
     |
     |  outdst
     |      Output destination.
     |      0 - screen
     |      1 - printer
     |
     |  owner
     |      Owner's password
     |
     |  pageLayout
     |      Document layout in PDF viewer:
     |      0 - Show the document in single page mode
     |      1 - Show the document in single page mode with the pages displayed continuously end to end like a scroll
     |      2 - Show the document with facing pages, starting with the first page displayed on the left
     |      3 - Show the document with facing pages, starting with the first page displayed on the right
     |
     |  pages
     |      List of pages to print
     |
     |  presentation
     |      Enable Presentation Effects.Bool value
     |
     |  printprofc
     |      Output profile for printing. If possible, get some guidance from your printer on profile selection.
     |
     |  profilei
     |      Embed a color profile for images. Bool value.
     |
     |  profiles
     |      Embed a color profile for solid colors. Bool value.
     |
     |  quality
     |      Image quality
     |      0 - Maximum
     |      1 - High
     |      2 - Medium
     |      3 - Low
     |      4 - Minimum
     |
     |  registrationMarks
     |      Add registration marks to each separation.
     |
     |  resolution
     |      Resolution of output file. Values from 35 to 4000.
     |
     |  rotateDeg
     |      Automatically rotate the exported pages
     |      Value must be one of integers: 0, 90, 180 or 270
     |
     |  solidpr
     |      Color profile for solid colors
     |
     |  subsetList
     |      List of fonts to subsetted.
     |
     |  thumbnails
     |      Generate thumbnails. Bool value.
     |
     |  useDocBleeds
     |      Use the existing bleed settings from the document preferences. Bool value
     |
     |  useLayers
     |      Layers in your document are exported to the PDF. Only available if PDF 1.5 is chosen.
     |
     |  uselpi
     |      Use Custom Rendering Settings. Bool value
     |
     |  user
     |      User's password
     |
     |  usespot
     |      Use Spot Colors. Bool value
     |
     |  version
     |      Choose PDF version to use:
     |      10 = PDF/X4
     |      11 = PDF/X1a
     |      12 = PDF/X-3
     |      13 = PDF 1.3 (Acrobat 4)
     |      14 = PDF 1.4 (Acrobat 5)
     |      15 = PDF 1.5 (Acrobat 6)
     |
     | ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __new__ = <built-in method __new__ of type object >
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T

    class Printer(__builtin__.object)
    |  Printing
     |
     |  Class Printer() provides printing for Python scripting.
     |
     |  Example:
     |  p = Printer()
     |  p.print()
     |
     |  Methods defined here:
     |
     |  __init__(...)
     |      x.__init__(...) initializes x
     see help(type(x)) for signature
     |
     |  printNow(...)
     |      Prints selected pages.
     |
     | ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  allPrinters
     |      List of installed printers  - -  read only
     |
     |  cmd
     |      Alternative Printer Command
     |
     |  color
     |      Print in color.
     |      True - color  - -  Default
     |      False - greyscale
     |
     |  copies
     |      Number of copies
     |
     |  file
     |      Name of file to print into
     |
     |  mph
     |      Mirror Pages Horizontal
     |      True
     |      False  - -  Default
     |
     |  mpv
     |      Mirror Pages Vertical
     |       True
     |      False  - -  Default
     |
     |  pages
     |      List of pages to be printed
     |
     |  printer
     |      Name of printer to use.
     |      Default is 'File' for printing into file
     |
     |  pslevel
     |      PostScript Level
     |      Can be 1 or 2 or 3    - - Default is 3.
     |
     |  separation
     |      Print separationl
     |               'No'  - - Default
     |               'All'
     |               'Cyan'
     |               'Magenta'
     |               'Yellow'
     |               'Black'
     |      Beware of misspelling because check is not performed
     |
     |  ucr
     |      Apply Under Color Removal
     |      True  - -  Default
     |      False
     |
     |  useICC
     |      Use ICC Profile
     |      True
     |      False  - -  Default
     |
     | ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __new__ = <built-in method __new__ of type object >
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T

    class ScribusException(exceptions.Exception)
    |  Method resolution order:
     |      ScribusException
     |      exceptions.Exception
     |      exceptions.BaseException
     |      __builtin__.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object(if defined)
     |
     | ----------------------------------------------------------------------
     |  Methods inherited from exceptions.Exception:
     |
     |  __init__(...)
     |      x.__init__(...) initializes x
     see help(type(x)) for signature
     |
     | ----------------------------------------------------------------------
     |  Data and other attributes inherited from exceptions.Exception:
     |
     |  __new__ = <built-in method __new__ of type object >
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |
     | ----------------------------------------------------------------------
     |  Methods inherited from exceptions.BaseException:
     |
     |  __delattr__(...)
     |      x.__delattr__('name') <= => del x.name
     |
     |  __getattribute__(...)
     |      x.__getattribute__('name') <= => x.name
     |
     |  __getitem__(...)
     |      x.__getitem__(y) <= => x[y]
     |
     |  __getslice__(...)
     |      x.__getslice__(i, j) <= => x[i:j]
     |
     |      Use of negative indices is not supported.
     |
     |  __reduce__(...)
     |
     |  __repr__(...)
     |      x.__repr__() <= => repr(x)
     |
     |  __setattr__(...)
     |      x.__setattr__('name', value) <= => x.name = value
     |
     |  __setstate__(...)
     |
     |  __str__(...)
     |      x.__str__() <= => str(x)
     |
     |  __unicode__(...)
     |
     | ----------------------------------------------------------------------
     |  Data descriptors inherited from exceptions.BaseException:
     |
     |  __dict__
     |
     |  args
     |
     |  message

    class WrongFrameTypeError(ScribusException)
    |  Method resolution order:
     |      WrongFrameTypeError
     |      ScribusException
     |      exceptions.Exception
     |      exceptions.BaseException
     |      __builtin__.object
     |
     |  Data descriptors inherited from ScribusException:
     |
     |  __weakref__
     |      list of weak references to the object(if defined)
     |
     | ----------------------------------------------------------------------
     |  Methods inherited from exceptions.Exception:
     |
     |  __init__(...)
     |      x.__init__(...) initializes x
     see help(type(x)) for signature
     |
     | ----------------------------------------------------------------------
     |  Data and other attributes inherited from exceptions.Exception:
     |
     |  __new__ = <built-in method __new__ of type object >
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |
     | ----------------------------------------------------------------------
     |  Methods inherited from exceptions.BaseException:
     |
     |  __delattr__(...)
     |      x.__delattr__('name') <= => del x.name
     |
     |  __getattribute__(...)
     |      x.__getattribute__('name') <= => x.name
     |
     |  __getitem__(...)
     |      x.__getitem__(y) <= => x[y]
     |
     |  __getslice__(...)
     |      x.__getslice__(i, j) <= => x[i:j]
     |
     |      Use of negative indices is not supported.
     |
     |  __reduce__(...)
     |
     |  __repr__(...)
     |      x.__repr__() <= => repr(x)
     |
     |  __setattr__(...)
     |      x.__setattr__('name', value) <= => x.name = value
     |
     |  __setstate__(...)
     |
     |  __str__(...)
     |      x.__str__() <= => str(x)
     |
     |  __unicode__(...)
     |
     | ----------------------------------------------------------------------
     |  Data descriptors inherited from exceptions.BaseException:
     |
     |  __dict__
     |
     |  args
     |
     |  message

FUNCTIONS
   applyMasterPage(...)
       applyMasterPage(masterPageName, pageNumber)

        Apply master page masterPageName on page pageNumber.

    changeColor(...)
       changeColor("name", c, m, y, k)

        Changes the color "name" to the specified CMYK value. The color value is defined via four components c = Cyan, m = Magenta, y = Yellow and k = Black. Color components should be in the range from 0 to 255. Note: deprecated, use changeColorCMYK() instead.

        May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified.

    changeColorCMYK(...)
       changeColorCMYK("name", c, m, y, k)

        Changes the color "name" to the specified CMYK value. The color value is defined via four components c = Cyan, m = Magenta, y = Yellow and k = Black. Color components should be in the range from 0 to 255.

        May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified.

    changeColorCMYKFloat(...)
       changeColorCMYKFloat("name", c, m, y, k)

        Changes the color "name" to the specified CMYK value. The color value is defined via four components c = Cyan, m = Magenta, y = Yellow and k = Black. Color components are floating point values between 0 and 100.

        May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified.

    changeColorLab(...)
       changeColorLab("name", r, g, b)

        Changes the color "name" to the specified CIELab values. The color value is defined via three components: L = luminosity, a = green/red, b = blue/yellow. Color components are floating point values with L between 0 and 100, a and b between - 128 and 128.

        May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified.

    changeColorRGB(...)
       changeColorRGB("name", r, g, b)

        Changes the color "name" to the specified RGB value. The color value is defined via three components r = red, g = green, b = blue. Color components should be in the range from 0 to 255.

        May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified.

    changeColorRGBFloat(...)
       changeColorRGBFloat("name", r, g, b)

        Changes the color "name" to the specified RGB value. The color value is defined via three components r = red, g = green, b = blue. Color components are floating point values between 0 and 255.

        May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified.

    closeDoc(...)
       closeDoc()

        Closes the current document without prompting to save.

        May throw NoDocOpenError if there is no document to close

    closeMasterPage(...)
       closeMasterPage()

        Closes the currently active master page, if any, and returns editing to normal. Begin editing with editMasterPage().

    combinePolygons(...)
       combinePolygons()

        Combine two or more selected Polygons

    copyObject(...)
       copyObject(["name"]) -> string

        copies the selected Object(or Selection Group).

    createBezierLine(...)
       createBezierLine(list, ["name"]) -> string

        Creates a new bezier curve and returns its name. The points for the bezier curve are stored in the list "list" in the following order: [x1, y1, kx1, ky1, x2, y2, kx2, ky2...xn. yn, kxn. kyn] In the points list, x and y mean the x and y coordinates of the point and kx and ky meaning the control point for the curve.  The coordinates are given in the current measurement units of the document(see UNIT constants). "name" should be a unique identifier for the object because you need this name for further access to that object. If "name" is not given Scribus will create one for you.

        May raise NameExistsError if you explicitly pass a name that's already used. May raise ValueError if an insufficient number of points is passed or if the number of values passed don't group into points without leftovers.

    createCharStyle(...)
       createCharStyle(...)

        Creates a character style. This function takes the following keyword parameters:

        "name" [required] -> name of the char style to create

        "font" [optional] -> name of the font to use

        fontsize[optional] -> font size to set (double)

        "features" [optional] -> nearer typographic details can be defined by a string that might contain the following phrases comma-seperated(without spaces!):

        -> inherit

        -> bold

        -> italic

        -> underline

        -> underlinewords

        -> strike

        -> superscript

        -> subscript

        -> outline

        -> shadowed

        -> allcaps

        -> smallcaps

        "fillcolor" [optional], "fillshade" [optional] -> specify fill options

        "strokecolor" [optional], "strokeshade" [optional] -> specify stroke options

        baselineoffset[optional] -> offset of the baseline

        shadowxoffset[optional], shadowyoffset [optional] -> offset of the shadow if used

        outlinewidth[optional] -> width of the outline if used

        underlineoffset[optional], underlinewidth [optional] -> underline options if used

        strikethruoffset[optional], strikethruwidth [optional] -> strikethru options if used

        scaleh[optional], scalev [optional] -> scale of the chars

        tracking[optional] -> tracking of the text

        "language" [optional] -> language code

    createCustomLineStyle(...)
       createCustomLineStyle(styleName, style)

        Creates the custom line style 'styleName'.

        styleName -> name of the custom line style to create

        This function takes list of dictionary as parameter for "style". Each dictionary represent one subline within style. Dictionary can have those keys:

               Color [optional] -> name of the color to use (string)

                Dash[optional] -> type of line to use (integer)

                LineEnd[optional] -> type of LineEnd to use (integer)

                LineJoin[optional] -> type of LineJoin to use (integer)

                Shade[optional] -> opacity of line (integer)

                Width[optional] -> width of line (double)

    createEllipse(...)
       createEllipse(x, y, width, height, ["name"]) -> string

        Creates a new ellipse on the current page and returns its name. The coordinates are given in the current measurement units of the document(see UNIT constants). "name" should be a unique identifier for the object because you need this name for further referencing of that object. If "name" is not given Scribus will create one for you.

        May raise NameExistsError if you explicitly pass a name that's already used.

    createImage(...)
       createImage(x, y, width, height, ["name"]) -> string

        Creates a new picture frame on the current page and returns its name. The coordinates are given in the current measurement units of the document. "name" should be a unique identifier for the object because you need this name for further access to that object. If "name" is not given Scribus will create one for you.

        May raise NameExistsError if you explicitly pass a name that's already used.

    createLayer(...)
       createLayer(layer)

        Creates a new layer with the name "name".

        May raise ValueError if the layer name isn't acceptable.

    createLine(...)
       createLine(x1, y1, x2, y2, ["name"]) -> string

        Creates a new line from the point(x1, y1) to the point(x2, y2) and returns its name. The coordinates are given in the current measurement unit of the document(see UNIT constants). "name" should be a unique identifier for the object because you need this name for further access to that object. If "name" is not given Scribus will create one for you.

        May raise NameExistsError if you explicitly pass a name that's already used.

    createMasterPage(...)
       createMasterPage(pageName)

        Creates a new master page named pageName and opens it for editing.

    createParagraphStyle(...)
       createParagraphStyle(...)

        Creates a paragraph style. This function takes the following keyword parameters:

        "name" [required] -> specifies the name of the paragraphstyle to create

        linespacingmode [optional] -> specifies the linespacing mode
        possible modes are:

        fixed linespacing:          0

        automatic linespacing:      1

        baseline grid linespacing:  2

        linespacing[optional] -> specifies the linespacing if using fixed linespacing

        alignment[optional] -> specifies the alignment of the paragraph

        -> left:     0

        -> center:   1

        -> right:    2

        -> justify:  3

        -> extend:   4

        leftmargin[optional], rightmargin [optional] -> specify the margin

        gapbefore[optional], gapafter [optional] -> specify the gaps to the heading and following paragraphs

        firstindent[optional] -> the indent of the first line

        hasdropcap [optional] -> specifies if there are caps (1= yes, 0 = no)

        dropcaplines[optional] -> height (in lines) of the caps if used

        dropcapoffset[optional] -> offset of the caps if used

        "charstyle" [optional] -> char style to use

    createPathText(...)
       createPathText(x, y, "textbox", "beziercurve", ["name"]) -> string

        Creates a new pathText by merging the two objects "textbox" and "beziercurve" and returns its name. The coordinates are given in the current measurement unit of the document(see UNIT constants). "name" should be a unique identifier for the object because you need this name for further access to that object. If "name" is not given Scribus will create one for you.

        May raise NameExistsError if you explicitly pass a name that's already used. May raise NotFoundError if one or both of the named base object don't exist.

    createPdfAnnotation(...)
        createPdfAnnotation(which, x,y,w,h,["name"])

        Creates a pdf annotation.

        Arguments: "which" is one of the following: (0 PDFBUTTON, 1 PDFRADIOBUTTON, 2 PDFTEXTFIELD, 3 PDFCHECKBOX, 4 PDFCOMBOBOX, 5 PDFLISTBOX, 6 PDFTEXTANNOTATION, 7 PDFLINKANNOTATION, 8 PDF3DANNOTATION) "x" and "y" are the coordinates where it will be placed. "w" is its width. "h" is its height. On systems without OSG installed a runtime error will be raised. "name" should be a unique identifier for the object because you need this name for further referencing of that object. If "name" is not given Scribus will create one for you.

        Returns: The name of the newly created annotation.

        May raise NameExistsError if you explicitly pass a name that's already used.

    createPolyLine(...)
       createPolyLine(list, ["name"]) -> string

        Creates a new polyline and returns its name. The points for the polyline are stored in the list "list" in the following order: [x1, y1, x2, y2...xn. yn]. The coordinates are given in the current measurement units of the document(see UNIT constants). "name" should be a unique identifier for the object because you need this name for further access to that object. If "name" is not given Scribus will create one for you.

        May raise NameExistsError if you explicitly pass a name that's already used. May raise ValueError if an insufficient number of points is passed or if the number of values passed don't group into points without leftovers.

    createPolygon(...)
       createPolygon(list, ["name"]) -> string

        Creates a new polygon and returns its name. The points for the polygon are stored in the list "list" in the following order: [x1, y1, x2, y2...xn. yn]. At least three points are required. There is no need to repeat the first point to close the polygon. The polygon is automatically closed by connecting the first and the last point.  The coordinates are given in the current measurement units of the document(see UNIT constants).  "name" should be a unique identifier for the object because you need this name for further access to that object. If "name" is not given Scribus will create one for you.

        May raise NameExistsError if you explicitly pass a name that's already used. May raise ValueError if an insufficient number of points is passed or if the number of values passed don't group into points without leftovers.

    createRect(...)
       createRect(x, y, width, height, ["name"]) -> string

        Creates a new rectangle on the current page and returns its name. The coordinates are given in the current measurement units of the document(see UNIT constants). "name" should be a unique identifier for the object because you need this name to reference that object in future. If "name" is not given Scribus will create one for you.

        May raise NameExistsError if you explicitly pass a name that's already used.

    createTable(...)
       createTable(x, y, width, height, numRows, numColumns, ["name"]) -> string

        Creates a new table with the given number of rows and columns on the actual page and returns its name. The coordinates are given in the actual measurement unit of the document(see UNIT constants). "name" should be a unique identifier for the object because you need this name for further referencing of that object. If "name" is not given Scribus will create one for you.

        May raise NameExistsError if you explicitly pass a name that's already used. May raise ValueError if an insufficient number of rows or columns is passed.

    createText(...)
       createText(x, y, width, height, ["name"]) -> string

        Creates a new text frame on the actual page and returns its name. The coordinates are given in the actual measurement unit of the document(see UNIT constants). "name" should be a unique identifier for the object because you need this name for further referencing of that object. If "name" is not given Scribus will create one for you.

        May raise NameExistsError if you explicitly pass a name that's already used.

    currentPage(...)
       currentPage() -> integer

        Returns the number of the current working page. Page numbers are counted from 1 upwards, no matter what the displayed first page number of your document is.

    defineColor(...)
       defineColor("name", c, m, y, k)

        Defines a new color "name". The color Value is defined via four components: c = Cyan, m = Magenta, y = Yellow and k = Black. Color components should be in the range from 0 to 255. Note: deprecated, use defineColorCMYK() instead.

        May raise ValueError if an invalid color name is specified.

    defineColorCMYK(...)
       defineColorCMYK("name", c, m, y, k)

        Defines a new color "name". The color Value is defined via four components: c = Cyan, m = Magenta, y = Yellow and k = Black. Color components should be in the range from 0 to 255.

        May raise ValueError if an invalid color name is specified.

    defineColorCMYKFloat(...)
       defineColorCMYKFloat("name", c, m, y, k)

        Defines a new color "name". The color Value is defined via four components: c = Cyan, m = Magenta, y = Yellow and k = Black. Color components are floating point values between 0 and 100.

        May raise ValueError if an invalid color name is specified.

    defineColorLab(...)
       defineColorLab("name", r, g, b)

        Defines a new color "name" using CIELab values. The color value is defined via three components: L = luminosity, a = green/red, b = blue/yellow. Color components are floating point values with L between 0 and 100, a and b between - 128 and 128.

        May raise ValueError if an invalid color name is specified.

    defineColorRGB(...)
       defineColorRGB("name", r, g, b)

        Defines a new color "name". The color Value is defined via three components: r = red, g = green, b = blue. Color components should be in the range from 0 to 255.

        May raise ValueError if an invalid color name is specified.

    defineColorRGBFloat(...)
       defineColorRGBFloat("name", r, g, b)

        Defines a new color "name". The color Value is defined via three components: r = red, g = green, b = blue. Color components are floating point values between 0 and 255.

        May raise ValueError if an invalid color name is specified.

    dehyphenateText(...)
       dehyphenateText(["name"]) -> bool

        Does dehyphenation on text frame "name". If "name" is not given the currently selected item is used.

        May raise WrongFrameTypeError if the target frame is not a text frame

    deleteColor(...)
       deleteColor("name", "replace")

        Deletes the color "name". Every occurrence of that color is replaced by the color "replace". If not specified, "replace" defaults to the color "None" - transparent.

        deleteColor works on the default document colors if there is no document open. In that case, "replace", if specified, has no effect.

        May raise NotFoundError if a named color wasn't found. May raise ValueError if an invalid color name is specified.

    deleteLayer(...)
       deleteLayer("layer")

        Deletes the layer with the name "layer". Nothing happens if the layer doesn't exists or if it's the only layer in the document.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    deleteMasterPage(...)
       deleteMasterPage(pageName)

        Delete the named master page.

    deleteObject(...)
       deleteObject(["name"])

        Deletes the item with the name "name". If "name" is not given the currently selected item is deleted.

    deletePage(...)
       deletePage(nr)

        Deletes the given page. Does nothing if the document contains only one page. Page numbers are counted from 1 upwards, no matter what the displayed first page number is.

        May raise IndexError if the page number is out of range

    deleteText(...)
       deleteText(["name"])

        Deletes any text in the text frame "name". If there is some text selected, only the selected text will be deleted. If "name" is not given the currently selected item is used.

    deselectAll(...)
       deselectAll()

        Deselects all objects in the whole document.

    docChanged(...)
       docChanged(bool)

        Enable/disable save icon in the Scribus icon bar and the Save menu item. It's useful to call this procedure when you're changing the document, because Scribus won't automatically notice when you change the document using a script.

    duplicateObject(...)
       duplicateObject(["name"]) -> string

        creates a Duplicate of the selected Object(or Selection Group).

    editMasterPage(...)
       editMasterPage(pageName)

        Enables master page editing and opens the named master page for editing. Finish editing with closeMasterPage().

    fileDialog(...)
       fileDialog("caption", ["filter", "defaultname", haspreview, issave, isdir]) -> string with filename

        Shows a File Open dialog box with the caption "caption". Files are filtered with the filter string "filter". A default filename or file path can also supplied, leave this string empty when you don't want to use it.  A value of True for haspreview enables a small preview widget in the FileSelect box.  When the issave parameter is set to True the dialog acts like a "Save As" dialog otherwise it acts like a "File Open Dialog". When the isdir parameter is True the dialog shows and returns only directories. The default for all of the optional parameters is False.

        The filter, if specified, takes the form 'comment (*.type *.type2 ...)'. For example 'Images (*.png *.xpm *.jpg)'.

        Refer to the Qt-Documentation for QFileDialog for details on filters.

        Example: fileDialog('Open input', 'CSV files (*.csv)') Example: fileDialog('Save report', defaultname='report.txt', issave=True)

    fileQuit(...)
       fileQuit()

        Quit Scribus.

    flipObject(...)
        flipObject(H, V,["name"])

        Toggle the object "name" horizontal and/or vertical flip. If "name" is not given the currently selected item is used.

    getActiveLayer(...)
       getActiveLayer() -> string

        Returns the name of the current active layer.

    getAllObjects(...)
       getAllObjects(["page"]) -> list

        Returns a list containing the names of all objects on the current page. Takes an optional keyword argument that changes the page from which the objects are returned The page index starts at 0 and goes to the total number of pages - 1.

    getAllStyles(...)
       getAllStyles() -> list

        Return a list of the names of all paragraph styles in the current document.

    getAllText(...)
       getAllText(["name"]) -> string

        Returns the text of the text frame "name" and of all text frames which are linked with this frame. If this textframe has some text selected, the selected text is returned. If "name" is not given the currently selected item is used.

    getCellColumnSpan(...)
       getCellColumnSpan(row, column, ["name"]) -> int

        Returns the column span of the cell at "row", "column" in the table "name" or -1 if the cell does not exist. If the cell is covered by another spanning cell, the column span of the spanning cell is returned. If "name" is not given the currently selected item is used.

    getCellFillColor(...)
       getCellFillColor(row, column, ["name"]) -> string

        Returns the fill color of the cell at "row", "column" in the table "name" If "name" is not given the currently selected item is used.

    getCellRowSpan(...)
       getCellRowSpan(row, column, ["name"]) -> int

        Returns the row span of the cell at "row", "column" in the table "name" or -1 if the cell does not exist. If the cell is covered by another spanning cell, the row span of the spanning cell is returned. If "name" is not given the currently selected item is used.

    getCellStyle(...)
       getCellStyle(row, column, ["name"]) -> string

        Returns the named style of the cell at "row", "column" in the table "name". If "name" is not given the currently selected item is used.

        May throw ValueError if the cell does not exist.

    getCharStyles(...)
       getCharStyles() -> list

        Return a list of the names of all character styles in the current document.

    getColor(...)
       getColor("name") -> tuple

        Returns a tuple(C, M, Y, K) containing the four color components of the color "name" from the current document. If no document is open, returns the value of the named color from the default document colors.

        May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified.

    getColorAsRGB(...)
       getColorAsRGB("name") -> tuple

        Returns a tuple (R, G,B) containing the three color components of the color "name" from the current document, converted to the RGB color space. If no document is open, returns the value of the named color from the default document colors.

        May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified.

    getColorAsRGBFloat(...)
       getColorAsRGBFloat("name") -> tuple

        Returns a tuple (R, G,B) containing the three color components of the color "name" from the current document, converted to the RGB color space. Color components are floating point values between 0 and 255. If no document is open, returns the value of the named color from the default document colors.

        May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified.

    getColorFloat(...)
       getColorFloat("name") -> tuple

        Returns a tuple(C, M, Y, K) containing the four color components of the color "name" from the current document. Color components are floating point values between 0 and 100. If no document is open, returns the value of the named color from the default document colors.

        May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified.

    getColorNames(...)
       getColorNames() -> list

        Returns a list containing the names of all defined colors in the document. If no document is open, returns a list of the default document colors.

    getColumnGap(...)
       getColumnGap(["name"]) -> float

        Returns the column gap size of the text frame "name" expressed in points. If "name" is not given the currently selected item is used.

    getColumns(...)
       getColumns(["name"]) -> integer

        Gets the number of columns of the text frame "name". If "name" is not given the currently selected item is used.

    getCornerRadius(...)
       getCornerRadius(["name"]) -> integer

        Returns the corner radius of the object "name". The radius is expressed in points. If "name" is not given the currently selected item is used.

    getCustomLineStyle(...)
       getCustomLineStyle(["name"]) -> string

        Returns the styleName of custom line style for the object. If object's "name" is not given the currently selected item is used.

    getDocName(...)
       getDocName() -> string

        Returns the name the document was saved under. If the document was not saved before the name is empty.

    getFillBlendmode(...)
       getFillBlendmode(["name"]) -> integer

        Returns the fill blendmode of the object "name". If "name" is not given the currently selected Item is used.

    getFillColor(...)
       getFillColor(["name"]) -> string

        Returns the name of the fill color of the object "name". If "name" is not given the currently selected item is used.

    getFillShade(...)
       getFillShade(["name"]) -> integer

        Returns the shading value of the fill color of the object "name". If "name" is not given the currently selected item is used.

    getFillTransparency(...)
       getFillTransparency(["name"]) -> float

        Returns the fill transparency of the object "name". If "name" is not given the currently selected Item is used.

    getFont(...)
       getFont(["name"]) -> string

        Returns the font name for the text frame "name". If this text frame has some text selected the value assigned to the first character of the selection is returned. If "name" is not given the currently selected item is used.

    getFontFeatures(...)
       getFontFeatures(["name"]) -> string

        Returns the font features for the text frame "name". If this text frame has some text selected the value assigned to the first character of the selection is returned. If "name" is not given the currently selected item is used.

    getFontNames(...)
       getFontNames() -> list

        Returns a list with the names of all available fonts.

    getFontSize(...)
       getFontSize(["name"]) -> float

        Returns the font size in points for the text frame "name". If this text frame has some text selected the value assigned to the first character of the selection is returned. If "name" is not given the currently selected item is used.

    getGuiLanguage(...)
       getGuiLanguage() -> string

        Returns a string with the - lang value.

    getHGuides(...)
       getHGuides() -> list

        Returns a list containing positions of the horizontal guides. Values are in the document's current units - see UNIT_ <type> constants.

    getImageColorSpace(...)
       getImageColorSpace(["name"]) -> integer Returns the color space for the image loaded in image frame "name" as  one of following integer constants: CSPACE_RGB (0), CSPACE_CMYK (1),  CSPACE_GRAY (2), CSPACE_DUOTONE (3) or CSPACE_MONOCHROME (4). Returns CSPACE_UNDEFINED (-1) if no image is loaded in the frame. If "name" is not given the currently selected item is used.

    getImageFile(...)
       getImageFile(["name"]) -> string

        Returns the filename for the image in the image frame. If "name" is not given the currently selected item is used.

    getImageOffset(...)
        getImageOffset(["name"]) -> (x, y)

        Returns a(x, y) tuple containing the offset values in point unit of the image frame "name".  If "name" is not given the currently selected item is used.

    getImageScale(...)
        getImageScale(["name"]) -> (x, y)

        Returns a(x, y) tuple containing the scaling values of the image frame "name".  If "name" is not given the currently selected item is used.

    getJSActionScript(...)
        getJSActionScript(which, ["name"])

        Gets the JavaScript action for a particular event "which" is one of the following: (0 Mouse Up, 1 Mouse Down, 2 Mouse Enter, 3 Mouse Exit, 4 Focus In, 5 Focus Out, 6 Selection Change, 7 Field Format, 8 Field Validate, 9 Field Calculate) "name" uses the currently selected item if not given. Page item must be an annotation or an error will be raised. Returns: Returns a string if object's action type is Javascript,  NONE otherwise.

    getLayerBlendmode(...)
       getLayerBlendmode("layer") -> int

        Returns the "layer" layer blendmode,

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    getLayerTransparency(...)
       getLayerTransparency("layer") -> float

        Returns the "layer" layer transparency,

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    getLayers(...)
       getLayers() -> list

        Returns a list with the names of all defined layers.

    getLineBlendmode(...)
       getLineBlendmode(["name"]) -> integer

        Returns the line blendmode of the object "name". If "name" is not given the currently selected Item is used.

    getLineCap(...)
       getLineCap(["name"]) -> integer (see constants)

        Returns the line cap style of the object "name". If "name" is not given the currently selected item is used. The cap types are: CAP_FLAT, CAP_ROUND, CAP_SQUARE

    getLineColor(...)
       getLineColor(["name"]) -> string

        Returns the name of the line color of the object "name". If "name" is not given the currently selected item is used.

    getLineJoin(...)
       getLineJoin(["name"]) -> integer (see constants)

        Returns the line join style of the object "name". If "name" is not given the currently selected item is used.  The join types are: JOIN_BEVEL, JOIN_MITTER, JOIN_ROUND

    getLineShade(...)
       getLineShade(["name"]) -> integer

        Returns the shading value of the line color of the object "name". If "name" is not given the currently selected item is used.

    getLineSpacing(...)
       getLineSpacing(["name"]) -> float

        Returns the line spacing("leading") of the text frame "name" expressed in points. If "name" is not given the currently selected item is used.

    getLineStyle(...)
       getLineStyle(["name"]) -> integer (see constants)

        Returns the line style of the object "name". If "name" is not given the currently selected item is used. Line style constants are: LINE_DASH, LINE_DASHDOT, LINE_DASHDOTDOT, LINE_DOT, LINE_SOLID

    getLineTransparency(...)
       getLineTransparency(["name"]) -> float

        Returns the line transparency of the object "name". If "name" is not given the currently selected Item is used.

    getLineWidth(...)
       getLineWidth(["name"]) -> integer

        Returns the line width of the object "name". If "name" is not given the currently selected Item is used.

    getMasterPage(...)
       getMasterPage(nr)

        Get Master Page of the page "nr".

        May raise IndexError if the page number is out of range.

    getObjectAttributes(...)
       getObjectAttributes(["name"]) -> list Returns a list containing all attributes of object "name".

    getObjectType(...)
       getObjectType(["name"]) -> string

        Get type of object "name" as a string.

    getPageItems(...)
       getPageItems() -> list

        Returns a list of tuples with items on the current page. The tuple is: (name, objectType, order) E.g. [('Text1', 4, 0), ('Image1', 2, 1)] means that object named 'Text1' is a text frame(type 4) and is the first at the page...

    getPageMargins(...)
       getPageMargins()

        Returns the document page margins as a (top, left, right, bottom) tuple in the document's current units. See UNIT_ <type> constants and getPageSize().

    getPageNMargins(...)
       getPageNMargins(nr) -> tuple

        Returns a tuple with a particular page's margins measured in the document's current units. See UNIT_ <type> constants and getPageMargins()

    getPageNSize(...)
       getPageNSize(nr) -> tuple

        Returns a tuple with a particular page's size measured in the document's current units. See UNIT_ <type> constants and getPageMargins()

    getPageSize(...)
       getPageSize() -> tuple

        Returns a tuple with document page dimensions measured in the document's current units. See UNIT_ <type> constants and getPageMargins()

    getPageType(...)
       getPageType() -> integer

        Returns the type of the Page, 0 means left Page, 1 is a middle Page and 2 is a right Page

    getParagraphStyles(...)
       getAllStyles() -> list

        Return a list of the names of all paragraph styles in the current document.

    getPosition(...)
        getPosition(["name"]) -> (x, y)

        Returns a (x, y) tuple with the position of the object "name". If "name" is not given the currently selected item is used. The position is expressed in the actual measurement unit of the document - see UNIT_ <type> for reference.

    getProperty(...)
       getProperty(object, property)

        Return the value of the property `property' of the passed `object'.

        The `object' argument may be a string, in which case the named PageItem is searched for. It may also be a PyCObject, which may point to any C++ QObject instance.

        The `property' argument must be a string, and is the name of the property to look up on `object'.

        The return value varies depending on the type of the property.

    getPropertyCType(...)
       getPropertyCType(object, property, includesuper=True)

        Returns the name of the C type of `property' of `object'. See getProperty() for details of arguments.

        If `includesuper' is true, search inherited properties too.

    getPropertyNames(...)
       getPropertyNames(object, includesuper=True)

        Return a list of property names supported by `object'. If `includesuper' is true, return properties supported by parent classes as well.

    getRotation(...)
       getRotation(["name"]) -> integer

        Returns the rotation of the object "name". The value is expressed in degrees, and clockwise is positive. If "name" is not given the currently selected item is used.

    getSelectedObject(...)
       getSelectedObject([nr]) -> string

        Returns the name of the selected object. "nr" if given indicates the number of the selected object, e.g. 0 means the first selected object, 1 means the second selected Object and so on.

    getSize(...)
        getSize(["name"]) -> (width, height)

        Returns a (width, height) tuple with the size of the object "name". If "name" is not given the currently selected item is used. The size is expressed in the current measurement unit of the document - see UNIT_ <type> for reference.

    getStyle(...)
       getStyle(["name"])

        Return name of style applied to object named "name". If "name" is not given, the currently selected object is used. If current object has a text selection,  the name of style applied to start of selection is returned. Otherwise the name  of the item default style is returned.

    getTableColumnWidth(...)
       getTableColumnWidth(column, ["name"]) -> float

        Returns the column width of "column" in the table "name" expressed in points, or 0.0 if the column does not exist. If "name" is not given the currently selected item is used.

    getTableColumns(...)
       getTableColumns(["name"]) -> integer

        Gets the number of columns in the table "name". If "name" is not given the currently selected item is used.

    getTableFillColor(...)
       getTableFillColor(["name"]) -> string

        Returns the fill color of the table "name". If "name" is not given the currently selected item is used.

    getTableRowHeight(...)
       getTableRowHeight(row, ["name"]) -> float

        Returns the row height of "row" in the table "name" expressed in points, or 0.0 if the row does not exist. If "name" is not given the currently selected item is used.

    getTableRows(...)
       getTableRows(["name"]) -> integer

        Gets the number of rows in the table "name". If "name" is not given the currently selected item is used.

    getTableStyle(...)
       getTableStyle(["name"]) -> string

        Returns the named style of the table "name". If "name" is not given the currently selected item is used.

    getText(...)
       getText(["name"]) -> string

        Returns the text of the text frame "name". If this text frame has some text selected, the selected text is returned. All text in the frame, not just currently visible text, is returned. If "name" is not given the currently selected item is used.

    getTextColor(...)
       getTextColor(["name"]) -> string

        Returns the name of the text color used for text frame "name". If this text frame has some text selected the value assigned to the first character of the selection is returned. If "name" is not given the currently selected item is used.

    getTextDistances(...)
       getTextDistances(["name"]) -> tuple

        Returns the text distances of the text frame "name" expressed in points. The distances are returned as a tuple like(left, right, top, bottom). If "name" is not given the currently selected item is used.

    getTextLength(...)
       getTextLength(["name"]) -> integer

        Returns the length of the text in the text frame "name". If "name" is not given the currently selected item is used.

    getTextLines(...)
       getTextLines(["name"]) -> integer

        Returns the number of lines of the text in the text frame "name". If "name" is not given the currently selected item is used.

    getTextShade(...)
       getTextShade(["name"]) -> integer

        Returns the shade of text color used for text frame "name". If this text frame has some text selected the value assigned to the first character of the selection is returned. If "name" is not given the currently selected item is used.

    getTextVerticalAlignment(...)
       getTextVerticalAlignment(["name"]) -> integer

        Gets the vertical alignment of text inside text frame "name". If "name" is not given the currently selected item is used.

    getUnit(...)
       getUnit() -> integer (Scribus unit constant)

        Returns the measurement units of the document. The returned value will be one of the UNIT_ * constants: UNIT_INCHES, UNIT_MILLIMETERS, UNIT_PICAS, UNIT_POINTS.

    getVGuides(...)
       getVGuides()

        See getHGuides.

    getXFontNames(...)
       getXFontNames() -> list of tuples

        Returns a larger font info. It's a list of the tuples with: [(Scribus name, Family, Real name, subset (1|0), embed PS (1|0), font file), (...), ... ]

    getval(...)
       Scribus internal.

    gotoPage(...)
       gotoPage(nr)

        Moves to the page "nr" (that is, makes the current page "nr"). Note that gotoPage doesn't (currently) change the page the user's view is displaying, it just sets the page that script commands will operates on.

        May raise IndexError if the page number is out of range.

    groupObjects(...)
       groupObjects(list) -> string

        Groups the objects named in "list" together. "list" must contain the names of the objects to be grouped. If "list" is not given the currently selected items are used. Returns the group name for further referencing.

    haveDoc(...)
       haveDoc() -> int

        Returns the quantity of open documents: 0 if none are opened.

    hyphenateText(...)
       hyphenateText(["name"]) -> bool

        Does hyphenation on text frame "name". If "name" is not given the currently selected item is used.

        May raise WrongFrameTypeError if the target frame is not a text frame

    importPage(...)
       importPage("fromDoc", (pageList), [create, imortwhere, importwherePage])

        Imports a set of pages (given as a tuple) from an existing document (the file name must be given). This functions maps the "Page->Import" dropdown menu function. fromDoc: string
        the filename of the document to import pages from pageList: tuple with page numbers of pages to import create: number; 0 to replace existing pages, 1 (default) to insert new pages importWhere: number; the page number (of the current document) at which import the pages importWherePage: number; used if create==1; 0 to create pages before selected page; 1 to create pages after selected page; 2 (default) to create pages at the end of the document

    insertHtmlText(...)
       insertHTMLText("file", ["name"])

        Inserts the text from "file" into the text frame "name". Text must be UTF encoded(see setText() as reference). If "name" is not given the currently selected Item is used.

    insertTableColumns(...)
       insertTableColumns(index, numColumns, ["name"])

        Inserts "numColumns" columns before the column at "index" in the table "name". If "name" is not given the currently selected item is used.

        May throw ValueError if number of columns is not at least one or index is out of bounds.

    insertTableRows(...)
       insertTableRows(index, numRows, ["name"])

        Inserts "numRows" rows before the row at "index" in the table "name". If "name" is not given the currently selected item is used.

        May throw ValueError if number of rows is not at least one or index is out of bounds.

    insertText(...)
       insertText("text", pos, ["name"])

        Inserts the text "text" at the position "pos" into the text frame "name". Text must be UTF encoded (see setText() as reference) The first character has an index of 0. Inserting text at position - 1 appends it to the frame. If "name" is not given the currently selected Item is used.

        May throw IndexError for an insertion out of bounds.

    isAnnotated(...)
        isAnnotated(["name"], ["deannotate=False"])

        Queries the item to see if it has a Pdf annotation.

        Arguments: "name" uses the currently selected item if not given.

        Keyword Arguments: "deannotate" if set to True will turn off the annotation flag

        Returns: A tuple with a string at 0 that indicates what type of pdf annotation it is.  A dictionary is in index 1 that contains data the function was able to gather. If the item is not a pdf annotation returns None. Passing the keyword parameter deannotate =True returns None.

        May raise WrongFrameTypeError if the target frame is not a text frame

    isLayerFlow(...)
       isLayerFlow("layer") -> bool

        Returns whether text flows around objects on layer "layer", a value of True means that text flows around, a value of False means that the text does not flow around.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    isLayerLocked(...)
       isLayerLocked("layer") -> bool

        Returns whether the layer "layer" is locked or not, a value of True means that the layer "layer" is editable, a value of False means that the layer "layer" is locked.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    isLayerOutlined(...)
       isLayerOutlined("layer") -> bool

        Returns whether the layer "layer" is outlined or not, a value of True means that the layer "layer" is outlined, a value of False means that the layer "layer" is normal.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    isLayerPrintable(...)
       isLayerPrintable("layer") -> bool

        Returns whether the layer "layer" is printable or not, a value of True means that the layer "layer" can be printed, a value of False means that printing the layer "layer" is disabled.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    isLayerVisible(...)
       isLayerVisible("layer") -> bool

        Returns whether the layer "layer" is visible or not, a value of True means that the layer "layer" is visible, a value of False means that the layer "layer" is invisible.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    isLocked(...)
       isLocked(["name"]) -> bool

        Returns true if is the object "name" locked.  If "name" is not given the currently selected item is used.

    isPDFBookmark(...)
       isPDFBookmark(["name"]) -> bool

        Returns true if the text frame "name" is a PDF bookmark. If "name" is not given the currently selected item is used.

        May raise WrongFrameTypeError if the target frame is not a text frame

    isSpotColor(...)
       isSpotColor("name") -> bool

        Returns True if the color "name" is a spot color. See also setSpotColor()

        May raise NotFoundError if a named color wasn't found. May raise ValueError if an invalid color name is specified.

    linkTextFrames(...)
       linkTextFrames("fromname", "toname")

        Link two text frames. The frame named "fromname" is linked to the frame named "toname". The target frame must be an empty text frame and must not link to or be linked from any other frames already.

        May throw ScribusException if linking rules are violated.

    loadImage(...)
       loadImage("filename" [, "name"])

        Loads the picture "picture" into the image frame "name". If "name" is not given the currently selected item is used.

        May raise WrongFrameTypeError if the target frame is not an image frame

    loadStylesFromFile(...)
       loadStylesFromFile("filename")

        Loads paragraph styles from the Scribus document at "filename" into the current document.

    lockObject(...)
       lockObject(["name"]) -> bool

        Locks the object "name" if it's unlocked or unlock it if it's locked. If "name" is not given the currently selected item is used. Returns true if locked.

    masterPageNames(...)
       masterPageNames()

        Returns a list of the names of all master pages in the document.

    mergeTableCells(...)
       mergeTableCells(row, column, numRows, numColumns, ["name"])

        Merges the cell at the specified "row" and "column" with the adjacent cells into one cell.

        May throw ValueError if number if numRows or numColumns is less than 1 or the specified area is out of bounds.

    messageBox(...)
       messageBox("caption", "message",     icon=ICON_NONE, button1=BUTTON_OK|BUTTONOPT_DEFAULT,     button2=BUTTON_NONE, button3=BUTTON_NONE) -> integer

        Displays a message box with the title "caption", the message "message", and an icon "icon" and up to 3 buttons. By default no icon is used and a single button, OK, is displayed. Only the caption and message arguments are required, though setting an icon and appropriate button(s) is strongly recommended. The message text may contain simple HTML-like markup.

        Returns the number of the button the user pressed. Button numbers start at 1.

        For the icon and the button parameters there are predefined constants available with the same names as in the Qt Documentation. These are the BUTTON_ * and ICON_* constants defined in the module. There are also two extra constants that can be binary-ORed with button constants:     BUTTONOPT_DEFAULT   Pressing enter presses this button.     BUTTONOPT_ESCAPE    Pressing escape presses this button.

        Usage examples: result = messageBox('Script failed',                     'This script only works when you have a text frame selected.',                     ICON_ERROR) result = messageBox('Monkeys!', 'Something went ook! <i>Was it a monkey?</i>',                     ICON_WARNING, BUTTON_YES |BUTTONOPT_DEFAULT,                     BUTTON_NO, BUTTON_IGNORE|BUTTONOPT_ESCAPE)

        Defined button and icon constants: BUTTON_NONE, BUTTON_ABORT, BUTTON_CANCEL, BUTTON_IGNORE, BUTTON_NO, BUTTON_NOALL, BUTTON_OK, BUTTON_RETRY, BUTTON_YES, BUTTON_YESALL, ICON_NONE, ICON_INFORMATION, ICON_WARNING, ICON_CRITICAL.

    messagebarText(...)
       messagebarText("string")

        Writes the "string" into the Scribus message bar(status line). The text must be UTF8 encoded or 'unicode' string(recommended).

    moveObject(...)
       moveObject(dx, dy [, "name"])

        Moves the object "name" by dx and dy relative to its current position. The distances are expressed in the current measurement unit of the document(see UNIT constants). If "name" is not given the currently selected item is used. If the object "name" belongs to a group, the whole group is moved.

    moveObjectAbs(...)
       moveObjectAbs(x, y [, "name"])

        Moves the object "name" to a new location. The coordinates are expressed in the current measurement unit of the document(see UNIT constants).  If "name" is not given the currently selected item is used.  If the object "name" belongs to a group, the whole group is moved.

    moveSelectionToBack(...)
       moveSelectionToBack()

        Moves current selection to back.

    moveSelectionToFront(...)
       moveSelectionToFront()

        Moves current selection to front.

    newDoc(...)
       newDoc(size, margins, orientation, firstPageNumber,                    unit, facingPages, firstSideLeft) -> bool

        WARNING: Obsolete procedure! Use newDocument instead.

        Creates a new document and returns true if successful. The parameters have the following meaning:

            size = A tuple (width, height) describing the size of the document. You can     use predefined constants named PAPER_ <paper_type> e.g. PAPER_A4 etc.

            margins = A tuple(left, right, top, bottom) describing the document     margins

            orientation = the page orientation - constants PORTRAIT, LANDSCAPE

            firstPageNumer = is the number of the first page in the document used for pagenumbering. While you'll usually want 1, it's useful to have higher     numbers if you're creating a document in several parts.

            unit: this value sets the measurement units used by the document. Use a     predefined constant for this, one of: UNIT_INCHES, UNIT_MILLIMETERS,     UNIT_PICAS, UNIT_POINTS.

            facingPages = FACINGPAGES, NOFACINGPAGES

            firstSideLeft = FIRSTPAGELEFT, FIRSTPAGERIGHT

        The values for width, height and the margins are expressed in the given unit for the document. PAPER_ * constants are expressed in points. If your document is not in points, make sure to account for this.

        example: newDoc(PAPER_A4, (10, 10, 20, 20), LANDSCAPE, 1, UNIT_POINTS,                 FACINGPAGES, FIRSTPAGERIGHT)

    newDocDialog(...)
       newDocDialog() -> bool

        Displays the "New Document" dialog box. Creates a new document if the user accepts the settings. Does not create a document if the user presses cancel. Returns true if a new document was created.

    newDocument(...)
       newDocument(size, margins, orientation, firstPageNumber,                         unit, pagesType, firstPageOrder, numPages) -> bool

        Creates a new document and returns true if successful. The parameters have the following meaning:

        size = A tuple (width, height) describing the size of the document. You can use predefined constants named PAPER_ <paper_type> e.g. PAPER_A4 etc.

        margins = A tuple(left, right, top, bottom) describing the document margins

        orientation = the page orientation - constants PORTRAIT, LANDSCAPE

        firstPageNumer = is the number of the first page in the document used for pagenumbering. While you'll usually want 1, it's useful to have higher numbers if you're creating a document in several parts.

        unit: this value sets the measurement units used by the document. Use a predefined constant for this, one of: UNIT_INCHES, UNIT_MILLIMETERS, UNIT_PICAS, UNIT_POINTS.

        pagesType = One of the predefined constants PAGE_n. PAGE_1 is single page, PAGE_2 is for facing pages documents, PAGE_3 is for 3 pages fold and PAGE_4 is 4-fold.

        firstPageOrder = What is position of first page in the document. Indexed from 0 (0= first).

        numPage = Number of pages to be created.

        The values for width, height and the margins are expressed in the given unit for the document. PAPER_ * constants are expressed in points. If your document is not in points, make sure to account for this.

        example: newDocument(PAPER_A4, (10, 10, 20, 20), LANDSCAPE, 7, UNIT_POINTS, PAGE_4, 3, 1)

        May raise ScribusError if is firstPageOrder bigger than allowed by pagesType.

    newPage(...)
        newPage(where [, "masterpage"])

        Creates a new page. If "where" is -1 the new Page is appended to the document, otherwise the new page is inserted before "where". Page numbers are counted from 1 upwards, no matter what the displayed first page number of your document is. The optional parameter "masterpage" specifies the name of the master page for the new page.

        May raise IndexError if the page number is out of range

    newStyleDialog(...)
       newStyleDialog() -> string

        Shows 'Create new paragraph style' dialog. Function returns real style name or None when user cancels the dialog.

    objectExists(...)
       objectExists(["name"]) -> bool

        Test if an object with specified name really exists in the document. The optional parameter is the object name. When no object name is given, returns True if there is something selected.

    openDoc(...)
       openDoc("name")

        Opens the document "name".

        May raise ScribusError if the document could not be opened.

    pageCount(...)
       pageCount() -> integer

        Returns the number of pages in the document.

    pageDimension(...)
       Obsolete function. Don't use it.

    pasteObject(...)
       pasteObject(["name"]) -> string

        pastes a Duplicate of the selected Object(or Selection Group).

    placeEPS(...)
       placeEPS("filename", x, y)

        Places the EPS "filename" onto the current page, x and y specify the coordinate of the topleft corner of the EPS placed on the page

        If loading was successful, the selection contains the imported EPS

    placeODG(...)
       placeODG("filename", x, y)

        Places the ODG "filename" onto the current page, x and y specify the coordinate of the topleft corner of the ODG placed on the page

        If loading was successful, the selection contains the imported ODG

    placeSVG(...)
       placeSVG("filename", x, y)

        Places the SVG "filename" onto the current page, x and y specify the coordinate of the topleft corner of the SVG placed on the page

        If loading was successful, the selection contains the imported SVG

    placeSXD(...)
       placeSXD("filename", x, y)

        Places the SXD "filename" onto the current page, x and y specify the coordinate of the topleft corner of the SXD placed on the page

        If loading was successful, the selection contains the imported SXD

    placeVectorFile(...)
       placeVectorFile("filename", x, y)

        Places the vector graphic "filename" onto the current page, x and y specify the coordinate of the topleft corner of the graphic placed on the page

        If loading was successful, the selection contains the imported graphic

    progressReset(...)
       progressReset()

        Cleans up the Scribus progress bar previous settings. It is called before the new progress bar use. See progressSet.

    progressSet(...)
       progressSet(nr)

        Set the progress bar position to "nr", a value relative to the previously set progressTotal. The progress bar uses the concept of steps
        you give it the total number of steps and the number of steps completed so far and it will display the percentage of steps that have been completed. You can specify the total number of steps with progressTotal(). The current number of steps is set with progressSet(). The progress bar can be rewound to the beginning with progressReset(). [based on info taken from Trolltech's Qt docs]

    progressTotal(...)
       progressTotal(max)

        Sets the progress bar's maximum steps value to the specified number. See progressSet.

    readPDFOptions(...)
       readPDFOptions(fileName)

        Read PDF options from fileName.

    redrawAll(...)
       redrawAll()

        Redraws all pages.

    removeTableColumns(...)
       removeTableColumns(index, numColumns, ["name"])

        Removes "numColumns" columns from the table "name" starting with the column at "index". If "name" is not given the currently selected item is used.

        May throw ValueError if number of columns is not at least one or the range to be deleted is out of bounds.

    removeTableRows(...)
       removeTableRows(index, numRows, ["name"])

        Removes "numRows" rows from the table "name" starting with the row at "index". If "name" is not given the currently selected item is used.

        May throw ValueError if number of rows is not at least one or the range to be deleted is out of bounds.

    renderFont(...)
       renderFont("name", "filename", "sample", size, format="PPM") -> bool

        Creates an image preview of font "name" with given text "sample" and size. If "filename" is not "", image is saved into "filename". Otherwise image data is returned as a string. The optional "format" argument specifies the image format to generate, and supports any format allowed by QPixmap.save(). Common formats are PPM, JPEG, PNG and XPM.

        May raise NotFoundError if the specified font can't be found. May raise ValueError if an empty sample or filename is passed.

    replaceColor(...)
       replaceColor("name", "replace")

        Every occurence of the color "name" is replaced by the color "replace".

        May raise NotFoundError if a named color wasn't found. May raise ValueError if an invalid color name is specified.

    resizeTableColumn(...)
       resizeTableColumn(column, width, ["name"])

        Resizes "column" to "width" in the table "name". If "name" is not given the currently selected item is used.

        May throw ValueError if the width is less than 0 or the column does not exist.

    resizeTableRow(...)
       resizeTableRow(row, height, ["name"])

        Resizes "row" to "height" in the table "name". If "name" is not given the currently selected item is used.

        May throw ValueError if the height is less than 0 or the row does not exist.

    retval(...)
       Scribus internal.

    rotateObject(...)
       rotateObject(rot [, "name"])

        Rotates the object "name" by "rot" degrees relatively. The object is rotated by the vertex that is currently selected as the rotation point - by default, the top left vertex at zero rotation. Positive values mean counter clockwise rotation when the default rotation point is used. If "name" is not given the currently selected item is used.

    rotateObjectAbs(...)
       rotateObjectAbs(rot [, "name"])

        Sets the rotation of the object "name" to "rot". Positive values mean counter clockwise rotation. If "name" is not given the currently selected item is used.

    saveDoc(...)
       saveDoc()

        Saves the current document with its current name, returns true if successful. If the document has not already been saved, this may bring up an interactive save file dialog.

        If the save fails, there is currently no way to tell.

    saveDocAs(...)
       saveDocAs("name")

        Saves the current document under the new name "name" (which may be a full or relative path).

        May raise ScribusError if the save fails.

    savePDFOptions(...)
       savePDFOptions(fileName)

        Save PDF options to fileName.

    savePageAsEPS(...)
       savePageAsEPS("name")

        Saves the current page as an EPS to the file "name".

        May raise ScribusError if the save failed.

    scaleGroup(...)
        scaleGroup(factor [, "name"])

        Scales the group the object "name" belongs to. Values greater than 1 enlarge the group, values smaller than 1 make the group smaller e.g a value of 0.5 scales the group to 50 % of its original size, a value of 1.5 scales the group to 150 % of its original size.  The value for "factor" must be greater than 0. If "name" is not given the currently selected item is used.

        May raise ValueError if an invalid scale factor is passed.

    scaleImage(...)
       scaleImage(x, y [, "name"])

        Sets the internal scaling factors of the picture in the image frame "name". If "name" is not given the currently selected item is used. A number of 1 means 100 % . Internal scaling factors are different from the values shown on  properties palette. Note : deprecated, use setImageScale() instead.

        May raise WrongFrameTypeError if the target frame is not an image frame

    scrollDocument(...)
        scrollDocument(x, y)

        Scroll the document in main GUI window by x and y.

    selectObject(...)
       selectObject("name")

        Selects the object with the given "name".

    selectText(...)
       selectText(start, count, ["name"])

        Selects "count" characters of text in the text frame "name" starting from the character "start". Character counting starts at 0. If "count" is zero, any text selection will be cleared.  If "name" is not given the currently selected item is used.

        May throw IndexError if the selection is outside the bounds of the text.

    selectionCount(...)
       selectionCount() -> integer

        Returns the number of selected objects.

    sentToLayer(...)
       sentToLayer("layer" [, "name"])

        Sends the object "name" to the layer "layer". The layer must exist. If "name" is not given the currently selected item is used.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    setActiveLayer(...)
       setActiveLayer("name")

        Sets the active layer to the layer named "name".

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    setBaseLine(...)
       setBaseLine(grid, offset)

        Sets the base line settings of the document, grid spacing(grid), grid offset(offset). Values are given in the measurement units of the document - see UNIT_ <type> constants.

    setCellBottomBorder(...)
       setCellBottomBorder(row, column, borderLines, ["name"])

        Sets the bottom border of the cell at "row", "column" in the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_ * constants. If "name" is not given the currently selected item is used.

        May throw ValueError the cell does not exist or if "borderLines" is of the wrong format.

    setCellBottomPadding(...)
       setCellBottomPadding(row, column, padding, ["name"])

        Sets the bottom padding of the cell at "row", "column" in the table "name" to "padding". If "name" is not given the currently selected item is used.

        May throw ValueError the cell does not exist or if "padding" is less than 0.

    setCellFillColor(...)
       setCellFillColor(row, column, color, ["name"])

        Sets the fill color of the cell at "row", "column" in the table "name" to "color". If "name" is not given the currently selected item is used.

        May throw ValueError the cell does not exist.

    setCellLeftBorder(...)
       setCellLeftBorder(row, column, borderLines, ["name"])

        Sets the left border of the cell at "row", "column" in the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_ * constants. If "name" is not given the currently selected item is used.

        May throw ValueError the cell does not exist or if "borderLines" is of the wrong format.

    setCellLeftPadding(...)
       setCellLeftPadding(row, column, padding, ["name"])

        Sets the left padding of the cell at "row", "column" in the table "name" to "padding". If "name" is not given the currently selected item is used.

        May throw ValueError the cell does not exist or if "padding" less than 0.

    setCellRightBorder(...)
       setCellRightBorder(row, column, borderLines, ["name"])

        Sets the right border of the cell at "row", "column" in the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_ * constants. If "name" is not given the currently selected item is used.

        May throw ValueError the cell does not exist or if "borderLines" is of the wrong format.

    setCellRightPadding(...)
       setCellRightPadding(row, column, padding, ["name"])

        Sets the right padding of the cell at "row", "column" in the table "name" to "padding". If "name" is not given the currently selected item is used.

        May throw ValueError the cell does not exist or if "padding" less than 0.

    setCellStyle(...)
       setCellStyle(row, column, style, ["name"])

        Sets the named style of the cell at "row", "column" in the table "name" to "style". If "name" is not given the currently selected item is used.

        May throw ValueError if the cell does not exist.

    setCellText(...)
       setCellText(row, column, text, ["name"])

        Sets the text of the cell at "row", "column" in the table "name" to "text". If "name" is not given the currently selected item is used.

        May throw ValueError if the cell does not exist.

    setCellTopBorder(...)
       setCellTopBorder(row, column, borderLines, ["name"])

        Sets the top border of the cell at "row", "column" in the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_ * constants. If "name" is not given the currently selected item is used.

        May throw ValueError the cell does not exist or if "borderLines" is of the wrong format.

    setCellTopPadding(...)
       setCellTopPadding(row, column, padding, ["name"])

        Sets the top padding of the cell at "row", "column" in the table "name" to "padding". If "name" is not given the currently selected item is used.

        May throw ValueError the cell does not exist or if "padding" is less than 0.

    setCharacterStyle(...)
       setCharacterStyle("style" [, "name"])

        Apply the named character "style" to the object named "name". If object name is given, style is applied to the current text selection in object "name". If no object name is given, style is applied on selected object.

    setColumnGap(...)
       setColumnGap(size, ["name"])

        Sets the column gap of the text frame "name" to the value "size". If "name" is not given the currently selected item is used.

        May throw ValueError if the column gap is out of bounds(must be positive).

    setColumns(...)
       setColumns(nr, ["name"])

        Sets the number of columns of the text frame "name" to the integer "nr". If "name" is not given the currently selected item is used.

        May throw ValueError if number of columns is not at least one.

    setCornerRadius(...)
       setCornerRadius(radius, ["name"])

        Sets the corner radius of the object "name". The radius is expressed in points. If "name" is not given the currently selected item is used.

        May raise ValueError if the corner radius is negative.

    setCursor(...)
       setCursor()

        [UNSUPPORTED!] This might break things, so steer clear for now.

    setCustomLineStyle(...)
       setCustomLineStyle("styleName", ["name"])

        Sets the custom line style of the object "name" to "styleName" Argument "styleName" is the name of line style as seen in Style Manager If "name" is not given the currently selected item is used.

    setDocType(...)
       setDocType(facingPages, firstPageLeft)

        Sets the document type. To get facing pages set the first parameter to FACINGPAGES, to switch facingPages off use NOFACINGPAGES instead.  If you want to be the first page a left side set the second parameter to FIRSTPAGELEFT, for a right page use FIRSTPAGERIGHT.

    setFileAnnotation(...)
        setFileAnnotation(path, page, x, y, ["name"]), ["absolute=True"])

            Turns a text frame into a absolute or relative link annotation. Arguments: "path" is the absolute or relative path to the file. "page" is the page that it links to. "x" and "y" are the x and y coordinates of the page. "name" uses the currently selected item if not given.

            Keyword arguments: "absolute" if set to False will make this a relative path. True is its default.

            Returns: None

            May raise WrongFrameTypeError if the target frame is not a text frame

            setFillBlendmode(...)
            setFillBlendmode(blendmode, ["name"])

            Sets the fill blendmode of the object "name" to blendmode If "name" is not given the currently selected item is used.

            setFillColor(...)
            setFillColor("color", ["name"])

            Sets the fill color of the object "name" to the color "color". "color" is the name of one of the defined colors. If "name" is not given the currently selected item is used.

            setFillShade(...)
            setFillShade(shade, ["name"])

            Sets the shading of the fill color of the object "name" to "shade". "shade" must be an integer value in the range from 0 (lightest) to 100 (full Color intensity). If "name" is not given the currently selected Item is used.

            May raise ValueError if the fill shade is out of bounds.

            setFillTransparency(...)
            setFillTransparency(transparency, ["name"])

            Sets the fill transparency of the object "name" to transparency If "name" is not given the currently selected item is used.

            setFont(...)
            setFont("font", ["name"])

            Sets the font of the text frame "name" to "font". If there is some text selected only the selected text is changed.  If "name" is not given the currently selected item is used.

            May throw ValueError if the font cannot be found.

            setFontFeatures(...)
            setFontFeatures("fontfeature", ["name"])

            Sets the font features of the text frame "name" to "fontfeature". If there is some text selected only the selected text is changed.  If "name" is not given the currently selected item is used.

            May throw ValueError if the font cannot be found.

            setFontSize(...)
            setFontSize(size, ["name"])

            Sets the font size of the text frame "name" to "size". "size" is treated as a value in points. If there is some text selected only the selected text is changed. "size" must be in the range 1 to 512. If "name" is not given the currently selected item is used.

            May throw ValueError for a font size that's out of bounds.

            setGradientFill(...)
            setGradientFill(type, "color1", shade1, "color2", shade2, ["name"])

        Sets the gradient fill of the object "name" to type. Color descriptions are the same as for setFillColor() and setFillShade(). See the constants for available types (FILL_ <type>).

            setGradientStop(...)
            setGradientStop("color", shade, opacity, ramppoint, ["name"])

            Set or add a gradient stop to the gradient fill of the object "name" at position ramppoint. Color descriptions are the same as for setFillColor() and setFillShade(). setGradientFill() must have been called previously for the gradient fill to be visible.

            setHGuides(...)
            setHGuides(list)

        Sets horizontal guides. Input parameter must be a list of guide positions measured in the current document units - see UNIT_ <type> constants.

            Example: setHGuides(getHGuides() + [200.0, 210.0] # add new guides without any lost          setHGuides([90,250]) # replace current guides entirely

    setImageBrightness(...)
       setImageBrightness(n [, "name"])

        Set image brightness effect of the picture in the image frame "name". If "name" is not given the currently selected item is used. A number of 1 means 100 % . Brightness factor is equal to the value shown on properties palette.

        May raise WrongFrameTypeError if the target frame is not an image frame

    setImageGrayscale(...)
       setImageGrayscale(["name"])

        Set image grayscale effect of the picture in the image frame "name". If "name" is not given the currently selected item is used.

        May raise WrongFrameTypeError if the target frame is not an image frame

    setImageOffset(...)
       setImageOffset(x, y [, "name"])

        Sets the position of the picture in the image frame "name". If "name" is not given the currently selected item is used. The specified offset values are equal to the values shown on  properties palette when point unit is used.

        May raise WrongFrameTypeError if the target frame is not an image frame

    setImageScale(...)
       setImageScale(x, y [, "name"])

        Sets the scaling factors of the picture in the image frame "name". If "name" is not given the currently selected item is used. A number of 1 means 100 % . Scaling factors are equal to the values shown on properties palette.

        May raise WrongFrameTypeError if the target frame is not an image frame

    setInfo(...)
       setInfo("author", "info", "description") -> bool

        Sets the document information. "Author", "Info", "Description" are strings.

    setJSActionScript(...)
        setJSActionScript(which, script,["name"])

        Sets the JavaScript action for a particular event. Also sets the annotation's action to JavaScript. "which" is one of the following: (0 Mouse Up, 1 Mouse Down, 2 Mouse Enter, 3 Mouse Exit, 4 Focus In, 5 Focus Out, 6 Selection Change, 7 Field Format, 8 Field Validate, 9 Field Calculate) "script" is the JavaScript set to the action. "name" uses the currently selected item if not given. Page item must be an annotation or an error will be raised. Returns: None

    setLayerBlendmode(...)
       setLayerBlendmode("layer", blend)

        Sets the layers "layer"  blendmode to blend.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    setLayerFlow(...)
       setLayerFlow("layer", flow)

        Sets the layers "layer"  flowcontrol to flow. If flow is set to true text in layers above this one will flow around objects on this layer.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    setLayerLocked(...)
       setLayerLocked("layer", locked)

        Sets the layer "layer" to be locked or not. If locked is set to true the layer will be locked.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    setLayerOutlined(...)
       setLayerOutlined("layer", outline)

        Sets the layer "layer" to be locked or not. If outline is set to true the layer will be displayed outlined.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    setLayerPrintable(...)
       setLayerPrintable("layer", printable)

        Sets the layer "layer" to be printable or not. If is the printable set to false the layer won't be printed.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    setLayerTransparency(...)
       setLayerTransparency("layer", trans)

        Sets the layers "layer"  transparency to trans.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    setLayerVisible(...)
       setLayerVisible("layer", visible)

        Sets the layer "layer" to be visible or not. If is the visible set to false the layer is invisible.

        May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable.

    setLineBlendmode(...)
       setLineBlendmode(blendmode, ["name"])

        Sets the line blendmode of the object "name" to blendmode If "name" is not given the currently selected item is used.

    setLineCap(...)
       setLineCap(endtype, ["name"])

        Sets the line cap style of the object "name" to the style "cap". If "name" is not given the currently selected item is used. There are predefined constants for "cap" - CAP_ <type>.

    setLineColor(...)
       setLineColor("color", ["name"])

        Sets the line color of the object "name" to the color "color". If "name" is not given the currently selected item is used.

    setLineJoin(...)
       setLineJoin(join, ["name"])

        Sets the line join style of the object "name" to the style "join". If "name" is not given the currently selected item is used. There are predefined constants for join - JOIN_ <type>.

    setLineShade(...)
       setLineShade(shade, ["name"])

        Sets the shading of the line color of the object "name" to "shade". "shade" must be an integer value in the range from 0 (lightest) to 100 (full color intensity). If "name" is not given the currently selected item is used.

        May raise ValueError if the line shade is out of bounds.

    setLineSpacing(...)
       setLineSpacing(size, ["name"])

        Sets the line spacing("leading") of the text frame "name" to "size". "size" is a value in points. If "name" is not given the currently selected item is used.

        May throw ValueError if the line spacing is out of bounds.

    setLineSpacingMode(...)
       setLineSpacingMode(mode, ["name"])

        Sets the line spacing mode of the text frame "name" to "mode". If "name" is not given the currently selected item is used. Mode values are the same as in createParagraphStyle.

        May throw ValueError if the mode is out of bounds.

    setLineStyle(...)
       setLineStyle(style, ["name"])

        Sets the line style of the object "name" to the style "style". If "name" is not given the currently selected item is used. Argument for this function is number - value from 1 to 37 There are few predefined constants for "style" - LINE_ <style>. In Property Palette this feature is selected in box named 'Type of line'

    setLineTransparency(...)
       setLineTransparency(transparency, ["name"])

        Sets the line transparency of the object "name" to transparency If "name" is not given the currently selected item is used.

    setLineWidth(...)
       setLineWidth(width, ["name"])

        Sets line width of the object "name" to "width". "width" must be in the range from 0.0 to 12.0 inclusive, and is measured in points. If "name" is not given the currently selected item is used.

        May raise ValueError if the line width is out of bounds.

    setLinkAnnotation(...)
        setLinkAnnotation(page, x,y,["name"])

        Turns a text fame into a link that gotos a page in the document.

        Arguments: "page" is the page the link will take you to. Must be 1 and cannot be greater than the number of pages in the document. "x" and "y" are the x and y coordinates of the page. "name" uses the currently selected item if not given.

        Returns: None

        May raise WrongFrameTypeError if the target frame is not a text frame

    setMargins(...)
       setMargins(lr, rr, tr, br)

        Sets the margins of the document, Left(lr), Right(rr), Top(tr) and Bottom(br) margins are given in the measurement units of the document - see UNIT_ <type> constants.

    setMultiLine(...)
       setMultiLine("namedStyle", ["name"])

        Sets the line style of the object "name" to the named style "namedStyle". If "name" is not given the currently selected item is used.

        May raise NotFoundError if the line style doesn't exist.

    setNewName(...)
       setNewName(newname, ["name"])

        Sets the new name of the object "name" to the newname. If "name" is not given the currently selected item is used.

        May raise NotFoundError if the line style doesn't exist.

    setObjectAttributes(...)
       setObjectAttributes(attributes, ["name"])

        Sets attributes of the object "name". If "name" is not given the currently selected item is used.

        attributes is a list of dictionary. Each dictionary must have those keys: Name, Type, Value, Parameter, Relationship, RelationshipTo, AutoAddTo All values must be strings.

        May raise NotFoundError if the object doesn't exist.

    setPDFBookmark(...)
       setPDFBookmark("toggle", ["name"])

        Sets whether (toggle= 1) the text frame "name" is a bookmark nor not. If "name" is not given the currently selected item is used.

        May raise WrongFrameTypeError if the target frame is not a text frame

    setProperty(...)
       setProperty(object, property, value)

        Set `property' of `object' to `value'. If `value' cannot be converted to a type compatible with the type of `property', an exception is raised. An exception may also be raised if the underlying setter fails.

        See getProperty() for more information.

    setRedraw(...)
       setRedraw(bool)

        Disables page redraw when bool = False, otherwise redrawing is enabled. This change will persist even after the script exits, so make sure to call setRedraw(True) in a finally: clause at the top level of your script.

    setScaleFrameToImage(...)
       setScaleFrameToImage([name])

        Set frame size on the selected or specified image frame to image size.

        May raise WrongFrameTypeError.

    setScaleImageToFrame(...)
        setScaleImageToFrame(scaletoframe, proportional=None, name= <selection>)

        Sets the scale to frame on the selected or specified image frame to `scaletoframe'. If `proportional' is specified, set fixed aspect ratio scaling to `proportional'. Both `scaletoframe' and `proportional' are boolean.

        May raise WrongFrameTypeError.

    setSpotColor(...)
       setSpotColor("name", spot)

        Set the color "name" as a spot color if spot parameter is True. See also isSpotColor()

        May raise NotFoundError if a named color wasn't found. May raise ValueError if an invalid color name is specified.

    setStyle(...)
       setStyle("style" [, "name"])

        Apply the named "style" to the object named "name". If object name is given, style is applied to the current text selection in object "name". If no object name is given, style is applied on selected object.

    setTableBottomBorder(...)
       setTableBottomBorder(borderLines, ["name"])

        Sets the bottom border of the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_ * constants. If "name" is not given the currently selected item is used.

        May throw ValueError if "borderLines" is of the wrong format.

    setTableFillColor(...)
       setTableFillColor(color, ["name"])

        Sets the fill color of the table "name" to "color". If "name" is not given the currently selected item is used.

        May throw ValueError the table does not exist.

    setTableLeftBorder(...)
       setTableLeftBorder(borderLines, ["name"])

        Sets the left border of the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_ * constants. If "name" is not given the currently selected item is used.

        May throw ValueError if "borderLines" is of the wrong format.

    setTableRightBorder(...)
       setTableRightBorder(borderLines, ["name"])

        Sets the right border of the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_ * constants. If "name" is not given the currently selected item is used.

        May throw ValueError if "borderLines" is of the wrong format.

    setTableStyle(...)
       setTableStyle(style, ["name"])

        Sets the named style of the table "name" to "style". If "name" is not given the currently selected item is used.

    setTableTopBorder(...)
       setTableTopBorder(borderLines, ["name"])

        Sets the top border of the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_ * constants. If "name" is not given the currently selected item is used.

        May throw ValueError if "borderLines" is of the wrong format.

    setText(...)
       setText("text", ["name"])

        Sets the text of the text frame "name" to the text of the string "text". Text must be UTF8 encoded - use e.g. unicode(text, 'iso-8859-2'). See the FAQ for more details. If "name" is not given the currently selected item is used.

    setTextAlignment(...)
       setTextAlignment(align, ["name"])

        Sets the text alignment of the text frame "name" to the specified alignment. If "name" is not given the currently selected item is used. "align" should be one of the ALIGN_ constants defined in this module - see dir(scribus).

        May throw ValueError for an invalid alignment constant.

    setTextAnnotation(...)
        setTextAnnotation(icon, isopen,["name"])

        Turns a text fame into a text annotation.

        Arguments: "icon" must be 0-8.  The values correspond to: ( 0 "Note", 1 "Comment", 2 "Key", 3 "Help", 4 "NewParagraph", 5 "Paragraph", 6 "Insert",7 "Cross", 8 "Circle")n"isopen" is True or False. "name" uses the currently selected item if not given.

        Returns: None

        May raise WrongFrameTypeError if the target frame is not a text frame

    setTextColor(...)
       setTextColor("color", ["name"])

        Sets the text color of the text frame "name" to the color "color". If there is some text selected only the selected text is changed. If "name" is not given the currently selected item is used.

    setTextDirection(...)
       setTextDirection(direction, ["name"])

        Sets the text direction of the text frame "name" to the specified direction. If "name" is not given the currently selected item is used. "direction" should be one of the DIRECTION_ constants defined in this module - see dir(scribus).

        May throw ValueError for an invalid direction constant.

    setTextDistances(...)
       setTextDistances(left, right, top, bottom, ["name"])

        Sets the text distances of the text frame "name" to the values "left" "right", "top" and "bottom". If "name" is not given the currently selected item is used.

        May throw ValueError if any of the distances are out of bounds(must be positive).

    setTextScalingH(...)
       setTextScalingH(scale, ["name"])

        Sets the horizontal character scaling of the object "name" to "scale" in percent. If "name" is not given the currently selected item is used.

    setTextScalingV(...)
       setTextScalingV(scale, ["name"])

        Sets the vertical character scaling of the object "name" to "scale" in percent. If "name" is not given the currently selected item is used.

    setTextShade(...)
       setTextShade(shade, ["name"])

        Sets the shading of the text color of the object "name" to "shade". If there is some text selected only the selected text is changed. "shade" must be an integer value in the range from 0 (lightest) to 100 (full color intensity). If "name" is not given the currently selected item is used.

    setTextStroke(...)
       setTextStroke("color", ["name"])

        Set "color" of the text stroke. If "name" is not given the currently selected item is used.

    setTextVerticalAlignment(...)
       setTextVerticalAlignment(align, ["name"])

        Sets the vertical alignment of text inside text frame "name" to the specified alignment. If "name" is not given the currently selected item is used. "align"  should be one of the ALIGNV constants defined in this module - see dir(scribus).

        May throw ValueError for an invalid alignment constant.

    setURIAnnotation(...)
        setURIAnnotation(uri, ["name"])

        Turns a text fame into a uri link that gotos the uri specified.

        Arguments: "uri" is the uri that the link will be set to. "name" uses the currently selected item if not given.

        Returns: None

        May raise WrongFrameTypeError if the target frame is not a text frame

    setUnit(...)
       setUnit(type)

        Changes the measurement unit of the document. Possible values for "unit" are defined as constants UNIT_ <type>.

        May raise ValueError if an invalid unit is passed.

    setVGuides(...)
       setVGuides()

        See setHGuides.

    sizeObject(...)
       sizeObject(width, height [, "name"])

        Resizes the object "name" to the given width and height. If "name" is not given the currently selected item is used.

    statusMessage(...)
       messagebarText("string")

        Writes the "string" into the Scribus message bar(status line). The text must be UTF8 encoded or 'unicode' string(recommended).

    textFlowMode(...)
       textFlowMode("name" [, state])

        Enables/disables "Text Flows Around Frame" feature for object "name". Called with parameters string name and optional int "state" (0 <= state <= 3). Setting "state" to 0 will disable text flow. Setting "state" to 1 will make text flow around object frame. Setting "state" to 2 will make text flow around bounding box. Setting "state" to 3 will make text flow around contour line. If "state" is not passed, text flow is toggled.

    textOverflows(...)
       textOverflows(["name", nolinks]) -> integer

        Returns 1 if there are overflowing characters in text frame "name", 0 if not. If is nolinks set to non zero value it takes only one frame - it doesn't use text frame linking. Without this parameter it search all linking chain.

        May raise WrongFrameTypeError if the target frame is not an text frame

    traceText(...)
       traceText(["name"])

        Convert the text frame "name" to outlines. If "name" is not given the currently selected item is used.

    unGroupObject(...)
       unGroupObjects("name")

        Destructs the group the object "name" belongs to.If "name" is not given the currently selected item is used.

    unlinkTextFrames(...)
       unlinkTextFrames("name")

        Remove the specified(named) object from the text frame flow/linkage. If the frame was in the middle of a chain, the previous and next frames will be connected, eg 'a->b->c' becomes 'a->c' when you unlinkTextFrames(b)'

        May throw ScribusException if linking rules are violated.

    valueDialog(...)
        valueDialog(caption, message [, defaultvalue]) -> string

        Shows the common 'Ask for string' dialog and returns its value as a string Parameters: window title, text in the window and optional 'default' value.

        Example: valueDialog('title', 'text in the window', 'optional')

    zoomDocument(...)
       zoomDocument(double)

        Zoom the document in main GUI window. Actions have whole number values like 20.0, 100.0, etc. Zoom to Fit uses - 100 as a marker.

DATA
   ALIGNV_BOTTOM = 2
    ALIGNV_CENTERED = 1
    ALIGNV_TOP = 0
    ALIGN_BLOCK = 3
    ALIGN_CENTERED = 1
    ALIGN_FORCED = 4
    ALIGN_LEFT = 0
    ALIGN_RIGHT = 2
    BUTTON_ABORT = 262144
    BUTTON_CANCEL = 4194304
    BUTTON_DEFAULT = 256
    BUTTON_IGNORE = 1048576
    BUTTON_NO = 65536
    BUTTON_NONE = 0
    BUTTON_OK = 1024
    BUTTON_RETRY = 524288
    BUTTON_YES = 16384
    CAP_FLAT = 0
    CAP_ROUND = 32
    CAP_SQUARE = 16
    COLOR = 14
    COLOR_BURN = 11
    COLOR_DODGE = 10
    CSPACE_CMYK = 1
    CSPACE_DUOTONE = 3
    CSPACE_GRAY = 2
    CSPACE_MONOCHROME = 4
    CSPACE_RGB = 0
    CSPACE_UNDEFINED = -1
    DARKEN = 1
    DIFFERENCE = 8
    DIRECTION_LTR = 0
    DIRECTION_RTL = 1
    EXCLUSION = 9
    FACINGPAGES = 1
    FILL_CROSSDIAGONALG = 4
    FILL_DIAGONALG = 3
    FILL_HORIZONTALG = 1
    FILL_NOG = 0
    FILL_RADIALG = 5
    FILL_VERTICALG = 2
    FIRSTPAGELEFT = 0
    FIRSTPAGERIGHT = 1
    HARD_LIGHT = 6
    HUE = 12
    ICON_CRITICAL = 3
    ICON_INFORMATION = 1
    ICON_NONE = 0
    ICON_WARNING = 2
    JOIN_BEVEL = 64
    JOIN_MITTER = 0
    JOIN_ROUND = 128
    LANDSCAPE = 1
    LIGHTEN = 2
    LINE_DASH = 2
    LINE_DASHDOT = 4
    LINE_DASHDOTDOT = 5
    LINE_DOT = 3
    LINE_SOLID = 1
    LUMINOSITY = 15
    MULTIPLY = 3
    NOFACINGPAGES = 0
    NORMAL = 0
    OVERLAY = 5
    PAGE_1 = 0
    PAGE_2 = 1
    PAGE_3 = 2
    PAGE_4 = 3
    PAPER_A0 = (2380.0, 3368.0)
    PAPER_A0_MM = (841.0, 1189.0)
    PAPER_A1 = (1684.0, 2380.0)
    PAPER_A1_MM = (594.0, 841.0)
    PAPER_A2 = (1190.0, 1684.0)
    PAPER_A2_MM = (420.0, 594.0)
    PAPER_A3 = (842.0, 1190.0)
    PAPER_A3_MM = (297.0, 420.0)
    PAPER_A4 = (595.0, 842.0)
    PAPER_A4_MM = (210.0, 297.0)
    PAPER_A5 = (421.0, 595.0)
    PAPER_A5_MM = (148.0, 210.0)
    PAPER_A6 = (297.0, 421.0)
    PAPER_A6_MM = (105.0, 148.0)
    PAPER_A7 = (210.0, 297.0)
    PAPER_A7_MM = (74.0, 105.0)
    PAPER_A8 = (148.0, 210.0)
    PAPER_A8_MM = (52.0, 74.0)
    PAPER_A9 = (105.0, 148.0)
    PAPER_A9_MM = (37.0, 52.0)
    PAPER_B0 = (2836.0, 4008.0)
    PAPER_B0_MM = (1000.0, 1414.0)
    PAPER_B1 = (2004.0, 2836.0)
    PAPER_B10 = (89.0, 125.0)
    PAPER_B10_MM = (31.0, 44.0)
    PAPER_B1_MM = (707.0, 1000.0)
    PAPER_B2 = (1418.0, 2004.0)
    PAPER_B2_MM = (500.0, 707.0)
    PAPER_B3 = (1002.0, 1418.0)
    PAPER_B3_MM = (353.0, 500.0)
    PAPER_B4 = (709.0, 1002.0)
    PAPER_B4_MM = (250.0, 353.0)
    PAPER_B5 = (501.0, 709.0)
    PAPER_B5_MM = (176.0, 250.0)
    PAPER_B6 = (355.0, 501.0)
    PAPER_B6_MM = (125.0, 176.0)
    PAPER_B7 = (250.0, 355.0)
    PAPER_B7_MM = (88.0, 125.0)
    PAPER_B8 = (178.0, 250.0)
    PAPER_B8_MM = (62.0, 88.0)
    PAPER_B9 = (125.0, 178.0)
    PAPER_B9_MM = (44.0, 62.0)
    PAPER_C5E = (462.0, 649.0)
    PAPER_COMM10E = (298.0, 683.0)
    PAPER_DLE = (312.0, 624.0)
    PAPER_EXECUTIVE = (542.0, 720.0)
    PAPER_FOLIO = (595.0, 935.0)
    PAPER_LEDGER = (1224.0, 792.0)
    PAPER_LEGAL = (612.0, 1008.0)
    PAPER_LETTER = (612.0, 792.0)
    PAPER_TABLOID = (792.0, 1224.0)
    PORTRAIT = 0
    SATURATION = 13
    SCREEN = 4
    SOFT_LIGHT = 7
    UNIT_C = 5
    UNIT_CENTIMETRES = 4
    UNIT_CICERO = 5
    UNIT_CM = 4
    UNIT_IN = 2
    UNIT_INCHES = 2
    UNIT_MILLIMETERS = 1
    UNIT_MM = 1
    UNIT_P = 3
    UNIT_PICAS = 3
    UNIT_POINTS = 0
    UNIT_PT = 0
    c = 0.07818656422379827
    cm = 0.035277777777777776
    inch = 0.013888888888888888
    mainInterpreter = True
    mainWindow = <PyCObject object >
    mm = 0.35277777777777775
    p = 1.0
    pt = 1.0
    qApp = <PyCObject object >
    scribus_version = '1.5.5'
    scribus_version_info = (1, 5, 5, '', 0)

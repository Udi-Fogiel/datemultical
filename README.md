# The `datemultical` package

Named dates and multi-calendar date formatting for LaTeX.

## Description

The `datemultical` package provides a unified interface for defining,
converting, and formatting dates in LaTeX documents.

It provides two calculation backends:

- `basic`: the built-in backend, available under all supported engines,
  with support for the three core calendars: Gregorian, Solar Hijri,
  and Lunar Hijri;
- `lua`: the LuaLaTeX backend, which includes the same three core
  calendars and additionally supports the calendar systems provided by
  `lua-calendrica`.

When Persian localization is enabled, Persian month and weekday names are
available where defined by the package.

Under LuaLaTeX, the `lua` backend is selected by default. The `basic`
backend can be selected with the `native` option.

## Installation

Manual installation from GitHub:
~~~bash
git clone https://github.com/gambi-shah/datemultical.git
~~~

Copy the package files (`.sty`, `.def`, and `.lua`) into a
TeX-searchable directory. Alternatively, keep them in the same
directory as your document.

If necessary, refresh the TeX filename database:

~~~bash
mktexlsr
~~~

## Usage

A minimal example:

~~~latex
\documentclass{article}
\usepackage{datemultical}

\begin{document}

\dmcset[sh]{birth}{1365}{3}{11}

\dmc{birth}{short}

\dmc[lh]{birth}{full}

\end{document}
~~~

Here, `birth` is defined once as a Solar Hijri date and can then be
formatted in different styles and calendar systems.

To enable Persian localization:

~~~latex
\usepackage[persian]{datemultical}
~~~

To select the basic backend explicitly under LuaLaTeX:

~~~latex
\usepackage[native]{datemultical}
~~~

## Documentation

see the [main manual](doc/datemultical.pdf) for the complete documentation.

## License and maintainer

- License: LPPL 1.3c or later
- Maintainer: Amer Amikhteh
- Bug reports: please use the repository issue tracker


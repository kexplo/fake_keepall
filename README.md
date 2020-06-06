# Fake KeepAll

Apply the fake `word-break: keep-all;` CSS property to static HTML file.

This is useful when using the HTML->PDF converter that does not support the `word-break: keep-all;` CSS property.

## How it works

Add the `white-space: nowrap;` CSS property to every word to prevent line breaks.

## Usage

```bash
$ fake-keepall example.html --out example_out.html --tags 'p,li'
```

## Screenshot


# Build Date

Exposes the date that the site was built, e.g., the current date when Pelican is processing it, to jinja2 templates.

## Usage

1. In a template, insert for example `{{ BUILD_DATE|strftime('%Y') }}` for the year the site was last built.
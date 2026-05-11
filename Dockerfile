# Self-contained environment, useful commands:
#
# Prevent MSYS from messing up docker paths:
# export MSYS2_ARG_CONV_EXCL="*"
#
# Build environment image:
# docker build --pull --rm -t svg:ci .
#
# After image has been built, you can run:
#
# Interactive shell, useful for debugging:
# docker run --rm -it -v .:/src -w /src --entrypoint=bash svg:ci
#
# Convert everything to PNG bundles:
# docker run --rm -v .:/src -w /src svg:ci svgs.py --svgdirs=svgs --builddir=bundles --resolutions=720,1080,1440,2160
# 
# Convert single image to PNG bundle:
# docker run --rm -v .:/src -w /src svg:ci svg.py --svgdir=svgs/nichijou-logo --builddir=bundles --resolutions=720,1080,1440,2160

FROM alpine:3.23.4

RUN apk add \
    bash=5.3.3-r1 \
    rsvg-convert=2.61.2-r0 \
    python3=3.12.13-r0

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python3"]
import os
import sys
import argparse
import subprocess


def parse_args():
    parser = argparse.ArgumentParser('Convert SVG images into PNG bundles')
    parser.add_argument('--svgdirs',
        help='directory with svg image directories')
    parser.add_argument('--builddir',
        help='directory to put bundles into')
    parser.add_argument('--resolutions',
        help='comma-separated list of vertical resolutions to generate (horizontal resolution is calculated from aspect ratio)')
    return parser.parse_args()


def main():
    args = parse_args()

    for package in os.listdir(args.svgdirs):
        print(f'Processing image {package}')
        subprocess.check_call([
            sys.executable, 'svg.py',
            '--svgdir', os.path.join(args.svgdirs, package),
            '--builddir', args.builddir,
            '--resolutions', "128," + args.resolutions # 128 is the thumbnail size from release.py
        ])


if __name__ == '__main__':
    main()

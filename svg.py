import os
import shutil
import argparse
import subprocess



def parse_args():
    parser = argparse.ArgumentParser('Convert SVG image into PNG bundle (multiple resolutions)')
    parser.add_argument('--svgdir',
        help='directory with SVG image')
    parser.add_argument('--builddir',
        help='directory to put bundle into')
    parser.add_argument('--resolutions',
        help='comma-separated list of vertical resolutions to generate (horizontal resolution is calculated from aspect ratio)')
    return parser.parse_args()


def main():
    args = parse_args()

    image_title = os.path.basename(args.svgdir)
    deploy_directory = os.path.join(args.builddir, image_title)
    if not os.path.isdir(deploy_directory):
        os.makedirs(deploy_directory)

    # copy source into bundle directory
    shutil.copy(os.path.join(args.svgdir, f'{image_title}.svg'), deploy_directory)

    # generate PNG files for each resolution
    for resolution in args.resolutions.split(','):
        print(f'Generating image {image_title} at ?x{resolution} px')
        subprocess.check_call([
            'rsvg-convert',
            '--height', resolution,
            '--keep-aspect-ratio',
            '--format', 'png',
            '--output', os.path.abspath(os.path.join(deploy_directory, image_title + f'_{resolution}.png')),
            os.path.abspath(os.path.join(args.svgdir, f'{image_title}.svg'))
        ])

if __name__ == '__main__':
    main()

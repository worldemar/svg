import os


def _get_svg_resolutions_links(svg_name):
    formats = []
    for format_file in os.listdir(os.path.join('docs', svg_name)):
        if format_file.endswith('.png'):
            # extract resolution from filename
            vertical_resolution = int(format_file.replace(svg_name, '').replace('.png', '').replace('_', ' ').strip())
            formats.append({
                'link' : f'[{vertical_resolution}]({svg_name}/{format_file})',
                'vres' : vertical_resolution
            })
    links = [link['link'] for link in sorted(formats, key=lambda x: x['vres'])]
    links.append(f'[SVG]({svg_name}/{svg_name}.svg)')
    return links

def write_svg_info(svg_name, readme_file):
    svg_readme_path = os.path.join('svgs', svg_name, 'README.md')
    with open(svg_readme_path, 'rb') as svg_readme:
        svg_readme_lines = svg_readme.readlines()
    assert len(svg_readme_lines) > 2, 'SVG README.md must have at least 3 lines'
    assert svg_readme_lines[0].startswith(b'# '), 'SVG README.md must start with #'
    assert svg_readme_lines[1] == b'\n', 'SVG README.md must have a blank line after the title'
    assert b'#' not in b''.join(svg_readme_lines[2:]), 'SVG README.md must not have a # in the description'

    svg_readme_header = svg_readme_lines[0]
    svg_readme_description = b'<br>'.join(svg_readme_lines[2:])

    # header
    readme_file.write(b'\n')
    readme_file.write(svg_readme_header)
    readme_file.write(b'\n')

    # list all formats and resolutions
    links = _get_svg_resolutions_links(svg_name)
    readme_file.write(b"| " + " | ".join(links).encode('utf-8') + b" |\n\n")

    # thumbnail
    thumbnail = f'| ![{svg_name}]({svg_name}/{svg_name}_128.png) | '
    readme_file.write(thumbnail.encode('utf-8'))
    readme_file.write(svg_readme_description)
    readme_file.write(b' |\n\n')


def main():
    with open(os.path.join('docs', 'README.md'), 'wb') as readme_pages:
        with open('README.md', 'rb') as readme_github:
            readme_pages.write(readme_github.read())
        for app_name in os.listdir('svgs'):
            write_svg_info(app_name, readme_pages)


if __name__ == '__main__':
    main()

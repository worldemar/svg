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
    links.append(f'[**SVG**]({svg_name}/{svg_name}.svg)')
    return links

def write_svg_info(svg_name, readme_file):
    svg_readme_path = os.path.join('svgs', svg_name, 'README.md')
    with open(svg_readme_path, 'rb') as svg_readme:
        svg_readme_lines = svg_readme.readlines()
    svg_readme_description = b'<br>'.join(line.strip() for line in svg_readme_lines)

    thumbnail = f'| ![{svg_name}]({svg_name}/{svg_name}_128.png) | '
    links = _get_svg_resolutions_links(svg_name)

    readme_file.write(thumbnail.encode('utf-8'))
    readme_file.write(svg_readme_description)
    readme_file.write(b'<br><br>')
    readme_file.write(" - ".join(links).encode('utf-8'))
    readme_file.write(b' |\n')


def main():
    with open(os.path.join('docs', 'README.md'), 'wb') as readme_pages:
        with open('README.md', 'rb') as readme_github:
            readme_pages.write(readme_github.read())
        readme_pages.write(b'\n\n---\n\n')
        readme_pages.write(b'| Preview | Description and links |\n')
        readme_pages.write(b'| :-: | :- |\n')
        for app_name in os.listdir('svgs'):
            write_svg_info(app_name, readme_pages)
        readme_pages.write(b'\n\n---\n\n')
        with open('LICENSE', 'rb') as license:
            readme_pages.write(license.read())



if __name__ == '__main__':
    main()

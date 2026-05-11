import os


def write_svg_info(svg_name, readme_file):
    # header
    link = f'### [{svg_name}]({svg_name}/{svg_name}.svg)\n\n'
    readme_file.write(link.encode('utf-8'))

    # list all formats and resolutions
    links = []
    for format_file in os.listdir(os.path.join('docs', svg_name)):
        if format_file.endswith('.png'):
            # extract resolution from filename
            link_text = format_file.replace(svg_name, '').replace('.png', '').replace('_', ' ').strip()
            links.append(f'[{link_text}]({svg_name}/{format_file})')
        if format_file.endswith('.svg'):
            links.append(f'[SVG]({svg_name}/{format_file})')
    readme_file.write(b"[ " + " | ".join(links).encode('utf-8') + b" ]\n\n")

    # description
    svg_readme_path = os.path.join('svgs', svg_name, 'README.md')
    with open(svg_readme_path, 'rb') as svg_readme:
        readme_file.write(svg_readme.read())
        readme_file.write(b'\n\n')

    # thumbnail
    thumbnail = f'![{svg_name}]({svg_name}/{svg_name}_128.png)\n\n'
    readme_file.write(thumbnail.encode('utf-8'))


def main():
    with open(os.path.join('docs', 'README.md'), 'wb') as readme_pages:
        with open('README.md', 'rb') as readme_github:
            readme_pages.write(readme_github.read())
        for app_name in os.listdir('svgs'):
            write_svg_info(app_name, readme_pages)


if __name__ == '__main__':
    main()

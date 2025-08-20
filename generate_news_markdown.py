import os
import re
import yaml

def slugify(title):
    # Lowercase, replace spaces with hyphens, remove non-alphanum
    slug = re.sub(r'[^a-zA-Z0-9\-]', '', title.lower().replace(' ', '-'))
    return slug

def main(yaml_path, output_dir):
    with open(yaml_path, 'r') as f:
        news_items = yaml.safe_load(f)
    os.makedirs(output_dir, exist_ok=True)
    for item in news_items:
        title = item.get('title', 'untitled')
        content = item.get('content', '')
        meta = {k: v for k, v in item.items() if k != 'content'}
        meta['hidePagination'] = item.get('hidePagination', True)
        date = item.get('date')
        if not date:
            print(f"Warning: No date found for news item '{title}', skipping.")
            continue
        # Use date as filename, e.g., 2025-08-01.md
        md_path = os.path.join(output_dir, f'{date}.md')
        with open(md_path, 'w') as md:
            md.write('---\n')
            for k, v in meta.items():
                # md.write(f'{k}: "{v}"\n' if isinstance(v, str) else f'{k}: {v}\n')
                if isinstance(v, str):
                    md.write(f'{k}: "{v}"\n')
                elif isinstance(v, bool):
                    md.write(f'{k}: {"false" if not v else "true"}\n')
                else:
                    md.write(f'{k}: {v}\n')
            md.write('---\n')
            md.write(content + '\n')

if __name__ == '__main__':
    # Example usage: python generate_news_markdown.py [news.yaml]
    import sys
    output_dir = 'content/news/'
    if len(sys.argv) == 2:
        yaml_path = sys.argv[1]
    else:
        yaml_path = os.path.join(output_dir, 'news.yaml')
        print(f'No YAML file specified, using default: {yaml_path}')
    main(yaml_path, output_dir)

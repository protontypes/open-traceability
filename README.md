# Open Traceability

A framework that enables consistent assessment across environmental claims by breaking the knowledge-creation process into traceability dimensions covering evidence, methods, execution, review, publication, and linkage.

## Repository Structure

- `docs/`: Core documentation and project planning
  - `definition.md`: The Open Traceability Definition
  - `website/`: Design specs, branding, and content drafts
    - `branding/`: Branding assets and [Figma Links](docs/website/branding/README.md)
    - `content/`: Landing page and audience-specific copy
- `web/`: Source code for the static website
  - `content/`: Page content (Markdown)
  - `data/`: Structured data (YAML) used throughout the site
- `assets/`: Shared images, icons, and infographics
- `model/`: Underlying model, ontologies and knowledge graph building 

## Running the Website

The website is built using [Hugo](https://gohugo.io/).

### Prerequisites

- [Hugo](https://gohugo.io/installation/) (extended version recommended)

### Local Development

1. Navigate to the `web` directory:
   ```bash
   cd web
   ```
2. Start the Hugo development server:
   ```bash
   hugo server -D
   ```
3. Open your browser to `http://localhost:1313`.

### Building for Production

To generate the static site files in the `web/public` directory:
```bash
cd web
hugo
```

## Contributing

Please place your documentation and drafts in the appropriate `docs/` subfolder. For website-related design, use the `docs/website/branding` folder to link Figma assets.

To contribute directly to the website content:
- Update page text in `web/content/`.
- Update structured data in `web/data/`.

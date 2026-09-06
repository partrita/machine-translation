# AGENTS.md

## Project Overview
- **Purpose**: Document translation and publication as a Quarto-based Web Book.
- **Source Root**: `mybook/`
- **Configuration**: `mybook/_quarto.yml` (book structure, chapters, metadata)
- **Environment & Dependency**: Managed via `pixi` (`pixi.toml`)

## Key Commands
- **Preview (Live Server)**: `pixi run preview` (or `pixi run quarto preview mybook`)
- **Build / Render**: `pixi run test` (or `pixi run quarto render mybook`)
- **Add Dependency**: `pixi add <package_name>`

## Conventions & Rules for AI Agents
1. **Book Structure**: When adding new chapters or documents, update `mybook/_quarto.yml` under `chapters` or `sidebar`.
2. **Content Files**: Place source content (`.qmd`, `.md`, `.ipynb`) inside `mybook/`.
3. **Validation**: Run `pixi run test` (quarto render) to verify builds before finalizing document edits.

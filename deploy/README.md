# Deploying the site to GitHub Pages

`github-pages.workflow.yml` is a ready GitHub Actions workflow that publishes `site/` to GitHub Pages
on every push to `main`. It could not be committed under `.github/workflows/` from this session
(the GitHub App lacks the `workflows` permission), so enable it by hand once:

1. Move the file: `git mv deploy/github-pages.workflow.yml .github/workflows/pages.yml` and push.
2. In the repository settings open **Pages** and set **Source** to **GitHub Actions**.
3. The site appears at `https://<owner>.github.io/blank-app/` after the first run.

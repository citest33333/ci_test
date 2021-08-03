# CI test

## Editing GitHub Workflows

Do not edit `.github/workflows/*.yml` directly. To support yaml anchors/aliasing, we can edit `.github/*.yml` and feed it as source to `.github/gwp.py`.

- Install [yq](https://mikefarah.gitbook.io/yq/#install) if not already installed
- Edit the desired `.github/*.yml`
- cd into `.github` and run `python .github/gwp.py .github/<filename>.yml` where `<filename>` is replaced with the actual extension-less name of the file
